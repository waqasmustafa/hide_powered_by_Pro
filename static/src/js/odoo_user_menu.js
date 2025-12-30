/** @odoo-module **/

import { registry } from "@web/core/registry";
import { user_menu_items } from "@web/webclient/user_menu/user_menu_items"; // Ensures default items are registered

registry.category("user_menuitems").remove("documentation");
registry.category("user_menuitems").remove("support");
registry.category("user_menuitems").remove("odoo_account");
registry.category("user_menuitems").remove("install_pwa");
