"""
solar - Plot day-night terminators.
"""

import datetime

import pandas as pd
from pygmt.clib import Session
from pygmt.exceptions import GMTInvalidInput
from pygmt.helpers import build_arg_string, fmt_docstring, kwargs_to_strings, use_alias


@fmt_docstring
@use_alias(
    R="region",
    J="projection",
    G="fill",
    B="frame",
    W="pen",
    U="timestamp",
    V="verbose",
    X="xshift",
    Y="yshift",
    c="panel",
    p="perspective",
    t="transparency",
)
@kwargs_to_strings(R="sequence", p="sequence")
def solar(self, terminator="d", terminator_datetime=None, **kwargs):
    r"""
    Plot day-light terminators.

    This function plots the day-night terminator. Additionally, it can
    plot the terminators for civil twilight, nautical twilight, and
    astronomical twilight.

    {aliases}

    Parameters
    ----------
    terminator : str
        Set the type of terminator displayed. Valid arguments are
        **day_night**, **civil**, **nautical**, and **astronomical**, which
        can be set with either the full name or the first letter of the name.
        [Default is **day_night**\ ]
    terminator_datetime : str or datetime object
        Set the UTC date and time of the displayed terminator. It can be
        passed as a string or a datetime object.
        [Default is the current UTC date and time]
    {R}
    {J}
    {B}
    fill : str
        Color or pattern for filling of terminators.
    pen : str
        Set pen attributes for lines. The default pen
        is ``default,black,solid``.
    {U}
    {V}
    {XY}
    {c}
    {p}
    {t}
    """
    # TODO: Incorporate "-T+zTZ"

    kwargs = self._preprocess(**kwargs)  # pylint: disable=protected-access
    if "T" in kwargs:
        raise GMTInvalidInput(
            "Use 'terminator' and 'terminator_datetime' instead of 'T'."
        )
    if terminator not in [
        "day_night",
        "nautical",
        "civil",
        "astronomical",
        "astro",
        "d",
        "n",
        "c",
        "a",
    ]:
        raise GMTInvalidInput(
            f"Unrecognized solar terminator type '{terminator}'. Valid values "
            "are 'day_night', 'civil', 'nautical', and 'astronomical'."
        )
    kwargs["T"] = terminator[0]
    if terminator_datetime:
        try:
            datetime_string = pd.to_datetime(terminator_datetime).strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        except ValueError as verr:
            raise GMTInvalidInput("Unrecognized datetime format.") from verr
        kwargs["T"] += f"+d{datetime_string}" 
    with Session() as lib:
        lib.call_module("solar", build_arg_string(kwargs))
