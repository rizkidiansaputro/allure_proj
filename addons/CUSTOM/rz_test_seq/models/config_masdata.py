from odoo import models, fields, api

class CustomConfigModel(models.Model):
    _name = 'brand.mass.model'
    _description = 'Brand Master Data Model'

    nama = fields.Char(string="Nama Brand", required=True)
    kode = fields.Char(string="Kode Sequence", required=True)
    desc = fields.Char(string="Deskripsi")