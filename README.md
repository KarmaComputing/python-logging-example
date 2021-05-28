# Python logging example

- Set log level by environment var (`PYTHON_LOG_LEVEL`)
- Defaults to log all logging messages
- Change log level easily by changing `PYTHON_LOG_LEVEL` env

```
# Display all logging messages
export PYTHON_LOG_LEVEL=DEBUG
python3 __init__.py

# Only display log messages equal or greater than WARNING
export PYTHON_LOG_LEVEL=WARNING
python3 __init__.py

# Only display log messages equal or greater than info
export PYTHON_LOG_LEVEL=INFO
python3 __init__.py

# Only display log CRITICAL messages 
export PYTHON_LOG_LEVEL=CRITICAL
python3 __init__.py


```
