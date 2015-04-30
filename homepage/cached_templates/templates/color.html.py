# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429588377.775862
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\final\\homepage\\templates/color.html'
_template_uri = 'color.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        colors = context.get('colors', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        colors = context.get('colors', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <a class="btn btn-primary" href="/homepage/select/">Back</a>\r\n    <div class="row">\r\n')
        for color in colors:
            __M_writer('            <div class="shade">\r\n                <div style="background-color: ')
            __M_writer(str( color ))
            __M_writer('; height: 200px; width: 200px">\r\n                     <h3>')
            __M_writer(str( color ))
            __M_writer('</h3>\r\n                </div>\r\n            </div>\r\n')
        __M_writer('    </div>\r\n        \r\n    </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "color.html", "line_map": {"66": 60, "35": 1, "40": 18, "46": 3, "59": 9, "53": 3, "54": 6, "55": 7, "56": 8, "57": 8, "58": 9, "27": 0, "60": 13}, "filename": "C:\\Users\\Steven\\final\\homepage\\templates/color.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
