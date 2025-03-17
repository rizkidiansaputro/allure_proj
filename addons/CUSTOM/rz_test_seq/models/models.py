# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rz_test_seq(models.Model):
#     _name = 'rz_test_seq.rz_test_seq'
#     _description = 'rz_test_seq.rz_test_seq'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
