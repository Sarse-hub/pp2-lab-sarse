import re
import sys


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class Lexer:
    TOKEN_SPEC = [
        ('NUMBER',   r'\d+(?:\.\d+)?'),
        ('IDENT',    r'[A-Za-z_]\w*'),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('MUL',      r'\*'),
        ('DIV',      r'/'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('ASSIGN',   r'='),
        ('SKIP',     r'[ \t]+'),
        ('NEWLINE',  r'\\n'),
        ('MISMATCH', r'.'),
    ]

    def __init__(self, text):
        self.text = text
        self.tokens = []
        self._tokenize()
        self.pos = 0

    def _tokenize(self):
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.TOKEN_SPEC)
        get_token = re.compile(tok_regex).match
        line = self.text
        pos = 0
        mo = get_token(line, pos)
        while mo:
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                self.tokens.append(Token('NUMBER', value))
            elif kind == 'IDENT':
                self.tokens.append(Token('IDENT', value))
            elif kind in ('PLUS','MINUS','MUL','DIV','LPAREN','RPAREN','ASSIGN'):
                self.tokens.append(Token(kind, value))
            elif kind in ('SKIP','NEWLINE'):
                pass
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {value}')
            pos = mo.end()
            mo = get_token(line, pos)
        self.tokens.append(Token('EOF', None))

    def peek(self):
        return self.tokens[self.pos]

    def next(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = lexer.next()

    def eat(self, type_):
        if self.current.type == type_:
            self.current = self.lexer.next()
        else:
            raise SyntaxError(f'Expected {type_}, got {self.current.type}')

    def parse(self):
        # assignment or expression
        if self.current.type == 'IDENT':
            # lookahead
            tok = self.lexer.tokens[self.lexer.pos]
            if tok.type == 'ASSIGN':
                name = self.current.value
                self.eat('IDENT')
                self.eat('ASSIGN')
                expr = self.expr()
                return ('assign', name, expr)
        return self.expr()

    def expr(self):
        node = self.term()
        while self.current.type in ('PLUS','MINUS'):
            op = self.current.type
            self.eat(op)
            right = self.term()
            node = ('binop', op, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.current.type in ('MUL','DIV'):
            op = self.current.type
            self.eat(op)
            right = self.factor()
            node = ('binop', op, node, right)
        return node

    def factor(self):
        tok = self.current
        if tok.type == 'NUMBER':
            self.eat('NUMBER')
            return ('num', tok.value)
        if tok.type == 'IDENT':
            self.eat('IDENT')
            return ('var', tok.value)
        if tok.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        if tok.type == 'MINUS':
            self.eat('MINUS')
            node = self.factor()
            return ('unary', 'MINUS', node)
        raise SyntaxError(f'Unexpected token: {tok}')


class Interpreter:
    def __init__(self):
        self.env = {}

    def eval(self, node):
        t = node[0]
        if t == 'num':
            return node[1]
        if t == 'var':
            name = node[1]
            if name in self.env:
                return self.env[name]
            raise NameError(f"Undefined variable '{name}'")
        if t == 'assign':
            _, name, expr = node
            val = self.eval(expr)
            self.env[name] = val
            return val
        if t == 'binop':
            _, op, left, right = node
            l = self.eval(left)
            r = self.eval(right)
            if op == 'PLUS':
                return l + r
            if op == 'MINUS':
                return l - r
            if op == 'MUL':
                return l * r
            if op == 'DIV':
                return l / r
        if t == 'unary':
            _, kind, expr = node
            v = self.eval(expr)
            if kind == 'MINUS':
                return -v
        raise RuntimeError(f'Unknown node {node}')


def run_line(line, interp):
    # strip comments
    if '#' in line:
        line = line.split('#', 1)[0]
    line = line.strip()
    if not line:
        return None
    if line in ('exit','quit'):
        raise EOFError()
    # support `print expr` or plain expression/assignment
    if line.startswith('print'):
        rest = line[5:].strip()
        if rest.startswith('(') and rest.endswith(')'):
            rest = rest[1:-1].strip()
        lexer = Lexer(rest)
        parser = Parser(lexer)
        node = parser.parse()
        val = interp.eval(node)
        print(val)
        return val

    lexer = Lexer(line)
    parser = Parser(lexer)
    node = parser.parse()
    val = interp.eval(node)
    # echo expressions (including variable name alone)
    if node[0] != 'assign':
        print(val)
    return val


def repl():
    interp = Interpreter()
    try:
        while True:
            try:
                line = input('>>> ')
            except EOFError:
                break
            try:
                run_line(line, interp)
            except EOFError:
                break
            except Exception as e:
                print('Error:', e)
    except KeyboardInterrupt:
        print('\nExiting')


def run_file(path):
    interp = Interpreter()
    with open(path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip():
                continue
            try:
                run_line(line, interp)
            except Exception as e:
                print('Error while processing', line, ':', e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()
