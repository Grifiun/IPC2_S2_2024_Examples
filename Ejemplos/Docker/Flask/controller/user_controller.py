from flask import Blueprint, request, jsonify
from entity.user import User
from service.user_service import UserService

# Crear el Blueprint para manejar rutas de usuario
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def user_register():
    try:
        # Obtener datos del request
        nombre = request.json.get('nombre')
        dpi = request.json.get('dpi')
        correo = request.json.get('correo')
        edad = request.json.get('edad')

        # Crear el objeto de usuario
        user = User(nombre, dpi, correo, edad)
        message, status_code = UserService.save_user(user)

        result_final = {"message": message}

        return jsonify(result_final), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/<correo>', methods=['GET'])
def get_user(correo):
    try:
        user, status_code = UserService.get_user_by_email(correo)
        if status_code == 200:
            result_final = {
                "nombre": user.nombre,
                "dpi": user.dpi,
                "correo": user.correo,
                "edad": user.edad  
            }
            return jsonify(result_final), status_code
        else:
            return jsonify({"error": user}), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

