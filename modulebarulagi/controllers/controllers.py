# -*- coding: utf-8 -*-
# from odoo import http


# class Modulebarulagi(http.Controller):
#     @http.route('/modulebarulagi/modulebarulagi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulebarulagi/modulebarulagi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulebarulagi.listing', {
#             'root': '/modulebarulagi/modulebarulagi',
#             'objects': http.request.env['modulebarulagi.modulebarulagi'].search([]),
#         })

#     @http.route('/modulebarulagi/modulebarulagi/objects/<model("modulebarulagi.modulebarulagi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulebarulagi.object', {
#             'object': obj
#         })
