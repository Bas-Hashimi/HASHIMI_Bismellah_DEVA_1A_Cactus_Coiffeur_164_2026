from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import Length, InputRequired, NumberRange

class FormWTFAjouterProduit(FlaskForm):
    nom_produit_wtf = StringField("Nom du produit", validators=[Length(min=2, max=100), InputRequired()])
    quantite_stock_wtf = IntegerField("Quantité en stock", validators=[InputRequired(), NumberRange(min=0, message="La quantité doit être positive")])
    prix_unitaire_wtf = DecimalField("Prix unitaire (CHF)", validators=[InputRequired(), NumberRange(min=0.0, message="Le prix doit être positif")])
    submit = SubmitField("Enregistrer le produit")

class FormWTFUpdateProduit(FlaskForm):
    nom_produit_update_wtf = StringField("Nom du produit", validators=[Length(min=2, max=100), InputRequired()])
    quantite_stock_update_wtf = IntegerField("Quantité en stock", validators=[InputRequired(), NumberRange(min=0)])
    prix_unitaire_update_wtf = DecimalField("Prix unitaire (CHF)", validators=[InputRequired(), NumberRange(min=0.0)])
    submit = SubmitField("Mettre à jour le produit")

class FormWTFDeleteProduit(FlaskForm):
    nom_produit_delete_wtf = StringField("Effacer ce produit")
    submit_btn_del = SubmitField("Effacer le produit")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")