from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.vendre.gestion_vendre_wtf_forms import FormWTFAjouterVente, FormWTFDeleteVente, FormWTFUpdateVente

@app.route("/vendre_afficher/<string:order_by>/<int:id_vente_sel>", methods=['GET', 'POST'])
def vendre_afficher(order_by, id_vente_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                # Jointure pour récupérer les noms (employé, produit, client) au lieu de juste voir leurs IDs
                requete_base = """
                    SELECT v.id_vente, e.nom_employe, e.prenom_employe, p.nom_produit, c.nom, c.prenom, v.quantite 
                    FROM t_vendre v
                    LEFT JOIN t_employe e ON v.id_employe = e.id_employe
                    LEFT JOIN t_produit p ON v.id_produit = p.id_produit
                    LEFT JOIN t_client c ON v.id_client = c.id_client
                """
                if order_by == "ASC" and id_vente_sel == 0:
                    strsql = requete_base + " ORDER BY v.id_vente ASC"
                    mc_afficher.execute(strsql)
                elif order_by == "ASC":
                    strsql = requete_base + " WHERE v.id_vente = %(v)s"
                    mc_afficher.execute(strsql, {"v": id_vente_sel})
                else:
                    strsql = requete_base + " ORDER BY v.id_vente DESC"
                    mc_afficher.execute(strsql)
                
                data_ventes = mc_afficher.fetchall()
                flash("Données des ventes affichées", "success")
        except Exception as e:
            raise Exception(f"Erreur affichage ventes : {e}")
            
    return render_template("vendre/vendre_afficher.html", data=data_ventes)

@app.route("/vendre_ajouter_wtf", methods=['GET', 'POST'])
def vendre_ajouter_wtf():
    form = FormWTFAjouterVente()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id_emp": form.id_employe_wtf.data,
                "id_prod": form.id_produit_wtf.data,
                "id_cli": form.id_client_wtf.data,
                "qte": form.quantite_wtf.data
            }
            strsql = "INSERT INTO t_vendre (id_employe, id_produit, id_client, quantite) VALUES (%(id_emp)s, %(id_prod)s, %(id_cli)s, %(qte)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Vente ajoutée avec succès !", "success")
            return redirect(url_for('vendre_afficher', order_by='DESC', id_vente_sel=0))
        except Exception as e:
            raise Exception(f"Erreur ajout vente : {e}")
            
    return render_template("vendre/vendre_ajouter_wtf.html", form=form)

@app.route("/vendre_update_wtf", methods=['GET', 'POST'])
def vendre_update_wtf():
    id_upd = request.values.get('id_vente_btn_edit_html')
    form = FormWTFUpdateVente()
    
    if form.validate_on_submit():
        try:
            valeurs = {
                "id_vente": id_upd,
                "id_emp": form.id_employe_update_wtf.data,
                "id_prod": form.id_produit_update_wtf.data,
                "id_cli": form.id_client_update_wtf.data,
                "qte": form.quantite_update_wtf.data
            }
            strsql = """UPDATE t_vendre 
                        SET id_employe=%(id_emp)s, id_produit=%(id_prod)s, id_client=%(id_cli)s, quantite=%(qte)s 
                        WHERE id_vente=%(id_vente)s"""
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Mise à jour réussie", "success")
            return redirect(url_for('vendre_afficher', order_by="ASC", id_vente_sel=id_upd))
        except Exception as e:
            raise Exception(f"Erreur update vente : {e}")
            
    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT * FROM t_vendre WHERE id_vente = %(id)s", {"id": id_upd})
            res = mconn.fetchone()
            
        form.id_employe_update_wtf.data = res["id_employe"]
        form.id_produit_update_wtf.data = res["id_produit"]
        form.id_client_update_wtf.data = res["id_client"]
        form.quantite_update_wtf.data = res["quantite"]
        
    return render_template("vendre/vendre_update_wtf.html", form_update=form)

@app.route("/vendre_delete_wtf", methods=['GET', 'POST'])
def vendre_delete_wtf():
    id_del = request.values.get('id_vente_btn_delete_html')
    form = FormWTFDeleteVente()
    btn_del = False
    
    if form.validate_on_submit():
        if form.submit_btn_annuler.data: 
            return redirect(url_for("vendre_afficher", order_by="ASC", id_vente_sel=0))
        if form.submit_btn_conf_del.data: 
            btn_del = True
        if form.submit_btn_del.data:
            try:
                with DBconnection() as mconn:
                    mconn.execute("DELETE FROM t_vendre WHERE id_vente = %(id)s", {"id": id_del})
                flash("Vente supprimée !", "success")
                return redirect(url_for('vendre_afficher', order_by="ASC", id_vente_sel=0))
            except Exception as e:
                flash(f"Erreur lors de la suppression : {e}", "danger")
                return redirect(url_for('vendre_afficher', order_by="ASC", id_vente_sel=0))
                
    if request.method == "GET" or btn_del:
        with DBconnection() as mconn:
            mconn.execute("SELECT id_vente FROM t_vendre WHERE id_vente = %(id)s", {"id": id_del})
            res = mconn.fetchone()
            
        form.info_vente_delete_wtf.data = f"Vente Numéro {res['id_vente']}"

    return render_template("vendre/vendre_delete_wtf.html", form_delete=form, btn_submit_del=btn_del)