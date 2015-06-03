from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.monitoramento import monitoramentoMessageFactory as _



class INoticia(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    link = schema.TextLine(
        title=_(u"Link"),
        required=False,
    )
#
    editoria = schema.List(
        title=_(u"Editoria"),
        required=True,
        description=_(u"Field description"),
    )
#
    noticia = schema.Text(
        title=_(u"Noticia"),
        required=False,
    )
#
    reporter = schema.Text(
        title=_(u"Reporter"),
        required=False,
    )
#
    data = schema.Date(
        title=_(u"Data e Hora"),
        required=False,
    )
#
    sutia = schema.Text(
        title=_(u"Sutia"),
        required=False,
    )
#
    veiculo = schema.List(
        title=_(u"Veiculo"),
        required=True,
    )
#
