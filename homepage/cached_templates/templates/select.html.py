# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429585531.773871
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\final\\homepage\\templates/select.html'
_template_uri = 'select.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <button id="random">Random Color</button>\r\n    <div class="content">\r\n        <form method="POST">\r\n            <div class="page-header">\r\n            <h1> Color Entry Form <small></small></h1>\r\n             \r\n            </div >\r\n        \r\n                <div id="colorForm" class="form-group">\r\n\r\n                    ')
        __M_writer(str(form))
        __M_writer('\r\n                </div>\r\n\r\n            <button type="submit" class="btn btn-default">Submit</button>\r\n        </form>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Steven\\final\\homepage\\templates/select.html", "line_map": {"35": 1, "53": 3, "54": 14, "55": 14, "40": 21, "27": 0, "61": 55, "46": 3}, "uri": "select.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
