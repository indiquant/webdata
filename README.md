# webdata

web scraper to retrieve live options data from NSE (National Stock Exchange of India) and store in a local sqlite db

####Keywords: NSE options, NSE futures, web scraper, NSE website, NIFTY options, NIFTY futures, NSE, NIFTY, NSE live options, NSE live
 
Currently the following features are available:
  1. /webdata/examples/nse_options.py parses the last snapshot of options data available in the NSE website and loads in the c:\temp\webdata.sqlite3 database, table options_intraday
  2. all the accompanying parsing functions are available in /webdata/scrapers/nse.py
  3. Loading futures data will also be added in subsequent work
  
 
The project was inspired by http://quantsnippets.blogspot.com/2014/01/get-option-dataspot-price-from-nse.html
  
