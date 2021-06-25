from odoo.models import Model
from odoo.fields import Datetime

class StockMoveLine(Model):
    _inherit = 'stock.move.line'

    use_date = Datetime(related="lot_id.use_date", readonly=False)
