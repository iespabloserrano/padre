# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Person(models.Model):
    _name = 'padre.person'
    _description = 'Person'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')