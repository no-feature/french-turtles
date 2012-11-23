#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The FONTLOG is SIL’s concept of a chancelog for a font. When doing a release, 
we generate one automatically based on the repository history.

An example of a FONTLOG:
http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=OFL-FAQ_web#11bc4f28
(pretty url’s wouldn’t hurt the SIL)

"""

from textwrap import fill, TextWrapper
from subprocess import Popen, PIPE
import sys

# Get the data

LOG = Popen(['git','log','--reverse'], stdout=PIPE)

# Setup TextWrap instances

wrapper = TextWrapper(width=82)
commit_msg_wrapper = TextWrapper(subsequent_indent='    ', width=82)

# Print FONTLOG to stdout

print """
FRENCH TURTLES FONTLOG
The history of these typefaces

generated from the GIT source repository

For more info on authors, licensing: see OFL.txt

"""

for line in LOG.stdout:
    if len(line) > 82:
        print commit_msg_wrapper.fill(line)
    else:
        print line,

