import token_table as tt


class Token:
    def __init__(self, type, start_pos, value=None, end_pos=None):
        self.type = type
        self.start_pos = start_pos
        self.value = value
        self.end_pos = end_pos

    def __str__(self):
        return f'{self.type} {self.value} position: {self.start_pos}'


def is_keyword(txt):
    for keyword in tt.keyword_table:
        if txt == keyword:
            return True
    return False


def is_operator(txt):
    for operator in tt.operators_table.keys():
        if operator.startswith(txt):
            return True
    return False


class Scanner:
    def __init__(self, text):
        self.text = text
        self.current_index = 0

    def get_next(self):
        character = self.text[self.current_index] if self.current_index < len(self.text) else ''
        self.current_index += 1
        return character

    def check_next(self):
        return self.text[self.current_index] if self.current_index < len(self.text) else ''

    def get_index(self):
        return self.current_index

    def scan(self):
        while self.check_next().isspace():
            self.get_next()

        start_pos = self.get_index()
        character = self.get_next()

        if character == '':
            return Token('END_OF_FILE', start_pos, '', start_pos)

        if character.isalpha() or character == '_':
            token_val = character
            while self.check_next().isalpha() or self.check_next().isdigit() or self.check_next() == '_':
                token_val += self.get_next()
            if is_keyword(token_val):
                return Token('KEYWORD', start_pos, token_val, self.get_index())
            else:
                return Token('IDENTIFIER', start_pos, token_val, self.get_index())
        elif character.isdigit():
            token_val = character
            while self.check_next().isdigit():
                token_val += self.get_next()
            return Token('NUMBER', start_pos, token_val, self.get_index())
        elif character == '"':
            token_val = ''
            while self.check_next() != '"':
                next_character = self.get_next()
                if next_character == '':
                    raise Exception(f'Unfinished string starting at {start_pos}')
                token_val += next_character
            self.get_next()
            return Token('STRING', start_pos, token_val, self.get_index())
        elif character == "'":
            token_val = ''
            while self.check_next() != "'":
                next_character = self.get_next()
                if next_character == '':
                    txt = f"Unfinished string starting at {start_pos}"
                    raise Exception(txt)
                token_val += next_character
            self.get_next()
            return Token('STRING', start_pos, token_val, self.get_index())

        if not is_operator(character):
            raise Exception(f"Unknown character at {start_pos} - `{character}`")

        recognized_operator = character if character in tt.operators_table else None
        last_valid_position = self.get_index()
        last_character = character
        while True:
            next_character = self.check_next()
            if next_character == '':
                break
            last_character += next_character
            if not is_operator(last_character):
                break
            self.get_next()
            if last_character in tt.operators_table:
                recognized_operator = last_character
                last_valid_position = self.get_index()

        if recognized_operator is not None:
            return Token(tt.operators_table[recognized_operator], start_pos, recognized_operator, last_valid_position)

        raise Exception(f"Unknown character at {start_pos} - `{character}`")

    def run(self):
        token_list = []
        while self.current_index <= len(self.text):
            token = self.scan()
            token_list.append(token)
        token_list.pop()
        return token_list

