"""application and routing."""
from flask import Flask

def create_app():
    """configure instance of Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html', title='Main')
        
    return app