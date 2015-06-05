## Script (Python) "moveObject"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=state_change
##title=
##
# get the object and its ID

obj = state_change.object
id = obj.getId()
editoria = obj.getEditoria()
if len(editoria) > 0:
  editoria = editoria[0]

# get the src folder and the destination folder
dstFldr = context.noticias[editoria]
srcFldr = obj.aq_parent

# perform the move
objs = srcFldr.manage_cutObjects([id,])
dstFldr.manage_pasteObjects(objs)

# get the new object
new_obj = dstFldr[id]

# pass new_obj to the error, *twice*
raise state_change.ObjectMoved(new_obj, new_obj)
