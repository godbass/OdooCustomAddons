# -- coding: utf-8 --

from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)

class CoutureCouturier(models.Model):
    _name = 'couture.couturier'
    _description = 'Dressmaker'

    couturier_name = fields.Char("Nom", required=True, )
    couturier_firstname = fields.Char("Prenom", required=True, )
    contact = fields.Many2one('res.partner', 'Contact', ondelete='cascade')
    speciality = fields.Selection([ ('men', 'Homme'),('women', 'Femme'),('children', 'Enfant')], string="Specialite")
    couturier_age = fields.Char("Age")

    client = fields.One2many('couture.clientslist', 'name', string='Clients')


class CoutureClient(models.Model):
    _name = 'couture.client'
    _description = 'Dressmaker'

    client_name = fields.Char("Nom", required=True)
    client_firstname = fields.Char("Prenom", required=True, )
    contact = fields.Many2one('res.partner', 'Contact', ondelete='cascade')
    speciality = fields.Selection([ ('men', 'Homme'),('women', 'Femme'),('children', 'Enfant')], string="Specialite")
    client_age = fields.Char("Age")


class modele(models.Model):
    _name = 'couture.modele'

    client = fields.Many2one('couture.client', 'Client')
    modele_name = fields.Char(string="Nom du modèle", required=True)
    modele_type = fields.Char(string="Description")
    modele_mesure = fields.Many2one('couture.mesure', 'Mésures corporelles', ondelete='cascade')
    mesures = fields.Many2one('couture.modele', 'Modèle', ondelete='cascade')


class ClientsList(models.Model):
    _name = 'couture.clientslist'
    
    name = fields.Many2one('res.partner', 'Client')
    test = fields.Char("Test")


class mesure(models.Model):
    _name = 'couture.mesure'

    client = fields.Char("Client")
    taille = fields.Float(string="Taille (cm)")
    poitrine = fields.Float(string="Poitrine (cm)")
    hanche = fields.Float(string="Hanche (cm)")
    ceinture = fields.Float(string="Ceinture(cm)")
    epaules = fields.Float(string="Epaule(cm)")
    bras = fields.Float(string="Bras(cm)")
    image = fields.Binary("Tissu", help="Veuillez insérer une image")


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'        

    birthday = fields.Date('Date de naissance', required=True)
    age = fields.Char("Age")
    mesures = fields.Char("Age")
    birthday = fields.Char("Age")

class factureInherit(models.Model):
    _inherit = 'res.partner'