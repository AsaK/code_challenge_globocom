var pieData = [
    {
        value: 40,
        color:"#878BB6"
    },
    {
        value : 60,
        color : "#4ACAB4"
    },
];
// pie chart options
var pieOptions = {
     segmentShowStroke : false,
     animateScale : true
}
// get pie chart canvas
var countries= document.getElementById("resultChart").getContext("2d");
// draw pie chart
new Chart(countries).Doughnut(pieData, pieOptions);