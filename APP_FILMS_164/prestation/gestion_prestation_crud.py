from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.prestation.gestion_prestation_wtf_forms import FormWTFAjouterPrestation, FormWTFDeletePrestation, FormWTFUpdatePrestation
@app.route("/prestations_afficher/<string:order_by>/<int:id_prestation_sel>", methods=['GET', 'POST'])
def prestations_afficher(order_by, id_prestation_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_prestation_sel == 0:
                    strsql = "SELECT id_prestation, libelle, prix, duree FROM t_prestation ORDER BY id_prestation ASC"
                    mc_afficher.execute(strsql)
                elif order_by == "ASC":
                    strsql = "SELECT id_prestation, libelle, prix, duree FROM t_prestation WHERE id_prestation = %(v)s"
                    mc_afficher.execute(strsql, {"v": id_prestation_sel})
                else:
                    strsql = "SELECT id_prestation, libelle, prix, duree FROM t_prestation ORDER BY id_prestation DESC"
                    mc_afficher.execute(strsql)
                data_prestations = mc_afficher.fetchall()
                flash("Données des prestations affichées", "success")
        except Exception as e:
            raise Exception(f"Erreur affichage prestations : {e}")
    return render_template("prestations/prestation_afficher.html", data=data_prestations)


@app.route("/prestations_ajouter_wtf", methods=['GET', 'POST'])
def prestations_ajouter_wtf():
    form = FormWTFAjouterPrestation()
    if form.validate_on_submit():
        try:
            valeurs = {
                "lib": form.libelle_wtf.data,
                "prix": form.prix_wtf.data,
                "duree": form.duree_wtf.data
            }
            strsql = "INSERT INTO t_prestation (libelle, prix, duree) VALUES (%(lib)s, %(prix)s, %(duree)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Prestation ajoutée avec succès !", "success")
            return redirect(url_for('prestations_afficher', order_by='DESC', id_prestation_sel=0))
        except Exception as e:
            raise Exception(f"Erreur ajout prestation : {e}")
    return render_template("prestations/prestation_ajouter_wtf.html", form=form)


@app.route("/prestations_update_wtf", methods=['GET', 'POST'])
def prestations_update_wtf():
    id_upd = request.values.get('id_prestation_btn_edit_html')
    form = FormWTFUpdatePrestation()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id": id_upd,
                "lib": form.libelle_update_wtf.data,
                "prix": form.prix_update_wtf.data,
                "duree": form.duree_update_wtf.data
            }
            strsql = "UPDATE t_prestation SET libelle=%(lib)s, prix=%(prix)s, duree=%(duree)s WHERE id_prestation=%(id)s"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Mise à jour réussie", "success")
            return redirect(url_for('prestations_afficher', order_by="ASC", id_prestation_sel=id_upd))
        except Exception as e:
            raise Exception(f"Erreur update prestation : {e}")
    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT * FROM t_prestation WHERE id_prestation = %(id)s", {"id": id_upd})
            res = mconn.fetchone()
        form.libelle_update_wtf.data = res["libelle"]
        form.prix_update_wtf.data = res["prix"]
        form.duree_update_wtf.data = res["duree"]
    return render_template("prestations/prestation_update_wtf.html", form_update=form)


@app.route("/prestations_delete_wtf", methods=['GET', 'POST'])
def prestations_delete_wtf():
    id_del = request.values.get('id_prestation_btn_delete_html')
    form = FormWTFDeletePrestation()
    btn_del = False
    data_rdv_associes = None

    if form.validate_on_submit():
        if form.submit_btn_annuler.data:
            return redirect(url_for("prestations_afficher", order_by="ASC", id_prestation_sel=0))
        if form.submit_btn_conf_del.data:
            btn_del = True
        if form.submit_btn_del.data:
            try:
                with DBconnection() as mconn:
                    mconn.execute("DELETE FROM t_prestation WHERE id_prestation = %(id)s", {"id": id_del})
                flash("Prestation supprimée !", "success")
                return redirect(url_for('prestations_afficher', order_by="ASC", id_prestation_sel=0))
            except Exception as e:
                flash(f"Erreur lors de la suppression (vérifiez les rendez-vous associés) : {e}", "danger")
                return redirect(url_for('prestations_afficher', order_by="ASC", id_prestation_sel=0))

    if request.method == "GET" or btn_del:
        with DBconnection() as mconn:
            mconn.execute("SELECT libelle FROM t_prestation WHERE id_prestation = %(id)s", {"id": id_del})
            res = mconn.fetchone()

            # Vérifier si la prestation est liée à des rendez-vous
            mconn.execute("SELECT id_rdv FROM t_rdv_prestation WHERE id_prestation = %(id)s", {"id": id_del})
            data_rdv_associes = mconn.fetchall()

        form.libelle_delete_wtf.data = res["libelle"]

    return render_template("prestations/prestation_delete_wtf.html", form_delete=form, btn_submit_del=btn_del, data_rdv_associes=data_rdv_associes)