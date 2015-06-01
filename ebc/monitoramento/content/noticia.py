# -*- coding: utf-8 -*-
"""Definition of the Noticia content type
"""

from zope.interface import implements
from DateTime.DateTime import *

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.monitoramento import monitoramentoMessageFactory as _
from ebc.monitoramento.interfaces import INoticia
from ebc.monitoramento.config import PROJECTNAME

NoticiaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'link',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Link"),
            size=80,            
        ),
    ),

    atapi.StringField(
        'veiculo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Veículo"),
            size=80,
        ),
    ),

    atapi.TextField(
        'sutia',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Sutiã"),
            rows=3,            
        ),
        allowable_content_types="('text/html','text/plain')",
        default_output_type="text/html",        
        searchable=1,
    ),

    atapi.DateTimeField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data e Hora"),
            format='%d/%m/%Y %H:%M',
            starting_year='2015',
            minute_step=1,            
        ),
        required='true',
        default_method = 'getDefaultTime',
        validators=('isValidDate'),
    ),

    atapi.TextField(
        'reporter',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Repórter"),
            rows=3,            
        ),
        allowable_content_types=('text/plain',),
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.TextField(
        'noticia',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Notícia"),
            rows=15,
        ),
        allowable_content_types=('text/plain',),
        default_output_type="text/html",
        searchable=1,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

NoticiaSchema['title'].storage = atapi.AnnotationStorage()
NoticiaSchema['description'].storage = atapi.AnnotationStorage()
NoticiaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
NoticiaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(NoticiaSchema, moveDiscussion=False)


class Noticia(base.ATCTContent):
    """Description of the Example Type"""
    implements(INoticia)

    meta_type = "Noticia"
    schema = NoticiaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    link = atapi.ATFieldProperty('link')
    veiculo = atapi.ATFieldProperty('veiculo')
    sutia = atapi.ATFieldProperty('sutia')
    data = atapi.ATFieldProperty('data')
    reporter = atapi.ATFieldProperty('reporter')
    noticia = atapi.ATFieldProperty('noticia')

    def getDefaultTime(self):
        return DateTime()

    def getDataStr(self):
        return self.getData().strftime("%d/%m/%y")

    def getHoraStr(self):
        return self.getData().strftime("%H:%M")

atapi.registerType(Noticia, PROJECTNAME)
