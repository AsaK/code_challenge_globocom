var pieData = [
    {
        value: 20,
        color:"#878BB6"
    },
    {
        value : 40,
        color : "#4ACAB4"
    },
    {
        value : 10,
        color : "#FF8153"
    },
    {
        value : 30,
        color : "#FFEA88"
    }
];
// pie chart options
var pieOptions = {
     segmentShowStroke : false,
     animateScale : true
}
// get pie chart canvas
var countries= document.getElementById("resultChart").getContext("2d");
// draw pie chart
new Chart(countries).Pie(pieData, pieOptions);