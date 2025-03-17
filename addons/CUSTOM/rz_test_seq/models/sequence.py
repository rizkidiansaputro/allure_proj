from odoo import models, fields, api

class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", readonly=True)
    
    ## generate saat sebelum disave menggunakan _generate_code
    ## code = fields.Char(string="Code", readonly=True, default=lambda self: self._generate_code())

    ## @api.model
    ## def _generate_code(self):
    ##     return self.env['ir.sequence'].next_by_code('custom.sequence') or '/'

    # Override metode create untuk generate sequence setelah record disimpan
    @api.model
    def create(self, vals):
        # Panggil metode create dari parent class
        record = super(CustomModel, self).create(vals)
        # Generate sequence setelah record disimpan
        record.code = self.env['ir.sequence'].next_by_code('custom.sequence') or '/'
        return record



class FpppModel(models.Model):
    _name = 'fppp.model'
    _description = 'FPPP Model'

    name_fppp = fields.Char(string="Name FPPP", required=True)
    code_fppp = fields.Char(string="Code FPPP", readonly=True)

    # Override metode create untuk generate sequence setelah record disimpan
    @api.model
    def create(self, vals):
        # Panggil metode create dari parent class
        record = super(FpppModel, self).create(vals)
        # Generate sequence setelah record disimpan
        record.code_fppp = self.env['ir.sequence'].next_by_code('fppp.custom.sequence') or '/'
        return record



class SequenceConfig(models.Model):
    _name = 'sequence.config'
    _description = 'Sequence Configuration'

    name = fields.Char(string="Name", required=True)
    prefix = fields.Char(string="Prefix", required=True)
    padding = fields.Integer(string="Padding", required=True, default=5)
    number_next = fields.Integer(string="Next Number", required=True, default=1)
    number_increment = fields.Integer(string="Increment", required=True, default=1)

    # Fungsi untuk mengupdate sequence
    def update_sequence(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'custom.sequence')], limit=1)
        if sequence:
            sequence.write({
                'prefix': self.prefix,
                'suffix': self.suffix,
                'padding': self.padding,
                'number_next': self.number_next,
                'number_increment': self.number_increment,
            })