import os
import logging

def get_system_logger(name: str) -> logging.Logger:
    """Initialize standard logging configuration for automated pipelines."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

# Environment configuration
PIPELINE_ENV = os.getenv("PIPELINE_ENV", "production")
