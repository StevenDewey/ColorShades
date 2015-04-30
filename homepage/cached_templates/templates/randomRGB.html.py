# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429582209.445909
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\final\\homepage\\templates/randomRGB.html'
_template_uri = 'randomRGB.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        color = context.get('color', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(color))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "randomRGB.html", "line_map": {"16": 0, "28": 22, "22": 1}, "source_encoding": "ascii", "filename": "C:\\Users\\Steven\\final\\homepage\\templates/randomRGB.html"}
__M_END_METADATA
"""
