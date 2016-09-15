# webdata
web scraper to get data

Keywords: NSE options, NSE futures, web scraper, NSE website, NIFTY options, NIFTY futures
 
Currently the following features are available:
  1. nse_options.py parses the last snapshot of options data available in the NSE website and loads in the c:\temp\webdata.sqlite3 database, table options_intraday
  2. all the accompanying/parsing functions are available in /webdata/scrapers/nse.py
  3. Loading futures data will also be added in subsequent work
  
 
The project was inspired by http://quantsnippets.blogspot.com/2014/01/get-option-dataspot-price-from-nse.html
  