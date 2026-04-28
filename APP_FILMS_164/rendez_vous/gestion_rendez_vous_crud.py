from pathlib import Path
from flask import render_template, redirect, url_for, request, session, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.rendez_vous.gestion_rendez_vous_wtf_forms import FormWTFAjouterRendezVous, FormWTFDeleteRendezVous, \
    FormWTFUpdateRendezVous


@app.route("/rendez_vous_afficher/<string:order_by>/<int:id_rdv_sel>", methods=['GET', 'POST'])
def rendez_vous_afficher(order_by, id_rdv_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                # Jointure pour récupérer le nom du client avec le RDV
                requete_base = """
                    SELECT r.id_rdv, r.date_rdv, r.date_annulation, c.nom, c.prenom, r.id_client 
                    FROM t_rendez_vous r 
                    LEFT JOIN t_client c ON r.id_client = c.id_client
                """
                if order_by == "ASC" and id_rdv_sel == 0:
                    strsql = requete_base + " ORDER BY r.id_rdv ASC"
                    mc_afficher.execute(strsql)
                elif order_by == "ASC":
                    strsql = requete_base + " WHERE r.id_rdv = %(v)s"
                    mc_afficher.execute(strsql, {"v": id_rdv_sel})
                else:
                    strsql = requete_base + " ORDER BY r.id_rdv DESC"
                    mc_afficher.execute(strsql)

                data_rdv = mc_afficher.fetchall()
                flash("Données des rendez-vous affichées", "success")
        except Exception as e:
            raise Exception(f"Erreur affichage RDV : {e}")

    return render_template("rendez_vous/rendez_vous_afficher.html", data=data_rdv)


@app.route("/rendez_vous_ajouter", methods=['GET', 'POST'])
def rendez_vous_ajouter_wtf():
    form = FormWTFAjouterRendezVous()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id_client": form.id_client_wtf.data,
                "date_rdv": form.date_rdv_wtf.data
            }
            strsql = "INSERT INTO t_rendez_vous (id_client, date_rdv) VALUES (%(id_client)s, %(date_rdv)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Rendez-vous ajouté avec succès !", "success")
            return redirect(url_for('rendez_vous_afficher', order_by='DESC', id_rdv_sel=0))
        except Exception as e:
            raise Exception(f"Erreur ajout RDV : {e}")

    return render_template("rendez_vous/rendez_vous_ajouter_wtf.html", form=form)


@app.route("/rendez_vous_update", methods=['GET', 'POST'])
def rendez_vous_update_wtf():
    id_upd = request.values.get('id_rdv_btn_edit_html')
    form = FormWTFUpdateRendezVous()

    if form.validate_on_submit():
        try:
            valeurs = {
                "id_rdv": id_upd,
                "id_client": form.id_client_update_wtf.data,
                "date_rdv": form.date_rdv_update_wtf.data,
                "date_annulation": form.date_annulation_update_wtf.data
            }
            strsql = """UPDATE t_rendez_vous 
                        SET id_client=%(id_client)s, date_rdv=%(date_rdv)s, date_annulation=%(date_annulation)s 
                        WHERE id_rdv=%(id_rdv)s"""
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Mise à jour réussie", "success")
            return redirect(url_for('rendez_vous_afficher', order_by="ASC", id_rdv_sel=id_upd))
        except Exception as e:
            raise Exception(f"Erreur update RDV : {e}")

    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT * FROM t_rendez_vous WHERE id_rdv = %(id)s", {"id": id_upd})
            res = mconn.fetchone()

        form.id_client_update_wtf.data = res["id_client"]
        form.date_rdv_update_wtf.data = res["date_rdv"]
        form.date_annulation_update_wtf.data = res["date_annulation"]

    return render_template("rendez_vous/rendez_vous_update_wtf.html", form_update=form)


@app.route("/rendez_vous_delete", methods=['GET', 'POST'])
def rendez_vous_delete_wtf():
    id_del = request.values.get('id_rdv_btn_delete_html')
    form = FormWTFDeleteRendezVous()
    btn_del = False

    if form.validate_on_submit():
        if form.submit_btn_annuler.data:
            return redirect(url_for("rendez_vous_afficher", order_by="ASC", id_rdv_sel=0))
        if form.submit_btn_conf_del.data:
            btn_del = True
        if form.submit_btn_del.data:
            try:
                valeur_del = {"id_rdv": id_del}
                with DBconnection() as mconn:
                    # 1. On efface d'abord les liens avec les prestations et employés pour éviter l'erreur de contrainte (FOREIGN KEY)
                    mconn.execute("DELETE FROM t_rdv_employe WHERE id_rdv = %(id_rdv)s", valeur_del)
                    mconn.execute("DELETE FROM t_rdv_prestation WHERE id_rdv = %(id_rdv)s", valeur_del)
                    # 2. On peut enfin effacer le rendez-vous !
                    mconn.execute("DELETE FROM t_rendez_vous WHERE id_rdv = %(id_rdv)s", valeur_del)

                flash("Rendez-vous définitivement supprimé !", "success")
                return redirect(url_for('rendez_vous_afficher', order_by="ASC", id_rdv_sel=0))
            except Exception as e:
                flash(f"Erreur lors de la suppression : {e}", "danger")
                return redirect(url_for('rendez_vous_afficher', order_by="ASC", id_rdv_sel=0))

    if request.method == "GET" or btn_del:
        with DBconnection() as mconn:
            mconn.execute("""SELECT r.date_rdv, c.nom, c.prenom 
                             FROM t_rendez_vous r 
                             LEFT JOIN t_client c ON r.id_client = c.id_client 
                             WHERE r.id_rdv = %(id)s""", {"id": id_del})
            res = mconn.fetchone()

        # Afficher les infos du RDV qu'on s'apprête à effacer
        form.info_rdv_delete_wtf.data = f"RDV de {res['prenom']} {res['nom']} le {res['date_rdv']}"

    return render_template("rendez_vous/rendez_vous_delete_wtf.html", form_delete=form, btn_submit_del=btn_del)