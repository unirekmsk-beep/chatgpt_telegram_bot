from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import sys

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.debug("Health check request received")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run_server():
    logging.debug("Starting health check server on port 8080")
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    logging.debug("Server started successfully")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
