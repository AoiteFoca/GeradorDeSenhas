from flask import Blueprint, render_template, jsonify
import random
import string

# Blueprint para as rotas
bp = Blueprint('routes', __name__)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return ''.join(random.choice(chars) for _ in range(length))

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/generate', methods=['GET'])
def generate_password_api():
    return jsonify({"password": generate_password()})
