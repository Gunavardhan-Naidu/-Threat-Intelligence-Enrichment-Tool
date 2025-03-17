import logging
import os
import json
from scanner.manager import Manager
from scanner.parser import parse_line

def threading(file_path:str,start:int,end:int, output_file:str):
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
                # lines = line.strip()
                # indicators.extend(line)
                lines = [line.strip() for line in file if line.strip()]
    except Exception as e:
        logging.error(f"Error file not found {file_path}: {e}")
        return indicators
    #take input start to end
    size = len(lines)
    if size == 0:
         logging.error("The file is empty, no indicators to process.")
         return
    #indicators create
    if start < 0 or start >= size:
        logging.error(f"Invalid start index: {start}")
        return
    if end > size:
        end = size

    core = Manager()
    results = {}
    
    for line in lines[start:end]:
        line = line.strip()
        if not line:
           continue

        indicators = parse_line(line) 
        for input_type, value in indicators[start:end]:
            try:
                # logging.info(f"Processing: {input_type}, {value}")
                data = core.controller(input_type, value)
                logging.info(f"Result: {data}")
                results[f"{input_type}: {value}"] = data
            except Exception as e:
                logging.error(f"Error processing {input_type}:{value}: {str(e)}")
                results[f"{input_type}: {value}"] = {"error": str(e)}
        try:
            with open(output_file, "w") as f:
                json.dump(results, f, indent=2, default=str)
        except Exception as e:
                 logging.error(f"Error writing to temporary file {output_file}: {str(e)}")
        
            
      

    

   
    
