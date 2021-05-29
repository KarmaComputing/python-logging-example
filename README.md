# Python logging example

- Set log level by environment var (`PYTHON_LOG_LEVEL`)
- Defaults to log all logging messages
- Change log level easily by changing `PYTHON_LOG_LEVEL` env


# What is useful logging? (opinion)
When there's a problem I want to see:

- Filename => so I know where to look
- Line number => so I know exactly where to start looking
- Contexual error message => "Database bad credentials" is better than "There was an error"
- The function name executing at the time 
- Level of log (is it a critial, error or just information?)

## Example helpful log:

```
2021-05-29 15:51:06,186 mymodule     WARNING  Hello from example() example /home/fred/code/python/logging-example/pythonlogging/mymodule.py:7
```

From the above log we get:
- *mymodule* - the name of the python module
- *WARNING*  - The level of the log message
- *example*  - The name of the name of the containing function
- *File path and line number* - The exact file path and line number

Don't confuse the above with security.

Logging can reduced with (using PYTHON_LOG_LEVEL=CRITICAL for example), and all logging is
sent to stderr which may be redirected.

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


## Links

- https://docs.python.org/3/library/logging.html#logrecord-attributes
- https://docs.python-guide.org/writing/logging/
- https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial
- gnu_lorien - https://stackoverflow.com/a/16993115/885983