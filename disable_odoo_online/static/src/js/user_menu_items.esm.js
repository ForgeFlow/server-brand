import {registry} from "@web/core/registry";
// Needed so that this is run after adding the menu entries
import {user_menu_items} from "@web/webclient/user_menu/user_menu_items"; // eslint-disable-line no-unused-vars
import "@mysubscription/user_menu";

registry.category("user_menuitems").remove("support");
// Odoo.com subscription and plans dashboard (new in 20.0)
registry.category("user_menuitems").remove("mysubscription_user_menu");
