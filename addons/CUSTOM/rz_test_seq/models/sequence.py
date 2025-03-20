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
    fppp_config_id = fields.Many2one('sequence.config', string="Configuration")  # Many2one ke sequence.config

    # Override metode create untuk generate sequence setelah record disimpan
    # Default Awal
    # @api.model
    # def create(self, vals):
    #     # Panggil metode create dari parent class
    #     record = super(FpppModel, self).create(vals)
    #     # Generate sequence setelah record disimpan
    #     record.code_fppp = self.env['ir.sequence'].next_by_code('fppp.custom.sequence') or '/'
    #     return record

    # #Tes ambil dari config
    # Override metode create untuk generate sequence setelah record disimpan
    @api.model
    def create(self, vals):
        # Panggil metode create dari parent class
        record = super(FpppModel, self).create(vals)
        # Generate sequence setelah record disimpan
        # prefix = record.fppp_config_id.code_prefix_fppp or ''  # Ambil prefix dari configuration
        # suffix = record.fppp_config_id.name_fppp or ''  # Ambil suffix dari configuration
        prefix = record.fppp_config_id.prefix_seq_conf or ''  # Ambil prefix dari configuration
        suffix = record.fppp_config_id.suffix_seq_conf or ''  # Ambil suffix dari configuration
        
        ## debug log
        # _logger = logging.getLogger(__name__)
        # _logger.info(f"Prefix: {prefix}, Suffix: {suffix}")  # Debugging
        
        # sequence_code = f"{prefix}{suffix}"  # Gabungkan prefix dan suffix
        # record.code_fppp = self.env['ir.sequence'].with_context(sequence_code=sequence_code).next_by_code('fppp.custom.sequence') or '/'

        # Pastikan prefix dan suffix dikirim dalam context
        record.code_fppp = self.env['ir.sequence'].with_context(prefix=prefix, suffix=suffix).next_by_code('fppp.custom.sequence') or '/'


        # Kirim prefix dan suffix sebagai konteks terpisah
        # record.code_fppp = self.env['ir.sequence'].with_context(
        #     prefix=prefix,
        #     suffix=suffix
        # ).next_by_code('fppp.custom.sequence') or '/'
        return record



class SequenceConfig(models.Model):
    _name = 'sequence.config'
    _description = 'Sequence Configuration'

    name = fields.Char(string="Nama", required=True)
    prefix_seq_conf = fields.Char(string="Prefix", required=True)
    suffix_seq_conf = fields.Char(string="Suffix", required=True)
    padding_seq_conf = fields.Integer(string="Padding", required=True, default=5)
    number_next_seq_conf = fields.Integer(string="Next Number", required=True, default=1)
    number_increment_seq_conf = fields.Integer(string="Increment", required=True, default=1)

    # Fungsi untuk mengupdate sequence
    def update_sequence(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'fppp.custom.sequence')], limit=1)
        if sequence:
            sequence.write({
                'prefix': self.prefix_seq_conf,
                'suffix': self.suffix_seq_conf,
                'padding': self.padding_seq_conf,
                'number_next': self.number_next_seq_conf,
                'number_increment': self.number_increment_seq_conf,
            })