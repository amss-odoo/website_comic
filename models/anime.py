from odoo import fields,models

class anime(models.Model):
    _name= "anime.prod"
    _description= "Anime products"

    name = fields.Char(required=True)
    description = fields.Text()
    volume = fields.Selection(
        string='Volume',
        default="",
        selection=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],
        help="Volumes of the mangas available",
        tracking=True
    )
    image = fields.Binary(attachment=True, store=True)
    price = fields.Float(required=True)
    language = fields.Selection(
        string='Language',
        default="",
        selection=[('english','English'),('japanese','Japanese')],
        help="Available languages for manga",
        tracking=True
    )
    edition = fields.Selection(
        string='Edition',
        default="",
        selection=[('paperback','Paperback'),('hardcover','Hardcover'),('kindle','Kindle')],
        help="Available editions for manga",
        tracking=True
    )
    author = fields.Many2one(comodel_name='author',string='Author')
    publisher = fields.Many2one(comodel_name='publisher',string='Publisher')

    