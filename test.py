"""
Example usage of py-logger demonstrating various features and configurations
"""

import logging
import time
import os
from py_logger import PyLogger

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def simulate_user_actions():
    """Simulate some user actions to demonstrate logging."""
    return {
        'user_id': '12345',
        'action': 'purchase',
        'item_id': 'PROD_789',
        'amount': 99.99
    }

def process_data(data):
    """Simulate data processing with potential errors."""
    if data['amount'] > 1000:
        raise ValueError("Amount exceeds maximum limit")
    return True

def main():
    # Create logs directory in project root if it doesn't exist
    logs_dir = os.path.join(PROJECT_ROOT, 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Set up log file path
    log_file = os.path.join(logs_dir, 'test_app.log')
    
    # Create a basic logger for this test
    logger = PyLogger(
        logger_name="TestApp",
        log_level=logging.DEBUG,
        log_format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d)',
        log_file_path=log_file
    )
    
    # Log application startup
    logger.info("Starting test application...")
    
    # Rest of the testing code...
    logger.debug("This is a debug message - useful for troubleshooting")
    logger.info("This is an info message - normal application flow")
    logger.warning("This is a warning - something might be wrong")
    
    try:
        logger.info("Processing user actions...")
        user_data = simulate_user_actions()
        logger.debug(f"Received user data: {user_data}")
        process_result = process_data(user_data)
        logger.info(f"Data processing completed successfully: {process_result}")
    except Exception as e:
        logger.exception(f"Error processing user data: {str(e)}")

if __name__ == "__main__":
    # Create logs directory in project root
    logs_dir = os.path.join(PROJECT_ROOT, 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Set up advanced log file path
    advanced_log_file = os.path.join(logs_dir, 'advanced_test.log')
    
    # Create an advanced logger with custom configuration
    advanced_logger = PyLogger(
        logger_name="AdvancedTest",
        log_level=logging.DEBUG,
        log_format='%(asctime)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d)',
        log_file_path=advanced_log_file,
        rotate_logs=True,
        max_bytes=1024,  # Small size for testing rotation
        backup_count=3,
        rotate_when='S',  # Rotate every second (for testing)
        console_output=True
    )
    
    # Log some messages to demonstrate rotation
    advanced_logger.info("Starting advanced logging test...")
    for i in range(10):
        advanced_logger.info(f"Test log message {i+1} with some extended content to increase log size")
        time.sleep(0.5)
    
    # Run the main test
    main()