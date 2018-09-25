import os
from app import create_app

app = create_app(os.getenv("APP_SETTINGS") or "development")

port = os.environ.get("PORT", 5000)
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = port)