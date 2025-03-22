import logging

# Configure logging
logging.basicConfig(
    filename="reports/test_log.txt",  # Save logs in reports folder
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"  # Overwrites logs in each test run
)

def get_logger():
    """Return a configured logger instance."""
    return logging.getLogger()
