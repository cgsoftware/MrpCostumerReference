# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from tools.translate import _

from osv import fields, osv

#
# Dimensions Definition
#
class mrp_production(osv.osv):
    _inherit = 'mrp.production'
    
    def _production_partner(self, cr, uid, ids, prop, unknow_none, context=None):
        """ Calculates total hours and total no. of cycles for a production order.
        @param prop: Name of field.
        @param unknow_none:
        @return: Dictionary of values.
        """
        result = {}
        for prod in self.browse(cr, uid, ids, context=context):
            result[prod.id] = {
                'partner_id':'',
                'partner_rag_soc':'',
            }
            #import pdb;pdb.set_trace()
            if  prod.origin:
              # ha trovato un dato nelle origini verifica che esista un ordine cliente e ne legge l'informazione
              cerca = [('name','=',prod.origin)]
              sale_ids = self.pool.get('sale.order').search(cr,uid,cerca)
              if sale_ids:
                riga_sale = self.pool.get('sale.order').browse(cr,uid,sale_ids)[0]
                result[prod.id]['partner_ref'] = riga_sale.partner_id.ref
                result[prod.id]['partner_rag_soc'] = riga_sale.partner_id.name
        return result      


    _columns = {

        'partner_ref': fields.function(_production_partner, method=True, type='char', string='Codice Partner', multi='workorder', store=False),
        'partner_rag_soc': fields.function(_production_partner, method=True, type='char', string='Nome Partner', multi='workorder', store=False),
    }
   
mrp_production()


