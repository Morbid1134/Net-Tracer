# Net Tracer

Net Tracer is a simple port scanner that scans a target IP address or hostname for open ports and generates a JSON report of the scan results.

## Requirements

- Python 3.7+
- python-nmap (https://xael.org/pages/python-nmap-en.html)
- pyfiglet (https://pypi.org/project/pyfiglet/)

## Installation

You can install `net-tracer` using pip. First, make sure you have Python 3.6 or later installed on your system. Then, open a terminal or command prompt and enter the following command:
```cmd
pip install net-tracer
```

This will download and install the latest version of `net-tracer` and all its dependencies.

Alternatively, you can clone the GitHub repository and install `net-tracer` manually. First, navigate to the directory where you want to clone the repository, then enter the following commands:
```bash
git clone https://github.com/your_username/net-tracer.git
cd net-tracer
pip install -r requirements.txt
pip install .
```

This will clone the repository, install the required dependencies, and install `net-tracer` locally on your system.

Once `net-tracer` is installed, you can import it into your Python scripts using the following statement:
```python
import net_tracer
```

That's it! You're ready to use net-tracer in your Python projects.

## Usage

To run the port scanner, open a terminal window and navigate to the directory where the `net_tracer.py` script is located.
```cmd
python -m net_tracer.py [-h] [-t TARGET] [-p PORTS [PORTS ...]] [-s SOCKET_THREADS] [-n NMAP_THREADS] [-o OUTPUT]
```

You can, also, simply call the tracer() function from within your Python script.
```python
from net_tracer import tracer

tracer(target=None, ports=None, socket_threads=10000, nmap_threads=8, output=None)
```

### Terminal Arguments

- `-h, --help`: show the help message and exit.
- `-t TARGET, --target TARGET`: target IP address or hostname.
- `-p PORTS [PORTS ...], --ports PORTS [PORTS ...]`: ports to scan (default: all ports).
- `-s SOCKET_THREADS, --socket-threads SOCKET_THREADS`: number of socket threads to use (default: 10000).
- `-n NMAP_THREADS, --nmap-threads NMAP_THREADS`: number of nmap threads to use (default: 8).
- `-o OUTPUT, --output OUTPUT`: output file name (default: <target>.json).

### Import Parameters
- `target`: The IP address or hostname of the target you want to scan. If no value is provided, the user will be prompted to enter a target at runtime.
- `ports`: A list or range of ports to scan. If no value is provided, all 65,535 ports will be scanned.
- `socket_threads`: The number of threads to use for socket scanning. Default is set to 10,000.
- `nmap_threads`: The number of threads to use for Nmap scanning. Default is set to 8.
- `output`: The name of the output file to write the results to. If no value is provided, the output file will be named after the target IP address or hostname.

#### Examples

This will scan ports 1 to 100 on the target IP address 192.168.1.1 and write the results to a file named "results.json".
```python
from net_tracer import tracer

tracer(target="192.168.1.1", ports=range(1, 100), output="results.json")
```
  
as well as
```cmd
python -m net_tracer 192.1.1 -p 1:100 -o results.json
```
  
## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
