let ex = document.getElementById("Exit");
let patient = document.getElementById("patient");
let dash = document.getElementById("dashboard");
let dashboard_content = document.getElementById("dash-content");
let admin = document.getElementsByClassName("admintable");
// admin = ` `;
$(".navspan").click(() => {
  $(".sidebar").animate({ width: "0px" }, 500);
  $(".navspan").animate({ marginLeft: "0px" }, 500);
  $(".navspan1").css({ display: "block" });
  $(".navspan1").animate({ marginLeft: "0px" }, 500);
  $(".navspan").css({ display: "none" });

  //   $("#Exit").fadeToggle("100");
});

$(".navspan1").click(() => {
  $(".sidebar").animate({ width: "200px" }, 500);
  $(".navspan1").animate({ marginLeft: "200px" }, 500);
  $(".navspan").animate({ marginLeft: "200px" }, 500);
  $(".navspan1").animate({ marginLeft: "200px" }, 500);
  $(".navspan").css({ display: "block" });
  $(".navspan1").css({ display: "none" });

  //   $("#Exit").fadeToggle("100");
});

$("#Exit").click(() => {
  $(".sidebar").animate({ width: "0px" }, 500);
  $(".navspan").animate({ marginLeft: "0" }, 500);
});
$(".nav-cart").click(() => {
  $(".cart").slideToggle(500);
});
