import Scanner as sc


token_color = {
    'ADD': 'color: Crimson',
    'SUBTRACT': 'color: Crimson',
    'MULTIPLY': 'color: Crimson',
    'DIVIDE': 'color: Crimson',
    'LEFT_PAR': 'color: Crimson',
    'RIGHT_PAR': 'color: Crimson',
    'COLON': 'color: Crimson',
    'SEMICOLON': 'color: Crimson',
    'ASSIGN': 'color: Crimson',
    'EQUALS': 'color: Crimson',
    'GRATER': 'color: Crimson',
    'GRATE_EQUAL': 'color: Crimson',
    'SMALLER': 'color: Crimson',
    'SMALL_EQUAL': 'color: Crimson',
    'NOT_EQ': 'color: Crimson',
    'COMA': 'color: Crimson',
    'INCREMENT': 'color: Crimson',
    'NUMBER': 'color: MediumSeaGreen',
    'IDENTIFIER': 'color: DodgerBlue',
    'KEYWORD': 'color: SlateBlue',
    'STRING': 'color: Orange'
}

text_to_color = open("text.txt", "r").read()
testScanner = sc.Scanner(text_to_color)
tokens_to_color = testScanner.run()


f = open("result.html", "w")
f.write("<html>\n<body>")
f.close()

f = open("result.html", "a")
for token in tokens_to_color:
    f.write(f"<p style = \"{token_color[token.type]}\">{token.value}</p>\n")
f.write("</body>\n</html>")
f.close()
