#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import json
import unicodedata
from elasticsearch import Elasticsearch
import numpy as np

es = Elasticsearch(host='0.0.0.0', port=9200)
index = "pst"

conn = sqlite3.connect('test.sqlite3')
cur = conn.cursor()
cur.execute('SELECT * FROM message')
rows = cur.fetchall()
rows_json = json.dumps(rows)
chunk = unicodedata.normalize('NFKD', np.unicode(rows_json, 'utf-8', 'ignore')).encode('ASCII', 'ignore').replace('[', '').replace(']', '').replace('"null"', 'null').replace(
    '999999.99', '0.0')
res = es.index(index=index, body=chunk)
print("Result - Created : ", (res['created']), "OK\n")



