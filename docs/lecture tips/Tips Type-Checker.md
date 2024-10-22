# Semester Project ADVICE: The Type-Checker

In the **attachment** I've provided a somewhat abstract 'high-level' specification of a Type System which you shall use as the basis of the implementation of the type-checker module within your compiler for RecSPL. The document clearly shows the idea of '**attributed grammars**' whereby **semantic rules are affiliated with the syntax rules** (such as in Chapter #5 of our Textbook).

- **I hope** that my type system specification is consistent and does not contain too many 'bugs' 😅.
- **IF** you spot any 'bugs' in my specification then you've got to fix them before you can actually program your type-checker software along those lines 😅.

In the attached PDF you can see that the specification of the Type System contains **two** recursive procedures, which are both working on the Syntax-Tree which the Parser has already generated:

- **typecheck** is the main procedure and returns true/false depending on whether (or not) an analysed RecSPL program was correctly typed.
- **typeof** - also recursive - is an auxiliary procedure which 'helps' the typecheck procedure: This auxiliary procedure has access to the already existing Symbol Table, in which relevant type information gets stored, and reports type information to the typecheck procedure by way of various characters (such as 'n' for the numeric type, '**v**' for the void type, '**t**' for the text type, etc...)

## More Tips From Prof G.

**RecSPL** is **strongly** and **statically** typed. Its type checking shall be implemented as a recursive Boolean procedure that analyses a given syntax tree (from the parser) by "tree crawling", and which

- returns **true** if the syntax tree (with all its branches) was correctly typed
- returns **false** otherwise.

It is thereby assumed that a suitable symbol table is already in place, and that the correctness of the name scopes (for variable names and function names) has already been verified before the type checker gets launched.
The type checker's semantic rules are attributed to their corresponding grammar rules as follows:

### Grammar and Type-Checking Rules

**Program Structure**

```
PROG ::= main GLOBVARS ALGO FUNCTIONS
```

**Type-Checking for Programs**

```
PROG ::= main GLOBVARS ALGO FUNCTIONS
typecheck(PROG) = ( typecheck(GLOBVARS) && typecheck(ALGO) && typecheck(FUNCTIONS) )
```

**Global Variables**

```
GLOBVARS ::= epsilon
typecheck(GLOBVARS) = true // base-case of the type-checking-recursion

GLOBVARS ::= VTYP VNAME, [ GLOBVARS]
typecheck(GLOBVARS1 [, GLOBVARS2]) = (
    let T := typeof(VTYP1)
    let id := symboltable(VNAME1) // access the existing symbol table
    link(T, id) // Add to symbol table // symbol table now knows the type
    typeof(VNAME1) == typeof(VTYP1)
) && typecheck(GLOBVARS2)
```

**Variable Types**

```
VTYP ::= num | text

typeof(num) = 'n' // the auxiliary function typeof returns a character that represents the type
typeof(text) = 't' // the auxiliary function typeof returns a character that represents the type
```

**Variable Names**

```
VNAME ::= V // At this point we assume that the compiler's Scope Analyser has already entered some ID for this variable name into the above mentioned symbol table, such that symboltable(VNAME) will yield use-able information about that node of the syntax tree.
```

**Algorithm**

```
ALGO ::= begin INSTRUC end

typecheck(ALGO) = typecheck(INSTRUC)
```

**Instructions**

```
INSTRUC ::= typecheck(INSTRUC) = true // base-case of the type-checking-recursion
INSTRUC ::= COMMAND ; INSTRUC
typecheck(INSTRUC1 ; INSTRUC2) = (typecheck(COMMAND1) && typecheck(INSTRUC2))

INSTRUC ::= COMMAND
typecheck(INSTRUC) = typecheck(COMMAND)
```

**Commands**

```
COMMAND ::= skip
typecheck(skip) = true // base-case of the type-checking-recursion

COMMAND ::= halt
typecheck(halt) = true // base-case of the type-checking-recursion

COMMAND ::= print ATOMIC
typecheck(print ATOMIC) = (typeof(ATOMIC) == 'n' || typeof(ATOMIC) == 't')
                        // if typeof(ATOMIC)=='n' then typecheck(COMMAND) = true
                        // if typeof(ATOMIC)=='t'  then typecheck(COMMAND) = true
                        // else typecheck(COMMAND) = false

COMMAND ::= return ATOMIC // must stand 'inside' of a Function-Scope
typecheck(return ATOMIC) = {
    return typecheck(COMMAND) = {
        //Let a tree-crawler find the FTYP node which belongs to the same Function-Scope inside of which also this COMMAND is standing inside the function's BODY.
        // We assume that Scope Analysis was already done!
        Let X be this 'matching' function-type-node in the tree. 
        if typeof(ATOMIC) == typeof(X) == 'n' // functions can return only n
        then return true
        else return false
    }
}

COMMAND ::= ASSIGN
typecheck(ASSIGN) = typecheck(ASSIGN)

COMMAND ::= CALL
typecheck(CALL) = (typeof(CALL) == 'v')
// if typeof(CALL) == 'v' // the void-type
// then typecheck(COMMAND) = true
// else typecheck(COMMAND) = false

COMMAND ::= BRANCH
typecheck(BRANCH) = typecheck(BRANCH)
```

**Atomic Expressions**

```
ATOMIC ::= VNAME
typeof(ATOMIC) = typeof(VNAME) // as per symbol table, which gets consulted at this point

ATOMIC ::= CONST
typeof(CONST) = typeof(CONST) // as per symbol table, which gets consulted at this point

CONST ::= N // Token class N (numeric constant)
typeof(N) = 'n' // this is obviously a base-case

CONST ::= T // Token class T (text constant)
typeof(T) = 't' // this is obviously a base-case
```

**Assignments**

```
ASSIGN ::= VNAME < input // we only allow numeric user-inputs in RecSPL
typecheck(ASSIGN) = (typeof(VNAME) == 'n')
// if typeof(VNAME) == 'n'
// then typecheck(ASSIGN) = true
// else typecheck(ASSIGN) = false

ASSIGN ::= VNAME = TERM // texts or numbers can be assigned to variables
typecheck(ASSIGN) = (typeof(VNAME) == typeof(TERM))
// if typeof(VNAME) == typeof(TERM)
// then typecheck(ASSIGN) = true
// else typecheck(ASSIGN) = false
```

**Terms**

```
TERM ::= ATOMIC
typeof(TERM) = typeof(ATOMIC)

TERM ::= CALL
typeof(TERM) = typeof(CALL)

TERM ::= OP
typeof(TERM) = typeof(OP)
```

**Calls**

```
CALL ::= FNAME( ATOMIC1, ATOMIC2, ATOMIC3)
typecheck(CALL) = (typeof(ATOMIC1) == 'n' && typeof(ATOMIC2) == 'n' && typeof(ATOMIC3) == 'n') && typeof(CALL) == typeof(FNAME)

// if(typeof(ATOMIC1) == 'n' && typeof(ATOMIC2) == 'n' && typeof(ATOMIC3) == 'n') // all three parameters of the function must be numeric
// then typeof(CALL) = typeof(FNAME)  // symbol table may be consulted at this point
// else typeof(CALL) = 'u' // undefined which will cause the type-checker to return false
```

**Operators**

```
OP ::= UNOP( ARG )
typecheck(OP) = (typeof(UNOP) == typeof(ARG) == 'b' || typeof(UNOP) == typeof(ARG) == 'n')

// if typeof(UNOP) == typeof(ARG) == 'b' then typeof(OP) = 'b' // bool-type
// if typeof(UNOP) == typeof(ARG) == 'n' then typeof(OP) = 'n' // numeric type
// else typeof(OP) = 'u' // undefined which will cause the type-checker to return false

OP ::= BINOP( ARG1, ARG2)
typecheck(OP) = (typeof(BINOP) == typeof(ARG1) == typeof(ARG2) == 'b' || typeof(BINOP) == typeof(ARG1) == typeof(ARG2) == 'n' || (typeof(BINOP) == 'c' && typeof(ARG1) == typeof(ARG2) == 'n'))

// if typeof(BINOP) == typeof(ARG1) == typeof(ARG2) == 'b'  thentypeof(OP) = 'b' // bool-type
// if typeof(BINOP) == typeof(ARG1) == typeof(ARG2) == 'n'  thentypeof(OP) = 'n' // numeric type
// if typeof(BINOP) == 'c' // comparison-type, which "takes" numbers and "yields" a boolean result 
   && typeof(ARG1) == typeof(ARG2) == 'n'  thentypeof(OP) = 'b'else typeof(OP) = 'u' // undefined which will cause the type-checker to return false
```

**Arguments**

```
ARG ::=  ATOMIC
typeof(ARG) = typeof(ATOMIC)
ARG ::=  OP
typeof(ARG) = typeof(OP)
```

**Unary Operators**

```
UNOP ::= not
typeof(UNOP) = 'b' // bool-type

UNOP ::= sqrt
typeof(UNOP) = 'n' // numeric type
```

**Binary Operators**

```
BINOP ::= or | and | eq | grt | add | sub | mul | div

BINOP ::= or 
typeof(BINOP) = 'b'
BINOP ::= and
typeof(BINOP) = 'b'

BINOP ::= eq
typeof(BINOP) = 'c'// comparison-type
BINOP ::= grt
typeof(BINOP) = 'c'// comparison-type

BINOP ::= add
typeof(BINOP) = 'n'
BINOP ::= sub
typeof(BINOP) = 'n'
BINOP ::= mul
typeof(BINOP) = 'n'
BINOP ::= div
typeof(BINOP) = 'n'
```

**Branches**

```
BRANCH ::= if COND then ALGO1 else ALGO2
typecheck(BRANCH) = (typeof(COND) == 'b') && (typecheck(ALGO1) && typecheck(ALGO2))

// Attention: do not confuse the syntactic if-then-else in the Syntax Tree with the semantic if-then-else of the recursive type analysis procedure!
// if typeof(COND) == 'b'
// then typecheck(BRANCH) = (typecheck(ALGO1) && typecheck(ALGO2))
// else typecheck(BRANCH) = false
```

**Conditions**

```
COND ::= SIMPLE
typeof(COND) = typeof(SIMPLE)

COND ::= COMPOSIT
typeof(COND) = typeof(COMPOSIT)
```

**Simple Conditions**

```
SIMPLE ::= BINOP( ATOMIC1, ATOMIC2)
typecheck(SIMPLE) = (typeof(BINOP) == typeof(ATOMIC1) == typeof(ATOMIC2) == 'b' || (typeof(BINOP) == 'c' && typeof(ATOMIC1) == typeof(ATOMIC2) == 'n'))

// if typeof(BINOP) == typeof(ATOMIC1) == typeof(ATOMIC2) == 'b'  then typeof(SIMPLE) = 'b'
// if typeof(BINOP) == 'c' // comparison-type
// && typeof(ATOMIC1) == typeof(ATOMIC2) == 'n'  then typeof(SIMPLE) = 'b'
// else typeof(SIMPLE) = 'u' // undefined which will cause the type-checker to return false
```

**Composite Conditions**

```
COMPOSIT ::= BINOP( SIMPLE1, SIMPLE2)
typecheck(COMPOSIT) = (typeof(BINOP) == typeof(SIMPLE1) == typeof(SIMPLE2) == 'b')
// if typeof(BINOP) == typeof(SIMPLE1) == typeof(SIMPLE2) == 'b'  then typeof(COMPOSIT) = 'b'
// else typeof(COMPOSIT) = 'u' // undefined which will cause the type-checker to return false

COMPOSIT ::= UNOP ( SIMPLE )
typecheck(COMPOSIT) = (typeof(UNOP) == typeof(SIMPLE) == 'b')
// if typeof(UNOP) == typeof(SIMPLE) == 'b'  thentypeof(COMPOSIT) = 'b'
// else typeof(COMPOSIT) = 'u' // undefined which will cause the type-checker to return false
```

**Function Names**

```
FNAME ::= F // Token class F (assumed to be in symbol table)
// at this point we assume that the compiler's Scope Analyser has already entered some ID for this variable name into the above-mentioned symbol table, such that symboltable(FNAME) will yield use-able information about that node of the syntax tree.
```

**Functions**

```
FUNCTIONS ::= DECL FUNCTIONS
typecheck(FUNCTIONS1 DECL FUNCTIONS2) = (typecheck(DECL) && typecheck(FUNCTIONS2))

FUNCTIONS ::= epsilon
typecheck(FUNCTIONS) = true // base-case of the type-checking-recursion
```

**Declarations**

```
DECL ::= HEADER BODY
typecheck(DECL) = (typecheck(HEADER) && typecheck(BODY))

// Attention! This is exactly the "area" in the tree where the above-mentioned Tree-crawler must find the above-mentioned return ATOMIC command for comparing its type against the function's return-type that is specified in the HEADER!
```

**Headers**

```
HEADER ::= FTYP FNAME( VNAME1, VNAME2, VNAME3 )
typecheck(HEADER) = (typeof(VNAME1) == typeof(VNAME2) == typeof(VNAME3) == 'n') && (typeof(FNAME) == typeof(FTYP))

// Attention! This is exactly the "area" in the tree where the above-mentioned Tree-crawler must find the above-mentioned return ATOMIC command for comparing its type against the function's return-type that is specified in the HEADER!

typeckeck(HEADER) = { 
    let T := typeof(FTYP)
    let id := symboltable(FNAME)  // access the existing symbol table!
    link (T,id) in the symbol table // symbol table now knows the type!
    typeof(FNAME) = typeof(FTYP)
    if typeof(VNAME1) == typeof(VNAME2) == typeof(VNAME3) == 'n' // RecSPL allows only numeric arguments
        then return true
        else return false
}
```

**Function Types**

```
FTYP ::= num
typeof(FTYP) = 'n' // numeric return type

FTYP ::= void
typeof(FTYP) = 'v' // void, for return-less functions
```

**Bodies**

```
BODY ::= PROLOG LOCVARS ALGO EPILOG SUBFUNCS
typecheck(BODY) = (typecheck(PROLOG) && typecheck(LOCVARS) && typecheck(ALGO) && typecheck(EPILOG) && typecheck(SUBFUNCS))
```

**Prologs and Epilogs**

```
PROLOG ::=
typecheck(PROLOG) = true // base-case of the type-checking procedure

EPILOG ::=
typecheck(EPILOG) = true // base-case of the type-checking procedure
```

**Local Variables**

```
LOCVARS ::= VTYP1 VNAME1, VTYP2 VNAME2, VTYP3 VNAME3
typecheck(LOCVARS) = (
    let T := typeof(VTYP1)
    let id := symboltable(VNAME1)  // access the existing symbol table!
    link (T,id) in the symbol table // symbol table now knows the type!
    typeof(VNAME1) = typeof(VTYP1) 
    let T := typeof(VTYP2)
    let id := symboltable(VNAME2)  // access the existing symbol table!
    link (T,id) in the symbol table // symbol table now knows the type!
    typeof(VNAME2) = typeof(VTYP2)
    let T := typeof(VTYP3)
    let id := symboltable(VNAME3)  // access the existing symbol table!
    link (T,id) in the symbol table // symbol table now knows the type!
    typeof(VNAME3) = typeof(VTYP3) 
    
    return true
)
```

**Subfunctions**

```
SUBFUNCS ::= FUNCTIONS
typecheck(SUBFUNCS) = typecheck(FUNCTIONS)
```

**Additional Notes**

- Ensure that the symbol table is properly managed and updated during type-checking.
- Implement tree-crawling or other techniques to handle function return types and scope-based checks.
- Consider adding error handling and reporting mechanisms to provide informative feedback to the user.

By following these improved type-checking rules, you can enhance the reliability and correctness of your RecSPL compiler.

---

And now: HAPPY PROGRAMMING 😀👍
