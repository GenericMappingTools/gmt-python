"""
Create an inset figure
======================

Plotting an inset figure inside another figure can be done with the
:meth:`pygmt.Figure.inset` method. After a large figure as been created,
``inset`` is called using a ``with`` statement to add elements to the inset
figure.
"""

import pygmt

########################################################################################
# Create a figure
# ---------------
#
# Prior to creating an inset figure, a larger figure must first be plotted. In the
# example below, :meth:`pygmt.Figure.coast` is used to create a map of the US state of
# Massachusetts.

fig = pygmt.Figure()
fig.coast(
    # Sets the region plotted in the larger figure
    region=[-74, -69.5, 41, 43],
    # Sets the state boundaries to be plotted with thin lines
    borders="2/thin",
    # Plots all shorelines with thin lines
    shorelines="thin",
    # Sets a 15 centimeter figure showing a Mercator projection
    projection="M15c",
    # Sets the color of the land to "lightyellow"
    land="lightyellow",
    # Sets the color of the water to "lightblue"
    water="lightblue",
    # Sets the frame to use the automatic settings
    frame="a",
)
fig.show()

########################################################################################
#
# The :meth:`pygmt.Figure.inset` method use a context manager, and is called using a
# ``with`` statement. It does not require any arguments, but will not display an inset
# figure without a ``location`` argument. Both the location and width of the inset must
# be set for it to be displayed. Using the **j** argument, the grid of the inset can
# be set . In the example below, ``BL`` sets the inset to the bottom left. The
# ``border`` argument can set the fill and border of the inset. In the example below,
# ``+pblack`` sets the border color to black and ``+gred`` sets the fill to red.

fig = pygmt.Figure()
fig.coast(
    region=[-74, -69.5, 41, 43],
    borders="2/thin",
    shorelines="thin",
    projection="M15c",
    land="lightyellow",
    water="lightblue",
    frame="a",
)
with fig.inset(location="jBL+w3c", border="+pblack+glightred"):
    # pass is used to exit the with statement as no plotting functions are called
    pass
fig.show()

########################################################################################
#
# When using **j** to set the grid location of the inset, the default location is in
# contact with the nearby axis or axes. The offset of the inset can be set with **+o**,
# followed by the offset distance along the x- and y-axis. If only one distance is
# passed, it is applied to both axes. The unit of the distance is placed at the end. In
# the example below, the inset is shifted 0.5 centimeters on the x-axis and
# 0.2 centimeters on the y-axis.

fig = pygmt.Figure()
fig.coast(
    region=[-74, -69.5, 41, 43],
    borders="2/thin",
    shorelines="thin",
    projection="M15c",
    land="lightyellow",
    water="lightblue",
    frame="a",
)
with fig.inset(location="jBL+w3c+o0.5/0.2c", border="+pblack+glightred"):
    pass
fig.show()

