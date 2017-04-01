# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Functional_Area_Analytical_Accounts(models.Model):
    _description = "Areas Funcionales"
    _name = 'functional.area'
    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Name', translate=True, required=True)
    desc = fields.Text('Texto', translate=True)
    debe = fields.Float('Debe', translate=True)
    haber = fields.Float('Haber', translate=True)
    saldo = fields.Float('Saldo', translate=True)