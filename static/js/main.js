$(document).ready(function(){
    $("#arrow").click(function(){
        $('html, body').animate({
            scrollTop: $("#info-section").offset().top}, 1250);
    });

  $(".jumbotron").css({ height: $(window).height() + "px" });

  $(window).on("resize", function() {
    $(".jumbotron").css({ height: $(window).height() + "px" });
  });
  $("#results-hero").click(function() {
    $('html, body').animate({
        scrollTop: $("#answers").offset().top
    }, 2000);
});
});
