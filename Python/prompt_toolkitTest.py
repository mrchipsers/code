from prompt_toolkit import formatted_text
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import style_from_pygments_cls, merge_styles
from prompt_toolkit.lexers import PygmentsLexer
from pygments.styles.tango import TangoStyle
from pygments.lexers.html import HtmlLexer

tango_style = style_from_pygments_cls(TangoStyle)

text = prompt(
    "Enter HTML: ",
    lexer=PygmentsLexer(HtmlLexer),
    style=tango_style
)

#style = Style.from_dict({
    # User input (default text)
    #'r': '#ff0000',
    #'g': '#00ff00',
    #'b': '#0000ff',
    #'y': '#ffff00',
    #'o': '#ffa500',
    
    # Prompt
    #'username': '#884444',
    #'at': '#00aa00',
    #'colon': '#0000aa',
    #'pound': '#00aa00',
    #'host': '#00ffff bg:#444400',
    #'path': 'ansicyan underline',
#})
#message = formatted_text.FormattedText([
    #('class:username', 'john'),
    #('class:at', '@'),
    #('class:host', 'localhost'),
    #('class:colon', ':'),
    #('class:path', '/user/john'),
    #('class:pound', '# '),
#])

#text = prompt(style=style)