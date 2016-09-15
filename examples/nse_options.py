__author__ = 'anishghosh'


from datetime import date, datetime, time
from bs4 import BeautifulSoup
import time as tm
from webdata.scrapers.nse import *
from webdata.utils.dbhelper import *


DB = r'C:\temp\webdata.sqlite3'


NSE_OPN_EST = time(11, 30, 0)
NSE_CLS_EST = time(6, 30, 0)


NSE_OPTION_EXPIRIES = ['2016-09-29',
                       '2016-10-27',
                       '2016-11-24',
                       '2016-12-29',
                       '2017-03-30']

cols = [EnumDBOptionTable.undl.name,
        EnumDBOptionTable.undl_type.name,
        EnumDBOptionTable.spot.name,
        EnumDBOptionTable.opt_type.name,
        EnumDBOptionTable.exc_type.name,
        EnumDBOptionTable.expiry.name,
        EnumDBOptionTable.strike.name,
        EnumDBOptionTable.recdate.name,
        EnumDBOptionTable.rectime.name,
        EnumDBOptionTable.bidpx.name,
        EnumDBOptionTable.bidqty.name,
        EnumDBOptionTable.askpx.name,
        EnumDBOptionTable.askqty.name,
        EnumDBOptionTable.lastpx.name,
        EnumDBOptionTable.volume.name]

coltypes = ['TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'INTEGER',
            'REAL',
            'INTEGER',
            'INTEGER',
            'REAL',
            'REAL',
            'REAL',
            'REAL',
            'REAL',
            'REAL']

pkeys = [EnumDBOptionTable.undl.name,
         EnumDBOptionTable.opt_type.name,
         EnumDBOptionTable.exc_type.name,
         EnumDBOptionTable.expiry.name,
         EnumDBOptionTable.strike.name,
         EnumDBOptionTable.recdate.name,
         EnumDBOptionTable.rectime.name]


def mkemptytable():
    createfileifmissing(DB)
    createtable(DB, 'options_intraday', cols, coltypes, pkeys)


def flush(undl, exc_type, expiry, recdtime):

    qry = "DELETE FROM options_intraday WHERE {colundl}='{undl}' AND {colexctype}='{exc_type}'" \
          + " AND {colexpiry}={expiry} AND {colrecdate}={recdate} AND {colrectime}={rectime}"

    qry = qry.format(colundl=EnumDBOptionTable.undl.name, undl=undl,
                     colexctype=EnumDBOptionTable.exc_type.name, exc_type=exc_type,
                     colexpiry=EnumDBOptionTable.expiry.name, expiry=yyyymmdd(expiry),
                     colrecdate=EnumDBOptionTable.recdate.name, recdate=yyyymmdd(recdtime),
                     colrectime=EnumDBOptionTable.rectime.name, rectime=hhmmss(recdtime))

    print(qry)

    execute_w(DB, qry)


def main():

    mkemptytable()

    while True:

        for undl, undltype in [('NIFTY', 'index')]:

            for exp in NSE_OPTION_EXPIRIES:
                pg = get_option_page(undl, exp, undltype)
                sp = BeautifulSoup(pg)
                t, s = get_live(sp.body)
                opts = get_options(sp.body)
                df = get_sql_df(undl, t, s, exp, opts, undltype)
                flush(undl, 'E', datetime.strptime(exp, '%Y-%m-%d'), t)
                bulkinsert(DB, 'options_intraday', cols, df.to_records(index=False).tolist())

        tm.sleep(30)

        nw = datetime.now()
        if time(nw.hour, nw.minute, nw.second) >= NSE_CLS_EST:
            break


if __name__ == '__main__':
    main()