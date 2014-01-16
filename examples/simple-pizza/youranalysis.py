"""
Simple pizza example
"""

from collections import Counter

import lysis.analysis as analysis
from lysis.analysis import draw


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
