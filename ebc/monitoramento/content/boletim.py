# -*- coding: utf-8 -*-
"""Definition of the Boletim content type
"""

from zope.interface import implements
from DateTime.DateTime import *

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

from archetypes.referencebrowserwidget import ReferenceBrowserWidget

# -*- Message Factory Imported Here -*-
from ebc.monitoramento import monitoramentoMessageFactory as _
from ebc.monitoramento.interfaces import IBoletim
from ebc.monitoramento.config import PROJECTNAME

BoletimSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'tipo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Tipo"),
        ),
        vocabulary=NamedVocabulary("""boletim"""),
        required=True,
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
        required=True,
        default_method = 'getDefaultTime',        
        validators=('isValidDate'),
    ),

    atapi.TextField(
        'sumario',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Sumário"),
        ),
        searchable=1,        
    ),

    atapi.ReferenceField(
        'noticias',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Notícias"),
            startup_directory="/monitoramento/noticias"
        ),
        required=True,
        relationship='boletim_noticias',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BoletimSchema['title'].storage = atapi.AnnotationStorage()
BoletimSchema['description'].storage = atapi.AnnotationStorage()
BoletimSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(BoletimSchema, moveDiscussion=False)


class Boletim(base.ATCTContent):
    """ """
    implements(IBoletim)

    meta_type = "Boletim"
    schema = BoletimSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    tipo = atapi.ATFieldProperty('tipo')
    data = atapi.ATFieldProperty('data')
    sumario = atapi.ATFieldProperty('sumario')
    noticias = atapi.ATReferenceFieldProperty('noticias')

    def getDefaultTime(self):
        return DateTime()

    def getDataStr(self):
        return self.getData().strftime("%d/%m/%y")

    def getHoraStr(self):
        return self.getData().strftime("%H:%M")

    def getTipoStr(self):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName('boletim')
        dict = vocab.getVocabularyDict(self)
        tipo = self.getTipo()
        t = ""
        if tipo:
            t = dict[tipo[0]]
        return t


atapi.registerType(Boletim, PROJECTNAME)
