# -*- coding: utf-8 -*-
# from odoo import http


# class RzTestSeq(http.Controller):
#     @http.route('/rz_test_seq/rz_test_seq/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rz_test_seq/rz_test_seq/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rz_test_seq.listing', {
#             'root': '/rz_test_seq/rz_test_seq',
#             'objects': http.request.env['rz_test_seq.rz_test_seq'].search([]),
#         })

#     @http.route('/rz_test_seq/rz_test_seq/objects/<model("rz_test_seq.rz_test_seq"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rz_test_seq.object', {
#             'object': obj
#         })
