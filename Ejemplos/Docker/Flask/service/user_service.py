from entity.user import User

class UserService:   
    # Simular base de datos en memoria con un diccionario
    users_db = {}

    @classmethod
    def save_user(cls, user):
        if user.correo in cls.users_db:
            return "User already exists", 400
        
        try:
            cls.users_db[user.correo] = user
            return "User created successfully", 201
        
        except Exception as e:
            return f"Error saving user: {str(e)}", 500

    @classmethod
    def get_user_by_email(cls, correo):
        user = cls.users_db.get(correo)

        if user:
            return user, 200
        
        else:
            return "User not found", 404
