"""
Gestion des "routes" FLASK et des données pour les CLIENTS.
Fichier : gestion_clients_crud.py
"""
from pathlib import Path

from flask import redirect, request, session, url_for, render_template, flash

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *

# On importe les nouveaux formulaires qu'on vient de créer
from APP_FILMS_164.clients.gestion_clients_wtf_forms import FormWTFAjouterClient, FormWTFUpdateClient, FormWTFDeleteClient

@app.route("/clients_afficher/<string:order_by>/<int:id_client_sel>", methods=['GET', 'POST'])
def clients_afficher(order_by, id_client_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_client_sel == 0:
                    strsql_clients_afficher = "SELECT * FROM t_client ORDER BY id_client ASC"
                    mc_afficher.execute(strsql_clients_afficher)
                elif order_by == "ASC":
                    valeur_id_client_selected_dictionnaire = {"value_id_client_selected": id_client_sel}
                    strsql_clients_afficher = "SELECT * FROM t_client WHERE id_client = %(value_id_client_selected)s"
                    mc_afficher.execute(strsql_clients_afficher, valeur_id_client_selected_dictionnaire)
                else:
                    strsql_clients_afficher = "SELECT * FROM t_client ORDER BY id_client DESC"
                    mc_afficher.execute(strsql_clients_afficher)

                data_clients = mc_afficher.fetchall()

                if not data_clients and id_client_sel == 0:
                    flash("""La table "t_client" est vide. !!""", "warning")
                elif not data_clients and id_client_sel > 0:
                    flash(f"Le client demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données clients affichées !!", "success")

        except Exception as Exception_clients_afficher:
            raise Exception(f"Erreur clients_afficher : {Exception_clients_afficher}")

    # ATTENTION: Assure-toi que ton fichier s'appelle bien "clients_afficher.html"
    return render_template("clients/clients_afficher.html", data=data_clients)


@app.route("/clients_ajouter", methods=['GET', 'POST'])
def clients_ajouter_wtf():
    form = FormWTFAjouterClient()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom = form.nom_client_wtf.data
                prenom = form.prenom_client_wtf.data
                telephone = form.telephone_client_wtf.data

                valeurs_insertion_dictionnaire = {"value_nom": nom, "value_prenom": prenom, "value_telephone": telephone}

                strsql_insert_client = """INSERT INTO t_client (id_client, nom, prenom, telephone) 
                                          VALUES (NULL, %(value_nom)s, %(value_prenom)s, %(value_telephone)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_client, valeurs_insertion_dictionnaire)

                flash(f"Nouveau client inséré !!", "success")
                return redirect(url_for('clients_afficher', order_by='DESC', id_client_sel=0))

        except Exception as Exception_clients_ajouter_wtf:
            raise Exception(f"Erreur ajout client : {Exception_clients_ajouter_wtf}")

    return render_template("clients/clients_ajouter_wtf.html", form=form)


@app.route("/clients_update", methods=['GET', 'POST'])
def clients_update_wtf():
    id_client_update = request.values.get('id_client_btn_edit_html')
    form_update = FormWTFUpdateClient()
    try:
        if request.method == "POST" and form_update.submit.data:
            nom = form_update.nom_client_update_wtf.data
            prenom = form_update.prenom_client_update_wtf.data
            telephone = form_update.telephone_client_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_client": id_client_update,
                "value_nom": nom,
                "value_prenom": prenom,
                "value_telephone": telephone
            }

            str_sql_update_client = """UPDATE t_client SET nom = %(value_nom)s, prenom = %(value_prenom)s, 
                                       telephone = %(value_telephone)s WHERE id_client = %(value_id_client)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_client, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            return redirect(url_for('clients_afficher', order_by="ASC", id_client_sel=id_client_update))

        elif request.method == "GET":
            str_sql_id_client = "SELECT id_client, nom, prenom, telephone FROM t_client WHERE id_client = %(value_id_client)s"
            valeur_select_dictionnaire = {"value_id_client": id_client_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_client, valeur_select_dictionnaire)
            data_client = mybd_conn.fetchone()

            # Pré-remplir les champs
            form_update.nom_client_update_wtf.data = data_client["nom"]
            form_update.prenom_client_update_wtf.data = data_client["prenom"]
            form_update.telephone_client_update_wtf.data = data_client["telephone"]

    except Exception as Exception_client_update_wtf:
        raise Exception(f"Erreur update client : {Exception_client_update_wtf}")

    return render_template("clients/clients_update_wtf.html", form_update=form_update)


@app.route("/clients_delete", methods=['GET', 'POST'])
def clients_delete_wtf():
    data_rdv_associes = None
    btn_submit_del = None
    id_client_delete = request.values.get('id_client_btn_delete_html')
    form_delete = FormWTFDeleteClient()

    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("clients_afficher", order_by="ASC", id_client_sel=0))

            if form_delete.submit_btn_conf_del.data:
                data_rdv_associes = session.get('data_rdv_associes')
                flash(f"Attention, vous allez effacer ce client de façon définitive !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_client": id_client_delete}

                # S'il y a des clés étrangères, il faut d'abord supprimer les RDV de ce client
                str_sql_delete_rdv = """DELETE FROM t_rendez_vous WHERE id_client = %(value_id_client)s"""
                str_sql_delete_client = """DELETE FROM t_client WHERE id_client = %(value_id_client)s"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_rdv, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_client, valeur_delete_dictionnaire)

                flash(f"Client définitivement effacé !!", "success")
                return redirect(url_for('clients_afficher', order_by="ASC", id_client_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_client": id_client_delete}

            # Requête pour voir si le client a des rendez-vous
            str_sql_rdv_associes = """SELECT date_rdv FROM t_rendez_vous WHERE id_client = %(value_id_client)s"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_rdv_associes, valeur_select_dictionnaire)
                data_rdv_associes = mydb_conn.fetchall()
                session['data_rdv_associes'] = data_rdv_associes

                # Récupérer le nom du client pour l'afficher
                str_sql_client = "SELECT nom, prenom FROM t_client WHERE id_client = %(value_id_client)s"
                mydb_conn.execute(str_sql_client, valeur_select_dictionnaire)
                data_client = mydb_conn.fetchone()

            nom_complet = f"{data_client['nom']} {data_client['prenom']}"
            form_delete.nom_client_delete_wtf.data = nom_complet
            btn_submit_del = False

    except Exception as Exception_client_delete_wtf:
        raise Exception(f"Erreur delete client : {Exception_client_delete_wtf}")

    return render_template("clients_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_rdv_associes=data_rdv_associes)