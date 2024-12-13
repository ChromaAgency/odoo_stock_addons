from odoo.models import Model
from odoo.fields import Float

class SaleOrderLine(Model):
    _inherit = 'sale.order.line'

    qty_available = Float(string="Stock a mano", related="product_id.qty_available")
    virtual_available = Float(string="Stock previsto", related="product_id.virtual_available")
    