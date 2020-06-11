import base64
from datetime import datetime
from io import BytesIO
import calendar

from odoo import api, fields, models, _
from odoo.tools.misc import xlwt


class StockConsignmentReport(models.TransientModel):
    _name = 'stock.consignment.report'

    from_date = fields.Date(string='Date From')
    to_date = fields.Date(string='Date To')
    company_id = fields.Many2one(comodel_name='res.company', string='Company')

    @api.multi
    def consignment_stock_report_print(self):
        print('23333333')
