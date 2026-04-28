from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.rdv_employe.gestion_rdv_employe_wtf_forms import FormWTFAjouterRdvEmploye, FormWTFDeleteRdvEmploye

@app.route("/rdv_employe_afficher/<int:id_rdv_sel>", methods=['GET', 'POST'])
def rdv_employe_afficher(id_rdv_sel):
    try:
        with DBconnection() as mc_afficher:
            strsql = """
                SELECT re.id_rdv, re.id_employe, e.nom_employe, e.prenom_employe, e.post_employe,
                       c.nom AS nom_client, c.prenom AS prenom_client, r.date_rdv
                FROM t_rdv_employe re
                JOIN t_employe e ON re.id_employe = e.id_employe
                JOIN t_rendez_vous r ON re.id_rdv = r.id_rdv
                JOIN t_client c ON r.id_client = c.id_client
            """
            if id_rdv_sel == 0:
                mc_afficher.execute(strsql + " ORDER BY re.id_rdv DESC")
            else:
                mc_afficher.execute(strsql + " WHERE re.id_rdv = %(id)s", {"id": id_rdv_sel})
            
            data_re = mc_afficher.fetchall()
            flash("Assignations des employés aux rendez-vous affichées", "success")
    except Exception as e:
        raise Exception(f"Erreur affichage rdv_employe : {e}")
        
    return render_template("rdv_employe/rdv_employe_afficher.html", data=data_re)

@app.route("/rdv_employe_ajouter_wtf", methods=['GET', 'POST'])
def rdv_employe_ajouter_wtf():
    form = FormWTFAjouterRdvEmploye()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id_r": form.id_rdv_wtf.data,
                "id_e": form.id_employe_wtf.data
            }
            strsql = "INSERT INTO t_rdv_employe (id_employe, id_rdv) VALUES (%(id_e)s, %(id_r)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Employé assigné au rendez-vous avec succès !", "success")
            return redirect(url_for('rdv_employe_afficher', id_rdv_sel=0))
        except Exception as e:
            flash(f"Erreur : Cet employé est peut-être déjà assigné à ce RDV.", "danger")
    return render_template("rdv_employe/rdv_employe_ajouter_wtf.html", form=form)

@app.route("/rdv_employe_delete_wtf", methods=['GET', 'POST'])
def rdv_employe_delete_wtf():
    # Pour une table de liaison, on a besoin des DEUX ID pour cibler la bonne ligne
    id_rdv_del = request.values.get('id_rdv_del')
    id_emp_del = request.values.get('id_emp_del')
    
    form = FormWTFDeleteRdvEmploye()
    btn_del = False
    
    if form.validate_on_submit():
        if form.submit_btn_annuler.data: 
            return redirect(url_for("rdv_employe_afficher", id_rdv_sel=0))
        if form.submit_btn_conf_del.data: 
            btn_del = True
        if form.submit_btn_del.data:
            try:
                with DBconnection() as mconn:
                    mconn.execute("DELETE FROM t_rdv_employe WHERE id_rdv = %(id_r)s AND id_employe = %(id_e)s", 
                                  {"id_r": id_rdv_del, "id_e": id_emp_del})
                flash("Assignation supprimée !", "success")
                return redirect(url_for('rdv_employe_afficher', id_rdv_sel=0))
            except Exception as e:
                flash(f"Erreur lors de la suppression : {e}", "danger")
                return redirect(url_for('rdv_employe_afficher', id_rdv_sel=0))
                
    if request.method == "GET" or btn_del:
        with DBconnection() as mconn:
            mconn.execute("""
                SELECT e.prenom_employe, e.nom_employe, r.date_rdv 
                FROM t_rdv_employe re
                JOIN t_employe e ON re.id_employe = e.id_employe
                JOIN t_rendez_vous r ON re.id_rdv = r.id_rdv
                WHERE re.id_rdv = %(id_r)s AND re.id_employe = %(id_e)s
            """, {"id_r": id_rdv_del, "id_e": id_emp_del})
            res = mconn.fetchone()
            
        form.info_rdv_emp_delete_wtf.data = f"{res['prenom_employe']} {res['nom_employe']} assigné au RDV du {res['date_rdv']}"

    return render_template("rdv_employe/rdv_employe_delete_wtf.html", form_delete=form, btn_submit_del=btn_del)