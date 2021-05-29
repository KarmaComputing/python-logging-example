from mymodule import example
from mysubmodule.anotherthing import sayHello
from logger import logger


# Use the debugger
logger.critical("This is a critical message")
logger.error("This is an error  message")
logger.warning("This is a warning message")
logger.info("This is an info message")
logger.debug("This is a debug message")

example()
sayHello()
