#!/usr/bin/env python
# -*- coding: utf-8 -*-

# usage: $ python stroke-font.py votre.ufo outputfont.otf

import fontforge
import sys

font = fontforge.open(sys.argv[1])

for glyph in font.glyphs():
    # ("circular",width[,linecap,linejoin,flags])
    # ("eliptical",width,minor-width,angle[,linecap,linejoin,flags])
    # ("caligraphic",width,height,angle[,flags])
    # ("polygonal",contour[,flags])

    # Parce que maintenant il y a encore des fonts déjà doublé
    # dedans, on fait pas le stroke (ça cause des soucis autrement)
    # glyph.stroke("circular", 50, "square", "round")
    pass

font.generate(sys.argv[2])

"""
glyph.stroke()

Strokes the contours of the glyph using one of the indicated pens. Line cap may be one of

    butt
    round
    square 

line join may be

    miter
    round
    bevel 

flags is a tuple containing some of the following strings

    removeinternal
    removeexternal
    cleanup 

If a polygonal pen is specified, the contour must be a closed convex polygon (no curved edges) with fewer than 100 vertices.
"""
