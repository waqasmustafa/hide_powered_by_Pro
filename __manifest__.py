
{
    'name': 'Remove Powered by Odoo from Website Footer , Email Template , Portal & Add Custom Text',
    'version': '18.0.1.6',
    'category': 'Website',
    'summary': 'Remove or Replace "Powered by Odoo" branding from Website, Portal, and Emails with Custom Text. Whitelabel your Odoo instance.',
    'description': """ 
    White-label your Odoo instance by removing default branding or replacing it with your own.

    **Key Features:**
    - **Hide Branding:** Removes "Powered by Odoo" from Website Footer, Portal, and Email Templates.
    - **Custom Branding:** Option to display your own custom text (HTML supported) instead of Odoo's.
    - **Easy Configuration:** New settings in General Settings to toggle custom branding and set your text.
    - **Scope:**
        - Website Footer
        - Customer Portal Sidebar
        - Email Templates (Welcome, Reset Password, Notifications, Digest, etc.)
        - Backend User Menu (Removes Documentation, Support links)
    """,
    'author': 'Waqas Mustafa',
    'price': 10.00,
    'currency': "USD",
    'website': 'https://www.linkedin.com/in/waqas-mustafa-ba5701209/',
    'support': 'mustafawaqas0@gmail.com',
    'depends': ['auth_signup','website', 'portal', 'base'],
    'data': [
        'views/res_config_settings_view.xml',
        'data/mail_template_data_portal_welcome.xml',
        'data/set_password_email.xml',
        'data/mail_template_user_signup_account_created.xml',
        'data/mail_notification_light.xml',
        'data/auth_signup_templates_email.xml',
        'data/digest_data.xml',
        'data/digest_tips_data.xml',
        'views/brand_promotion_message.xml',
        'views/portal_record_sidebar.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "hide_powered_by_Pro/static/src/js/odoo_user_menu.js"
        ],
    },
    'installable': True,
    'auto_install': False,
    "images": ['static/description/banner.gif'],
    'license': 'LGPL-3',
}


