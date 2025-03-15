import logging
import argparse
import os
import re
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
    for item in line.split(","):
        item = item.strip()
        if ":" in item and not re.match(r"\[.*\]", item):
            parts = item.split(":", 1)
            if len(parts) == 2:
                input_type = parts[0].lower()
                value = parts[1]
                parsed_data.append((input_type, value))
                continue
    if len(line.split(","))==1:
        input_type = detect_input_type(line)
        parsed_data.append((input_type, line))
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
    ip = ip.strip()
    ip_regex = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not ip_regex.match(ip):
        return False
    parts = ip.split(".")
    return all(0 <= int(part) <= 255 for part in parts)

def valid_domain(domain: str) -> bool:
    domain_regex = re.compile(
        r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.[A-Za-z]{2,})+$"
    )
    return bool(domain_regex.match(domain))