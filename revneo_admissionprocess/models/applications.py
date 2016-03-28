# -*- coding: utf-8 -*-
from openerp import models,fields,api
from openeducat_core.models import course
from mx.DateTime.DateTime import today
from openerp.exceptions import except_orm, Warning, RedirectWarning

class ApApplicationsModel(models.Model):
    _name = 'ap.applications.model'    
    
    @api.multi
    @api.depends('ap_person_model.ap_persontype')
    def person_default_func(self):
        for rec in self:
            if rec.ap_person_id.ap_persontype == 'student':
                raise Warning('student record parsed')
                
            
                
    ap_number = fields.Integer("Application Number")
    ap_date = fields.Date("Application Date",default=today, required=True) 
    ap_tc = fields.Boolean("Transfer Certificate", default=False)
    ap_batch = fields.Selection ( 
        [('start2017', '2017 to 2018'),('start2018', '2018 to 2019')],
        'Batch',   default='start2017', required=True)
     

    ap_course_id = fields.Many2one('op.course','Course Applied', required=True)
    ap_prevschool_id = fields.One2many('ap.prevschool.model','ap_prevschoolid','Prev School Studied',required=True)
    ap_person_id = fields.One2many('ap.person.model','ap_personid','Applicant Person Details',required=True)
        
    #@api.onchange('ap_father_id')
    #def on_change_ap_father(self):
        #self.ap_father_id.__setattr__('ap_persontype', 'father')*/
            
class ApPrevSchoolModel(models.Model):  
    
    _name = 'ap.prevschool.model'
    ap_prevschoolid = fields.Integer("School Id") 
    ap_recognized = fields.Boolean("School Recognized", default=False)
    ap_name = fields.Char("School Name", size=256)
    ap_registrationnumber = fields.Char("Registration Number", size=256)
    ap_affiliation = fields.Selection(
        [('matric','Matriculation'),('cbse','Central Board'),('sbse','State Board'),
         ('anglo','Anglo Indian Board'),('other','Other Board')],'Affiliation',
         default='matric')    
    ap_mediumofinstruction = fields.Selection(
        [('eng','English'),('tamil','Tamil')],'Instruction Language',
        default='eng')
    ap_schooltype = fields.Selection(
        [('aided','Government Funded'),('self','Self Funded'),('govt','Government Operated'),('kv','Kendriya Vidyalaya')],
        'School Type', default='aided') 
    ap_tccopy = fields.Binary("Transfer Certificate Scanned Copy")
    ap_tccomments = fields.Text("Transfer Certificate Comments")
    ap_emisid = fields.Char("Emis Number", required=True)
    
class ApPersonModel(models.Model):  
    
    _name = 'ap.person.model' 
    _inherit = 'op.student'   
    
    ap_personid = fields.Integer("Person Id")
    ap_income = fields.Float("Income")  
    ap_religion = fields.Selection(
        [('islam','ISLAM'),('hindu','Hindu'),('christ','Christian'),('other','Other')],'Religion',
        default='islam') 
    ap_community = fields.Selection(
        [('BC','Backward Class'),('OBC','Other Backward Class'),('scst','Scheduled Class/Tribe')],'Community',
        default='BC')         
    ap_qualification = fields.Selection(
        [('ug','Under Graduate'),('g','Graduate'),('pg','Post Graduate')],'Qualification',
        default='g') 
    ap_identity = fields.Selection(
        [('ac','Aadhar Card'),('pc','PAN Card'),('rc','Ration Card')],'Identity',
        default='ac')
    ap_identityavbl = fields.Boolean("Identity Card Available", default=False)
    ap_identitycopy = fields.Binary("Identity Card Scanned Copy")
    ap_identitynumber = fields.Char("Identity Number", required=True)
    
    ap_addressproof = fields.Selection(
        [('tb','Telephone Bill'),('eb','Electricity Bill'),('bs','Bank Statement')],'Address',
        default='tb')
    ap_addressproofavbl = fields.Boolean("Identity Card Available", default=False)
    
    ap_persontype = fields.Selection(
        [('student','Student'),('parent','Parent'),('grd','Guardian')],'Person Type',
        default='student', track_visibility='onchange')
    course_id = fields.Many2one(required=False)
    batch_id = fields.Many2one(required=False)
    partner_id = fields.Many2one(required=False)
