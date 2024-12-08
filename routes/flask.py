from flask import (
    Flask,
    current_app,
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)


app = Flask()
