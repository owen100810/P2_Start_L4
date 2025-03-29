from tkinter import messagebox
import random

titels = [
    "Error",
    "Warning",
    "Critical Error",
    "System Alert",
    "Notification",
    "Attention Required",
    "Security Alert",
    "Failure",
    "Unexpected Issue",
    "Critical Failure",
    "Access Issue",
    "Permission Warning",
    "Network Error",
    "Configuration Warning",
    "System Failure",
    "Processing Error"
]

msg = [
    "File Not Found",
    "Access Denied",
    "Connection Timed Out",
    "Invalid Input",
    "Syntax Error",
    "Out of Memory",
    "Permission Denied",
    "Disk Full",
    "Network Unreachable",
    "Internal Server Error",
    "Unsupported Format",
    "Authentication Failed",
    "Resource Not Found",
    "Operation Not Allowed",
    "Dependency Missing",
    "Timeout Error",
    "Unexpected Token",
    "Divide by Zero",
    "Key Error",
    "Type Mismatch",
    "Index Out of Range",
    "Module Not Found",
    "Configuration Error",
    "Parsing Error",
    "Service Unavailable",
    "File Corrupted",
    "Invalid Argument",
    "Process Failed",
    "Hardware Failure"
]


for i in range(15):
    messagebox.showinfo(random.choice(titels), random.choice(msg))