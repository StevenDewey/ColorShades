# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429232434.978475
_enable_loop = True
_template_filename = '/Users/conan/Documents/data/teaching/2015/IS Core Winter - 413/final/homepage/templates/index.html'
_template_uri = 'index.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <h2 class="text-success">Description:</h2>\n  <p>\n    One of the color theories in web page design is to use <i>monotone chromatic</i> colors. A monotone color scheme is one hue with different\n    saturations and shades. In other words, a blue monotone color scheme contains various shades of the same blue, from light blue to dark blue.\n    Web sites that solely use the same monotone color scheme can be dull, but used correctly, monotone works really well.\n    The web page designers that work in your company have asked you to create a monotone color scheme calculator. Given a source color, they want\n    to see one shade lighter and one shade darker. HTML colors are given in the form #RRGGBB, where RR is the red part in hexadecimal (00-FF), GG\n    is the green part, and BB is the blue part.\n  </p>\n  <p>\n    Your final project is to create a small web site that calculates darker and lighter versions of colors for developers.\n    I\'ve already started a project for you (this project), and it should run correctly right now.  It already includes \n    JQuery and Bootstrap.  If it doesn\'t run correctly, stop here and make it work.  This won\'t count against your time.\n  </p>\n  <p>\n    Some of the requirements you\'ll see below could be done with Javascript or with CSS.  However, you need to do exactly what you are asked to do below.  This isn\'t the time to deviate from the instructions, and it isn\'t the time to impress me with extra features.  Just go through the instructions and follow them.\n  </p>\n  <p>\n    When you are finished, fill out the spreadsheet (just like all the other rubrics we\'ve done).  The rubric file is in the root directory of this project and is called "FinalExam.xlsx".  I\'ll go through this rubric as I grade your project.  Fill out the values to the best of your knowledge so I know what to expect.\n  </p>\n  \n  <h2 class="text-success">The Rules:</h2>\n  <ol>\n    <li>You have exactly 4 hours to finish this final.  The time starts when you read the "Tasks" section below.  You may remember 3 hours from class, but I\'ve decided to allow 4 hours. Don\'t feel obligated to take the entire time.</li>\n    <li>The 4 hours must be done in a single time block.  No starting, stopping, and restarting. No wishing for more wishes.</li>\n    <li>The exam is closed neighbor.  You cannot get help from anyone on it.</li>\n    <li>The exam is open book and open internet and open project.  Feel free to use your resources to solve the tasks.  Just don\'t get help from other human beings.</li>\n    <li>The exam is due the last day of finals at midnight.  Be sure it is posed to Learning Suite by then.</li>\n    <li>The rubric spreadsheet is required.  Don\'t forget to fill it out.  It sets our expectations during grading.</li>\n  </ol>  \n  \n  <p>&nbsp;</p>\n  <p>&nbsp;</p>\n  <h2 align="center">If you read further, your 4 hours starts!</h2>\n  <p>&nbsp;</p>\n  <p>&nbsp;</p>\n\n  <h2 class="text-success">The Tasks (start your time now):</h2>\n  <ol>\n    <li>Make the following modifications to the base template:</li>\n    <ul>\n      <li>Add a title (both the <tt>title</tt> tag and an <tt>h1</tt> tag) that prints on all pages of the site.</li>\n      <li>Add an image of your choosing underneath the <tt>h1</tt> tag.  Place this image in the homepage/media/ folder.</li>\n    </ul>\n    <br/>\n    \n    <li>Create base.css in your styles/ folder:</li>\n    <ul>\n      <li>Style your image to be 200 x 200 pixels.</li>\n      <li>Center both the page title (h1 tag) and the image horizontally.</li>\n    </ul>\n    <br/>\n    \n    <li>Create select.py in your views/ folder:</li>\n    <ul>\n      <li>Add a view_function called process_request.  This function should create and clean the color form.  If the form is valid, redirect the user to a the /homepage/color/RRGGBB/ url, where RRGGBB is the hex code the user entered.</li>\n      <li>Add a form class with one text input field.  The user will enter the color here.  Place one clean method in the form class that ensures the user entered a valid color in hex format (RRGGBB).</li>\n    </ul>\n    <br/>\n    \n    <li>Create select.html in your templates/ folder:</li>\n    <ul>\n      <li>Place the form on the page (the variable comes from select.py).</li>\n      <li>Add the form tags and submit button.</li>\n    </ul>\n    <br/>\n    \n    <li>Create color.py in your views/ folder, and add the following:</li>\n    <ul>\n      <li>Add one or more functions to scale colors to darker/lighter shades.  I suggest you use the code\n          found at <a href="http://thadeusb.com/weblog/2010/10/10/python_scale_hex_color">http://thadeusb.com/weblog/2010/10/10/python_scale_hex_color</a>.</li>\n      <li>Add a view_function called process_request:</li>\n        <ul>\n          <li>Get the color code from the urlparams.  You can assume that the code is valid (it was cleaned on the select page).</li>\n          <li>Create a list of 5 items with two lighter shades of the color, the exact color, and two darker shades of the color.  The \n              colors in the list should get progressively lighter (start with dark and go lighter).</li>\n          <li>For example, the color #df3c3c might go to [ #852424, #b23030, #df3c3c, #ff4848, #ff5454 ].  This example used scale\n              values of .6, .8, 1, 1.2, and 1.4.</li>\n          <li>Send this list variable to the color.html template.</li>\n        </ul>\n    </ul>\n    <br/>\n\n    <li>Create color.html in your templates/ folder:</li>\n    <ul>\n      <li>Using a <tt>for</tt> loop, go through the five colors in the list (that you created in color.py) and print\n          five boxes on the screen.  Set the background color of each box to each color, and print the color\n          hex code inside each box.</li>\n      <li>You are welcome to use any HTML tags for your boxes, from table cells to divs.</li>\n      <li>Set the color and box width/height in the <tt>style</tt> property of each box tag.  Each box should be about 200 x 200 pixels.</li>\n      <li>Provide a bootstrap-styled "back" button that takes the user back to the /homepage/select/ page.</li>\n    </ul>\n    <br/>\n    \n    <li>For the final 10% of the final, add an ajax call to select a random color code for the user.  If you don\'t get to this part, you\'ll still get 90% of the points.</li>\n    <ul>\n      <li>Add a bootstrap-styled button to the select.html template.</li>\n      <li>When this button is pressed, trigger an Ajax call to /homepage/select.random_color/</li>\n      <li>The random_color() view function in select.py should create a random hex color and return it to the select page.\n          Use Python\'s <tt>random</tt> library (it\'s built into python, so just "import random") to generate a hex code\n          between 000000 and ffffff.\n      </li>\n      <li>When the random_color() method returns successfully, place the random code in the form\'s input box.</li>\n    </ul>\n    <br/>\n    \n   </ol>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/conan/Documents/data/teaching/2015/IS Core Winter - 413/final/homepage/templates/index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "index.html"}
__M_END_METADATA
"""
