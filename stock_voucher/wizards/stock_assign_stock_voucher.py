##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, api, models, _
from odoo.exceptions import UserError

class StockPrintStockVoucher(models.TransientModel):
    _name = 'stock.assign_stock_voucher'
    _description = "Assign Stock Voucher"

    @property
    def picking_ids(self):
        picking_ids = self._context.get('picking_ids', [])
        return self.env['stock.picking'].browse(picking_ids)

    @api.model
    def _get_book(self):
        picking = self.picking_ids
        if len(picking.company_id) > 1:
            raise UserError(_('You must select a book for all pickings'))
        return picking.book_id or self.env['stock.book'].search([('company_id', '=', picking.company_id.id)], limit=1)

    book_id = fields.Many2one(
        'stock.book',
        'Book',
        default=lambda self: self._get_book(),
    )
    next_voucher_number = fields.Integer(
        'Next Voucher Number',
        related='book_id.sequence_id.number_next_actual',
    )
    estimated_number_of_pages = fields.Integer(
        'Number of Pages',
    )
    lines_per_voucher = fields.Integer(
        'Lines Per Voucher',
        related='book_id.lines_per_voucher',
    )

    def assign_numbers(self):
        for picking in self.picking_ids:
            picking.assign_numbers(picking.get_estimated_number_of_pages(), self.book_id)

    def do_print_and_assign(self):
        self.assign_numbers()
        return {'type': 'ir.actions.act_window_close'}
