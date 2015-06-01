from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.monitoramento import monitoramentoMessageFactory as _



class IBoletim(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    noticias = schema.Object(
        title=_(u"Noticias"),
        description=_(u"Field description"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
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
