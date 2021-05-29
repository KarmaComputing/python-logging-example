import logging
import os

PYTHON_LOG_LEVEL = os.getenv("PYTHON_LOG_LEVEL", "DEBUG")

# Links
# https://docs.python-guide.org/writing/logging/


# https://docs.python.org/3/library/logging.html#logging.getLogger
# if name is None, return a logger which is the root logger of the hierarchy
logger = (
    logging.getLogger()
)  # Will return root logger, don't set this to __name__ in this rool level logger, otherwise default formatting or handlers are not set

# https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
handler = logging.StreamHandler()  # sys.stderr will be used by default

formatter = logging.Formatter(
    "%(asctime)s %(name)-12s %(levelname)-8s %(message)s %(funcName)s %(pathname)s:%(lineno)d"
)  # noqa

# https://docs.python.org/3/library/logging.html#logging.Handler
handler.setFormatter(formatter)
handler.setLevel(
    PYTHON_LOG_LEVEL
)  # Both loggers and handlers have a setLevel method  noqa
logger.addHandler(handler)

logger.setLevel(PYTHON_LOG_LEVEL)
