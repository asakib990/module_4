# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentInfo(models.Model):
    _name = 'module4.student.info'
    _description = 'sakib_module_4.sakib_module_4'
    
    s_id = fields.Char(string="Student", required=True)
    name = fields.Char(string="Name", required=True)
    score = fields.Float(string="Score", required=True)
    

class QuestionInfo(models.Model):
    _name = 'module4.question.info'
    _description = 'sakib_module_4.sakib_module_4'
    
    que_id = fields.Char(string="Student Id", required=True)
    que = fields.Text(string="Name", required=True)
    ans = fields.Text(string="Score", required=True)
    marks = fields.Float(string="Marks", required=True)