# -*- coding: utf-8 -*-
from odoo import http
import xmlrpc.client
import json

class Ambassador(http.Controller):
    @http.route('/webservice',type='json', methods=['POST'], auth='none',cors='*')
    def find_ambassador(self,**args):
        name = args.get('name', False)
        # Testing a new route with the web server
        # return name
        url = 'https://academia-n2.odoo.com'
        db = 'academia-n-principal-1361278'
        username = 'harry.lopez@academia-n.com'
        password = '12345'
        #getting client version
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        #authenticate to db
        uid = common.authenticate(db, username, password, {})
        # get models
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        #get all models ids
        models_ids = models.execute_kw(db,uid,password,'res.partner','search',[[['is_company','=',True]]])
        # query to res.partner uing ORM and fields
        query = models.execute_kw(db,uid,password,'res.partner','search_read',[[['name','ilike',name]]],{'fields':['name','company_id']})
        return json.dumps(query)
