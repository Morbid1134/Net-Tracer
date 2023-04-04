# Net Tracer

Net Tracer is a simple port scanner that scans a target IP address or hostname for open ports and generates a JSON report of the scan results.

## Requirements

- Python 3.7+
- python-nmap (https://xael.org/pages/python-nmap-en.html)
- pyfiglet (https://pypi.org/project/pyfiglet/)

## Installation

1. Install the required packages: pip install python-nmap pyfiglet

2. Download the `net_tracer.py` script from this repository.

## Usage

To run the port scanner, open a terminal window and navigate to the directory where the `net_tracer.py` script is located.

python net_tracer.py [-h] [-t TARGET] [-p PORTS [PORTS ...]] [-s SOCKET_THREADS] [-n NMAP_THREADS] [-o OUTPUT]


### Optional Arguments

- `-h, --help`: show the help message and exit.
- `-t TARGET, --target TARGET`: target IP address or hostname.
- `-p PORTS [PORTS ...], --ports PORTS [PORTS ...]`: ports to scan (default: all ports).
- `-s SOCKET_THREADS, --socket-threads SOCKET_THREADS`: number of socket threads to use (default: 10000).
- `-n NMAP_THREADS, --nmap-threads NMAP_THREADS`: number of nmap threads to use (default: 8).
- `-o OUTPUT, --output OUTPUT`: output file name (default: <target>.json).

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
