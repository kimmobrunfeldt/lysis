var defaultChartOptions = {
    fontName: 'Arial',
    legend: {
        textStyle: {
            bold: false
        }
    },
    titleTextStyle: {
        bold: false
    },
    height: 300
};

function drawOne(result) {
    // Create data table
    var data = google.visualization.arrayToDataTable(result.data);

    // Dynamically get google chart object
    var chart = new google.visualization[result.chart]($('#chart_' + result.name)[0]);

    var options = _.has(result, 'options') ? result.options : {};
    chart.draw(data, _.extend(defaultChartOptions, options));
}

function drawAll(resultData) {
    _.each(window.analysis, function(result) {
        if (_.has(Charts, result.name)) {
            // Call custom made function
            Charts[result.name](result);
        } else {
            if (!_.has(result, 'chart')) {
                throw 'No custom handler defined for ' + result.name;
            }

            drawOne(result);
        }
    });
}