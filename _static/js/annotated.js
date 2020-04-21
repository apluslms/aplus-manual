// $( document ).ready(function() {
//     codecomment = document.getElementsByClassName("codecomment");

// })

(function($) {
    $(window).load(function() {
      const rootElement = $('body');
      const commentPrefix = "comment-";
      let lockedCodeComment = null;
  
      rootElement.find("div.codecomment.container").filter("div[class^=" + commentPrefix + "],div[class*=' " + commentPrefix + "']").each(function() {
        var commentClass = $(this).attr("class").split(" ").filter(function(className) { return className.indexOf(commentPrefix) === 0; });
        if (commentClass.length != 1) {
          console.error("Unexpected classes on code comment: " + $(this).attr("class"));
        }
        var classBits = commentClass[0].substring(commentPrefix.length).split("-");
        if (classBits.length != 2) {
          console.error("Unexpected classes on code comment: " + $(this).attr("class"));
        }
        var exampleName = classBits[0];
        var commentNumber = classBits[1];
        var commentID = exampleName + "-" + commentNumber;
  
        /* find all target locations for current commentary box */
        var matchingCodeLocations = $(".ex-" + exampleName + " .loc" + commentNumber);
        if (matchingCodeLocations.length === 0) {
          console.error("No code locations match this comment: " + commentClass[0]);
        }
  
        var targets = matchingCodeLocations.find("*").andSelf();
  
        $(this).hover( /* add hover effect for each comment and associated code locations: */
          function() {
            targets.addClass("loc-now-highlighted");
            $(this).addClass("comment-now-highlighted");
          },
          function() {
            targets.removeClass("loc-now-highlighted");
            $(this).removeClass("comment-now-highlighted");
          }
        );
        
        $(this).click( /* add click effect for each comment and associated code locations: */
          function() {
            if (lockedCodeComment === commentID) {
              targets.removeClass("loc-now-locked");
              $(this).removeClass("comment-now-locked");
              lockedCodeComment = null;
            } else {
              $("div.codecomment.comment-now-locked").each(function() {
                $(this).removeClass("comment-now-locked");
              });
              $(".loc-now-locked").each(function() {
                $(this).removeClass("loc-now-locked");
              });
              targets.addClass("loc-now-locked");
              $(this).addClass("comment-now-locked");
              lockedCodeComment = commentID;
            }
          }
        );
        
      });
    });
  })(jQuery);