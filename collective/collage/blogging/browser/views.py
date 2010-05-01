# -*- coding: utf-8 -*-
from Products.Collage.browser.views import BaseView
from collective.blogging.browser.blogview import BlogView

class BloggingView(BlogView, BaseView):
    """ Collage view implementing collective.blogging's BlogView
    """
