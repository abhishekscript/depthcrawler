import logging
 
# Setup basi logger with time format along with event
logging.basicConfig(
    filename="crawl.log", format='%(asctime)s %(message)s', filemode='w'
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
