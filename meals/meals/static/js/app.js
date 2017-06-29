$(document).ready(function(){
      $("#menu-toggle").click(function(e) {
              e.preventDefault();
              $("#wrapper").toggleClass("toggled");
      });
  $('.showFirst').click(function () {
    $(this).children('ul').slideToggle();
    $('.showFirst > li').not(this).find('ul').slideUp();
  });
  $('.showSecond').click(function () {
    $(this).children('ul').slideToggle("slow");
  });
      $('#myCarousel').carousel({
      interval: 0
    });

      $('#myCarousel').on('slid.bs.carousel', function() {
          alert("slid");
      });
});
