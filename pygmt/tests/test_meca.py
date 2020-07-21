"""
Tests for meca
"""
import os
import pandas as pd
import numpy as np
import pytest

from .. import Figure


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


@pytest.mark.mpl_image_compare
def test_meca_spec_dictionary():
    """
    Test supplying a dictionary containing a single focal mechanism to the
    `spec` argument.
    """

    fig = Figure()

    # Right lateral strike slip
    fig.meca(
        dict(strike=0, dip=90, rake=0, magnitude=5),
        lon=0,
        lat=5,
        depth=0,
        scale="2.5c",
        region=[-1, 4, 0, 6],
        projection="M14c",
        frame=2,
    )

    # Left lateral strike slip
    fig.meca(
        dict(strike=0, dip=90, rake=180, magnitude=5),
        lon=2,
        lat=5,
        depth=0,
        scale="2.5c",
    )

    # Thrust
    fig.meca(
        dict(strike=0, dip=45, rake=90, magnitude=5),
        lon=0,
        lat=3,
        depth=0,
        scale="2.5c",
    )
    fig.meca(
        dict(strike=45, dip=45, rake=90, magnitude=5),
        lon=2,
        lat=3,
        depth=0,
        scale="2.5c",
    )

    # Normal
    fig.meca(
        dict(strike=0, dip=45, rake=-90, magnitude=5),
        lon=0,
        lat=1,
        depth=0,
        scale="2.5c",
    )
    fig.meca(
        dict(strike=45, dip=45, rake=-90, magnitude=5),
        lon=2,
        lat=1,
        depth=0,
        scale="2.5c",
    )

    # Mixed
    fig.meca(
        dict(strike=10, dip=35, rake=129, magnitude=5),
        lon=3.4,
        lat=0.6,
        depth=0,
        scale="2.5c",
    )

    return fig


@pytest.mark.mpl_image_compare
def test_meca_spec_dict_list():
    """
    Test supplying a dictionary containing a list of focal mechanism to the
    `spec` argument.
    """

    fig = Figure()

    # supply focal mechanisms as a dict of lists
    focal_mechanisms = dict(
        strike=[330, 350], dip=[30, 50], rake=[90, 90], magnitude=[3, 2]
    )

    fig.meca(
        focal_mechanisms,
        lon=[-124.3, -124.4],
        lat=[48.1, 48.2],
        depth=[12.0, 11.0],
        region=[-125, -122, 47, 49],
        scale="2c",
        projection="M14c",
    )

    return fig


@pytest.mark.mpl_image_compare
def test_meca_spec_dataframe():
    """
    Test supplying a pandas DataFrame containing focal mechanisms and
    locations to the `spec` argument.
    """

    fig = Figure()

    # supply focal mechanisms to meca as a dataframe
    focal_mechanisms = dict(
        strike=[324, 353],
        dip=[20.6, 40],
        rake=[83, 90],
        magnitude=[3.4, 2.9],
        lon=[-124, -124.4],
        lat=[48.1, 48.2],
        depth=[12, 11.0],
    )
    df = pd.DataFrame(data=focal_mechanisms)

    fig.meca(df, region=[-125, -122, 47, 49], scale="2c", projection="M14c")

    return fig


@pytest.mark.mpl_image_compare
def test_meca_spec_1D_array():
    """
    Test supplying a 1D numpy array containing focal mechanisms and
    locations to the `spec` argument.
    """

    fig = Figure()

    # supply focal mechanisms to meca as a 1D numpy array, here we are using
    # the Harvard CMT zero trace convention but the focal mechanism
    # parameters may be specified any of the available conventions. Since we
    # are not using a dict or dataframe the convention and component should
    # be specified.
    focal_mechanism = [
        -127.40,
        40.87,
        12,
        -3.19,
        0.16,
        3.03,
        -1.02,
        -3.93,
        -0.02,
        23,
        0,
        0,
    ]
    focal_mech_array = np.asarray(focal_mechanism)

    fig.meca(
        focal_mech_array,
        convention="mt",
        component="full",
        region=[-128, -127, 40, 41],
        scale="2c",
        projection="M14c",
    )

    return fig
