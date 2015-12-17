# Steve's Web scraper

This is a simple Selenium Webdriver API endpoint for scraping business data from websites. Pass it a json dict formatted like sample.json, with xpaths for all your elements, and it will construct a csv with the results. Each term in the JSON gets its own column. You can sort out the columns later.

To get stuff:

> python generic_request.py --jsonsource `filename` --server `server-path`

jsonsource defaults to sample.json in the same directory. server defaults to my server endpoint until January, then you can override it once you get the server scripts running locally.  Or tell me when you want to do some work and I can spin it back up.
