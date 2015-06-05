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
        widget=atapi.RichWidget(
            label=_(u"Sumário"),
            rows=10,            
        ),
        allowable_content_types="('text/html',)",
        default_output_type="text/html",        
        searchable=1,
    ),

    atapi.ReferenceField(
        'destaques',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Destaques"),
            base_query={'portal_type':'Noticia','review_state':'Liberado','path':'{ "query": "monitoramento/noticias" }'}
        ),
        relationship='boletim_destaques',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),

    atapi.ReferenceField(
        'politica',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Política"),
            startup_directory="/monitoramento/noticias/politica",
            allow_search=False,
            show_results_without_query=1,
        ),
        relationship='boletim_politica',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'economia',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Economia"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/economia"
        ),
        relationship='boletim_economia',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'brasil',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Brasil"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/brasil"
        ),
        relationship='boletim_brasil',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'mundo',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Mundo"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/mundo"
        ),
        relationship='boletim_mundo',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'saude',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Saúde"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/saude"
        ),
        relationship='boletim_saude',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'educacao',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Educação"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/educacao"
        ),
        relationship='boletim_educacao',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),
    
    atapi.ReferenceField(
        'seguranca',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Segurança"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/seguranca"
        ),
        relationship='boletim_seguranca',
        allowed_types=('Noticia',), # specify portal type names here ('Example Type',)
        multiValued=True,
    ),    

    atapi.ReferenceField(
        'outras',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Outras"),
            allow_search=False,
            startup_directory="/monitoramento/noticias/outro"
        ),
        relationship='boletim_outras',
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
    destaques = atapi.ATReferenceFieldProperty('destaques')
    politica = atapi.ATReferenceFieldProperty('politica')
    economia = atapi.ATReferenceFieldProperty('economia')
    brasil = atapi.ATReferenceFieldProperty('brasil')
    mundo = atapi.ATReferenceFieldProperty('mundo')
    saude = atapi.ATReferenceFieldProperty('saude')
    educacao = atapi.ATReferenceFieldProperty('educacao')
    seguranca = atapi.ATReferenceFieldProperty('seguranca')
    outras = atapi.ATReferenceFieldProperty('outras')

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
        
    def getDestaques(self):
        cat = getToolByName(self, 'portal_catalog')
        destaques = cat.searchResults(Type='Noticia',path={ 'query': 'monitoramento/noticias' }, review_state='Liberado')
        return destaques

atapi.registerType(Boletim, PROJECTNAME)
