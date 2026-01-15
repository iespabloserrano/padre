# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Person(models.Model):
    _name = 'padre.person'
    _description = 'Person'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')


class Herbivore(models.Model):
    _name = 'padre.herbivore'
    _description = 'Herbivore'


    favorite_plant = fields.Char(string='Favorite Plant')

    def get_favorite_plant(self):
        return self.favorite_plant
    
class Carnivore(models.Model):
    _name = 'padre.carnivore'
    _description = 'Carnivore'


    favorite_meat = fields.Char(string='Favorite Meat')

    def get_favorite_meat(self):
        return self.favorite_meat