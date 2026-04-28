from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.rdv_prestation.gestion_rdv_prestation_wtf_forms import *

@app.route("/rdv_prestation_afficher/<int:id_rdv_sel>", methods=['GET', 'POST'])
def rdv_prestation_afficher(id_rdv_sel):
    try:
        with DBconnection() as mc_afficher:
            strsql = """
                SELECT rp.id_rdv, rp.id_prestation, rp.quantite, rp.prix_prestation, 
                       p.libelle, c.nom, c.prenom, r.date_rdv
                FROM t_rdv_prestation rp
                JOIN t_prestation p ON rp.id_prestation = p.id_prestation
                JOIN t_rendez_vous r ON rp.id_rdv = r.id_rdv
                JOIN t_client c ON r.id_client = c.id_client
            """
            if id_rdv_sel == 0:
                mc_afficher.execute(strsql + " ORDER BY rp.id_rdv DESC")
            else:
                mc_afficher.execute(strsql + " WHERE rp.id_rdv = %(id)s", {"id": id_rdv_sel})
            
            data_rp = mc_afficher.fetchall()
            flash("Détails des prestations par rendez-vous affichés", "success")
    except Exception as e:
        raise Exception(f"Erreur affichage rdv_prestation : {e}")
        
    return render_template("rdv_prestation/rdv_prestation_afficher.html", data=data_rp)

@app.route("/rdv_prestation_ajouter_wtf", methods=['GET', 'POST'])
def rdv_prestation_ajouter_wtf():
    form = FormWTFAjouterRdvPrestation()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id_r": form.id_rdv_wtf.data,
                "id_p": form.id_prestation_wtf.data,
                "qte": form.quantite_wtf.data,
                "prix": form.prix_prestation_wtf.data
            }
            strsql = "INSERT INTO t_rdv_prestation (id_rdv, id_prestation, quantite, prix_prestation) VALUES (%(id_r)s, %(id_p)s, %(qte)s, %(prix)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Prestation liée au rendez-vous avec succès !", "success")
            return redirect(url_for('rdv_prestation_afficher', id_rdv_sel=0))
        except Exception as e:
            flash(f"Erreur : Cette prestation est peut-être déjà liée à ce RDV.", "danger")
    return render_template("rdv_prestation/rdv_prestation_ajouter_wtf.html", form=form)