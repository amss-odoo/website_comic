from odoo import fields,models

class author(models.Model):
    _name= "author"
    _description= "Manga authors"

    name = fields.Char(required=True)
    
    _sql_constraints = [
        ('check_author','UNIQUE(name)','Authors should be unique.')
    ]