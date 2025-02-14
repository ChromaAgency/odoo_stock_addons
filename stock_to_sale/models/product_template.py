from odoo import models, fields, api
from odoo.tools import float_round
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    stock_to_sale = fields.Float(string="Stock para ventas", compute="_compute_stock_to_sale", compute_sudo=False, digits='Product Unit of Measure')


    def _compute_stock_to_sale(self):
        stocks = self.env['stock.quant'].search([('product_id', 'in', self.ids), ('location_id.usage', '=', 'internal')])
        for rec in self:
            rec.stock_to_sale = sum(stocks.filtered(lambda s: s.product_id.id == rec.id).mapped('available_quantity'))


