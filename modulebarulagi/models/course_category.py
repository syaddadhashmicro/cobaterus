
from odoo import models, fields

class Course(models.Model):
    _name = 'syaddad.course.category'
    _description = 'Data Course Category'

    name = fields.Char(string='Category Name', required=True, help="Fill Course Category Name...")
    
    description = fields.Text(string='Description')

    active = fields.Boolean(string='Active', default=True)

    course_ids = fields.One2many(
        comodel_name='syaddad.course', 
        inverse_name='category_id', string='Course',
    )