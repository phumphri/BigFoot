/* data route */
var url = "/data";

function buildPlot() {
    Plotly.d3.json('/data', function (error, data) {
        if (error) return console.warn(error);
        var labels = []
        var values = []
        for (var i = 0; i < data.length; i++) {
            labels.push(data[i][0])
            values.push(data[i][1])
        }
        var plot_data = [{ x: labels, y: values, type: 'bar' }]
        var layout = {
            height: 600,
            width: 750
        };
        Plotly.purge('plot')
        pie_div = document.getElementById("plot")
        Plotly.newPlot(pie_div, plot_data, layout)
    })
}

buildPlot();
