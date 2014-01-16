# Pizza example

This is a bit more complicated example which demonstrates how to easily use charts or alternatively write your custom render code.

# Step by step

First, all answers were gathered with Google Forms. Then the responses were imported as `pizza.csv` for further analysis.

1. `youranalysis.py` was modified to implement all needed methods.

2. `python main.py pizza.csv`

3. Custom render code were implemented to `js/charts.js`.

    Specifically, this method was added:

        ```javascript
        api.pizza_likers_haters_ratio = function(result) {
            // Create the data table.
            var data = google.visualization.arrayToDataTable(result.data);

            // Set chart options
            var options = {};

            // Draw the chart
            var chart = new google.visualization.PieChart($('#chart_' + result.name)[0]);
            chart.draw(data, _.extend(defaultChartOptions, options));
        };
        ```

4. Open `index.html`
