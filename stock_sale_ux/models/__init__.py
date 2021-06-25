from odoo.models import Model
from odoo.fields import Float

class SaleOrderLine(Model):
    _inherit = 'sale.order.line'

    qty_available = Float(string="Cantidad en inventario", related="product_id.qty_available")
    