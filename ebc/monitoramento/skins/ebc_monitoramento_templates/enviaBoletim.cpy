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


from Products.CMFCore.utils import getToolByName
REQUEST=context.REQUEST


form= REQUEST.form
mailTo=form.get('email')

boletim_id = REQUEST.get('id', '')
boletim = context.boletins[boletim_id]

tipo = boletim.getTipo()[0]
data = boletim.getDataStr()
hora = boletim.getHoraStr()
titulo = boletim.Title()
sumario = boletim.getSumario()
assuntos = boletim.getAssuntos()    


message =  """<html><body style="font-family: 'Times New Roman', Georgia, Serif;"><div style="text-align:center" >"""
message = message + """<img src='http://10.61.7.227:8080/monitoramento/"""+tipo+""".png' />  """
message = message + """</div>  """
message = message + """<br /> """
message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;text-align:center; font-family:'Times New Roman', Georgia, Serif;font-size: 24px;"> """
message = message + titulo
message = message + """</div><br />"""
message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 24px;">"""
message = message + sumario
message = message + """</div> """

message = message + """<div> """


for assunto in assuntos:
    
    noticias = assunto.getNotic
    links = assunto.getLinks

    message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 30px; font-weight: bold; text-decoration: underline">"""  + assunto.Title +  """</div><br>"""

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
        message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 26px; font-weight: bold;">"""  + manchete +  """</div>"""
        message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 20px; font-style: italic;">"""  + sutia +  """</div>"""
        message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 18px; text-transform: uppercase;">"""  + editoria
        message = message + data + ' - ' + hora +  """</div>"""
        message = message + """<div style="font-family: 'Times New Roman', Georgia, Serif;font-size: 18px;">"""  + texto +  """</div>"""
        message = message + """<a href='""" + link + """' style="font-family: 'Times New Roman', Georgia, Serif;font-size: 18px; font-style: italic;" target="_blank">"""  + link +  """</a><br /><br /><br />"""
        


message = message + """</div> """
message = message + """</body></html>"""

mh = getToolByName(context, 'MailHost')

try: 
    mh.send(str(message), mto=mailTo, mfrom='luis.rocha@ebc.com.br', subject=titulo, immediate=True, charset='utf8', msg_type='text/html')
except: 
    raise AttributeError, "cant find a Mail Host object"



#return printed
