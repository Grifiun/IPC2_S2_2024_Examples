from flask import Flask, render_template
from controller.user_controller import user_bp  # Import user routes

app = Flask(__name__)

# Ruta de prueba
@app.route('/test')
def test():
    return "Backend funcional"

# Agreagmos endpoints del usuario
app.register_blueprint(user_bp, url_prefix='/usuario') 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
