# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime

class Account_analytic_Area(models.Model):
    _inherit = "account.analytic.account"
    functional_area_id = fields.Many2one('functional.area', 'Area Funcional')
