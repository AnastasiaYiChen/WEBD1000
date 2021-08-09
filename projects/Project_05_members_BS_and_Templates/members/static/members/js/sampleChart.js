// Sample chart.js

var ctx = document.getElementById("myChart").getContext('2d');
// var dataValues = [12, 19, 3, 15];
// var dataLabels = ["zero", "one", "two", "three", "four"];

function init() {

    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataLabels,
            datasets: [{
                label: 'How many members are going to each conference ',
                data: dataValues,
                backgroundColor: 'rgba(255, 230, 0, 0.6)',
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    display: false,
                    barPercentage: 1.3,
                    ticks: {
                        max: 2,
                    }
                }, {
                    display: true,
                    ticks: {
                        autoSkip: false,
                        max: 4,
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
}
