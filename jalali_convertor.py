from osv import osv, fields


class JalaliConvertorWizard(osv.osv_memory):
    _name = 'jalali.convertor.wizard'
    _inherit = 'ir.wizard.screen'

    _columns = {
        'ir_model_id': fields.many2one('ir.model', 'IR Model'),
        'state': fields.selection([('init', 'init'), ('done', 'done')],
                                  'state', readonly=True),
    }

    _defaults = {'state': 'init'}

    def do_convert(self, cr, uid, ids, context=None):
        this = self.browse(cr, uid, ids, context=context)[0]
#        ir_model_field_list = this.ir_model_id.field_id

#        field_list = []
#
#        for ir_model_field in ir_model_field_list:
#            if ir_model_field.name.endswith("_group_by"):
#                field_list.append(ir_model_field.name[:-9])
#
#        if field_list:
        input_model_obj = self.pool.get(this.ir_model_id.model)
        input_id_list = input_model_obj.search(cr, uid, [], context=context)
        input_model_obj.write(cr, uid, input_id_list, {}, context=context)

        return self.write(cr, uid, ids, {'state': 'done'}, context=context)

JalaliConvertorWizard()
