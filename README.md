Enhanced Port Scanner with Vulnerability Detection
A Python-based port scanner that resolves IP addresses from URLs, scans a range of ports, and detects vulnerabilities in exposed services (FTP, SSH, HTTP/HTTPS). It checks for open ports and security issues like missing HTTP headers to identify potential vulnerabilities.

Features
IP Resolution: Resolves domain names (URLs) to IP addresses.
Port Scanning: Scans a specified range of ports on the target IP or URL.
Vulnerability Detection: Identifies potential vulnerabilities on common ports (FTP, SSH, HTTP/HTTPS).
FTP (Port 21): Flags possible anonymous access vulnerabilities.
SSH (Port 22): Warns about weak authentication practices.
HTTP/HTTPS (Ports 80/443): Checks for missing security headers like X-Content-Type-Options, X-Frame-Options, Content-Security-Policy, and Strict-Transport-Security.
Multi-threaded Scanning: Speeds up port scanning by using multiple threads.
Prerequisites
Python 3.x
requests library (Install using pip install requests)
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/port-scanner-vulnerability-detection.git
Install dependencies:

bash
Copy code
pip install requests
Usage
Run the script by providing a target IP address or URL:

bash
Copy code
python port_scanner.py
Input the port range and number of threads for scanning.

The script will resolve the URL to an IP (if applicable), scan the specified ports, and check for vulnerabilities.

Example
bash
Copy code
Enter the target IP address or URL: example.com
Enter the start port: 20
Enter the end port: 100
Enter the number of threads (default is 10): 10
Contributing
Feel free to fork this project, report issues, or submit pull requests. Contributions are welcome!

License
This project is open-source and available under the MIT License
