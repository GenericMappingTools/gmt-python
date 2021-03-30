"""
Tests colorbar.
"""
import pytest
from pygmt import Figure


@pytest.mark.mpl_image_compare
def test_colorbar_using_paper_coordinates():
    """
    Create colorbar positioned at 0cm,0cm with length 1cm and width 0.5cm.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_positioned_using_map_coordinates():
    """
    Create colorbar positioned at longitude,latitude 3,6 with length 2cm.
    """
    fig = Figure()
    fig.basemap(region=[2, 4, 6, 8], projection="t0/2c", frame=True)
    fig.colorbar(cmap="rainbow", position="g3/6+w2c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_positioned_using_normalized_coords():
    """
    Create colorbar at normalized coordinates 0.75,0.25 with length 2cm.
    """
    fig = Figure()
    fig.basemap(region=[2, 4, 6, 8], projection="t0/2c", frame=True)
    fig.colorbar(cmap="rainbow", position="n0.75/0.25+w2c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box():
    """
    Create colorbar with box around it.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box=True, position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_fill():
    """
    Create colorbar with box that has a different colored fill.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+gorange", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_truncated_to_zlow_zhigh():
    """
    Create colorbar truncated to z-low and z-high.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", truncate=[0.15, 0.85], position="x0c/0c+w2c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_scaled_z_values():
    """
    Create colorbar with z-values scaled to 0.1x of the original CPT.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", scale=0.1, position="x0c/0c+w2c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_shading_boolean():
    """
    Create colorbar and set shading with a Boolean value.
    """
    fig = Figure()
    fig.basemap(region=[0, 10, 0, 10], projection="X15c", frame="a")
    fig.colorbar(cmap="geo", shading=True)
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_shading_list():
    """
    Create colorbar and set shading by passing the high/low values as a list.
    """
    fig = Figure()
    fig.basemap(region=[0, 10, 0, 10], projection="X15c", frame="a")
    fig.colorbar(cmap="geo", shading=[-0.7, 0.2])
    return fig
