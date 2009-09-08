# -*- coding: utf-8 -*-
"""Pages page_tags template tags"""
from django.conf import settings
from django import template
register = template.Library()

def pages_menu(context, page, url='/'):
    """Render a nested list of all the descendents of the given page,
    including this page.

    :param page: the page where to start the menu from.
    :param url: not used anymore.
    """
    path = context.get('path', None)
    site_id = None
    children = page.get_children_for_frontend()
    MEDIA_URL = settings.MEDIA_URL
    if 'current_page' in context:
        current_page = context['current_page']
    return locals()
pages_menu = register.inclusion_tag('pages/menu.html',
                                    takes_context=True)(pages_menu)

def pages_sub_menu(context, page, url='/'):
    """Get the root page of the given page and
    render a nested list of all root's children pages.
    Good for rendering a secondary menu.

    :param page: the page where to start the menu from.
    :param url: not used anymore.
    """
    path = context.get('path', None)
    root = page.get_root()
    children = root.get_children_for_frontend()
    if 'page' in context:
        current_page = context['current_page']
    return locals()
pages_sub_menu = register.inclusion_tag('pages/sub_menu.html',
                                        takes_context=True)(pages_sub_menu)
                                        
def pages_dynamic_tree_menu(context, page):
    """
    Render a "dynamic" tree menu, with all nodes expanded which are either
    ancestors or the current page itself.

    Override ``pages/dynamic_tree_menu.html`` if you want to change the
    design.

    :param page: the current page
    :param url: not used anymore
    """
    request = context['request']
    site_id = None
    children = None
    if 'current_page' in context:
        current_page = context['current_page']
        # if this node is expanded, we also have to render its children
        # a node is expanded if it is the current node or one of its ancestors
        if page.lft <= current_page.lft and page.rght >= current_page.rght:
            children = page.get_children_for_frontend()
    return locals()
pages_dynamic_tree_menu = register.inclusion_tag(
    'pages/dynamic_tree_menu.html',
    takes_context=True
)(pages_dynamic_tree_menu)

def pages_breadcrumb(context, page):
    """
    Render a breadcrumb like menu.

    Override ``pages/breadcrumb.html`` if you want to change the
    design.
    
    :param page: the current page
    """
    site_id = None
    pages = page.get_ancestors()
    return locals()
pages_breadcrumb = register.inclusion_tag(
    'pages/breadcrumb.html',
    takes_context=True
)(pages_breadcrumb)