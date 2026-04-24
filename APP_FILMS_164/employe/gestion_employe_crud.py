from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.employe.gestion_employe_wtf_forms import FormWTFAjouterEmploye, FormWTFDeleteEmploye, FormWTFUpdateEmploye

@app.route("/employe_afficher/<string:order_by>/<int:id_employe_sel>", methods=['GET', 'POST'])
def employe_afficher(order_by, id_employe_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_employe_sel == 0:
                    strsql = "SELECT id_employe, nom_employe, prenom_employe, post_employe FROM t_employe ORDER BY id_employe ASC"
                    mc_afficher.execute(strsql)
                elif order_by == "ASC":
                    strsql = "SELECT id_employe, nom_employe, prenom_employe, post_employe FROM t_employe WHERE id_employe = %(v)s"
                    mc_afficher.execute(strsql, {"v": id_employe_sel})
                else:
                    strsql = "SELECT id_employe, nom_employe, prenom_employe, post_employe FROM t_employe ORDER BY id_employe DESC"
                    mc_afficher.execute(strsql)
                data_employe = mc_afficher.fetchall()
                flash("Données des employés affichées", "success")
        except Exception as e:
            raise Exception(f"Erreur affichage employés : {e}")
    return render_template("employe/employe_afficher.html", data=data_employe)

@app.route("/employe_ajouter_wtf", methods=['GET', 'POST'])
def employe_ajouter_wtf():
    form = FormWTFAjouterEmploye()
    if form.validate_on_submit():
        try:
            valeurs = {"n": form.nom_employe_wtf.data, "p": form.prenom_employe_wtf.data, "po": form.post_employe_wtf.data}
            strsql = "INSERT INTO t_employe (nom_employe, prenom_employe, post_employe) VALUES (%(n)s, %(p)s, %(po)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Employé inséré !", "success")
            return redirect(url_for('employe_afficher', order_by='DESC', id_employe_sel=0))
        except Exception as e:
            raise Exception(f"Erreur ajout : {e}")
    return render_template("employe/employe_ajouter_wtf.html", form=form)

@app.route("/employe_update_wtf", methods=['GET', 'POST'])
def employe_update_wtf():
    id_upd = request.values.get('id_employe_btn_edit_html')
    form = FormWTFUpdateEmploye()
    if form.validate_on_submit():
        try:
            valeurs = {"id": id_upd, "n": form.nom_employe_update_wtf.data, "p": form.prenom_employe_update_wtf.data, "po": form.post_employe_update_wtf.data}
            strsql = "UPDATE t_employe SET nom_employe=%(n)s, prenom_employe=%(p)s, post_employe=%(po)s WHERE id_employe=%(id)s"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Mise à jour réussie", "success")
            return redirect(url_for('employe_afficher', order_by="ASC", id_employe_sel=id_upd))
        except Exception as e:
            raise Exception(f"Erreur update : {e}")
    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT * FROM t_employe WHERE id_employe = %(id)s", {"id": id_upd})
            res = mconn.fetchone()
        form.nom_employe_update_wtf.data = res["nom_employe"]
        form.prenom_employe_update_wtf.data = res["prenom_employe"]
        form.post_employe_update_wtf.data = res["post_employe"]
    return render_template("employe/employe_update_wtf.html", form_update=form)

@app.route("/employe_delete_wtf", methods=['GET', 'POST'])
def employe_delete_wtf():
    id_del = request.values.get('id_employe_btn_delete_html')
    form = FormWTFDeleteEmploye()
    btn_del = False
    if form.validate_on_submit():
        if form.submit_btn_annuler.data: return redirect(url_for("employe_afficher", order_by="ASC", id_employe_sel=0))
        if form.submit_btn_conf_del.data: btn_del = True
        if form.submit_btn_del.data:
            with DBconnection() as mconn:
                mconn.execute("DELETE FROM t_employe WHERE id_employe = %(id)s", {"id": id_del})
            flash("Supprimé !", "success")
            return redirect(url_for('employe_afficher', order_by="ASC", id_employe_sel=0))
    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT nom_employe, prenom_employe FROM t_employe WHERE id_employe = %(id)s", {"id": id_del})
            res = mconn.fetchone()
        form.nom_employe_delete_wtf.data = f"{res['prenom_employe']} {res['nom_employe']}"
    return render_template("employe/employe_delete_wtf.html", form_delete=form, btn_submit_del=btn_del)