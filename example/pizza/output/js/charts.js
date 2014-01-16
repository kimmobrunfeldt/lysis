var Charts = (function() {

    var api = {};

    api.pizza_likers_haters_pie = function(result) {
        // Create the data table.
        var data = google.visualization.arrayToDataTable(result.data);

        // Set chart options
        var options = {};

        // Draw the chart
        var chart = new google.visualization.PieChart($('#chart_' + result.name)[0]);
        chart.draw(data, _.extend(defaultChartOptions, options));
    };

    return api;
})();