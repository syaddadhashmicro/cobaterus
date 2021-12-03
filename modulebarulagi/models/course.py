
from odoo import models, fields

class Course(models.Model):
    _name = 'syaddad.course'
    _description = 'Data Course'

    name = fields.Char(string='Course Name', required=True, help="Fill Course Name...")
    
    description = fields.Text(string='Description')

    active = fields.Boolean(string='Active', default=True)

    category_id = fields.Many2one(comodel_name="syaddad.course.category",
        string="Category",
        required=True,
    )