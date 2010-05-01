from zope.interface import implements
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Collage.interfaces import ICollageAlias
from collective.blogging.interfaces import IBlogMarker
from collective.collage.blogging.interfaces import ICollageBloggingUtil

class CollageBloggingUtil(BrowserView):
  """
  a public traversable utility that checks if a blog is enabled
  """
  implements(ICollageBloggingUtil)

  def should_include(self):
    utils = getToolByName(self.context, 'plone_utils')
    for row in self.context.folderlistingFolderContents():
      for column in row.folderlistingFolderContents():
        for item in column.folderlistingFolderContents():
          if ICollageAlias.providedBy(item):
            item=item.get_target()
          if IBlogMarker.providedBy(item):
#            return True
            return False
    return False

