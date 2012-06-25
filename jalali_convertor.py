from osv import osv, fields


class JalaliConvertorWizard(osv.osv_memory):
    _name = 'jalali.convertor.wizard'
    _inherit = 'ir.wizard.screen'

    _columns = {
        'ir_module_module_id': fields.many2one('ir.module.module',
                                               'IR Module Module'),
        'state': fields.selection([('init', 'init'), ('done', 'done')],
                                  'state', readonly=True),
    }

    _defaults = {'state': 'init'}

    def do_convert(self, cr, uid, ids, context=None):
        print "durud"
        pass

JalaliConvertorWizard()
