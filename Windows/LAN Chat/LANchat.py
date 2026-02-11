import socket
import threading
import sys

PORT = 5555
clients = []

# ANSI COLORS
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# ======================
# UTILS
# ======================
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# ======================
# SERVER FUNCTIONS
# ======================
def broadcast(message):
    """Send message to all connected clients"""
    for client in clients[:]:
        try:
            client.send(message)
        except:
            clients.remove(client)

def handle_client(client_socket):
    """Handle messages from one client"""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decoded = message.decode("utf-8")
            print(f"{GREEN}{decoded}{RESET}")  # client messages = green on server
            broadcast(message)
        except:
            break

    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def server_send_loop(username):
    """Allow server to send messages"""
    while True:
        msg = input()
        if msg.lower() == "/quit":
            shutdown_msg = f"{username} shut down the server."
            print(f"{RED}{shutdown_msg}{RESET}")
            broadcast(shutdown_msg.encode())
            sys.exit()

        full_msg = f"{username}: {msg}"
        print(f"{RED}{full_msg}{RESET}")   # server message = red on server
        broadcast(full_msg.encode())

def start_server(username):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", PORT))
    server.listen()

    print(f"\n{RED}[SERVER STARTED by {username}]{RESET}")
    print(f"{RED}Listening on {get_local_ip()}:{PORT}{RESET}\n")
    print(f"{RED}Type messages to chat. Type /quit to stop server.{RESET}\n")

    threading.Thread(
        target=server_send_loop,
        args=(username,),
        daemon=True
    ).start()

    while True:
        client_socket, _ = server.accept()
        clients.append(client_socket)
        threading.Thread(
            target=handle_client,
            args=(client_socket,),
            daemon=True
        ).start()

# ======================
# CLIENT FUNCTIONS
# ======================
def start_client(username):
    server_ip = input("Enter server IP: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, PORT))

    print(f"\n{GREEN}Connected to chat. Type /quit to exit.{RESET}\n")

    # Receive messages from server
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode("utf-8")
                sender = message.split(":", 1)[0]
                # Self message = green, server/others = red
                if sender == username:
                    print(f"{GREEN}{message}{RESET}")
                else:
                    print(f"{RED}{message}{RESET}")
            except:
                break

    # Send messages
    def send_messages():
        while True:
            msg = input()
            if msg.lower() == "/quit":
                client.send(f"{username} left the chat.".encode())
                client.close()
                print(f"{GREEN}You left the chat.{RESET}")
                sys.exit()
            client.send(f"{username}: {msg}".encode())

    threading.Thread(target=receive_messages, daemon=True).start()
    send_messages()

# ======================
# ENTRY POINT
# ======================
if __name__ == "__main__":

    print(r"""
      _      _   _  _    ___ _  _   _ _____ 
     | |    /_\ | \| |  / __| || | /_\_   _|
     | |__ / _ \| .` | | (__| __ |/ _ \| |  
     |____/_/ \_\_|\_|  \___|_||_/_/ \_\_|  
     =======================================
                  John Valinsky
     =======================================
    """)
    print("\nLocal Network Terminal Chat")
    print("----------------------------")
    print(f"Your Local IP : {get_local_ip()}")
    print(f"Port          : {PORT}\n")

    username = input("Enter your username: ").strip() or "Admin"
    role = input("Choose role (server/client) [S/C]: ").lower().strip()

    if role in ("server", "s"):
        start_server(username)
    elif role in ("client", "c"):
        start_client(username)
    else:
        print("Invalid role. Please restart and choose server (S) or client (C).")
