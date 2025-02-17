/** @odoo-module */
/**
 * registers a new handler to generate xlsx report
 */
import { registry } from "@web/core/registry";
import framework from 'web.framework';
import session from 'web.session';
registry.category("ir.actions.report handlers").add("reportXlsx", async (action) => {
   if (action.report_type === 'xlsx') {
       framework.blockUI();
       var def = $.Deferred();
       session.get_file({
           url: '/report_xlsx',
           data: action.data,
           success: def.resolve.bind(def),
           error: (error) => this.call('crash_manager', 'rpc_error', error),
           complete: framework.unblockUI,
       });
       return def;
   }
});