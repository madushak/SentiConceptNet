# -*- coding: utf-8 -*-

import csv
from collections import Counter, namedtuple
from sys import stderr
from itertools import imap
from itertools import compress
from sklearn.preprocessing import MinMaxScaler

__all__ = ('dictionary',)


# def _save(path, dict_data):
    # with open(path, 'wb') as outfile:
        # csv_writer = csv.writer(outfile, delimiter='\t')
        # for k,v,x,c,b in dict_data:
            # csv_writer.writerow([k, v, x, c, b])

# def dictionary(dict_path, nodes, anew, sn, swn, pred, rels, edges):
    # #print pred
    # keyset = [i for i,v in enumerate(pred) if v is not None]
    # expected_range = list(range(len(pred)))
    # #print expected_range
    # nont_none_pred = [x for x in pred if x is not None]
    # #list(itertools.compress(pred, keyset))
    # min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
    # not_none_pred = min_max_scaler.fit_transform(nont_none_pred)
    # pred_dict = dict(zip(keyset, not_none_pred))
	
    # for i,v in enumerate(pred):
        # if v is not None:
            # pred[i] = pred_dict[i]
			
	# #print pred
   
   # #pred = [i for i,v in enumerate(keyset) if v is not None]
	
    # idx_map = dict((c, i) for i, c in enumerate(nodes))
    # result = []
    # result.append(["Term", "Score", "ANEW", "ScnticNet", "SentiWordNet"])
    # for target in idx_map:
        # try:
            # idx = idx_map[target]
            # #print idx
        # except KeyError:
            # stderr.write('[ERROR] concept "{0}" doesn\'t exist.\n'.format(target))
            # continue
        # result.append([target, pred[idx], anew[idx], sn[idx], swn[idx]])
    
    # _save(dict_path, result)
	
def _save(path, dict_data):
    with open(path, 'wb') as outfile:
        csv_writer = csv.writer(outfile, delimiter='\t')
        for k,v,x,c,b in dict_data:
            csv_writer.writerow([k, v, x, c, b])

def dictionary(dict_path, nodes, anew, sn, swn, pred, rels, edges):
    idx_map = dict((c, i) for i, c in enumerate(nodes))
    result = []
    result.append(["Term", "Score", "ANEW", "ScnticNet", "SentiWordNet"])
    for target in idx_map:
        try:
            idx = idx_map[target]
        except KeyError:
            stderr.write('[ERROR] concept "{0}" doesn\'t exist.\n'.format(target))
            continue
        result.append([target, pred[idx], anew[idx], sn[idx], swn[idx]])
    
    _save(dict_path, result)