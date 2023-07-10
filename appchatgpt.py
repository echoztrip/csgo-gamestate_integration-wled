#ChatGPT added error handling for the file operations and HTTP requests.
#ChatGPT added error handling for JSON parsing in do_POST.
#ChatGPT moved the server creation and execution into a run_server function.
#ChatGPT wrapped the call to run_server in an if __name__ == "__main__" block to prevent it from running when the script is imported as a module.

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time
import json
from threading import Timer
import requests

class MyServer(HTTPServer):
    def __init__(self, server_address, RequestHandler, config_file='config.json'):
        super(MyServer, self).__init__(server_address, RequestHandler)
        self.wled_stat = self.get_wled(config_file)
        self.round_phase = None
        self.bomb_state = None
        self.timer30 = None
        self.timer35 = None
    
    def get_wled(self, config_file):
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                self.ip = config['ip']
        except (FileNotFoundError, KeyError) as e:
            print(time.asctime(), '[CS:GO WLED]', 'Error reading config file:', str(e))
            sys.exit(0)
        
        try:
            r = requests.get(url='http://%s/json/state' % self.ip, timeout=5)
            return r.json()
        except requests.exceptions.RequestException as e:
            print(time.asctime(), '[CS:GO WLED]', 'WLED not found:', str(e))
            sys.exit(0)

    # ...

    def send_to_wled(self, color=[[255,255,255],[0,0,0],[0,0,0]], effects=0, data=None):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Content-Encoding': 'utf-8'}
        if data is None:
            data = {"seg":[{"col":color, "fx": effects}]}
        try:
            requests.post(url='http://%s/json/state' % self.ip, data=json.dumps(data), headers=headers)
        except requests.exceptions.RequestException as e:
            print(time.asctime(), '[CS:GO WLED]', 'Error sending data to WLED:', str(e))

# ...

class MyRequestHandler(BaseHTTPRequestHandler):
    # ...

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        try:
            body = json.loads(self.rfile.read(length).decode('utf-8'))
        except json.JSONDecodeError as e:
            print(time.asctime(), '[CS:GO WLED]', 'Error parsing request body:', str(e))
            return
        self.parse_payload(body)
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()

    # ...

def run_server():
    server = MyServer(('127.0.0.1', 32092), MyRequestHandler)
    print(time.asctime(), '[CS:GO WLED]', 'Server start')
    try:
        server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    server.server_close()
    print(time.asctime(), '[CS:GO WLED]', 'Server stop')

if __name__ == "__main__":
    run_server()
