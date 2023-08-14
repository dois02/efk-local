import json
import logging
import time
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Define the log structure
log_structure = {
    "type": "",
    "severity": "",
    "message": "",
    "machine": "server-01",
    "user": "john.doe@example.com",
    "timestamp": "",
    "process": "payment-service",
    "thread": "",
    "context": "payment-12345",
    "source": "payment-processor",
    "requestId": "abcd1234",
    "correlationId": "xyz789",
    "exception": {
        "message": "Division by zero",
        "code": "DIV_ZERO",
        "stackTrace": "..."
    },
    "logContext": {
        "orderId": "54321",
        "amount": 100.0
    }
}

# Create a file handler to append logs to the dummy.log file
file_handler = logging.FileHandler('/app/dummy.log', mode='a')
file_handler.setFormatter(logging.Formatter('%(message)s'))
logging.getLogger().addHandler(file_handler)

# Generate and log dummy logs
log_types = ["error", "info", "warning"]

while True:
    for i, log_type in enumerate(log_types):
        log_structure["timestamp"] = datetime.utcnow().isoformat() + "Z"
        log_structure["thread"] = str(i + 1)
        log_structure["type"] = log_type
        log_structure["severity"] = "high" if log_type == "error" else "low"
        log_structure["message"] = f"A {log_type} occurred while processing the request."
        logging.info(json.dumps(log_structure))
    time.sleep(10)
