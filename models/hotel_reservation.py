from odoo import models, fields, api

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'

    room_number = fields.Char(string='Número de Habitación', required=True)
    client_id = fields.Many2one('res.partner', string='Cliente', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha Final', required=True)
    calendar_event_id = fields.Many2one('calendar.event', string='Evento del Calendario')

    @api.model
    def create(self, vals):
        event_vals = {
            'name': f"Reserva: {vals['room_number']}",
            'start': vals['start_date'],
            'stop': vals['end_date'],
            'partner_ids': [(6, 0, [vals['client_id']])],
        }
        event = self.env['calendar.event'].create(event_vals)
        vals['calendar_event_id'] = event.id
        return super(HotelReservation, self).create(vals)
