"""
    Fichier : gestion_clients_wtf_forms.py
    Gestion des formulaires avec WTF pour les CLIENTS
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterClient(FlaskForm):
    """
        Formulaire pour ajouter un client.
    """
    nom_client_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"

    nom_client_wtf = StringField("Nom du client ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_client_regexp, message="Lettres uniquement")])
    prenom_client_wtf = StringField("Prénom du client ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                   Regexp(nom_client_regexp, message="Lettres uniquement")])
    telephone_client_wtf = StringField("Téléphone ", validators=[Length(min=10, max=20, message="Format invalide")])

    submit = SubmitField("Enregistrer le client")


class FormWTFUpdateClient(FlaskForm):
    """
        Formulaire pour mettre à jour un client.
    """
    nom_client_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"

    nom_client_update_wtf = StringField("Nom du client ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(nom_client_update_regexp, message="Lettres uniquement")])
    prenom_client_update_wtf = StringField("Prénom du client ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(nom_client_update_regexp, message="Lettres uniquement")])
    telephone_client_update_wtf = StringField("Téléphone ", validators=[Length(min=10, max=20, message="Format invalide")])

    submit = SubmitField("Mettre à jour le client")


class FormWTFDeleteClient(FlaskForm):
    """
        Formulaire pour supprimer un client.
    """
    nom_client_delete_wtf = StringField("Effacer ce client")
    submit_btn_del = SubmitField("Effacer définitivement")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")