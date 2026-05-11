from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Ejemplo del tutorial, tema 3'

    name = fields.Char()
    description = fields.Text()
    expected_price = fields.Float()
