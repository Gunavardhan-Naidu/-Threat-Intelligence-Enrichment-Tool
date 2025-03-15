import argparse
import json
import logging

from scanner.parser import parse_indicators, parse_line
from scanner.manager import Manager


#logging module implementation
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
    )


def main():
    parser = argparse.ArgumentParser(
        # description=""" Threat Intelligence Enrichment Tool
        # This tool enriches domains, IPs, and URLs with threat intelligence data.
        
        # Examples:
        #     python main.py -c google.com
        #     python main.py -f input.txt
        #     python main.py -A""")
        description=(
            "Threat Intelligence Enrichment Tool\n"
            "--------------------------------------------------\n"
           """A Python-based enrichment tool that gathers information about domains, IP addresses, and URLs 
using external intelligence sources like WHOIS, VirusTotal, and other open APIs.\n\n"""
            "Examples:\n"
            "  python main.py -c google.com\n"
            "  python main.py -f input.txt\n"
            "  python3 main.py -A domain:vit.ac.in\n"
        ),
    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", "--file", type=str, help="provide text file path as input")
    parser.add_argument("-A", "--api", type=str, help="Run as API mode")
    parser.add_argument("-c", "--custom", type=str, help="Provide the domain, ip, or URL as input")
    parser.add_argument("-o", "--output", help="Provide JSON file path")
    args = parser.parse_args()

   # If no arguments provided
    if len(vars(args)) == 0 or not any(vars(args).values()):
        parser.print_help()
        return

#Assigning the Manager module to a variable  
    try:
        core = Manager()
        logging.info("Manager object created")
        result = {}
        indicators = []
        

        if args.file:
            logging.info(f"File Path: {args.file}")
            indicators.extend(parse_indicators([], args.file))
            logging.info(f"Parsed Indicators: {indicators}")
        
        if args.custom:
            logging.info(f"proceesing your input: {args.custom}")
            indicators.extend(parse_line(args.custom))
            # print(parse_line(args.custom))
            # print(parse_line("domain:google.com"))    # [('domain', 'google.com')]
            # print(parse_line("8.8.8.8"))              # [('ipaddress', '8.8.8.8')]
            # print(parse_line("http://example.com"))   # [('url', 'http://example.com')]
            # print(parse_line("google.com"))           # [('domain', 'google.com')]
            # print(parse_line("unknown_input"))        # [('unknown', 'unknown_input')]
            # print(parse_line("domain:google.com,8.8.8.8")) # [('domain', 'google.com'), ('ipaddress', '8.8.8.8')]

            
        
        if args.api:
            logging.info(f"processing your inout: {args.api}")
            indicators.extend(parse_line(args.api))

        #checking if indicators are provided
        if not indicators:
            logging.error("No valid indicators provided")
            return
        
        for input_type, value in indicators:
            try:
                logging.info(f"Processing: {input_type}, {value}")
                data = core.controller(input_type, value)
                logging.info(f"Result: {data}")
                result[f"{input_type}: {value}"] = data
            except Exception as e:
                logging.error(f"Error processing {input_type}:{value}: {str(e)}")
                result[f"{input_type}:{value}"] = {"error": str(e)}

        output = json.dumps(result, indent = 2 , default=str)
        print(output)

    except Exception as e:
        logging.error(f"Error during execution: {str(e)}")
        print(f"Error: {str(e)}")
        return 1
    
if __name__ == "__main__":
    main()