jQuery(function() {
    "use strict";

    jQuery('#exercise-page-content').aplusEnrollQuiz();
});

(function($) {
    "use strict";

    const pluginName = 'aplusEnrollQuiz';
    const defaults = {
        json_data_selector: '#enroll-submission-data',
        question_visibility_triggers: {
            'enroll-student': { // Question key (the name attribute of the input elements)
                // Show these questions when the option is selected; the other questions
                // that depend on this question are hidden.
                bsc: ['enroll-bsc', 'enroll-bsc-year'],
                msc: ['enroll-master', 'enroll-master-year'],
                // All questions controlled by this question.
                ALL: ['enroll-bsc', 'enroll-bsc-year', 'enroll-master', 'enroll-master-year'],
            },
        },
    };

    function AplusEnrollQuiz(element, options) {
        this.element = $(element);
        this.settings = $.extend({}, defaults, options);
        this.init();
    }

    $.extend(AplusEnrollQuiz.prototype, {

        init: function() {
            this.fillInPreviousAnswer();
            this.setHiddenQuestionEventHandlers();
        },

        fillInPreviousAnswer: function() {
            // Pre-fill form inputs with the values given in the embedded JSON submission data.
            const sbmsDataElem = this.element.find(this.settings.json_data_selector);
            if (!sbmsDataElem.length) {
                return;
            }
            try {
                var sbmsData = JSON.parse(sbmsDataElem.first().text());
            } catch (err) {
                console.error(err);
                return;
            }
            // sbmsData is an object mapping keys to values (values are arrays)
            const nameVals = new Map(Object.entries(sbmsData));
            for (let [inputName, values] of nameVals) {
                // Set values to the form inputs if nothing has been checked in the input group.
                const inputElem = this.element.find('input[name="' + inputName + '"]');
                if (!inputElem.length)
                    continue;
                const inputType = inputElem.attr('type');
                if ((inputType === 'radio' || inputType === 'checkbox')
                        && !inputElem.is(':checked')) {
                    // Do not override any existing values.
                    inputElem.val(values);
                }
            }
        },

        setHiddenQuestionEventHandlers: function() {
            // Set event handlers for hiding/revealing certain questions based on
            // the answer on another question.
            const triggers = this.settings.question_visibility_triggers;
            const self = this;
            Object.keys(triggers).forEach(function(questionKey) {
                const questionsToShowByOption = triggers[questionKey];
                const questionInput = self.element.find('input[name="' + questionKey + '"]');
                questionInput.change(function() {
                    if (this.checked) {
                        const qToShow = questionsToShowByOption[this.value];
                        const qToHide = qToShow
                            ? questionsToShowByOption.ALL.filter(k => !qToShow.includes(k))
                            : questionsToShowByOption.ALL;
                        if (qToShow) {
                            qToShow.forEach(function(name) {
                                self.toggleQuestionVisibility(name, true);
                            });
                        }
                        qToHide.forEach(function(name) {
                            self.toggleQuestionVisibility(name, false);
                        });
                    }
                });
                // Trigger the event since the form may be prefilled.
                questionInput.change();
            });
        },

        toggleQuestionVisibility: function(questionName, show) {
            // There are usually many inputs with the same name attribute.
            // The whole question is wrapped in a div.form-group element.
            const inputs = this.element.find('input[name="' + questionName + '"]');
            inputs.first().closest('div.form-group').toggle(show);
            if (show) {
                // Set the previous values to the inputs that are shown again.
                inputs.filter('[data-prev-checked="yes"]').prop('checked', true);
                inputs.removeAttr('data-prev-checked');
            } else {
                // Remove selected values from the hidden inputs.
                inputs.filter(':checked').attr('data-prev-checked', 'yes');
                inputs.prop('checked', false);
            }
        },

    });

    $.fn[pluginName] = function(options) {
        return this.each(function() {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName, new AplusEnrollQuiz(this, options));
            }
        });
    };

})(jQuery);
