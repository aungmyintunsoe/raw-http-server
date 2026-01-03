#My own http server
import socket

# 1. Define your connection constants
HOST = '127.0.0.1' 
PORT = 8080

def start_server():
    # 2. Create the socket (Think: What types of socket do we need for TCP?)
    # Hint: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with socket.socket(..., ...) as s:
        
        # 3. Bind the socket to our host and port
        s.bind((HOST, PORT))
        
        # 4. Start listening for incoming connections
        s.listen()
        print(f"Server is running on http://{HOST}:{PORT}")

        while True:
            # 5. Accept a new connection (This is like picking up the phone)
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                
                # 6. Receive the data (the 'Request')
                request_data = conn.recv(1024)
                print(request_data.decode('utf-8')) # Look at the raw text!

                # 7. Prepare the 'Response'
                # REMEMBER: It must be formatted as raw HTTP text!
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    "\r\n"
                    "<html><body><h1>Hello from Grog's Server!</h1></body></html>"
                )

                # 8. Send the response back (Don't forget to encode!)
                conn.sendall(...)

if __name__ == "__main__":
    start_server()