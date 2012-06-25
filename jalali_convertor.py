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
        print "durud"
        pass

JalaliConvertorWizard()
