# -*- coding: utf-8 -*-
"""Definition of the Assunto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata


from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.LinesColumn import LinesColumn


# -*- Message Factory Imported Here -*-
from ebc.monitoramento import monitoramentoMessageFactory as _

from ebc.monitoramento.interfaces import IAssunto
from ebc.monitoramento.config import PROJECTNAME

AssuntoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


    DataGridField('Noticias',
        searchable = True,
        columns=("Noticia",),
        widget = DataGridWidget(
            columns={
                'Noticia' : LinesColumn("Selecione as notícias"),
            },
        ),
    ),    
    
    DataGridField('Links',
        searchable = True,
        columns=("Link",),
        widget = DataGridWidget(
            columns={
                'Link' : LinesColumn("Selecione os links"),
            },
        ),        
    ),    


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

AssuntoSchema['title'].storage = atapi.AnnotationStorage()
AssuntoSchema['description'].storage = atapi.AnnotationStorage()

AssuntoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(AssuntoSchema, moveDiscussion=False)


class Assunto(base.ATCTContent):
    """Description of the Example Type"""
    implements(IAssunto)

    meta_type = "Assunto"
    schema = AssuntoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-


atapi.registerType(Assunto, PROJECTNAME)
