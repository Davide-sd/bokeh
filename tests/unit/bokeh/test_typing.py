#-----------------------------------------------------------------------------
# Copyright (c) Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from typing import Literal, assert_type

# Bokeh imports
from bokeh.models import GlyphRenderer, LegendItem
from bokeh.models.glyph import Glyph
from bokeh.plotting import figure

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def test_figure_list_attr_splat() -> None:
    p = figure()
    p.scatter([1, 2, 3], [1, 2, 3], legend_label="scatter")

    assert_type(p.axis.dimension, Literal[0, 1, "auto"])
    assert_type(p.xaxis.dimension, Literal[0, 1, "auto"])
    assert_type(p.yaxis.dimension, Literal[0, 1, "auto"])

    assert_type(p.grid.dimension, Literal[0, 1])
    assert_type(p.xgrid.dimension, Literal[0, 1])
    assert_type(p.ygrid.dimension, Literal[0, 1])

    assert_type(p.legend.items, list[LegendItem] | list[tuple[str, list[GlyphRenderer[Glyph]]]])
    assert_type(p.hover.show_arrow, bool)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
