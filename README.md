# Threat Intelligence Enrichment Tool
A Python based tool that gathers information about domains, IP addresses, and URLs 
using external sources like WHOIS, VirusTotal, Abusipdb, and other open source APIs.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Gunavardhan-Naidu/Threat-Intelligence-Enrichment-Tool.git

   cd Threat-Intelligence-Enrichment-Tool

2. **Create a Virtual Environment (Recommended)**

    ```bash
    python3 -m venv venv

    source venv/bin/activate   
    # On Windows: venv\Scripts\activate
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **You can then run the tool using**
    ```bash
     python3 main.py -c google.com

     python3 main.py -f '/<file_path>/input.txt'

     python3 main.py -A domain:google.com

    python3 main.py -c <input> -o <output_file_path 

    python3 main.py -f <input_file_path> -t <no of threads> -o <output_file_path"

## Project Structure
```graphql
    Threat-Intelligence-Enrichment-Tool/
├── docs/                   # Sample test and output files
├── scanner/                # Modules 
│   ├── __init__.py
│   ├── abuseipdb.py
│   ├── manager.py
│   ├── multithreading.py
│   ├── parser.py
│   ├── shodanmod.py
│   ├── virustotal.py
│   └── whois_lookup.py
├── main.py                 # Main entry point of the application
├── requirements.txt        # Dependency list
├── README.md               # Project overview and usage instructions
└── setup.py                # Packaging script

