# coding=utf-8
import numpy as np
from feature import Counter, Feature
import sqlite3


db = sqlite3.connect('ptt.db')
cur = db.execute('select * from articles')
f = Feature()
a = 0
for i in cur:
    a += 1
    try:
        f.features(i[5])
    except:
        print(i[5])
    print(f.size())

f.store()
