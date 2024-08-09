function FollowUpInit(exDiv) {
  const styles = `
    .qlc-loader {
      display: inline-block;
      width: 80px;
      height: 80px;
    }
    .qlc-loader:after {
      content: " ";
      display: block;
      width: 64px;
      height: 64px;
      margin: 8px;
      border-radius: 50%;
      border: 6px solid #fff;
      border-color: #fff transparent #fff transparent;
      animation: lds-dual-ring 1.2s linear infinite;
    }
    @keyframes lds-dual-ring {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }        
  `;
  let initialized = false;
  let loading = false;
  const exIndex = parseInt(exDiv.getAttribute('id').split('-').pop());
  const exForm = exDiv.querySelector('.exercise > form');
  addStyle(styles);

  async function load(isSilent) {
    if (initialized || loading) {
      return false;
    }
    loading = true;
    showLoader();
    const data = await searchQLCData(isSilent);
    if (data !== null) {
      exForm.innerHTML = '';
      exForm.append(QLCForm(exForm.getAttribute('action'), data));
      initialized = true;
    }
    hideLoader();
    loading = false;
  };

  async function searchQLCData(isSilent) {
    const errors = {
      location: 'No previous exercise found. This exercise must be in a chapter.',
      missing: 'You must first submit and complete the previous exercise.',
    };
    const linkSelect = (select) =>
      `.dropdown:has(.exercise-nav-submissions) .dropdown-menu a:${select}`;
    const exLinks = exDiv.querySelectorAll(linkSelect('not([href="#"])'));
    if (exLinks.length > 0) {
      return await loadQLCData(exLinks, isSilent);
    }
    const prIndex = exIndex - 1;
    const prDiv = document.getElementById(`chapter-exercise-${prIndex}`);
    if (prDiv === null) {
      showAlert(isSilent, 'danger', errors.location);
      return null;
    }
    let prLinks = prDiv.querySelectorAll(linkSelect('has(.badge-success)'));
    let isMissingPoints = false;
    if (prLinks.length == 0) {
      prLinks = prDiv.querySelectorAll(linkSelect('has(.badge-warning'));
      isMissingPoints = true;
      if (prLinks.length == 0) {
        showAlert(isSilent, 'warning', errors.missing);
        return null;
      }
    }
    return await loadQLCData(prLinks, isSilent, isMissingPoints);
  }

  async function loadQLCData(links, isSilent, isMissingPoints) {
    const errors = {
      status: 'Failed to load previous submission! Try again or contact staff.',
      points: 'You must first fix the remaining problems in the previous exercise.',
      json: 'Failed to read exercise data! Try again or contact staff.',
    };
    const res = await fetch(links[0].getAttribute('href'));
    if (res.status !== 200) {
      showAlert(isSilent, 'danger', errors.status);
      return null;
    }
    const html = mkElement('div', {}, await res.text());
    const elem = html.querySelector('.exercise-content [data-id="qlc-data"]');
    const data = elem ? JSON.parse(elem.textContent) : {};
    if (!data.qlcs || !data.files) {
      showAlert(isSilent, 'danger', isMissingPoints ? errors.points : errors.json);
      return null;
    }
    return data;
  }

  function showLoader() {
    exForm.append(mkElement('div', {class: 'qlc-loader'}));
  }

  function hideLoader() {
    exForm.querySelectorAll('.qlc-loader').forEach(e => e.remove());
  }

  function showAlert(silent, lvl, msg) {
    if (!silent) {
      exForm.querySelectorAll('.alert').forEach(e => e.remove());
      exForm.append(mkElement('div', {class: `alert alert-${lvl}`}, msg));
    }
  }

  function QLCForm(url, data) {
    const log = data.log || [];

    function logAdd(entry) {
      entry.time = new Date().getTime();
      log.push(entry);
    }

    async function logSend(solved, total) {
      showLoader();
      const body = new FormData();
      body.append('qlc', JSON.stringify({...data, log}));
      for (let i = 0; i < 5; i++) {
        if (solved / total * 5 > i) {
          body.append(`p${i + 1}`, 1);
        }
      }
      await fetch(url, {method: 'POST', body});
      hideLoader();
      window.postMessage({ type: 'a-plus-refresh-stats' });
    }

    if (log.length == 0) {
      logAdd({ type: 'init', files: data.files, qlcs: data.qlcs });
    }

    const qlcDiv = mkElement('div', {class: 'col-md-5'})
    qlcDiv.appendChild(SimpleQuizForm(
      data.qlcs,
      log,
      (q, o, checked, solved) => {
        const qlc = data.qlcs[q];
        const opt = qlc.options[o];
        logAdd({
          type: 'change',
          q,
          o,
          qlc: qlc.type,
          opt: opt.type,
          answer: opt.answer,
          correct: opt.correct,
          checked,
          solved,
        });
      },
      (solved, touched, total) => {
        logAdd({type: 'grade', solved, touched, total});
        logSend(solved, total);
      }
    ));

    const fileDiv = mkElement('div', {class: 'col-md-7'});
    data.files.forEach(entry => {
      fileDiv.appendChild(mkElement('h4', {}, entry[0]));
      const pre = mkElement('pre', {}, entry[1]);
      fileDiv.appendChild(pre);
      if ($ !== undefined) {
        $(pre).highlightCode({noCopy: true, noDownload: true});
      }
    });
    fileDiv.querySelectorAll('div > p').forEach(e => e.remove());
    return mkElement('div', {class: 'row'}, '', [qlcDiv, fileDiv]);
  }

  function SimpleQuizForm(questions, log, select_cb, grade_cb) {
    const styles = `
      .q-wrap .q-item {
        margin: 1em 0;
      }
      .q-wrap .q-item label {
        display: block;
        margin: 2px 0;
        border: 1px solid lightgrey;
        border-radius: 4px;
        cursor: pointer;
      }
      .q-wrap .q-item label:hover {
        background-color: gainsboro;
      }
      .q-wrap .q-item label.incorrect {
        background-color: salmon;
        color: darkred;
      }
      .q-wrap .q-item label.correct {
        background-color: springgreen;
        color: green;
      }
      .q-wrap .q-item label .info {
        margin-left: 2em;
        font-weight: normal;
        font-style: italic;
      }
    `;
    const state = questions.map(qSpec => ({
      many: qSpec.options.filter(oSpec => oSpec.correct).length > 1,
      correct: qSpec.options.map(oSpec => oSpec.correct || false),
      selected: qSpec.options.map(_ => false),
      solved: false,
      touched: false,
    }));

    function updateSelected(qState, o, checked) {
      return qState.selected.map(
        (old, oo) => oo === o ? checked : (qState.many ? old : false)
      );
    }

    function isSolved(qState) {
      for (let o = 0; o < qState.correct.length; o += 1) {
        if (qState.selected[o] != qState.correct[o]) {
          return false;
        }
      }
      return true;
    }

    function selectOption(q, o, checked) {
      const qState = state[q];
      qState.touched = true;
      qState.selected = updateSelected(qState, o, checked);
      qState.solved = isSolved(qState);
      select_cb(q, o, checked, qState.solved);
      return qState.solved;
    }

    function displayResult() {
      questions.forEach((qSpec, q) => {
        const qState = state[q];
        if (qState.solved) {
          qState.labels.forEach((l, i) => {
            displayInfo(l, qSpec.options[i].info);
            if (qState.correct[i]) {
              l.setAttribute('class', 'correct');
            } else {
              l.removeAttribute('class');
            }
          });
        } else {
          qState.labels.forEach((label, o) => {
            if (qState.selected[o]) {
              const cls = qState.correct[o] ? 'correct' : 'incorrect';
              label.setAttribute('class', cls);
              displayInfo(label, qSpec.options[o].info);
            } else {
              label.removeAttribute('class');
            }
          });
        }
      });
    }

    function displayInfo(label, info) {
      if (info && label.querySelector('span.info') === null) {
        label.appendChild(mkElement('span', { class: 'info' }, info));
      }
    }

    function registerResult() {
      grade_cb(
        state.filter(qState => qState.solved).length,
        state.filter(qState => qState.touched).length,
        state.length
      );
    }

    addStyle(styles);

    log.filter(e => e.type == 'change').forEach(({ q, o, checked }) => {
      const qState = state[q];
      qState.selected = updateSelected(qState, o, checked);
    });

    const qList = questions.map((qSpec, q) => {
      const qState = state[q];
      const labels = qSpec.options.map((oSpec, o) => {
        const label = mkElement(
          'label',
          {},
          `<input type="${qState.many ? 'checkbox' : 'radio'}" name="q${q}" value="${encodeURIComponent(oSpec.answer)}"${qState.selected[o] ? ' checked="checked"' : ''}> ${oSpec.answer}`
        );
        label.querySelector('input').addEventListener('change', evt => {
          selectOption(q, o, evt.target.checked);
        });
        return label;
      });
      qState.labels = labels;
      return mkElement(
        'div',
        { class: 'q-item' },
        `<strong>${qSpec.question}</strong>`,
        labels
      );
    });
    const button = mkElement(
      'button',
      {class: 'btn btn-primary', type: 'submit'},
      exForm.getAttribute("data-grade")
    );
    button.addEventListener('click', evt => {
      evt.preventDefault();
      displayResult();
      registerResult();
    });
    displayResult();
    return mkElement('div', { class: 'q-wrap' }, '', [...qList, button]);
  }

  function addStyle(css) {
    const style = document.getElementById('followups-styles');
    if (style === null) {
      document.head.appendChild(
        mkElement('style', {id: 'followups-styles'}, css)
      );
    } else {
      style.textContent += css;
    }
  }

  function mkElement(tag, attrs, html, childNodes) {
    const el = document.createElement(tag);
    if (attrs) {
      Object.entries(attrs).forEach(kv => el.setAttribute(kv[0], kv[1]));
    }
    if (html) {
      el.innerHTML = html;
    }
    if (childNodes) {
      childNodes.forEach(child => el.appendChild(child));
    }
    return el;
  }
  return { load };
}

addEventListener('aplus:exercise-ready', (e) => {
  const btn = e.target.querySelector('.exercise .qlc-generate');
  if (btn !== null) {
    const fup = FollowUpInit(e.target);
    btn.addEventListener('click', (evt) => {
      evt.preventDefault();
      fup.load();
    });
    addEventListener('aplus:submission-finished', () => fup.load(true));
    fup.load(true);
  }
});
