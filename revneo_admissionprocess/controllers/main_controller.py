from openerp import http
from openerp.http import request

class ApplicationController():

    @http.route(['/application/application/post'], type='http', auth='public', website=True)
    def submit_html(self, res_model='ap.application', res_id=None, message='', **kw):
 
        return message_data