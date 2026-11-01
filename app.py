from flask import Flask, render_template
import random, string

app = Flask(__name__)

# SEU ACESSO DE DONO
ADMIN_EMAIL = "derikwwm@gmail.com"

def gerar_zion():
    codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{codigo}Zion"

# Categorias iniciais
categorias = ["Roblox", "Rucoy", "Tibia"]

# Anúncios falsos pra testar
anuncios = [
    {"titulo": "Conta Rucoy lvl 450", "jogo": "Rucoy", "preco": "R$ 150", "dono": "#Neff_DANTE", "zion": "0001Zion"},
    {"titulo": "Conta Roblox com Korblox", "jogo": "Roblox", "preco": "R$ 300", "dono": "Player123", "zion": "245FZion"},
]

@app.route("/")
def home():
    return render_template("index.html", anuncios=anuncios, categorias=categorias, admin_email=ADMIN_EMAIL)

if __name__ == "__main__":
    print(f"Seu Zion de dono: 0001Zion | Seu gerador teste: {gerar_zion()}")
    app.run(debug=True)