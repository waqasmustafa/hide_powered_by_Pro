
{
    'name': 'Remove Powered by Odoo from Website Footer , Email Template , Portal & Add Custom Text',
    'version': '18.0.1.5',
    'category': 'Website',
    'summary': 'This Odoo module focuses on removing default branding (remove powered by odoo create a free website ) elements such as "Powered by Odoo" from websites, portals, and footers. It offers a seamless solution for businesses aiming to personalize their Odoo instance and maintain a professional, white-labeled appearance. remove Powered by Odoo - The #1 Open Source eCommerce, hide Powered by Odoo - The #1 Open Source eCommerce, Remove Powered by Odoo,Remove Built with Odoo – The #1 Open Source Business App Suite,Remove Odoo: Open Source ERP & eCommerce Platform,Remove Odoo Website Builder – Build Your Site with Ease,Remove Made with ❤ using Odoo,Remove Odoo eCommerce – Modern, Fast, and Open Source',
    'description': """ 
    removed website powered by odoo
    Remove Odoo eCommerce – Modern, Fast, and Open Source,
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


