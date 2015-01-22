# -*- coding: utf-8 -*-

from operator import itemgetter
from csv import DictReader

from fn import F

from . import load as _load

__all__ = ('iter_parse', 'load')


def _normalize_value(value):
    return None if float(value) == 0.0 else float(value)

def _normalize_synset(value):
    return value.split('#')[0].replace("-","_")


def iter_parse(path):
    with open(path, 'r') as fin:
        rdr = DictReader(fin)
        for record in rdr:
            yield record


def load(path):
    print itemgetter('SynsetTerms')
    value_getter = F(itemgetter('Score')) >> _normalize_value
    synset_getter = F(itemgetter('SynsetTerms')) >> _normalize_synset
    return _load(path, iter_parse, key=synset_getter, value=value_getter)
