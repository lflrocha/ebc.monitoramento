from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.monitoramento import monitoramentoMessageFactory as _



class IAssunto(Interface):
    """ """

    # -*- schema definition goes here -*-
    links = schema.Object(
        title=_(u"Links"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#

    notic = schema.Object(
        title=_(u"Noticias"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
