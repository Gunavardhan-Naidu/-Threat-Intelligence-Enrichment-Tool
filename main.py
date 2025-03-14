import argparse
import json
import logging

from scanner.parser import parse_indicators

def main():
    parser = argparse.ArgumentParser(description="Threat Intelligence Enrichment Tool")
    parser.add_argument("-f", "--file", type="str", help="provide text file as input")
    parser.add_argument("-A", "--api", type="store_true", help="Run as API mode")
    parser.add_argument("-c", "--custom", type="str", help="Provide the domain, ip, or URL as input")
    parser.add_argument("-o", "--output", help="Provide JSON file path")
    args = parser.parse_args()

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
    )

    indicators = parse_indicators(args.custom or [], args.file)
    if not indicators:
        logging.error("No valid indicators provided")
        return



print("hello main")
