# The DFA Construction for RecSPL

## Code/ Grammar

```go
// <!-- PROG      ::= main GLOBVARS ALGO FUNCTIONS -->
q0 --> q1: main;

q1 --> q2: GLOBVARS;
// Linking
q1 --> q5: ε;
q1 --> q7: ε;

q2 --> q3: ALGO;
// Linking
q2 --> q18: ε;

q3 --> q4: FUNCTIONS;
// Linking
q3 --> q141: ε;
q3 --> q143: ε;

// <!-- GLOBVARS  ::= ε -->
q5 --> q6: ε;

// <!-- GLOBVARS  ::= VTYP VNAME, GLOBVARS -->
q7 --> q8: VTYP;
// Linking
q7 --> q12: ε;
q7 --> q14: ε;

q8 --> q9: VNAME;
// Linking
q8 --> q16: ε;

q9 --> q10: ,;
q10 --> q11: GLOBVARS;
// Linking
q10 --> q5: ε;
q10 --> q7: ε;

// <!-- VTYP      ::= num -->
q12 --> q13: num;

// <!-- VTYP      ::= text -->
q14 --> q15: text;

// <!-- VNAME     ::= TokenClassOfV -->
q16 --> q17: TokenClassOfV;

// <!-- ALGO      ::= begin INSTRUC end -->
q18 --> q19: begin;
q19 --> q20: INSTRUC;
// Linking
q19 --> q20: ε;
q19 --> q24: ε;

q20 --> q21: end;

// <!-- INSTRUC   ::= ε -->
q22 --> q23: ε;

// <!-- INSTRUC   ::= COMMAND ; INSTRUC -->
q24 --> q25: COMMAND;
// Linking
q24 --> q28: ε;
q24 --> q30: ε;
q24 --> q32: ε;
q24 --> q35: ε;
q24 --> q37: ε;
q24 --> q39: ε;

q25 --> q26: ';';

q26 --> q27: INSTRUC;
// Linking
q26 --> q20: ε;
q26 --> q24: ε;

// <!-- COMMAND   ::= skip -->
q28 --> q29: skip;

// <!-- COMMAND   ::= halt -->
q30 --> q31: halt;

// <!-- COMMAND   ::= print ATOMIC -->
q32 --> q33: print;
q33 --> q34: ATOMIC;
// Linking
q33 --> q41: ε;
q33 --> q43: ε;

// <!-- COMMAND   ::= ASSIGN -->
q35 --> q36: ASSIGN;
// Linking
q35 --> q49: ε;
q35 --> q53: ε;

// <!-- COMMAND   ::= CALL -->
q37 --> q38: CALL;
// Linking
q37 --> q57: ε;

// <!-- COMMAND   ::= BRANCH -->
q39 --> q40: BRANCH;
// Linking
q39 --> q66: ε;

// <!-- ATOMIC    ::= VNAME -->
q41 --> q42: VNAME;
// Linking
q41 --> q16: ε;

// <!-- ATOMIC    ::= CONST -->
q43 --> q44: CONST;
// Linking
q43 --> q45: ε;
q43 --> q47: ε;

// <!-- CONST     ::= TokenClassOfN -->
q45 --> q46: TokenClassOfN;

// <!-- CONST     ::= TokenClassOfT -->
q47 --> q48: TokenClassOfT;

// <!-- ASSIGN    ::= VNAME < input -->
q49 --> q50: VNAME;
// Linking
q49 --> q16: ε;

q50 --> q51: <;
q51 --> q52: input;

// <!-- ASSIGN    ::= VNAME = TERM -->
q53 --> q54: VNAME;
// Linking
q53 --> q16: ε;

q54 --> q55: =;
q55 --> q56: TERM;
// Linking
q55 --> q73: ε;
q55 --> q75: ε;
q55 --> q77: ε;

// <!-- CALL      ::= FNAME( ATOMIC , ATOMIC , ATOMIC) -->
q57 --> q58: FNAME;
// Linking
q57 --> q139: ε;

q58 --> q59: (;

q59 --> q60: ATOMIC;
// Linking
q59 --> q41: ε;
q59 --> q43: ε;

q60 --> q61: ,;

q61 --> q62: ATOMIC;
// Linking
q61 --> q41: ε;
q61 --> q43: ε;

q62 --> q63: ,;

q63 --> q64: ATOMIC;
// Linking
q63 --> q41: ε;
q63 --> q43: ε;

q64 --> q65: );

// <!-- BRANCH    ::= if COND then ALGO else ALGO -->
q66 --> q67: if;

q67 --> q68: COND;
// Linking
q67 --> q96: ε;
q67 --> q98: ε;

q68 --> q69: then;

q69 --> q70: ALGO;
// Linking
q69 --> q18: ε;

q70 --> q71: else;

q71 --> q72: ALGO;
// Linking
q71 --> q18: ε;

// <!-- TERM      ::= ATOMIC -->
q73 --> q74: ATOMIC;
// Linking
q73 --> q41: ε;
q73 --> q43: ε;

// <!-- TERM      ::= CALL -->
q75 --> q76: CALL;
// Linking
q75 --> q57: ε;

// <!-- TERM      ::= OP -->
q77 --> q78: OP;
// Linking
q77 --> q79: ε;
q77 --> q85: ε;

// <!-- OP        ::= UNOP( ARG ) -->
q79 --> q80: UNOP;
// Linking
q79 --> q119: ε;
q79 --> q121: ε;

q81 --> q82: (;
q82 --> q83: ARG;
// Linking
q82 --> q92: ε;
q82 --> q94: ε;

q83 --> q84: );

// <!-- OP        ::= BINOP( ARG , ARG) -->
q85 --> q86: BINOP;
// Linking
q85 --> q123: ε;
q85 --> q125: ε;
q85 --> q127: ε;
q85 --> q129: ε;
q85 --> q131: ε;
q85 --> q133: ε;
q85 --> q135: ε;
q85 --> q137: ε;

q86 --> q87: (;

q87 --> q88: ARG;
// Linking
q87 --> q92: ε;
q87 --> q94: ε;

q88 --> q89: ,;

q89 --> q90: ARG;
// Linking
q89 --> q92: ε;
q89 --> q94: ε;

q90 --> q91: );

// <!-- ARG       ::= ATOMIC -->
q92 --> q93: ATOMIC;
// Linking
q92 --> q41: ε;
q92 --> q43: ε;

// <!-- ARG       ::= OP -->
q94 --> q95: OP;
// Linking
q94 --> q79: ε;
q94 --> q85: ε;

// <!-- COND      ::= SIMPLE -->
q96 --> q97: SIMPLE;
// Linking
q96 --> q100: ε;

// <!-- COND      ::= COMPOSIT -->
q98 --> q99: COMPOSIT;
// Linking
q98 --> q107: ε;
q98 --> q114: ε;

// <!-- SIMPLE    ::= BINOP( ATOMIC , ATOMIC ) -->
q100 --> q101: BINOP;
// Linking
q100 --> q123: ε;
q100 --> q125: ε;
q100 --> q127: ε;
q100 --> q129: ε;
q100 --> q131: ε;
q100 --> q133: ε;
q100 --> q135: ε;
q100 --> q137: ε;

q101 --> q102: (;

q102 --> q103: ATOMIC;
// Linking
q102 --> q41: ε;
q102 --> q43: ε;

q103 --> q104: ,;

q104 --> q105: ATOMIC;
// Linking
q104 --> q41: ε;
q104 --> q43: ε;

q105 --> q106: );

// <!-- COMPOSIT  ::= BINOP( SIMPLE , SIMPLE ) -->
q107 --> q108: BINOP;
// Linking
q107 --> q123: ε;
q107 --> q125: ε;
q107 --> q127: ε;
q107 --> q129: ε;
q107 --> q131: ε;
q107 --> q133: ε;
q107 --> q135: ε;
q107 --> q137: ε;

q108 --> q109: (;

q109 --> q110: SIMPLE;
// Linking
q109 --> q100: ε;

q110 --> q111: ,;

q111 --> q112: SIMPLE;
// Linking
q111 --> q100: ε;

q112 --> q113: );

// <!-- COMPOSIT  ::= UNOP ( SIMPLE ) -->
q114 --> q115: UNOP;
// Linking
q114 --> q119: ε;
q114 --> q121: ε;

q115 --> q116: (;

q116 --> q117: SIMPLE;
// Linking
q116 --> q100: ε;

q117 --> q118: );

// <!-- UNOP      ::= not -->
q119 --> q120: not;

// <!-- UNOP      ::= sqrt -->
q121 --> q122: sqrt;

// <!-- BINOP     ::= or -->
q123 --> q124: or;

// <!-- BINOP     ::= and -->
q125 --> q126: and;

// <!-- BINOP     ::= eq -->
q127 --> q128: eq;

// <!-- BINOP     ::= grt -->
q129 --> q130: grt;

// <!-- BINOP     ::= add -->
q131 --> q132: add;

// <!-- BINOP     ::= sub -->
q133 --> q134: sub;

// <!-- BINOP     ::= mul -->
q135 --> q136: mul;

// <!-- BINOP     ::= div -->
q137 --> q138: div;

// <!-- FNAME     ::= TokenClassOfF -->
q139 --> q140: TokenClassOfF;

// <!-- FUNCTIONS ::= ε -->
q141 --> q142: ε;

// <!-- FUNCTIONS ::= DECL FUNCTIONS -->
q143 --> q144: DECL;
// Linking
q143 --> q146: ε;

q144 --> q145: FUNCTIONS;
// Linking
q144 --> q141: ε;
q144 --> q143: ε;

// <!-- DECL      ::= HEADER BODY -->
q146 --> q147: HEADER;
// Linking
q146 --> q149: ε;

q147 --> q148: BODY;
// Linking
q147 --> q163: ε;

// <!-- HEADER    ::= FTYP FNAME( VNAME , VNAME , VNAME ) -->
q149 --> q150: FTYP;
// Linking
q149 --> q159: ε;
q149 --> q161: ε;

q150 --> q151: FNAME;
// Linking
q150 --> q139: ε;

q151 --> q152: (;
q152 --> q153: VNAME;
// Linking
q152 --> q16: ε;

q153 --> q154: ,;
q154 --> q155: VNAME;
// Linking
q154 --> q16: ε;

q155 --> q156: ,;
q156 --> q157: VNAME;
// Linking
q156 --> q16: ε;

q157 --> q158: );

// <!-- FTYP      ::= num -->
q159 --> q160: num;

// <!-- FTYP      ::= void -->
q161 --> q162: void;

// <!-- BODY      ::= PROLOG LOCVARS ALGO EPILOG SUBFUNCS end -->
q163 --> q164: PROLOG;
// Linking
q163 --> q169: ε;

q164 --> q165: LOCVARS;
// Linking
q164 --> q173: ε;

q165 --> q166: ALGO;
// Linking
q165 --> q18: ε;

q166 --> q167: EPILOG;
// Linking
q166 --> q171: ε;

q167 --> q168: SUBFUNCS;
// Linking
q167 --> q182: ε;

q168 --> q190: end;

// <!-- PROLOG    ::= { -->
q169 --> q170: {;

// <!-- EPILOG    ::= } -->
q171 --> q172: };

// <!-- LOCVARS   ::= VTYP VNAME , VTYP VNAME , VTYP VNAME -->
q173 --> q174: VTYP;
// Linking
q173 --> q12: ε;
q173 --> q14: ε;

q174 --> q175: VNAME;
// Linking
q174 --> q16: ε;

q175 --> q176: ,;

q176 --> q177: VTYP;
// Linking
q176 --> q12: ε;
q176 --> q14: ε;

q177 --> q178: VNAME;
// Linking
q177 --> q16: ε;

q178 --> q179: ,;

q179 --> q180: VTYP;
// Linking
q179 --> q12: ε;
q179 --> q14: ε;

q180 --> q181: VNAME;
// Linking
q180 --> q16: ε;

// <!-- SUBFUNCS  ::= FUNCTIONS -->
q182 --> q183: FUNCTIONS;
// Linking
q182 --> q141: ε;
q182 --> q143: ε;
```

## Diagramn

```mermaid
stateDiagram-v2
    [*] --> qS

    qS --> q0: ε 
    qS --> q5: ε 
    qS --> q7: ε 
    qS --> q12: ε 
    qS --> q14: ε 
    qS --> q16: ε 
    qS --> q18: ε 
    qS --> q22: ε 
    qS --> q24: ε 
    qS --> q28: ε 
    qS --> q30: ε 
    qS --> q32: ε 
    qS --> q35: ε 
    qS --> q37: ε 
    qS --> q39: ε 
    qS --> q41: ε 
    qS --> q43: ε 
    qS --> q45: ε 
    qS --> q47: ε 
    qS --> q49: ε 
    qS --> q53: ε 
    qS --> q57: ε 
    qS --> q66: ε 
    qS --> q73: ε 
    qS --> q75: ε 
    qS --> q77: ε 
    qS --> q79: ε 
    qS --> q85: ε 
    qS --> q92: ε 
    qS --> q94: ε 
    qS --> q96: ε 
    qS --> q98: ε 
    qS --> q100: ε 
    qS --> q107: ε 
    qS --> q114: ε 
    qS --> q119: ε 
    qS --> q121 ε 
    qS --> q123: ε 
    qS --> q125: ε 
    qS --> q127: ε 
    qS --> q129: ε 
    qS --> q131: ε 
    qS --> q133: ε 
    qS --> q135: ε 
    qS --> q137: ε 
    qS --> q139: ε 
    qS --> q141: ε 
    qS --> q143: ε 
    qS --> q146: ε 
    qS --> q149: ε 
    qS --> q159: ε 
    qS --> q161: ε 
    qS --> q163: ε 
    qS --> q169: ε 
    qS --> q171: ε 
    qS --> q173: ε 
    qS --> q182: ε

    q0 --> q1: main
    q1 --> q2: GLOBVARS
    q1 --> q5: ε
    q1 --> q7: ε
    q2 --> q3: ALGO
    q2 --> q18: ε
    q3 --> q4: FUNCTIONS
    q3 --> q141: ε
    q3 --> q143: ε

    q5 --> q6: ε

    q7 --> q8: VTYP
    q7 --> q12: ε
    q7 --> q14: ε
    q8 --> q9: VNAME
    q8 --> q16: ε
    q9 --> q10: ,
    q10 --> q11: GLOBVARS
    q10 --> q5: ε
    q10 --> q7: ε

    q12 --> q13: num

    q14 --> q15: text

    q16 --> q17: token_v

    q18 --> q19: begin
    q19 --> q20: INSTRUC
    q19 --> q20: ε
    q19 --> q24: ε
    q20 --> q21: end

    q22 --> q23: ε

    q24 --> q25: COMMAND
    q24 --> q28: ε
    q24 --> q30: ε
    q24 --> q32: ε
    q24 --> q35: ε
    q24 --> q37: ε
    q24 --> q39: ε
    q25 --> q26: ;
    q26 --> q27: INSTRUC
    q26 --> q20: ε
    q26 --> q24: ε

    q28 --> q29: skip

    q30 --> q31: halt

    q32 --> q33: print
    q33 --> q34: ATOMIC
    q33 --> q41: ε
    q33 --> q43: ε

    q35 --> q36: ASSIGN
    q35 --> q49: ε
    q35 --> q53: ε

    q37 --> q38: CALL
    q37 --> q57: ε

    q39 --> q40: BRANCH
    q39 --> q66: ε

    q41 --> q42: VNAME
    q41 --> q16: ε

    q43 --> q44: CONST
    q43 --> q45: ε
    q43 --> q47: ε

    q45 --> q46: token_n

    q47 --> q48: token_t

    q49 --> q50: VNAME
    q49 --> q16: ε
    q50 --> q51: <
    q51 --> q52: input

    q53 --> q54: VNAME
    q53 --> q16: ε
    q54 --> q55: =
    q55 --> q56: TERM
    q55 --> q73: ε
    q55 --> q75: ε
    q55 --> q77: ε

    q57 --> q58: FNAME
    q57 --> q139: ε
    q58 --> q59: (
    q59 --> q60: ATOMIC
    q59 --> q41: ε
    q59 --> q43: ε
    q60 --> q61: ,
    q61 --> q62: ATOMIC
    q61 --> q41: ε
    q61 --> q43: ε
    q62 --> q63: ,
    q63 --> q64: ATOMIC
    q63 --> q41: ε
    q63 --> q43: ε
    q64 --> q65: )

    q66 --> q67: if
    q67 --> q68: COND
    q67 --> q96: ε
    q67 --> q98: ε
    q68 --> q69: then
    q69 --> q70: ALGO
    q69 --> q18: ε
    q70 --> q71: else
    q71 --> q72: ALGO
    q71 --> q18: ε

    q73 --> q74: ATOMIC
    q73 --> q41: ε
    q73 --> q43: ε

    q75 --> q76: CALL
    q75 --> q57: ε

    q77 --> q78: OP
    q77 --> q79: ε
    q77 --> q85: ε

    q79 --> q80: UNOP
    q79 --> q119: ε
    q79 --> q121: ε
    q81 --> q82: (
    q82 --> q83: ARG
    q82 --> q92: ε
    q82 --> q94: ε
    q83 --> q84: )

    q85 --> q86: BINOP
    q85 --> q123: ε
    q85 --> q125: ε
    q85 --> q127: ε
    q85 --> q129: ε
    q85 --> q131: ε
    q85 --> q133: ε
    q85 --> q135: ε
    q85 --> q137: ε
    q86 --> q87: (
    q87 --> q88: ARG
    q87 --> q92: ε
    q87 --> q94: ε
    q88 --> q89: ,
    q89 --> q90: ARG
    q89 --> q92: ε
    q89 --> q94: ε
    q90 --> q91: )

    q92 --> q93: ATOMIC
    q92 --> q41: ε
    q92 --> q43: ε

    q94 --> q95: OP
    q94 --> q79: ε
    q94 --> q85: ε

    q96 --> q97: SIMPLE
    q96 --> q100: ε

    q98 --> q99: COMPOSIT
    q98 --> q107: ε
    q98 --> q114: ε

    q100 --> q101: BINOP
    q100 --> q123: ε
    q100 --> q125: ε
    q100 --> q127: ε
    q100 --> q129: ε
    q100 --> q131: ε
    q100 --> q133: ε
    q100 --> q135: ε
    q100 --> q137: ε
    q101 --> q102: (
    q102 --> q103: ATOMIC
    q102 --> q41: ε
    q102 --> q43: ε
    q103 --> q104: ,
    q104 --> q105: ATOMIC
    q104 --> q41: ε
    q104 --> q43: ε
    q105 --> q106: )

    q107 --> q108: BINOP
    q107 --> q123: ε
    q107 --> q125: ε
    q107 --> q127: ε
    q107 --> q129: ε
    q107 --> q131: ε
    q107 --> q133: ε
    q107 --> q135: ε
    q107 --> q137: ε
    q108 --> q109: (
    q109 --> q110: SIMPLE
    q109 --> q100: ε
    q110 --> q111: ,
    q111 --> q112: SIMPLE
    q111 --> q100: ε
    q112 --> q113: )

    q114 --> q115: UNOP
    q114 --> q119: ε
    q114 --> q121: ε
    q115 --> q116: (
    q116 --> q117: SIMPLE
    q116 --> q100: ε
    q117 --> q118: )

    q119 --> q120: not

    q121 --> q122: sqrt

    q123 --> q124: or

    q125 --> q126: and

    q127 --> q128: eq

    q129 --> q130: grt

    q131 --> q132: add

    q133 --> q134: sub

    q135 --> q136: mul

    q137 --> q138: div

    q139 --> q140: token_f

    q141 --> q142: ε

    q143 --> q144: DECL
    q143 --> q146: ε
    q144 --> q145: FUNCTIONS
    q144 --> q141: ε
    q144 --> q143: ε

    q146 --> q147: HEADER
    q146 --> q149: ε
    q147 --> q148: BODY
    q147 --> q163: ε

    q149 --> q150: FTYP
    q149 --> q159: ε
    q149 --> q161: ε
    q150 --> q151: FNAME
    q150 --> q139: ε
    q151 --> q152: (
    q152 --> q153: VNAME
    q152 --> q16: ε
    q153 --> q154: ,
    q154 --> q155: VNAME
    q154 --> q16: ε
    q155 --> q156: ,
    q156 --> q157: VNAME
    q156 --> q16: ε
    q157 --> q158: )

    q159 --> q160: num

    q161 --> q162: void

    q163 --> q164: PROLOG
    q163 --> q169: ε
    q164 --> q165: LOCVARS
    q164 --> q173: ε
    q165 --> q166: ALGO
    q165 --> q18: ε
    q166 --> q167: EPILOG
    q166 --> q171: ε
    q167 --> q168: SUBFUNCS
    q167 --> q182: ε
    q168 --> q184: end

    q169 --> q170: {

    q171 --> q172: }

    q173 --> q174: VTYP
    q173 --> q12: ε
    q173 --> q14: ε
    q174 --> q175: VNAME
    q174 --> q16: ε
    q175 --> q176: ,
    q176 --> q177: VTYP
    q176 --> q12: ε
    q176 --> q14: ε
    q177 --> q178: VNAME
    q177 --> q16: ε
    q178 --> q179: ,
    q179 --> q180: VTYP
    q179 --> q12: ε
    q179 --> q14: ε
    q180 --> q181: VNAME
    q180 --> q16: ε

    q182 --> q183: FUNCTIONS
    q182 --> q141: ε
    q182 --> q143: ε

    % Defining Starting State
    qS : "Starting"

    % Defining Accepting States
    q4: "Accept | PROG"
    q6: "Accept | GLOBVARS"
    q11: "Accept | GLOBVARS"
    q13: "Accept | VTYP"
    q15: "Accept | VTYP"
    q17: "Accept | T-VARIABLE"
    q21: "Accept | ALGO"
    q23: "Accept | INSTRUC"
    q27: "Accept | INSTRUC"
    q29: "Accept | COMMAND"
    q31: "Accept | COMMAND"
    q34: "Accept | COMMAND"
    q36: "Accept | COMMAND"
    q38: "Accept | COMMAND"
    q40: "Accept | COMMAND"
    q42: "Accept | ATOMIC"
    q44: "Accept | ATOMIC"
    q46: "Accept | T-NUMBER"
    q48: "Accept | T-STRING"
    q52: "Accept | ASSIGN"
    q56: "Accept | ASSIGN"
    q65: "Accept | CALL"
    q72: "Accept | BRANCH"
    q74: "Accept | TERM"
    q76: "Accept | TERM"
    q78: "Accept | TERM"
    q84: "Accept | OP"
    q91: "Accept | OP"
    q93: "Accept | ARG"
    q95: "Accept | ARG"
    q97: "Accept | COND"
    q99: "Accept | COND"
    q106: "Accept | SIMPLE"
    q113: "Accept | COMPOSIT"
    q118: "Accept | COMPOSIT"
    q120: "Accept | UNOP"
    q122: "Accept | UNOP"
    q124: "Accept | BINOP"
    q126: "Accept | BINOP"
    q128: "Accept | BINOP"
    q130: "Accept | BINOP"
    q132: "Accept | BINOP"
    q134: "Accept | BINOP"
    q136: "Accept | BINOP"
    q138: "Accept | BINOP"
    q140: "Accept | T-FNAME"
    q142: "Accept | FUNCTIONS"
    q145: "Accept | FUNCTIONS"
    q148: "Accept | DECL"
    q158: "Accept | HEADER"
    q160: "Accept | FTYP"
    q162: "Accept | FTYP"
    q184: "Accept | BODY"
    q170: "Accept | PROLOG"
    q172: "Accept | EPILOG"
    q181: "Accept | LOCVARS"
    q183: "Accept | SUBFUNCS"
```
