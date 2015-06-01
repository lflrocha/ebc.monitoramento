## Script (Python) "getAguardandoCadastramento"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
noticias = context.portal_catalog.searchResults(meta_type='Noticia', review_state='aguardando_cadastramento', sort_on="getData", path={'query': '/monitoramento/noticias/'} )

return noticias
