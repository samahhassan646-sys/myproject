from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To Do Task to'

    active = fields.Boolean(default=True)
    ref = fields.Char(default='new', readonly=True)
    name = fields.Char(string="Name", required=True ,translate=True)
    assign_to_id = fields.Many2one('res.partner')
    description = fields.Text(string="Description" ,translate=True)
    due_date = fields.Date(string="Due Date")
    estimated_time = fields.Float(string="Estimated Time (Hours)")


