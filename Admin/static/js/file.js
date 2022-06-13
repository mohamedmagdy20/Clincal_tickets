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
  $(".position").animate({ left: "10px" }, 500);

  //   $("#Exit").fadeToggle("100");
});

$(".navspan1").click(() => {
  $(".sidebar").animate({ width: "200px" }, 500);
  $(".navspan1").animate({ marginLeft: "200px" }, 500);
  $(".navspan").animate({ marginLeft: "200px" }, 500);
  $(".navspan1").animate({ marginLeft: "200px" }, 500);
  $(".navspan").css({ display: "block" });
  $(".navspan1").css({ display: "none" });
  $(".position").animate({ left: "80px" }, 500);
  //   $("#Exit").fadeToggle("100");
});

$("#Exit").click(() => {
  $(".sidebar").animate({ width: "0px" }, 500);
  $(".navspan").animate({ marginLeft: "0" }, 500);
});
$(".nav-cart").click(() => {
  $(".cart").slideToggle(500);
});

google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ["Contry", "Mhl"],
    ["Italy", 54.8],
    ["France", 48.6],
    ["Spain", 44.4],
    ["USA", 23.9],
    ["Argentina", 14.5],
  ]);

  var options = {
    title: "World Wide Wine Production",
  };

  var chart = new google.visualization.PieChart(
    document.getElementById("myChart")
  );
  chart.draw(data, options);
}
