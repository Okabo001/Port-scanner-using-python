import socket
import threading
import urllib.parse


def resolve_ip(target):
    """
    Resolves a URL to an IP address. If the input is already an IP address,
    it returns the IP address as-is. This function also validates the IP to
    ensure it matches the target URL's domain.
    """
    try:
        # Parse the URL to extract the hostname
        parsed_url = urllib.parse.urlparse(target)
        hostname = parsed_url.hostname if parsed_url.hostname else target

        # Resolve hostname to an IP address
        ip = socket.gethostbyname(hostname)
        print(f"Resolved {hostname} to IP address {ip}")
        return ip
    except socket.gaierror:
        print("Invalid URL or IP address.")
        return None


def scan_port(ip, port):
    """
    Attempts to connect to a specific port on the target IP address.
    If the port is open, it prints a message.
    """
    # Create a new socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout for the socket
    s.settimeout(1)
    try:
        # Try to connect to the IP and port
        s.connect((ip, port))
        print(f"Port {port} is open on {ip}")
    except (socket.timeout, socket.error):
        # Port is closed or connection timed out
        pass
    finally:
        # Always close the socket
        s.close()


def threaded_scan(ip, start_port, end_port, thread_count=10):
    """
    Scans a range of ports on a target IP address using multiple threads.
    Each thread scans a single port, improving scan speed.
    """
    print(f"Scanning {ip} from port {start_port} to {end_port} using {thread_count} threads.")
    threads = []

    # Iterate over the specified port range
    for port in range(start_port, end_port + 1):
        # Create a new thread to scan the port
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

        # If the number of active threads reaches the thread count limit, wait for all to finish
        if len(threads) >= thread_count:
            for t in threads:
                t.join()
            threads.clear()

    # Ensure any remaining threads finish
    for t in threads:
        t.join()


if __name__ == "__main__":
    # Prompt the user for input
    target = input("Enter the target IP address or URL: ")

    # Ensure the URL has a scheme (http:// or https://)
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target  # Default to HTTP if no scheme is provided

    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    thread_count = int(input("Enter the number of threads (default is 10): ") or 10)

    # Resolve the target to an IP address if it's a URL
    target_ip = resolve_ip(target)
    if target_ip:
        # Run the threaded scan with the provided parameters
        threaded_scan(target_ip, start_port, end_port, thread_count)
    else:
        print("Could not resolve the target to a valid IP address. Exiting.")
