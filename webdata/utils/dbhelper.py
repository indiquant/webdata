__author__ = 'anishghosh'

import os
import sqlite3
from qrymaker import qry_createtable

_DB = r'C:\temp\strat\webdata.sqlite3'


def dbname():
    return _DB


def createfileifmissing(fname):
    if not os.path.exists(fname):
        open(fname, 'w')


def createtable(dbname, tname, colnames, coltypes, pkeys):
    conn = sqlite3.connect(dbname)

    _qry = qry_createtable(tname, colnames, coltypes, pkeys)

    conn.execute(_qry)

    conn.commit()


def create_table(tname, colnames, coltypes, primarykeys):
    conn = sqlite3.connect(_DB)

    _qry = qry_createtable(tname, colnames, coltypes, primarykeys)

    conn.execute(_qry)

    conn.commit()


def bulkinsert(dbname, tname, colnames, rows):
    conn = sqlite3.connect(dbname)

    _qry = "INSERT OR REPLACE INTO " + tname + " ("

    for cname in colnames:
        _qry += ' ' + cname + ','

    _qry = _qry.rstrip(',')
    _qry += ') VALUES ('

    for cname in colnames:
        _qry += ' ?,'

    _qry = _qry.rstrip(',')
    _qry += ')'

    for _row in rows:
        conn.execute(_qry, _row)

    conn.commit()


def bulkinsert_codes(tname, colnames, rows):
    conn = sqlite3.connect(_DB)

    _qry = "INSERT OR REPLACE INTO " + tname + " ("

    for cname in colnames:
        _qry += ' ' + cname + ','

    _qry = _qry.rstrip(',')
    _qry += ') VALUES ('

    for cname in colnames:
        _qry += ' ?,'

    _qry = _qry.rstrip(',')
    _qry += ')'

    for _row in rows:
        conn.execute(_qry, _row)

    conn.commit()


def execute_r(qry):
    conn = sqlite3.connect(_DB)
    try:
        cur = conn.cursor()
        cur.execute(qry)
        x = cur.fetchall()
        conn.close()
        return x

    except sqlite3.OperationalError:
        conn.close()
        return None


def execute_w(dbname, qry):
    conn = sqlite3.connect(dbname)
    try:
        cur = conn.cursor()
        cur.execute(qry)
        conn.commit()
        conn.close()

    except sqlite3.OperationalError:
        conn.close()
        return None


if __name__ == '__main__':
    qry = "SELECT * FROM codes WHERE undltype='S'"
    x = execute_r(qry)
    print 'pause'
