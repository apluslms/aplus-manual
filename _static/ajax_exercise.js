;(function(document, window, undefined) {

window.addEventListener("message", function(event) {
    if (event.data.type === "a-plus-bind-exercise") {
        // The exercise has been loaded via AJAX and embedded into the chapter page.
        console.log("bind events for #" + event.data.id);
        exerciseLoadedHandler(document.getElementById(event.data.id));
    }
});

function exerciseLoadedHandler(exerciseDiv) {
    // the DOM is ready so we may load jQuery in a safe way
    if (typeof require === 'function') {
        // In a require.js environment (Moodle). Import jQuery.
        require(["jquery"], function(jQuery) {
            init(jQuery, exerciseDiv);
        });
    } else {
        // in A+ (jQuery defined in the global namespace)
        init(jQuery, exerciseDiv);
    }
}

function init($, exerciseDiv) {
    // Exercise grader code starts here. jQuery is available via the $ variable.

    const form = $(exerciseDiv).find('form');
    form.on('submit', function(event) {
        // The user has pressed the submit button.
        event.preventDefault();

        const ajax_key = form.find('[name="ajax_key"]').val();
        const submissionUrl = form.find('[name="submission_url"]').val();
        const answer = form.find('[name="submission"]').val();
        let points = 0;
        const maxPoints = 10;
        const graderUrl = form.find('[name="grader_url"]').val();

        // In this example, the submission "abc" receives full points.
        // Otherwise, zero points are granted.
        if (answer === 'abc') {
            points = maxPoints;
        }

        // Send the grading results to the grader.
        // It will send the results to A+ using the submission URL.
        // A+ stores the results in the database.
        $.post(graderUrl, {
            checksum: md5(ajax_key + [submissionUrl, answer, points, maxPoints].join(':')),
            submission_url: submissionUrl,
            answer: answer,
            points: points,
            max_points: maxPoints,
        })
        .done(function() {
            console.log("AJAX post succeeded");
            // Tell A+ to update the exercise info.
            window.postMessage({type: "a-plus-refresh-stats"}, "*");
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            console.error("AJAX post failed:", errorThrown);
        });
    });
}
})(document, window);
