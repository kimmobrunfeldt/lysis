# Lysis

*Lysis* offers simple way to create visual analysis from CSV file using [Google charts](https://developers.google.com/chart/). This tool was created to more easily visualize [Google Form's](https://support.google.com/drive/answer/87809) responses. Google offers a summary of responses, but it doesn't cover every aspect of answers.

*Lysis* turns this

```python
class Analysis(analysis.Analysis):
    """Pizza survey

    Opinions of pizza
    """

    @draw
    def pizza_likers_haters_pie(self, rows):
        """Pizza likers/haters ratio pie chart

        Who likes pizza and who doesn't
        """
        counter = Counter(row[1] for row in rows)
        headers = [['Answer', 'Count']]

        return {
            'chart': 'PieChart',
            'data': headers + [(x, y) for x, y in counter.items()]
        }
```

To this:

![Pizza survey](https://raw2.github.com/kimmobrunfeldt/lysis/master/doc/pizza.png)

It produces HTML file which will show all charts created by analysis methods. You can use any [chart type that Google supports](https://developers.google.com/chart/interactive/docs/gallery). If want something else than charts, just customize render function.

[Template](https://github.com/kimmobrunfeldt/lysis/blob/master/webstatic/index.html#L34) which produces the output is very minimal, it can easily be edited to suit your needs.

# Install

First install Python and [pip](http://en.wikipedia.org/wiki/Pip_(package_manager\)).

Then run:

    pip install -r requirements.txt

# Usage

1. Create your data analyzing methods to `youranalysis.py` file.

2. Run `python main.py data.csv`

3. Open `output/index.html` to see the analytics

Check examples in `examples` directory. Get started with *simple-pizza* example!

Charts are customizable by adding key `options` to dict which is returned by analysis method. For example all available options for pie chart is listed in [Google's documentation](https://developers.google.com/chart/interactive/docs/gallery/piechart#Configuration_Options).

Labels in HTML are extracted from docstrings in Analysis class' and its methods.
