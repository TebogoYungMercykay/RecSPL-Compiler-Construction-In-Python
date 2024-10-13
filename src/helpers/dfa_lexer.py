# DFA Lexer for the RecSPL Language
import xml.etree.ElementTree as ET

class Lexer:
    def __init__(self, states, initial_state, accepting_states, transitions):
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def process_symbol(self, symbol):
        print("Processing symbol: ", symbol, ", State: ", self.current_state)
        if symbol in self.transitions.get(self.current_state, {}):
            self.current_state = self.transitions[self.current_state][symbol]
        else:
            self.current_state = None

    def is_accepting(self):
        return self.current_state in self.accepting_states

    def process_string(self, input_string):
        self.reset()
        for symbol in input_string:
            self.process_symbol(symbol)
            if self.current_state is None:
                return False
        return self.is_accepting()

# Define the Lexer structure
states = {f's{i}' for i in range(140)}

initial_state = 's0'

accepting_states = {
    's7', 's30', 's34', 's74', 's135', 's1', 's56', 's25', 's76', 's77', 's11', 's55', 's69', 's10', 's73', 's33',
    's139', 's6', 's81', 's5', 's46', 's23', 's4', 's85', 's29', 's82', 's3', 's32', 's65', 's45', 's70', 's111',
    's12', 's8', 's121', 's24', 's0', 's31', 's35', 's36', 's101', 's98', 's78', 's138', 's94', 's64', 's86',
    's125', 's75', 's27', 's51', 's95', 's14', 's2', 's48', 's122', 's110', 's22', 's15', 's21', 's19', 's66',
    's123', 's124', 's134', 's113', 's41', 's9', 's20', 's13'
}

transitions = {
    's0': {'skip': 's1', 'halt': 's2', 'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12', '{': 's13', '}': 's14', 'main': 's15', 'begin': 's16', 'if': 's17', 'print': 's18', 'num': 's19', 'text': 's20', 'void': 's21', 'token_t': 's22', 'token_n': 's23', 'token_f': 's24', 'token_v': 's25', 'VTYP': 's26', 'VNAME': 's27', 'COMMAND': 's28', 'ATOMIC': 's29', 'CONST': 's30', 'ASSIGN': 's31', 'CALL': 's32', 'BRANCH': 's33', 'OP': 's34', 'SIMPLE': 's35', 'COMPOSIT': 's36', 'UNOP': 's37', 'BINOP': 's38', 'FNAME': 's39', 'FUNCTIONS': 's40', 'DECL': 's41', 'HEADER': 's42', 'FTYP': 's43', 'PROLOG': 's44' },
    's15': {'num': 's45', 'text': 's20', 'GLOBVARS': 's46', 'VTYP': 's47'},
    's16': {'skip': 's1', 'halt': 's2', 'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8',
            'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12', 'end': 's48', 'if': 's17', 'print': 's18',
            'token_f': 's24', 'token_v': 's25', 'VNAME': 's49', 'INSTRUC': 's50', 'COMMAND': 's28', 'ASSIGN': 's31',
            'CALL': 's51', 'BRANCH': 's33', 'SIMPLE': 's35', 'COMPOSIT': 's36', 'UNOP': 's52', 'BINOP': 's53', 'FNAME': 's39'},
    's17': {'COND': 's54'},
    's18': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's56', 'CONST': 's30'},
    's26': {'token_v': 's25', 'VNAME': 's57'},
    's27': {'=': 's58', '<': 's59'},
    's28': {';': 's60'},
    's37': {'(': 's61'},
    's38': {'(': 's62'},
    's39': {'(': 's63'},
    's41': {'num': 's64', 'void': 's21', 'FUNCTIONS': 's65', 'DECL': 's41', 'HEADER': 's42', 'FTYP': 's43'},
    's42': {'{': 's13', 'BODY': 's66', 'PROLOG': 's44'},
    's43': {'token_f': 's24', 'FNAME': 's67'},
    's44': {'num': 's45', 'text': 's20', 'VTYP': 's68', 'LOCVARS': 's69'},
    's46': {'begin': 's16', 'ALGO': 's70'},
    's47': {'token_v': 's25', 'VNAME': 's71'},
    's49': {'=': 's58', '<': 's59'},
    's50': {'end': 's48'},
    's52': {'(': 's61'},
    's53': {'(': 's72'},
    's54': {'then': 's73'},
    's57': {',': 's74'},
    's58': {'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10',
            'mul': 's11', 'div': 's12', 'token_t': 's22', 'token_n': 's23', 'token_f': 's24', 'token_v': 's25',
            'VNAME': 's55', 'ATOMIC': 's75', 'CONST': 's30', 'CALL': 's76', 'TERM': 's77', 'OP': 's78', 'UNOP': 's79',
            'BINOP': 's80', 'FNAME': 's39'},
    's59': {'input': 's81'},
    's60': {'skip': 's1', 'halt': 's2', 'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8',
            'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12', 'end': 's48', 'if': 's17', 'print': 's18',
            'token_f': 's24', 'token_v': 's25', 'VNAME': 's49', 'INSTRUC': 's82', 'COMMAND': 's28', 'ASSIGN': 's31',
            'CALL': 's51', 'BRANCH': 's33', 'SIMPLE': 's35', 'COMPOSIT': 's36', 'UNOP': 's52', 'BINOP': 's53', 'FNAME': 's39'},
    's61': {'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12',
            'SIMPLE': 's83', 'BINOP': 's84'},
    's62': {'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10',
            'mul': 's11', 'div': 's12', 'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55',
            'ATOMIC': 's85', 'CONST': 's30', 'OP': 's86', 'ARG': 's87', 'SIMPLE': 's88', 'UNOP': 's79', 'BINOP': 's89'},
    's63': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's90', 'CONST': 's30'},
    's67': {'(': 's91'},
    's68': {'token_v': 's25', 'VNAME': 's92'},
    's69': {'begin': 's16', 'ALGO': 's93'},
    's70': {'num': 's64', 'void': 's21', 'FUNCTIONS': 's94', 'DECL': 's41', 'HEADER': 's42', 'FTYP': 's43'},
    's71': {',': 's95'},
    's72': {'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12',
            'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's96', 'CONST': 's30',
            'SIMPLE': 's88', 'BINOP': 's84'},
    's73': {'begin': 's16', 'ALGO': 's97'},
    's74': {'num': 's45', 'text': 's20', 'GLOBVARS': 's98', 'VTYP': 's99'},
    's80': {'(': 's100'},
    's83': {')': 's101'},
    's84': {'(': 's102'},
    's85': {',': 's103'},
    's87': {',': 's104'},
    's88': {',': 's105'},
    's89': {'(': 's106'},
    's90': {',': 's107'},
    's91': {'token_v': 's25', 'VNAME': 's108'},
    's92': {',': 's109'},
    's93': {'}': 's14', 'EPILOG': 's110'},
    's95': {'num': 's45', 'text': 's20', 'GLOBVARS': 's98', 'VTYP': 's47'},
    's96': {',': 's103'},
    's97': {'else': 's111'},
    's99': {'token_v': 's25', 'VNAME': 's112'},
    's100': {'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10',
             'mul': 's11', 'div': 's12', 'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55',
             'ATOMIC': 's113', 'CONST': 's30', 'OP': 's86', 'ARG': 's87', 'UNOP': 's79', 'BINOP': 's80'},
    's102': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's96', 'CONST': 's30'},
    's103': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's114', 'CONST': 's30'},
    's104': {'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10',
             'mul': 's11', 'div': 's12', 'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55',
             'ATOMIC': 's113', 'CONST': 's30', 'OP': 's86', 'ARG': 's115', 'UNOP': 's79', 'BINOP': 's80'},
    's105': {'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10', 'mul': 's11', 'div': 's12',
             'SIMPLE': 's116', 'BINOP': 's84'},
    's106': {'not': 's3', 'sqrt': 's4', 'or': 's5', 'and': 's6', 'eq': 's7', 'grt': 's8', 'add': 's9', 'sub': 's10',
             'mul': 's11', 'div': 's12', 'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55',
             'ATOMIC': 's85', 'CONST': 's30', 'OP': 's86', 'ARG': 's87', 'UNOP': 's79', 'BINOP': 's80'},
    's107': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's117', 'CONST': 's30'},
    's108': {',': 's118'},
    's109': {'num': 's45', 'text': 's20', 'VTYP': 's119'},
    's110': {'num': 's64', 'void': 's21', 'FUNCTIONS': 's40', 'DECL': 's41', 'HEADER': 's42', 'FTYP': 's43',
             'SUBFUNCS': 's120'},
    's111': {'begin': 's16', 'ALGO': 's121'},
    's112': {',': 's122'},
    's114': {')': 's123'},
    's115': {')': 's124'},
    's116': {')': 's125'},
    's117': {',': 's126'},
    's118': {'token_v': 's25', 'VNAME': 's127'},
    's119': {'token_v': 's25', 'VNAME': 's128'},
    's120': {'end': 's129'},
    's122': {'num': 's45', 'text': 's20', 'GLOBVARS': 's98', 'VTYP': 's130'},
    's126': {'token_t': 's22', 'token_n': 's23', 'token_v': 's25', 'VNAME': 's55', 'ATOMIC': 's131', 'CONST': 's30'},
    's127': {',': 's132'},
    's128': {',': 's133'},
    's130': {'token_v': 's25', 'VNAME': 's134'},
    's131': {')': 's135'},
    's132': {'token_v': 's25', 'VNAME': 's136'},
    's133': {'num': 's45', 'text': 's20', 'VTYP': 's137'},
    's134': {',': 's95'},
    's136': {')': 's138'},
    's137': {'token_v': 's25', 'VNAME': 's139'}
}

follow = {
  "PROG": ["$"],
  "GLOBVARS": ["begin"],
  "VTYP": ["V"],
  "VNAME": [",", ";", "<", "=", ")", "then", "else"],
  "ALGO": ["end", "else", "$"],
  "INSTRUC": ["end"],
  "COMMAND": [";"],
  "ATOMIC": [",", ")", ";", "then", "else"],
  "CONST": [",", ")", ";", "then", "else"],
  "ASSIGN": [";"],
  "CALL": [",", ")", ";", "then", "else"],
  "BRANCH": [";"],
  "TERM": [",", ")", ";", "then", "else"],
  "OP": [",", ")", ";", "then", "else"],
  "ARG": [",", ")"],
  "COND": ["then"],
  "SIMPLE": [",", ")", "then"],
  "COMPOSIT": ["then"],
  "UNOP": ["("],
  "BINOP": ["("],
  "FNAME": ["("],
  "FUNCTIONS": ["$"],
  "DECL": ["num", "void", "$"],
  "HEADER": ["{"],
  "FTYP": ["F"],
  "BODY": ["end"],
  "PROLOG": ["num", "text"],
  "EPILOG": ["num", "void", "end"],
  "LOCVARS": ["begin"],
  "SUBFUNCS": ["end"]
}

first = {
  "PROG": ["main"],
  "GLOBVARS": ["num", "text", "ε"],
  "VTYP": ["num", "text"],
  "VNAME": ["V"],
  "ALGO": ["begin"],
  "INSTRUC": ["skip", "halt", "print", "V", "if", "F", "ε"],
  "COMMAND": ["skip", "halt", "print", "V", "if", "F"],
  "ATOMIC": ["V", "N", "T"],
  "CONST": ["N", "T"],
  "ASSIGN": ["V"],
  "CALL": ["F"],
  "BRANCH": ["if"],
  "TERM": ["V", "N", "T", "F", "not", "sqrt", "or", "and", "eq", "grt", "add", "sub", "mul", "div"],
  "OP": ["not", "sqrt", "or", "and", "eq", "grt", "add", "sub", "mul", "div"],
  "ARG": ["V", "N", "T", "not", "sqrt", "or", "and", "eq", "grt", "add", "sub", "mul", "div"],
  "COND": ["or", "and", "eq", "grt", "add", "sub", "mul", "div", "not"],
  "SIMPLE": ["or", "and", "eq", "grt", "add", "sub", "mul", "div"],
  "COMPOSIT": ["or", "and", "eq", "grt", "add", "sub", "mul", "div", "not"],
  "UNOP": ["not", "sqrt"],
  "BINOP": ["or", "and", "eq", "grt", "add", "sub", "mul", "div"],
  "FNAME": ["F"],
  "FUNCTIONS": ["num", "void", "ε"],
  "DECL": ["num", "void"],
  "HEADER": ["num", "void"],
  "FTYP": ["num", "void"],
  "BODY": ["{"],
  "PROLOG": ["{"],
  "EPILOG": ["}"],
  "LOCVARS": ["num", "text"],
  "SUBFUNCS": ["num", "void", "ε"]
}
