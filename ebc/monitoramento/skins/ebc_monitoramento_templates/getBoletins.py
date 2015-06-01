## Script (Python) "getBoletins"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=
##
data = DateTime(data,datefmt='international')

fim = DateTime(data.strftime("%d/%m/%Y 23:59:59"),datefmt='international')

noticias = context.portal_catalog.searchResults(meta_type='Boletim', sort_on="getData", sort_order="reverse", path={'query': '/monitoramento/boletins/'}, getData={"query": [data,fim], "range": "min:max"})

return noticias
