from os import getenv
from app.app import app
from app.models import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(getenv('APP_PORT', 5006))
    app.run(host='0.0.0.0', port=port)
