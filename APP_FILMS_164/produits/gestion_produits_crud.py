from flask import render_template, redirect, url_for, request, flash
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.produits.gestion_produits_wtf_forms import FormWTFAjouterProduit, FormWTFDeleteProduit, \
    FormWTFUpdateProduit


@app.route("/produits_afficher/<string:order_by>/<int:id_produit_sel>", methods=['GET', 'POST'])
def produits_afficher(order_by, id_produit_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_produit_sel == 0:
                    strsql = "SELECT id_produit, nom_produit, quantite_stock, prix_unitaire FROM t_produit ORDER BY id_produit ASC"
                    mc_afficher.execute(strsql)
                elif order_by == "ASC":
                    strsql = "SELECT id_produit, nom_produit, quantite_stock, prix_unitaire FROM t_produit WHERE id_produit = %(v)s"
                    mc_afficher.execute(strsql, {"v": id_produit_sel})
                else:
                    strsql = "SELECT id_produit, nom_produit, quantite_stock, prix_unitaire FROM t_produit ORDER BY id_produit DESC"
                    mc_afficher.execute(strsql)
                data_produits = mc_afficher.fetchall()
                flash("Données des produits affichées", "success")
        except Exception as e:
            raise Exception(f"Erreur affichage produits : {e}")
    return render_template("produits/produits_afficher.html", data=data_produits)


@app.route("/produits_ajouter_wtf", methods=['GET', 'POST'])
def produits_ajouter_wtf():
    form = FormWTFAjouterProduit()
    if form.validate_on_submit():
        try:
            valeurs = {
                "nom": form.nom_produit_wtf.data,
                "qte": form.quantite_stock_wtf.data,
                "prix": form.prix_unitaire_wtf.data
            }
            strsql = "INSERT INTO t_produit (nom_produit, quantite_stock, prix_unitaire) VALUES (%(nom)s, %(qte)s, %(prix)s)"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Produit ajouté avec succès !", "success")
            return redirect(url_for('produits_afficher', order_by='DESC', id_produit_sel=0))
        except Exception as e:
            raise Exception(f"Erreur ajout produit : {e}")
    return render_template("produits/produits_ajouter_wtf.html", form=form)


@app.route("/produits_update_wtf", methods=['GET', 'POST'])
def produits_update_wtf():
    id_upd = request.values.get('id_produit_btn_edit_html')
    form = FormWTFUpdateProduit()
    if form.validate_on_submit():
        try:
            valeurs = {
                "id": id_upd,
                "nom": form.nom_produit_update_wtf.data,
                "qte": form.quantite_stock_update_wtf.data,
                "prix": form.prix_unitaire_update_wtf.data
            }
            strsql = "UPDATE t_produit SET nom_produit=%(nom)s, quantite_stock=%(qte)s, prix_unitaire=%(prix)s WHERE id_produit=%(id)s"
            with DBconnection() as mconn:
                mconn.execute(strsql, valeurs)
            flash("Mise à jour réussie", "success")
            return redirect(url_for('produits_afficher', order_by="ASC", id_produit_sel=id_upd))
        except Exception as e:
            raise Exception(f"Erreur update produit : {e}")
    elif request.method == "GET":
        with DBconnection() as mconn:
            mconn.execute("SELECT * FROM t_produit WHERE id_produit = %(id)s", {"id": id_upd})
            res = mconn.fetchone()
        form.nom_produit_update_wtf.data = res["nom_produit"]
        form.quantite_stock_update_wtf.data = res["quantite_stock"]
        form.prix_unitaire_update_wtf.data = res["prix_unitaire"]
    return render_template("produits/produits_update_wtf.html", form_update=form)


@app.route("/produits_delete_wtf", methods=['GET', 'POST'])
def produits_delete_wtf():
    id_del = request.values.get('id_produit_btn_delete_html')
    form = FormWTFDeleteProduit()
    btn_del = False
    data_ventes_associees = None

    if form.validate_on_submit():
        if form.submit_btn_annuler.data:
            return redirect(url_for("produits_afficher", order_by="ASC", id_produit_sel=0))
        if form.submit_btn_conf_del.data:
            btn_del = True
        if form.submit_btn_del.data:
            try:
                with DBconnection() as mconn:
                    mconn.execute("DELETE FROM t_produit WHERE id_produit = %(id)s", {"id": id_del})
                flash("Produit supprimé !", "success")
                return redirect(url_for('produits_afficher', order_by="ASC", id_produit_sel=0))
            except Exception as e:
                flash(f"Erreur lors de la suppression (vérifiez les ventes associées) : {e}", "danger")
                return redirect(url_for('produits_afficher', order_by="ASC", id_produit_sel=0))

    if request.method == "GET" or btn_del:
        with DBconnection() as mconn:
            mconn.execute("SELECT nom_produit FROM t_produit WHERE id_produit = %(id)s", {"id": id_del})
            res = mconn.fetchone()

            # Vérifier si le produit est lié à des ventes
            mconn.execute("SELECT id_vente, quantite FROM t_vendre WHERE id_produit = %(id)s", {"id": id_del})
            data_ventes_associees = mconn.fetchall()

        form.nom_produit_delete_wtf.data = res["nom_produit"]

    return render_template("produits/produits_delete_wtf.html", form_delete=form, btn_submit_del=btn_del,
                           data_ventes_associees=data_ventes_associees)