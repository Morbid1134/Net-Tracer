from net_tracer import tracer # Importing the tracer function from the package

# This will scan ports 1 to 100 on the target IP address 192.168.1.1 and write the results to a file named "results.csv".
tracer(target="192.168.1.1", ports=range(1, 100), output="results")

""" 
    This will scan every port on the subnet of the target IP address 192.168.1.1 with no output file 
    Each ip results list is added to a dictionary "subnet_results" under the cooresponding ip as the key
    It also prints the subnet it's working on
"""
subnet_results = {}
for i in range(1, 255):
    target_ip = f"192.168.1.{i}"
    print(f"working... {target_ip}")
    subnet_results[target_ip] = tracer(target=target_ip)