from zope.interface import Interface

class ICollageBloggingLayer(Interface):
    """
    marker interface for collage blogging layer
    """

class ICollageBloggingUtil(Interface):

    def should_include():
        """
        if the blogging resource files should be included
        """

