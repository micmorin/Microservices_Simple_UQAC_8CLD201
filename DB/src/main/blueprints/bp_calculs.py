from flask import Blueprint
from main.controllers import calculs_cont

bp_objects = Blueprint('calculs', __name__,url_prefix="/calculs/<string:usertoken>")

bp_objects.route("/calculs/",                           methods=['POST'])     (calculs_cont.create)
bp_objects.route("/calculs/list",                       methods=['POST'])     (calculs_cont.index)
bp_objects.route("/calculs/<int:id>/delete",            methods=['POST'])     (calculs_cont.destroy)