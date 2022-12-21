# depthcrawler

- crawler.py ( application logic )
- crawl.log  ( error logs while crawling )
- customlog.py ( logger object used to log and debug )
- output.json ( ouptut captured while data being crawled )
- requirements.txt ( all libraries required )
- storage.py ( singleton storage class )
- tests  ( unit test )
  - |_  crawler_tests.py

# To Install
```pip install -r requirements.txt```

# To Run
```python crawler.py website_url 1```

# To Test
```python -m unittest tests.crawler_test```
