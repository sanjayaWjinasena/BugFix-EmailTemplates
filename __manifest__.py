# -*- coding: utf-8 -*-
{
    'name': 'BugFix - EmailTemplates',
    'version': '17.0.0.0.2',
    'summary': 'Studio-authored mail.template records',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Discuss',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization — Odoo SH does not ship a manifest for it.
    'depends': ['base_setup', 'mail'],
    'data': [
        'data/mail_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
