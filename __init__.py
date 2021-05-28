import logging
import os
from mymodule import example
from mysubmodule.anotherthing import sayHello

PYTHON_LOG_LEVEL = os.getenv("PYTHON_LOG_LEVEL", "DEBUG")

# Links
# https://docs.python-guide.org/writing/logging/


# https://docs.python.org/3/library/logging.html#logging.getLogger
# if name is None, return a logger which is the root logger of the hierarchy
logger = logging.getLogger()  # Will return root logger

# https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
handler = logging.StreamHandler()  # sys.stderr will be used by default

formatter = logging.Formatter(
    "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
)  # noqa

# https://docs.python.org/3/library/logging.html#logging.Handler
handler.setFormatter(formatter)
handler.setLevel(
    PYTHON_LOG_LEVEL
)  # Both loggers and handlers have a setLevel method  noqa
logger.addHandler(handler)
logger.setLevel(PYTHON_LOG_LEVEL)

# Use the debugger
logger.critical("This is a critical message")
logger.error("This is an error  message")
logger.warning("This is a warning message")
logger.info("This is an info message")
logger.debug("This is a debug message")

example()
sayHello()
