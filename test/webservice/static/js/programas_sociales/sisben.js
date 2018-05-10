$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});
       

$(document).ready(function() {
  $('a').tooltip({placement: 'top'});
  $( "#toggle1" ).click(function() {
      $("#widget-body1").slideToggle( "fast" );  
    $('#toggle1').toggleClass(function() {
    if ($(this).is('.fa fa-chevron-down')) {
    return '.fa fa-chevron-up';
    } else {
    return '.fa fa-chevron-down';
    }
  })
 });  

   $( "#toggle2" ).click(function() {
      $("#widget-body2").slideToggle( "fast" );
    $('#toggle2').toggleClass(function() {
    if ($(this).is('.fa fa-chevron-down')) {
    return '.fa fa-chevron-up';
    } else {
    return '.fa fa-chevron-down';
    }
  })
 }); 

   $( "#toggle3" ).click(function() {
      $("#widget-body3").slideToggle( "fast" );
    $('#toggle3').toggleClass(function() {
    if ($(this).is('.fa fa-chevron-down')) {
    return '.fa fa-chevron-up';
    } else {
    return '.fa fa-chevron-down';
    }
  })
 }); 
});