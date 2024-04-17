from odoo import fields,models

class publisher(models.Model):
    _name= "publisher"
    _description= "Publishing houses"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_publisher','UNIQUE(name)','Publishing house should be unique.')
    ]