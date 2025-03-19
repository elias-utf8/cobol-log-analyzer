import random
import time
from datetime import datetime

LOG_TYPES = ["apache", "nginx", "syslog", "auth", "database", "custom_app"]

ips = ["192.168.1.1", "10.0.0.2", "172.16.0.3", "203.0.113.4", "198.51.100.5"]
methods = ["GET", "POST", "PUT", "DELETE"]
urls = ["/index.html", "/login", "/dashboard", "/api/data", "/logout"]
statuses = [200, 301, 403, 404, 500]
sizes = [random.randint(200, 5000) for _ in range(10)]
users = ["root", "admin", "user123", "guest", "service"]
actions = ["LOGIN_SUCCESS", "LOGIN_FAILURE", "FILE_ACCESSED", "PERMISSION_DENIED", "USER_CREATED"]
db_queries = ["SELECT * FROM users", "UPDATE accounts SET balance=0", "DELETE FROM logs WHERE id=5"]
custom_messages = ["Service started", "Unexpected error occurred", "Task completed successfully"]

def generate_log(log_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if log_type == "apache" or log_type == "nginx":
        return f"{random.choice(ips)} - - [{timestamp}] \"{random.choice(methods)} {random.choice(urls)} HTTP/1.1\" {random.choice(statuses)} {random.choice(sizes)}"
    elif log_type == "syslog":
        return f"{timestamp} myserver systemd[1]: {random.choice(custom_messages)}"
    elif log_type == "auth":
        return f"{timestamp} sshd[12345]: {random.choice(actions)} for user {random.choice(users)} from {random.choice(ips)}"
    elif log_type == "database":
        return f"{timestamp} DB_QUERY: {random.choice(db_queries)}"
    elif log_type == "custom_app":
        return f"{timestamp} MyApp: {random.choice(custom_messages)}"
    else:
        return f"{timestamp} UNKNOWN_LOG_TYPE"

def generate_logs(n=10):
    for _ in range(n):
        log_type = random.choice(LOG_TYPES)
        print(generate_log(log_type))

generate_logs(20)
