from prompt_toolkit.lexers import Lexer
from prompt_toolkit.shortcuts import prompt


class mastermindLexer(Lexer):

    def lex_document(self, document):
        # Map first letters to hex color codes.
        mastermindCol = {
            "r": "#ff0000",  # red
            "o": "#ff7f00",  # orange
            "y": "#ffff00",  # yellow
            "g": "#00ff00",  # green
            "b": "#0000ff",  # blue
        }

        def getLetter(lineno):
            fragments = []
            for c in document.lines[lineno]:
                colour = mastermindCol.get(c.lower())
                if colour:
                    style_spec = f"fg:{colour}"
                else:
                    style_spec = ""
                fragments.append((style_spec, c))

            return fragments

        return getLetter


def main():
    answer = prompt("Give me some input: ", lexer=mastermindLexer())
    print(f"You said: {answer}")


if __name__ == "__main__":
    main()