__author__ = 'anishghosh'


def qry_createtable(tname, colnames, coltypes, primarykeys):
    _qry = 'CREATE TABLE IF NOT EXISTS ' + tname + ' ('

    for pk in primarykeys:
        _pktype = coltypes[colnames.index(pk)]
        _qry += ' ' + pk + ' ' + _pktype + ' NOT NULL,'
        # _qry += ' ' + pk + ' ' + _pktype + ' PRIMARY KEY NOT NULL,'

    for cname in colnames:
        if cname not in primarykeys:
            _cntype = coltypes[colnames.index(cname)]
            _qry += ' ' + cname + ' ' + _cntype + ','

    _qry += ' PRIMARY KEY ('

    for pk in primarykeys:
        _qry += ' ' + pk + ','

    _qry = _qry.rstrip(',')

    _qry += '));'

    return _qry


if __name__ == '__main__':
    print qry_createtable('transcodes',
                          ['code', 'dbname', 'description'],
                          ['TEXT', 'TEXT', 'TEXT'],
                          ['code', 'dbname'])