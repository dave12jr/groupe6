from os import getenv
from app.app import app

if __name__ == '__main__':
    port = int(getenv('APP_PORT', '5006'))
    app.run(host='0.0.0.0', port=port)
