from telegram import Bot
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "-"
CHAT_ID = 456
bot = Bot(token=TOKEN)


class ZabbixHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_lenght = int(self.headers['Content-Lenght'])
        post_data = self.rfile.read(content_lenght)
        try:
            data = json.loads(post_data.decode())
            message = f"Zabbix alert:\n{data.get('subject', '')}\n{data.get('message','')}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            self.send_response(200)
            self.end_headers()
        except Exception as e:
            self.send_response(500)
            self.end_headers()

if __name__ == "__main__":
    print("Bot is running on port 8000....")
    server = HTTPServer(('0.0.0.0', 8000), ZabbixHandler)
    server.serve_forever()
