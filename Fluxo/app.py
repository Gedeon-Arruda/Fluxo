from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def acessos():
    if request.method == "POST":
        escolha = request.form.get("opcao")
        if escolha == "liberar":
            return redirect(url_for("liberar_acessos"))
        elif escolha == "vpn":
            return redirect(url_for("acesso_vpn"))
        elif escolha == "equipamentos":
            return redirect(url_for("pagina_equipamentos"))
        elif escolha == "rede":
            return redirect(url_for("pagina_rede"))
        elif escolha == "sistemas":
            return redirect(url_for("pagina_sistemas"))
    return render_template("menus/acessos.html")

@app.route("/liberar")
def liberar_acessos():
    return render_template("menus/liberar.html")

@app.route("/vpn")
def acesso_vpn():
    return render_template("menus/vpn.html")

@app.route("/equipamentos")
def pagina_equipamentos():
    return render_template("menus/equipamentos.html")

@app.route("/rede")
def pagina_rede():
    return render_template("menus/rede.html")

@app.route("/sistemas")
def pagina_sistemas():
    return render_template("menus/sistemas.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
