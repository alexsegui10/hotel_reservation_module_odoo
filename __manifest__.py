{
    'name': 'Hotel Reservation',
    'version': '1.0',
    'summary': 'Gestión de Reservas de Hotel',
    'category': 'Services',
    'author': 'Tu Nombre',
    'website': 'tusitio.com',
    'license': 'AGPL-3',
    'depends': ['base', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_reservation_view.xml',
        'views/hotel_reservation_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
