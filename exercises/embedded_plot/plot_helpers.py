import bokeh.plotting as bokeh_plt
import bokeh.embed
from bokeh.models.ranges import Range1d


def make_base_figure(iterations):
    """
    Create the base plot with a horizontal "good value" band of height 60 in the middle.
    """
    figure = bokeh_plt.figure(tools="pan,box_zoom,reset,save",
            y_axis_label="output",
            x_axis_label="iteration",
            y_range=Range1d(0, 100),
            x_range=Range1d(0, iterations))
    figure.rect(50, 50, iterations, 80 - 20, color="green", fill_alpha=0.1)
    return figure


def add_circle(figure, x, y, color):
    figure.circle(x, y, line_alpha=0.8, fill_alpha=0.5, color=color, radius=1)


def make_html_plot(figure):
    """
    Wrap the bokeh figure into an embeddable HTML element, containing a function that can be called to draw the plot.
    """
    script, div = bokeh.embed.components(figure, wrap_script=False)
    script = "<script>;var _runBokehPlot = function() {\n" + script + "\n};\n</script>"
    return script + "\n" + div
