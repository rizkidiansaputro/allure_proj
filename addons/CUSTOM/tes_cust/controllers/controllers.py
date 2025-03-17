# -*- coding: utf-8 -*-
# from odoo import http


# class TesCust(http.Controller):
#     @http.route('/tes_cust/tes_cust/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tes_cust/tes_cust/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tes_cust.listing', {
#             'root': '/tes_cust/tes_cust',
#             'objects': http.request.env['tes_cust.tes_cust'].search([]),
#         })

#     @http.route('/tes_cust/tes_cust/objects/<model("tes_cust.tes_cust"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tes_cust.object', {
#             'object': obj
#         })
