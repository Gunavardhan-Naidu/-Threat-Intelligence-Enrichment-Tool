import logging
import argparse
import os

# Reads file path
def parse_indicators(inputs: list[str], file_path: str) -> list[tuple[str, str]]:
    indicators=[]
    
    if file_path:
        file_path = file_path.strip()
    else:
        file_path=""

    if not os.path.isfile(file_path):
        logging.error(f"File not found, invalid path:{file_path}")
        return indicators
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    indicators.extend(parse_line(line))
    except Exception as e:
        logging.error(f"Error file not found {file_path}: {e}")
        return indicators
    return indicators

#parses the input   
def parse_line(line: str) -> list[tuple[str,str]]:
    parsed_data = []
    parts = line.split(":", 1)

    if len(parts) == 2:
        input_type = parts[0].lower()
        value = parts[1]
        parsed_data.append((input_type, value))
    else:
        value = parts[0]
        input_type = detect_input_type(value)
        parsed_data.append((input_type, value))
    return parsed_data

#To detect what type of input (domain, url, ipaddress )
def detect_input_type(value: str) -> str:
    if value.startswith(("http://", "https://")):
        return "url"
    if valid_ip(value):
        return "ipaddress"
    if valid_domain(value):
        return "domain"
    return "unknown"

def valid_ip(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def valid_domain(domain: str) -> bool:
    if len(domain) > 253 or len(domain) == 0:
        return False
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-."
    if all(c.lower() in allowed_chars for c in domain) and "." in domain:
        return True
    return False