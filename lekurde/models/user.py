# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _inherit = 'res.users'

    def init(self):
        super().init()
        index = [
            "CREATE INDEX IF NOT EXISTS idx_res_partner_user_id_fkey ON res_partner(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_res_partner_write_uid_fkey ON res_partner(write_uid)",
            "CREATE INDEX IF NOT EXISTS idx_res_currency_rate_create_uid_fkey ON res_currency_rate(create_uid)",
            "CREATE INDEX IF NOT EXISTS idx_res_currency_rate_write_uid_fkey ON res_currency_rate(write_uid)",
            "CREATE INDEX IF NOT EXISTS idx_mail_tracking_value_create_uid_fkey ON mail_tracking_value(create_uid)",
            "CREATE INDEX IF NOT EXISTS idx_mail_tracking_value_write_uid_fkey ON mail_tracking_value(write_uid)",
            "CREATE INDEX IF NOT EXISTS idx_mail_message_write_uid_fkey ON mail_message(write_uid)",
            "CREATE INDEX IF NOT EXISTS idx_ir_filters_user_id_fkey ON ir_filters(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_ir_filters_write_uid_fkey ON ir_filters(write_uid)",
            "CREATE INDEX IF NOT EXISTS idx_ir_filters_create_uid_fkey ON ir_filters(create_uid)",
            "CREATE INDEX IF NOT EXISTS idx_ir_attachment_create_uid_fkey ON ir_attachment(create_uid)",
            "CREATE INDEX IF NOT EXISTS idx_ir_attachment_write_uid_fkey ON ir_attachment(write_uid)",
        ]
        for idx in index:
            self.env.cr.execute(idx)


