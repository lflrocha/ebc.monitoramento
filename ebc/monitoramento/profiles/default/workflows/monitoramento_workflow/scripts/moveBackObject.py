## Script (Python) "moveBackObject"
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

# get the src folder and the destination folder
dstFldr = context.noticias
srcFldr = obj.aq_parent

if dstFldr <> srcFldr:

  # perform the move
  objs = srcFldr.manage_cutObjects([id,])
  dstFldr.manage_pasteObjects(objs)

  # get the new object
  new_obj = dstFldr[id]

  # pass new_obj to the error, *twice*
  raise state_change.ObjectMoved(new_obj, new_obj)
