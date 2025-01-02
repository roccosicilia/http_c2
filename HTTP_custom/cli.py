import subprocess

def send_command_to_server(command, server_url):
    try:
        # command structure
        curl_command = [
            "curl",
            "-X", "POST",
            "-d", f"command={command}",
            f"{server_url}/set_command"
        ]
        # execution and output
        result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Server output: {result.stdout.strip()}")
        else:
            print(f"Error: {result.stderr.strip()}")
    except Exception as e:
        print(f"Errore: {e}")

def main():
    server_url = input("Insert the C2 url (ex. http://127.0.0.1:80): ").strip()
    
    while True:
        print("\nMenu:")
        print("1. Exit")
        print("2. New command")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            print("Exit...")
            break
        elif choice == "2":
            command = input("New command: ").strip()
            if command:
                send_command_to_server(command, server_url)
            else:
                print("Error!")
        else:
            print("Error!")

if __name__ == "__main__":
    main()
