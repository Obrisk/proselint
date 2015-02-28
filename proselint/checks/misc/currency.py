# -*- coding: utf-8 -*-
"""MSC110: Currency.

---
layout:     post
error_code: MSC110
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      symbols
date:       2014-06-10 12:31:19
categories: writing
---

Symbols.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "MSC110"
    msg = u"Incorrent use of symbols in {}."

    symbols = [
        "\$[\d]* ?(?:dollars|usd|us dollars)"
    ]

    return existence_check(blob, symbols, err, msg)
