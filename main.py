import argparse
import json
import logging
import multiprocessing

from scanner.parser import parse_indicators, parse_line
from scanner.manager import Manager
from scanner.multithreading import threading


#logging module implementation
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
    )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Threat Intelligence Enrichment Tool\n"
            "--------------------------------------------------\n"
           """A Python based tool that gathers information about domains, IP addresses, and URLs 
using external sources like WHOIS, VirusTotal, and other open APIs.\n\n"""
            "Examples:\n"
            "  python3 main.py -c google.com\n"
            "  python3 main.py -f input.txt\n"
            "  python3 main.py -A domain:vit.ac.in\n"
            "python3 main.py -c <input> -o <output_file_path "
        ),
    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", "--file", type=str, help="provide text file path as input")
    parser.add_argument("-A", "--api", type=str, help="Run as API mode")
    parser.add_argument("-c", "--custom", type=str, help="Provide the domain, ip, or URL as input")
    parser.add_argument("-o", "--output", help="Provide JSON file path")
    parser.add_argument("-t","--thread",type=int,help="multithreading")
    args = parser.parse_args()

   # If no arguments provided
    if len(vars(args)) == 0 or not any(vars(args).values()):
        parser.print_help()
        return

#Assigning the Manager module to a variable  
    try:
        core = Manager()
        result = {}
        indicators = []

       
        if args.file and args.thread:
            #find file length
            with open(args.file, "r") as file:
                lines = file.readlines()
            size = len(lines)
            logging.info(f"Total lines in file: {size}")
            threads = args.thread
            chunk_size = size // threads
            processes = []
            mp_manager = multiprocessing.Manager()
            shared_results = mp_manager.dict()
            #no of threads(input) if not (4)
            # implement for looop down
            #divide indicators line 0 to line 25
            try:
                for i in range(threads):
                        start = i * chunk_size
                        # Ensure the last process takes any remaining lines
                        end = size if i == threads - 1 else (i + 1) * chunk_size
                        p = multiprocessing.Process(target=threading, args=(args.file, start, end, shared_results))
                        processes.append(p)
                        p.start()

                    # Wait for all processes to complete
                for p in processes:
                        p.join()
            except KeyboardInterrupt:
                logging.info("KeyboardInterrupt caught, terminating processes...")
                for p in processes:
                    p.terminate()
                for p in processes:
                    p.join()
            output= json.dumps(shared_results, indent= 2 , default=str)

        else:
            if args.file:
                logging.info(f"File Path: {args.file}")
                indicators.extend(parse_indicators([], args.file))
            if args.custom:
                logging.info(f"processing your input: {args.custom}")
                indicators.extend(parse_line(args.custom))
            
            if args.api:
                logging.info(f"processing your input: {args.api}")
                indicators.extend(parse_line(args.api))

            #checking if indicators are provided
            if not indicators:
                logging.error("No valid indicators provided")
                return
            
            for input_type, value in indicators:
                try:
                    # logging.info(f"Processing: {input_type}, {value}")
                    data = core.controller(input_type, value)
                    logging.info(f"Result: {data}")
                    result[f"{input_type}: {value}"] = data
                except Exception as e:
                    logging.error(f"Error processing {input_type}:{value}: {str(e)}")
                    result[f"{input_type}:{value}"] = {"error": str(e)}

            output = json.dumps(result, indent = 2 , default=str)

        

        if args.output:
          try:
            with open(args.output, "w") as f:
                f.write(output)
          except Exception as e:
            logging.error(f"Error writing to {args.output}: {str(e)}")
        else:
             print(output)

    except Exception as e:
        logging.error(f"Error during execution: {str(e)}")
        print(f"Error: {str(e)}")
        return 1
    
if __name__ == "__main__":
    main()