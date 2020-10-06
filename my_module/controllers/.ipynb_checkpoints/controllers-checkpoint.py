# -*- coding: utf-8 -*-
from odoo import http
import xmlrpc.client
import json

class MyModule(http.Controller):
    @http.route('/my_module/my_module/', auth='public')
    def index(self, **kw):    
        return "Hello, world"
    @http.route('/my_module/my_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('my_module.listing', {
            'root': '/my_module/my_module',
            'objects': http.request.env['my_module.my_module'].search([]),
        })

    @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_module.object', {
            'object': obj
        })
    
    #webservice controller 
    @http.route('/webservice',type='json', methods=['POST'], auth='public')
    def find_ambassador(self,**kw):
        id =  http.request.params.get('id')
        return id.values()
        # Testing a new route with the web server
        url = 'https://academia-n2.odoo.com'
        db = 'academia-n-principal-1361278'
        username = 'harry.lopez@academia-n.com'
        password = '12345'
        return id.values()
        #getting client version
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        #authenticate to db
        uid = common.authenticate(db, username, password, {})
        # get models
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        #get all models ids
        models_ids = models.execute_kw(db,uid,password,'res.partner','search'
                                       ,[[['is_company','=',True]]])
        #test = models.execute_kw(db,uid,password,'res.partner', 'search_read',
        #                        [[['name','ilike',id]]],
        #                       {'fields':['name','company_id']})
        #return json.dumps(test)