import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from app import app


if __name__ == '__main__':
    app.run()



# from flask_script import Manager, Server

# app = create_app('development')

# manager = Manager(app)
# manager.add_command('server',Server)