# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429576663.191205
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\final\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>Steven\'s Final</title>\n')
        __M_writer('    <script src="/static/homepage/media/jquery-1.11.2.min.js"></script>\n    <script src="/static/homepage/media/bootstrap.min.js"></script>\n    <link rel="stylesheet" type="text/css" href="/static/homepage/media/bootstrap.min.css" />\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n    <header>\n      <h1>Steven\'s Final</h1>\n      <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Obama.jpg">\n    </header>\n    \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Steven\\final\\homepage\\templates/base.htm", "source_encoding": "ascii", "uri": "base.htm", "line_map": {"48": 32, "34": 5, "35": 13, "36": 18, "37": 18, "38": 18, "39": 24, "40": 24, "60": 27, "45": 29, "46": 32, "47": 32, "16": 4, "18": 0, "66": 60, "54": 27, "28": 2, "29": 4, "30": 5}}
__M_END_METADATA
"""
