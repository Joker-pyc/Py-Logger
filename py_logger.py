"""
py-logger: A flexible and feature-rich logging module for Python projects
GitHub: https://github.com/Joker-Pyc/py-logger
Author: Joker-pyc
License: Apache License 2.0
"""

import logging
import os
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from typing import Optional, Union

class PyLogger:
    """
    A configurable logger class that can be used across any project.
    Supports both file and console logging with different log levels,
    rotating file handlers, and custom formatting.
    """
    
    def __init__(
        self,
        logger_name: str = 'PyLogger',
        log_level: int = logging.INFO,
        log_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        log_file_path: Optional[str] = None,
        rotate_logs: bool = True,
        max_bytes: int = 5_242_880,  # 5MB
        backup_count: int = 5,
        rotate_when: str = 'midnight',
        console_output: bool = True
    ):
        """
        Initialize the logger with specified configuration.
        
        Args:
            logger_name (str): Name of the logger
            log_level (int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_format (str): Format string for log messages
            log_file_path (str): Path to log file (if None, uses default path)
            rotate_logs (bool): Whether to use rotating file handler
            max_bytes (int): Maximum size of each log file
            backup_count (int): Number of backup files to keep
            rotate_when (str): When to rotate logs ('S', 'M', 'H', 'D', 'midnight')
            console_output (bool): Whether to output logs to console
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        
        # Clear any existing handlers
        self.logger.handlers = []
        
        # Create formatter
        self.formatter = logging.Formatter(log_format)
        
        # Setup file logging
        if log_file_path:
            self.log_file_path = log_file_path
        else:
            # Create logs directory if it doesn't exist
            os.makedirs('logs', exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d')
            self.log_file_path = f'logs/{logger_name}_{timestamp}.log'
        
        if rotate_logs:
            # Use TimedRotatingFileHandler
            file_handler = TimedRotatingFileHandler(
                self.log_file_path,
                when=rotate_when,
                interval=1,
                backupCount=backup_count
            )
        else:
            # Use RotatingFileHandler
            file_handler = RotatingFileHandler(
                self.log_file_path,
                maxBytes=max_bytes,
                backupCount=backup_count
            )
        
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
        
        # Setup console logging
        if console_output:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(self.formatter)
            self.logger.addHandler(console_handler)
    
    def set_level(self, level: Union[int, str]) -> None:
        """Set the logging level."""
        if isinstance(level, str):
            level = getattr(logging, level.upper())
        self.logger.setLevel(level)
    
    def add_handler(self, handler: logging.Handler) -> None:
        """Add a custom handler to the logger."""
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)
    
    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log an info message."""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log an error message."""
        self.logger.error(message)
    
    def critical(self, message: str) -> None:
        """Log a critical message."""
        self.logger.critical(message)
    
    def exception(self, message: str) -> None:
        """Log an exception message with traceback."""
        self.logger.exception(message)

# Usage example
if __name__ == "__main__":
    # Basic usage
    logger = PyLogger(
        logger_name="MyProject",
        log_level=logging.DEBUG,
        console_output=True
    )
    
    # Log some messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    try:
        # Simulate an error
        raise ValueError("Example error")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
    
    # Advanced usage with custom configuration
    advanced_logger = PyLogger(
        logger_name="AdvancedProject",
        log_level=logging.INFO,
        log_format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d)',
        log_file_path='logs/custom_log.log',
        rotate_logs=True,
        max_bytes=1_048_576,  # 1MB
        backup_count=3,
        rotate_when='D',  # Daily rotation
        console_output=True
    )