# Follow and First Sets for Grammar Productions

## PROG

- First(PROG) = {main}
- Follow(PROG) = {$} (where $ represents the end of input)

## GLOBVARS

- First(GLOBVARS) = {num, text, ε}
- Follow(GLOBVARS) = {begin}

## VTYP

- First(VTYP) = {num, text}
- Follow(VTYP) = {V}

## VNAME

- First(VNAME) = {V}
- Follow(VNAME) = {,, ;, <, =, ), then, else}

## ALGO

- First(ALGO) = {begin}
- Follow(ALGO) = {end, else, $}

## INSTRUC

- First(INSTRUC) = {skip, halt, print, V, if, F, ε}
- Follow(INSTRUC) = {end}

## COMMAND

- First(COMMAND) = {skip, halt, print, V, if, F}
- Follow(COMMAND) = {;}

## ATOMIC

- First(ATOMIC) = {V, N, T}
- Follow(ATOMIC) = {,, ), ;, then, else}

## CONST

- First(CONST) = {N, T}
- Follow(CONST) = {,, ), ;, then, else}

## ASSIGN

- First(ASSIGN) = {V}
- Follow(ASSIGN) = {;}

## CALL

- First(CALL) = {F}
- Follow(CALL) = {,, ), ;, then, else}

## BRANCH

- First(BRANCH) = {if}
- Follow(BRANCH) = {;}

## TERM

- First(TERM) = {V, N, T, F, not, sqrt, or, and, eq, grt, add, sub, mul, div}
- Follow(TERM) = {,, ), ;, then, else}

## OP

- First(OP) = {not, sqrt, or, and, eq, grt, add, sub, mul, div}
- Follow(OP) = {,, ), ;, then, else}

## ARG

- First(ARG) = {V, N, T, not, sqrt, or, and, eq, grt, add, sub, mul, div}
- Follow(ARG) = {,, )}

## COND

- First(COND) = {or, and, eq, grt, add, sub, mul, div, not}
- Follow(COND) = {then}

## SIMPLE

- First(SIMPLE) = {or, and, eq, grt, add, sub, mul, div}
- Follow(SIMPLE) = {,, ), then}

## COMPOSIT

- First(COMPOSIT) = {or, and, eq, grt, add, sub, mul, div, not}
- Follow(COMPOSIT) = {then}

## UNOP

- First(UNOP) = {not, sqrt}
- Follow(UNOP) = {(}

## BINOP

- First(BINOP) = {or, and, eq, grt, add, sub, mul, div}
- Follow(BINOP) = {(}

## FNAME

- First(FNAME) = {F}
- Follow(FNAME) = {(}

## FUNCTIONS

- First(FUNCTIONS) = {num, void, ε}
- Follow(FUNCTIONS) = {$}

## DECL

- First(DECL) = {num, void}
- Follow(DECL) = {num, void, $}

## HEADER

- First(HEADER) = {num, void}
- Follow(HEADER) = {{}

## FTYP

- First(FTYP) = {num, void}
- Follow(FTYP) = {F}

## BODY

- First(BODY) = {{}
- Follow(BODY) = {end}

## PROLOG

- First(PROLOG) = {{}
- Follow(PROLOG) = {num, text}

## EPILOG

- First(EPILOG) = {}}
- Follow(EPILOG) = {num, void, end}

## LOCVARS

- First(LOCVARS) = {num, text}
- Follow(LOCVARS) = {begin}

## SUBFUNCS

- First(SUBFUNCS) = {num, void, ε}
- Follow(SUBFUNCS) = {end}

## `A Few Notes On The Notation`

- ε represents the empty string
- $ represents the end of input
- V, N, T, and F represent variable names, numbers, text constants, and function names respectively
