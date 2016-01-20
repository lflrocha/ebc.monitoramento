from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.monitoramento import monitoramentoMessageFactory as _



class IBoletim(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    sumario = schema.SourceText(
        title=_(u"Sumario"),
        required=False,
        description=_(u"Field description"),
    )
#
    data = schema.Date(
        title=_(u"Data"),
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
