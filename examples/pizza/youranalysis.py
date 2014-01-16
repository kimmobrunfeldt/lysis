"""
Pizza example analysis
"""

from collections import Counter

import lysis.analysis as analysis
from lysis.analysis import draw


class Analysis(analysis.Analysis):
    """Pizza survey

    This survey finds how people react with pizza
    """

    # This chart does not need any further actions
    # Chart is automatically drawn based on data returned
    @draw
    def pizza_likers_haters_bar(self, rows):
        """Pizza likers/haters ratio bar chart

        Who likes pizza and who doesn't
        """
        return {
            'chart': 'BarChart',
            'data': self._get_pizza_ratio(rows)
        }

    @draw
    def pizza_likers_haters_column(self, rows):
        """Pizza likers/haters ratio column chart

        Who likes pizza and who doesn't
        """
        return {
            'chart': 'ColumnChart',
            'data': self._get_pizza_ratio(rows)
        }

    # In addition to this method, custom render code must be implemented
    # in charts.js
    @draw
    def pizza_likers_haters_pie(self, rows):
        """Pizza likers/haters ratio pie chart

        Who likes pizza and who doesn't
        """
        return self._get_pizza_ratio(rows)

    def _get_pizza_ratio(self, rows):
        """This method is a not considered as analysis function."""
        counter = Counter()

        for row in rows:
            timestamp, pizza_answer = row[0:2]
            counter[pizza_answer] += 1

        headers = [['Answer', 'Count']]
        return headers + [(x, y) for x, y in counter.items()]
