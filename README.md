# Python logging example

- Set log level by environment var (`PYTHON_LOG_LEVEL`)
- Defaults to log all logging messages
- Change log level easily by changing `PYTHON_LOG_LEVEL` env


## Display all logging messages

```
export PYTHON_LOG_LEVEL=DEBUG
python3 __init__.py

2021-05-28 13:18:08,163 root         CRITICAL This is a critical message
2021-05-28 13:18:08,163 root         ERROR    This is an error  message
2021-05-28 13:18:08,163 root         WARNING  This is a warning message
2021-05-28 13:18:08,163 root         INFO     This is an info message
2021-05-28 13:18:08,163 root         DEBUG    This is a debug message
2021-05-28 13:18:08,163 root         DEBUG    Hello
2021-05-28 13:18:08,163 root         DEBUG    Saying hello from sayHello!

```

## Only display log messages equal or greater than WARNING
```
export PYTHON_LOG_LEVEL=WARNING
python3 __init__.py

2021-05-28 13:19:14,901 root         CRITICAL This is a critical message
2021-05-28 13:19:14,902 root         ERROR    This is an error  message
2021-05-28 13:19:14,902 root         WARNING  This is a warning message
```

## Only display log messages equal or greater than INFO
```
export PYTHON_LOG_LEVEL=INFO
python3 __init__.py

2021-05-28 13:19:55,396 root         CRITICAL This is a critical message
2021-05-28 13:19:55,396 root         ERROR    This is an error  message
2021-05-28 13:19:55,396 root         WARNING  This is a warning message
2021-05-28 13:19:55,396 root         INFO     This is an info message
```

## Only display log CRITICAL messages
```
export PYTHON_LOG_LEVEL=CRITICAL
python3 __init__.py

2021-05-28 13:20:33,671 root         CRITICAL This is a critical message
```
