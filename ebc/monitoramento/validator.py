# -*- coding: utf-8 -*-
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements


from zope.site.hooks import getSite
from Products.CMFCore.utils import getToolByName 

class UnicoValidator:
    implements(IValidator)

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        link = value
        catalog = getToolByName(getSite(), 'portal_catalog')
        links = catalog.uniqueValuesFor("getLink")

        print links
        if link in links:
            return("Link já cadastrado!")
        else:
            print "testou"
            return True