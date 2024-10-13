# Semester Project ADVICE: How to implement the Lexer

The **RecSPL input file**, which your Lexer software must analyse, will be given as a plain **\*.txt** file; for the purpose of experimenting and testing you can easily create such **\*.txt** files (containing some RecSPL program code) by yourself.

How you implement your Lexer - in which programming language, and with which methods and techniques - is entirely up to your own choice, as long as only the following **requirements** are met:

- IF the input **\*.txt** file contains any **lexical errors** (which corresponds, in theory, to the underlying DFA getting 'stuck' in a non-accepting state), then your **Lexer** software must "throw" a reasonably understandable **Error-Message** back to the User.
- IF the input **\*.txt** file does not contain any lexical errors, then your **Lexer** software must **create**, **write**, and **store** (as its output) an **XLM file** which the Parser can later use as its input.

In this manner, you can keep your implementations of Lexer and Parser completely separated from each other in different "phases" of your semester-project, because **the persistent XML file will serve as an "offline bridge"** between Lexer and Parser. This design approach is very "convenient" and will make your "project life" much easier (in comparison against having to implement one huge all-in-all Compiler software). Thus you'll even be able to switch your computer off and on again between Lexing and Parsing :)

Thereby, the "tokenized" **contents of the XML** file shall be structured as follows:

```xml
<TOKENSTREAM>
    <TOK>
        <!-- Comment: Each token has its own unique ID number -->
        <ID>1</ID>
        <!-- comment: See an example for illustration below -->
        <CLASS>the token's class</CLASS>
        <!-- comment: See example below -->
        <WORD>terminal characters for the Parser</WORD> 
    </TOK>
    <TOK>
        <ID>2</ID>
        <CLASS>the token's class</CLASS>
        <WORD>terminal characters for the Parser</WORD>
    </TOK>
    ... etc ...
    <TOK>
        ... etc ...
    </TOK>
</TOKENSTREAM>
```

## `Examples`

```xml
<TOK>
    <ID>126</ID>
    <!-- Comment: The class corresponds to some Accept-State of the DFA -->
    <CLASS>reserved_keyword<CLASS>
    <WORD>else</WORD>
</TOK>
...
<TOK>
    <ID>496</ID>
    <!-- comment: That is the token-class for Numbers, as per given Specification Sheet -->
    <CLASS>N<CLASS>
    <WORD>56.7</WORD>
</TOK>
```

**And now: HAPPY PROGRAMMING** 😀👍

**IF** in doubt, **THEN ==>** go to Tutor's Consultation Hour on Tuesdays!

## More Information (From Me)

### Token-Class V: User Defined Variable Names

Regular Expression: V_$[a‒z]([a‒z]|[0‒9])^*$
Note: The prefix `V_` makes it easy to distinguish variables from the reserved keywords
Errors: These types of names should be invalid variable names, aa, a, V_44, Vx and so on since they do not follow the regular expression pattern above. Variable names should begin with V_ and we cannot have ones like a, b, c and so on.


### Token-Class F: User Defined Function Names

Regular Expression: F_$[a‒z]([a‒z]|[0‒9])^*$
Note: The prefix `F_` makes it easy to distinguish functions from the reserved keywords
Errors: These types of function names should be invalid F_, F_0, F8 since they are not part of the regular expression pattern above. Function names should begin with F_ and we cannot have ones like a, b, c and so on.

### Token-Class T: Strings

Regular Expressions:
$"[A-Z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]"$ |
$"[A-Z][a-z][a-z][a-z][a-z][a-z][a-z]"$ |
$"[A-Z][a-z][a-z][a-z][a-z][a-z]"$ |
$"[A-Z][a-z][a-z][a-z][a-z]"$ |
$"[A-Z][a-z][a-z][a-z]"$ |
$"[A-Z][a-z][a-z]"$ |
$"[A-Z][a-z]"$ |
$"[A-Z]"$

Note: The strings are inside quotation marks ("") and for the sake of simplicity our short strings contain up to eight characters between quotation marks, whereby the string's first character is Capitalized.
Errors: These types of strings should be invalid "79", "6", "69999", "yyyyy", "Ykkkkkkkkk" since they do not obey the regular exression above pattern.

### Token-Class N: Numbers

Tokens: 
Regular Expression: $0$ `|` $0.([0‒9])^* [1‒9]$ `|` $-0.([0‒9])^* [1‒9]$ `|` $ [1‒9]([0‒9])^*$ `|` $-[1‒9]([0‒9])^*$ `|` $ [1‒9]([0‒9])^*. ([0‒9])^* [1‒9]$ `|` $-[1‒9]([0‒9])^*. ([0‒9])^* [1‒9]$
Note: in our programming language we do not distinguish between INT and REAL. The dot here belongs to the language itself, not to the meta language of Regular Expressions!. The yellow Minus (-) belongs to the language itself, for the composition of Negaive Numbers. The white Dash‒ belongs to the meta language of Regular Expressions!
Errors: These types of invalid combinations hould throw errors, d.9, 9.08r, since this class is for Numbers (Integers, Floats, Doubles, Longs and so on)

### Token-Class Reserved Keyword: These are Fixed Tokens

Legal Tokens: { 'skip', 'halt', '(', ')', ',', 'not', 'sqrt', 'or', 'and', 'eq', 'grt', 'add', 'sub', 'mul', 'div', '{', '}', '=', '<', 'input', 'main', 'begin', 'end', 'if', 'then', 'else', 'print', 'num', 'text', 'void' }
Erros: All the other characters and words (string like ones without the "" enclosing them) should be erros as far as they do not meet the above classes. exampls are a, aa, b , c , jj, number, gate and so on, int, double, float as words should be invalid and an error should be printed in the xml file (clearing all the parts done), an error only should appear and we stop lexing. we should also print the error.

---
---
