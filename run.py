from app import app
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('APP_CONFIG', 'default'))
@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Role=Role,
                App=App,
                Api=Api,
                ApiGroup=ApiGroup,
                ApiResponse=ApiResponse,
                ApiExample=ApiExample,
                Log=Log)


manager = Manager(app)
manager.add_command('shell', Shell(make_shell_context))
