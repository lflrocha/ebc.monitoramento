from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.monitoramento import monitoramentoMessageFactory as _



class IBoletim(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    sumario = schema.Text(
        title=_(u"Sumario"),
        required=False,
        description=_(u"Field description"),
    )
#
    data = schema.Date(
        title=_(u"Data e Hora"),
        required=True,
        description=_(u"Field description"),
    )
#
    tipo = schema.List(
        title=_(u"Tipo"),
        required=True,
        description=_(u"Field description"),
    )
#
    destaques = schema.Object(
        title=_(u"Destaques"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    politica = schema.Object(
        title=_(u"Politica"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    economia = schema.Object(
        title=_(u"Economia"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    brasil = schema.Object(
        title=_(u"Brasil"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    mundo = schema.Object(
        title=_(u"Mundo"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    saude = schema.Object(
        title=_(u"Saude"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    educacao = schema.Object(
        title=_(u"Educacao"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    seguranca = schema.Object(
        title=_(u"Seguranca"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    outras = schema.Object(
        title=_(u"Outras"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
