from app import create_app,db
from app.models import User
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server


#create app instance
app=create_app('development')
migrate = Migrate(app,db)

manager=Manager(app)
manager.add_command('db',MigrateCommand)

#the add_command method to create a new command 'server'
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)


if __name__=='__main__':
    manager.run()


