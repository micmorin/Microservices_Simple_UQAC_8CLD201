import flask
from main.models.md_user import User
from main.models.md_profil import Profil
from main.models.form_login import LoginForm
from flask import render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import check_password_hash

def index(): 
    return jsonify({"message":"Veuillez consulter la documentation de l'API"}), 404

def login(user, password):
    u = User.query.filter_by(username=user).first()
    if check_password_hash(u.password, password):
        return jsonify({"message":"Connexion reussie", "data": u.to_json()}), 200
    else:
        return jsonify({"message":"Identifiants invalides", "db":u.password, "sent":password}), 503

