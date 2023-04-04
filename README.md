# Net Tracer

Net Tracer is a simple port scanner that scans a target IP address or hostname for open ports and generates a JSON report of the scan results.

## Requirements

- Python 3.7+
- concurrent.futures (https://docs.python.org/3/library/concurrent.futures.html)
- json (https://docs.python.org/3/library/json.html)
- nmap (https://xael.org/pages/python-nmap-en.html)

## Installation

You can install `net-tracer` using pip. First, make sure you have Python 3.6 or later installed on your system. Then, open a terminal or command prompt and enter the following command:
```cmd
pip install net-tracer
```

This will download and install the latest version of `net-tracer` and all its dependencies.

Alternatively, you can clone the GitHub repository and install `net-tracer` manually. First, navigate to the directory where you want to clone the repository, then enter the following commands:
```bash
git clone https://github.com/Morbid1134/Net-Tracer.git
cd net-tracer
pip install -r requirements.txt
pip install .
```

This will clone the repository, install the required dependencies, and install `net-tracer` locally on your system.

Once `net-tracer` is installed, you can import it into your Python scripts using the following statement:
```python
import net_tracer
```

That's it! You're ready to use `net-tracer` in your Python projects.

## Usage

You can simply call the tracer() function from within your Python script.
```python
from net_tracer import tracer

tracer(target=None, ports=None, socket_threads=10000, nmap_threads=8, output=None)
```

### Imports
- ```python 
tracer(target=None)
```

#### Examples

This will scan ports 1 to 100 on the target IP address 192.168.1.1 and write the results to a file named "results.json".
```python
from net_tracer import tracer

tracer(target="192.168.1.1", ports=range(1, 100), output="results.json")
```
  
## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
