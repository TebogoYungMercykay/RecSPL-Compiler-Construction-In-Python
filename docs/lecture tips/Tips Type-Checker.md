# Semester Project ADVICE: The Type-Checker

In the **attachment** I've provided a somewhat abstract 'high-level' specification of a Type System which you shall use as the basis of the implementation of the type-checker module within your compiler for RecSPL. The document clearly shows the idea of '**attributed grammars**' whereby **semantic rules are affiliated with the syntax rules** (such as in Chapter #5 of our Textbook).

- **I hope** that my type system specification is consistent and does not contain too many 'bugs' 😅.
- **IF** you spot any 'bugs' in my specification then you've got to fix them before you can actually program your type-checker software along those lines 😅.

In the attached PDF you can see that the specification of the Type System contains **two** recursive procedures, which are both working on the Syntax-Tree which the Parser has already generated:

- **typecheck** is the main procedure and returns true/false depending on whether (or not) an analysed RecSPL program was correctly typed.
- **typeof** - also recursive - is an auxiliary procedure which 'helps' the typecheck procedure: This auxiliary procedure has access to the already existing Symbol Table, in which relevant type information gets stored, and reports type information to the typecheck procedure by way of various characters (such as 'n' for the numeric type, '**v**' for the void type, '**t**' for the text type, etc...)

[The Type Checker](./type-check.pdf)

---

And now: HAPPY PROGRAMMING 😀👍
