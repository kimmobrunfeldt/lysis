"""
Base class for a new analytics job.
"""



from . import utils


def draw(func, counter=[0]):
    """Decorator which injects order to methods. Also tells the base class
    that this is an analysis method.
    """
    func.order = counter[0]
    func.draw = True
    counter[0] += 1
    return func


class Analysis(object):
    """
    Base class for new analysis job.

    All methods that start with 'a_' are considered as analysis methods.
    """

    def __init__(self, rows):
        self.rows = rows
        self.headers = self.rows.pop(0)

    def execute(self):
        results = []

        # Find all methods which have draw attribute and sort based on order
        methods = utils.get_methods(self)
        methods = [(x, y) for x, y in methods if getattr(y, 'draw', False)]
        methods.sort(key=lambda t: t[1].order)

        for name, function in methods:

            header, description = utils.split_analysis_doc(function.__doc__)

            result = {
                'name': name,
                'header': header,
                'description': description
            }

            # If function returns other than dict, the return value is
            # passed to custom handler in JS
            ret = function(self.rows)
            if isinstance(ret, dict):
                result.update(ret)
            else:
                result['data'] = ret

            results.append(result)


        return results
