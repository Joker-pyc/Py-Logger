# py-logger

A flexible and feature-rich logging module for Python projects that provides both file and console logging capabilities with advanced configuration options.

## Features

- 📝 Both file and console logging support
- 🔄 Automatic log rotation (time-based or size-based)
- 📅 Timestamp-based log file naming
- 🎨 Customizable log formatting
- 📊 Multiple logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- 🔧 Highly configurable
- 🚀 Easy to integrate into any Python project

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/py-logger.git
```

2. Copy the `py_logger.py` file to your project directory.

3. Import the `PyLogger` class in your Python files.

## Basic Usage

```python
from py_logger import PyLogger

# Create a basic logger
logger = PyLogger(logger_name="MyApp")

# Log messages at different levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Log exceptions with traceback
try:
    raise ValueError("An example error")
except Exception as e:
    logger.exception(f"An error occurred: {str(e)}")
```

## Advanced Configuration

### Full Configuration Example

```python
logger = PyLogger(
    logger_name="MyAdvancedApp",
    log_level=logging.INFO,
    log_format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d)',
    log_file_path='logs/custom_log.log',
    rotate_logs=True,
    max_bytes=1_048_576,  # 1MB
    backup_count=3,
    rotate_when='D',  # Daily rotation
    console_output=True
)
```

### Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| logger_name | str | 'PyLogger' | Name of the logger instance |
| log_level | int | logging.INFO | Minimum logging level |
| log_format | str | '%(asctime)s - %(name)s - %(levelname)s - %(message)s' | Format string for log messages |
| log_file_path | str | None | Custom path for log file (default: logs/[logger_name]_[date].log) |
| rotate_logs | bool | True | Enable/disable log rotation |
| max_bytes | int | 5_242_880 (5MB) | Maximum size of each log file |
| backup_count | int | 5 | Number of backup files to keep |
| rotate_when | str | 'midnight' | When to rotate logs ('S', 'M', 'H', 'D', 'midnight') |
| console_output | bool | True | Enable/disable console output |

## Log Rotation

### Size-based Rotation
When `rotate_logs` is True and `max_bytes` is set, logs will rotate when the file size exceeds the specified limit:

```python
logger = PyLogger(
    rotate_logs=True,
    max_bytes=1_048_576,  # 1MB
    backup_count=3
)
```

### Time-based Rotation
Configure time-based rotation using the `rotate_when` parameter:

```python
logger = PyLogger(
    rotate_logs=True,
    rotate_when='D',  # Daily rotation
    backup_count=5
)
```

Available rotation intervals:
- 'S': Seconds
- 'M': Minutes
- 'H': Hours
- 'D': Days
- 'midnight': Roll over at midnight

## Custom Log Format

You can customize the log format using standard Python logging format strings:

```python
logger = PyLogger(
    log_format='%(asctime)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d)'
)
```

Available format attributes:
- %(asctime)s: Timestamp
- %(name)s: Logger name
- %(levelname)s: Log level
- %(message)s: Log message
- %(filename)s: Source file name
- %(lineno)d: Line number
- %(pathname)s: Full pathname
- %(module)s: Module name
- %(funcName)s: Function name

## Error Handling

The logger provides special handling for exceptions:

```python
try:
    # Your code here
    raise ValueError("Something went wrong")
except Exception as e:
    logger.exception(f"An error occurred: {str(e)}")
    # This will automatically include the full traceback
```

## Log Files Location

By default, logs are stored in a `logs` directory in your project:
- Default path: `logs/[logger_name]_[YYYYMMDD].log`
- The directory is automatically created if it doesn't exist

## Best Practices

1. Create a single logger instance for each module or component:
```python
logger = PyLogger(logger_name=__name__)
```

2. Use appropriate log levels:
- DEBUG: Detailed information for debugging
- INFO: General information about program execution
- WARNING: Indicate a potential problem
- ERROR: A more serious problem
- CRITICAL: Program may not be able to continue

3. Include contextual information in log messages:
```python
logger.info(f"Processing file: {filename}")
logger.error(f"Failed to connect to database at {db_url}")
```

4. Configure log rotation based on your application's needs:
- Use size-based rotation for applications with variable logging frequency
- Use time-based rotation for applications that need logs organized by time periods

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License - see the LICENSE file for details.

## Acknowledgments

- Built with Python's built-in logging module
- Inspired by the need for a simple yet flexible logging solution