#def main():
#    print("Hello from site-flask!")
#if __name__ == "__main__":
#    main()

from flask import Flask, render_template
app = Flask(__name__) # Criar um site vazio

# criar a 1ª página do site
# route = URL que você quer em sua página
# template = Ao criar uma pasta com o nome template com arquivos html, oflask reconhece automaticamente no código
@app.route("/") # página inicial em branco

def homepage(): #função = o que você quer exibir na pagína
    return render_template("homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__": # Serve para rodar o site local e para não der problema como for realizar o deploy do site na internet
    app.run(debug=True)

