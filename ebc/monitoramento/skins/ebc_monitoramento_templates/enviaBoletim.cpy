## Script (Python) "enviaEmail"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##

REQUEST=context.REQUEST

boletim_id = REQUEST.get('id', '')
boletim = context.boletins[boletim_id]

tipo = boletim.getTipo()[0]
data = boletim.getDataStr()
hora = boletim.getHoraStr()
titulo = boletim.Title()
sumario = boletim.getSumario()
noticias = boletim.getNoticias()


message =  """<html><body style="font-family: 'Times New Roman', Georgia, Serif;"><div style="text-align:center" >"""
message = message + """<img src='http://192.168.21.5:8080/monitoramento/"""+tipo+""".png' />  """
message = message + """</div>  """
message = message + """<br /> """
message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;text-align:center; font-family:'Times New Roman', Georgia, Serif;font-size: 24px;"> """
message = message + str(data) + ' - ' + str(hora) + ' - ' + titulo
message = message + """</div><br />"""
message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 24px;">"""
message = message + sumario
message = message + """</div> """

message = message + """<div> """
for noticia in noticias:
    veiculo = noticia.getVeiculoStr()
    manchete = noticia.Title()
    sutia = noticia.getSutia()
    editoria = noticia.getEditoriaStr()
    if editoria == "Outro":
        editoria = ''
    else:
        editoria = editoria + " <br />"
    data = noticia.getDataStr()
    hora = noticia.getHoraStr()
    reporter = noticia.getReporter()
    texto = noticia.getNoticia()
    link = noticia.getLink()
    
    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 18px; font-weight: bold;">"""  + veiculo +  """</div>"""
    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 34px; font-weight: bold;">"""  + manchete +  """</div>"""
    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 20px; font-style: italic;">"""  + sutia +  """</div>"""
    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 20px; text-transform: uppercase;">"""  + editoria
    message = message + data + ' - ' + hora 
    message = message + reporter +  """</div>"""
    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 20px;">"""  + texto +  """</div>"""
    message = message + """<a href='""" + link + """' style="font-family: 'Times New Roman', Georgia, Serif;font-size: 20px; font-style: italic;" target="_blank">"""  + link +  """</a><br /><br /><br />"""

message = message + """</div> """
message = message + """</body></html>"""

print message

return printed
