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

It produces HTML file which will show all charts created by analysis methods.

# Install

First install Python and [pip](http://en.wikipedia.org/wiki/Pip_(package_manager\)).

Then run:

    pip install -r requirements.txt

# Usage

1. Create your data analyzing methods to `youranalysis.py` file.

2. Run `python main.py data.csv`

3. Open `output/index.html` to see the analytics

Check examples in `examples` directory. Get started with *simple-pizza* example!
