# -*- coding: utf-8 -*-
"""Definition of the Assunto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

from archetypes.referencebrowserwidget import ReferenceBrowserWidget



# -*- Message Factory Imported Here -*-
from ebc.monitoramento import monitoramentoMessageFactory as _

from ebc.monitoramento.interfaces import IAssunto
from ebc.monitoramento.config import PROJECTNAME

AssuntoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


    atapi.ReferenceField(
        'notic',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Notícias"),
            startup_directory="/monitoramento/noticias",
            allow_search=False,
            allow_sorting=1,            
        ),
        relationship='boletim_noticias',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),

    atapi.ReferenceField(
        'links',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Links"),
            startup_directory="/monitoramento/noticias",
            allow_search=False,
            allow_sorting=1,
        ),
        relationship='boletim_links',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),




))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

AssuntoSchema['title'].storage = atapi.AnnotationStorage()
AssuntoSchema['description'].storage = atapi.AnnotationStorage()

AssuntoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
AssuntoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
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
    """ """
    implements(IAssunto)

    meta_type = "Assunto"
    schema = AssuntoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    notic = atapi.ATReferenceFieldProperty('notic')
    links = atapi.ATReferenceFieldProperty('links')


    # -*- Your ATSchema to Python Property Bridges Here ... -*-


atapi.registerType(Assunto, PROJECTNAME)
