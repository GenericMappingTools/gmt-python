# pylint: disable=redefined-outer-name
"""
Tests for makecpt
"""
import os

import numpy as np
import pytest

from .. import Figure, makecpt
from ..datasets import load_earth_relief
from ..exceptions import GMTInvalidInput
from ..helpers import GMTTempFile

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
POINTS_DATA = os.path.join(TEST_DATA_DIR, "points.txt")


@pytest.fixture(scope="module")
def points():
    "Load the points data from the test file"
    return np.loadtxt(POINTS_DATA)


@pytest.fixture(scope="module")
def region():
    "The data region"
    return [10, 70, -5, 10]


@pytest.fixture(scope="module")
def grid():
    "Load the grid data from the sample earth_relief file"
    return load_earth_relief()


@pytest.mark.mpl_image_compare
def test_makecpt_to_plot_points(points, region):
    """
    Use static color palette table to change color of points
    """
    fig = Figure()
    makecpt(cmap="rainbow")
    fig.plot(
        x=points[:, 0],
        y=points[:, 1],
        color=points[:, 2],
        region=region,
        style="c1c",
        cmap=True,
    )
    return fig


@pytest.mark.mpl_image_compare
def test_makecpt_to_plot_grid(grid):
    """
    Use static color palette table to change color of grid
    """
    fig = Figure()
    makecpt(cmap="relief")
    fig.grdimage(grid, projection="W0/6i")
    return fig


@pytest.mark.mpl_image_compare
def test_makecpt_to_plot_grid_scaled_with_series(grid):
    """
    Use static color palette table scaled to a min/max series to change color of grid
    """
    fig = Figure()
    makecpt(cmap="oleron", series="-4500/4500")
    fig.grdimage(grid, projection="W0/6i")
    return fig


def test_makecpt_output_to_cpt_file():
    """
    Save the generated static color palette table to a .cpt file
    """
    with GMTTempFile(suffix=".cpt") as cptfile:
        makecpt(output=cptfile.name)
        assert os.path.exists(cptfile.name)


def test_makecpt_blank_output():
    """
    Use incorrect setting by passing in blank file name to output parameter
    """
    with pytest.raises(GMTInvalidInput):
        makecpt(output="")


def test_makecpt_invalid_output():
    """
    Use incorrect setting by passing in invalid type to output parameter
    """
    with pytest.raises(GMTInvalidInput):
        makecpt(output=["some.cpt"])
