# DFA Cosntruction

## DFA States

- s0: {'q7', 'q16', 'q24', 'q96', 'q131', 'q135', 'q173', 'q121', 'q149', 'q169', 'q66', 'q5', 'q6', 'q129', 'q79', 'q142', 'q171', 'q163', 'q119', 'qS', 'q35', 'q100', 'q141', 'q22', 'q18', 'q0', 'q49', 'q127', 'q39', 'q77', 'q45', 'q57', 'q37', 'q75', 'q114', 'q30', 'q12', 'q85', 'q159', 'q43', 'q143', 'q14', 'q92', 'q146', 'q53', 'q28', 'q32', 'q139', 'q47', 'q41', 'q125', 'q94', 'q161', 'q133', 'q123', 'q98', 'q23', 'q107', 'q73', 'q137', 'q182'}
- s1: {'q29'}
- s2: {'q31'}
- s3: {'q120'}
- s4: {'q122'}
- s5: {'q124'}
- s6: {'q126'}
- s7: {'q128'}
- s8: {'q130'}
- s9: {'q132'}
- s10: {'q134'}
- s11: {'q136'}
- s12: {'q138'}
- s13: {'q170'}
- s14: {'q172'}
- s15: {'q5', 'q1', 'q7', 'q6', 'q12', 'q14'}
- s16: {'q30', 'q16', 'q114', 'q24', 'q96', 'q131', 'q135', 'q121', 'q57', 'q66', 'q129', 'q53', 'q28', 'q32', 'q137', 'q139', 'q35', 'q119', 'q19', 'q100', 'q125', 'q20', 'q49', 'q133', 'q123', 'q39', 'q127', 'q98', 'q107', 'q37'}
- s17: {'q67'}
- s18: {'q16', 'q41', 'q47', 'q43', 'q45', 'q33'}
- s19: {'q160', 'q13'}
- s20: {'q15'}
- s21: {'q162'}
- s22: {'q48'}
- s23: {'q46'}
- s24: {'q140'}
- s25: {'q17'}
- s26: {'q174', 'q8', 'q16'}
- s27: {'q54', 'q42', 'q50'}
- s28: {'q25'}
- s29: {'q93', 'q74'}
- s30: {'q44'}
- s31: {'q36'}
- s32: {'q76', 'q38'}
- s33: {'q40'}
- s34: {'q95', 'q78'}
- s35: {'q97'}
- s36: {'q99'}
- s37: {'q115', 'q80'}
- s38: {'q108', 'q86', 'q101'}
- s39: {'q58'}
- s40: {'q183'}
- s41: {'q144', 'q141', 'q159', 'q143', 'q149', 'q161', 'q146', 'q142'}
- s42: {'q147', 'q163', 'q169'}
- s43: {'q139', 'q150'}
- s44: {'q12', 'q173', 'q14', 'q164'}
- s45: {'q13'}
- s46: {'q2', 'q18'}
- s47: {'q8', 'q16'}
- s48: {'q21'}
- s49: {'q54', 'q50'}
- s50: {'q20'}
- s51: {'q38'}
- s52: {'q115'}
- s53: {'q108', 'q101'}
- s54: {'q68'}
- s55: {'q42'}
- s56: {'q34'}
- s57: {'q9', 'q175'}
- s58: {'q75', 'q16', 'q85', 'q131', 'q135', 'q121', 'q55', 'q79', 'q129', 'q137', 'q139', 'q119', 'q47', 'q41', 'q125', 'q133', 'q123', 'q127', 'q77', 'q73', 'q45', 'q57', 'q43'}
- s59: {'q51'}
- s60: {'q26', 'q30', 'q16', 'q114', 'q24', 'q96', 'q131', 'q135', 'q121', 'q57', 'q66', 'q129', 'q53', 'q28', 'q32', 'q137', 'q139', 'q35', 'q119', 'q100', 'q125', 'q20', 'q49', 'q133', 'q123', 'q39', 'q127', 'q98', 'q107', 'q37'}
- s61: {'q116', 'q100', 'q125', 'q131', 'q135', 'q133', 'q123', 'q127', 'q129', 'q137'}
- s62: {'q16', 'q85', 'q131', 'q135', 'q121', 'q109', 'q92', 'q129', 'q79', 'q119', 'q47', 'q100', 'q125', 'q87', 'q41', 'q102', 'q94', 'q133', 'q123', 'q127', 'q45', 'q137', 'q43'}
- s63: {'q16', 'q41', 'q47', 'q43', 'q45', 'q59'}
- s64: {'q160'}
- s65: {'q145'}
- s66: {'q148'}
- s67: {'q151'}
- s68: {'q174', 'q16'}
- s69: {'q165', 'q18'}
- s70: {'q3', 'q141', 'q159', 'q143', 'q149', 'q161', 'q146', 'q142'}
- s71: {'q9'}
- s72: {'q16', 'q131', 'q135', 'q109', 'q129', 'q41', 'q100', 'q125', 'q47', 'q102', 'q133', 'q123', 'q127', 'q45', 'q137', 'q43'}
- s73: {'q18', 'q69'}
- s74: {'q5', 'q7', 'q6', 'q10', 'q12', 'q176', 'q14'}
- s75: {'q74'}
- s76: {'q76'}
- s77: {'q56'}
- s78: {'q78'}
- s79: {'q80'}
- s80: {'q86'}
- s81: {'q52'}
- s82: {'q27'}
- s83: {'q117'}
- s84: {'q101'}
- s85: {'q103', 'q93'}
- s86: {'q95'}
- s87: {'q88'}
- s88: {'q110'}
- s89: {'q86', 'q101'}
- s90: {'q60'}
- s91: {'q152', 'q16'}
- s92: {'q175'}
- s93: {'q166', 'q171'}
- s94: {'q4'}
- s95: {'q5', 'q7', 'q6', 'q10', 'q12', 'q14'}
- s96: {'q103'}
- s97: {'q70'}
- s98: {'q11'}
- s99: {'q177', 'q8', 'q16'}
- s100: {'q16', 'q85', 'q131', 'q135', 'q121', 'q92', 'q79', 'q129', 'q119', 'q47', 'q87', 'q125', 'q41', 'q94', 'q133', 'q123', 'q127', 'q45', 'q137', 'q43'}
- s101: {'q118'}
- s102: {'q16', 'q41', 'q47', 'q102', 'q45', 'q43'}
- s103: {'q104', 'q16', 'q41', 'q47', 'q45', 'q43'}
- s104: {'q16', 'q85', 'q131', 'q135', 'q121', 'q92', 'q79', 'q129', 'q119', 'q47', 'q41', 'q125', 'q89', 'q94', 'q133', 'q123', 'q127', 'q45', 'q137', 'q43'}
- s105: {'q100', 'q125', 'q131', 'q135', 'q133', 'q123', 'q127', 'q129', 'q111', 'q137'}
- s106: {'q16', 'q85', 'q131', 'q135', 'q121', 'q92', 'q79', 'q129', 'q119', 'q41', 'q47', 'q102', 'q87', 'q125', 'q94', 'q133', 'q123', 'q127', 'q45', 'q137', 'q43'}
- s107: {'q16', 'q41', 'q47', 'q61', 'q45', 'q43'}
- s108: {'q153'}
- s109: {'q176', 'q14', 'q12'}
- s110: {'q141', 'q159', 'q143', 'q149', 'q161', 'q146', 'q167', 'q142', 'q182'}
- s111: {'q71', 'q18'}
- s112: {'q9', 'q178'}
- s113: {'q93'}
- s114: {'q105'}
- s115: {'q90'}
- s116: {'q112'}
- s117: {'q62'}
- s118: {'q16', 'q154'}
- s119: {'q177', 'q16'}
- s120: {'q168'}
- s121: {'q72'}
- s122: {'q5', 'q7', 'q6', 'q10', 'q12', 'q179', 'q14'}
- s123: {'q106'}
- s124: {'q91'}
- s125: {'q113'}
- s126: {'q63', 'q41', 'q47', 'q16', 'q45', 'q43'}
- s127: {'q155'}
- s128: {'q178'}
- s129: {'q184'}
- s130: {'q180', 'q16', 'q8'}
- s131: {'q64'}
- s132: {'q156', 'q16'}
- s133: {'q179', 'q14', 'q12'}
- s134: {'q181', 'q9'}
- s135: {'q65'}
- s136: {'q157'}
- s137: {'q180', 'q16'}
- s138: {'q158'}
- s139: {'q181'}

## DFA Initial State

- s0

## DFA Accepting States

- s7
- s30
- s34
- s74
- s135
- s1
- s56
- s25
- s76
- s77
- s11
- s55
- s69
- s10
- s73
- s33
- s139
- s6
- s81
- s5
- s46
- s23
- s4
- s85
- s29
- s82
- s3
- s32
- s65
- s45
- s70
- s111
- s12
- s8
- s121
- s24
- s0
- s31
- s35
- s36
- s101
- s98
- s78
- s138
- s94
- s64
- s86
- s125
- s75
- s27
- s51
- s95
- s14
- s2
- s48
- s122
- s110
- s22
- s15
- s21
- s19
- s66
- s123
- s124
- s134
- s113
- s41
- s9
- s20
- s13

## DFA Transitions

- s0 --skip--> s1
- s0 --halt--> s2
- s0 --not--> s3
- s0 --sqrt--> s4
- s0 --or--> s5
- s0 --and--> s6
- s0 --eq--> s7
- s0 --grt--> s8
- s0 --add--> s9
- s0 --sub--> s10
- s0 --mul--> s11
- s0 --div--> s12
- s0 --{--> s13
- s0 --}--> s14
- s0 --main--> s15
- s0 --begin--> s16
- s0 --if--> s17
- s0 --print--> s18
- s0 --num--> s19
- s0 --text--> s20
- s0 --void--> s21
- s0 --token_t--> s22
- s0 --token_n--> s23
- s0 --token_f--> s24
- s0 --token_v--> s25
- s0 --VTYP--> s26
- s0 --VNAME--> s27
- s0 --COMMAND--> s28
- s0 --ATOMIC--> s29
- s0 --CONST--> s30
- s0 --ASSIGN--> s31
- s0 --CALL--> s32
- s0 --BRANCH--> s33
- s0 --OP--> s34
- s0 --SIMPLE--> s35
- s0 --COMPOSIT--> s36
- s0 --UNOP--> s37
- s0 --BINOP--> s38
- s0 --FNAME--> s39
- s0 --FUNCTIONS--> s40
- s0 --DECL--> s41
- s0 --HEADER--> s42
- s0 --FTYP--> s43
- s0 --PROLOG--> s44
- s15 --num--> s45
- s15 --text--> s20
- s15 --GLOBVARS--> s46
- s15 --VTYP--> s47
- s16 --skip--> s1
- s16 --halt--> s2
- s16 --not--> s3
- s16 --sqrt--> s4
- s16 --or--> s5
- s16 --and--> s6
- s16 --eq--> s7
- s16 --grt--> s8
- s16 --add--> s9
- s16 --sub--> s10
- s16 --mul--> s11
- s16 --div--> s12
- s16 --end--> s48
- s16 --if--> s17
- s16 --print--> s18
- s16 --token_f--> s24
- s16 --token_v--> s25
- s16 --VNAME--> s49
- s16 --INSTRUC--> s50
- s16 --COMMAND--> s28
- s16 --ASSIGN--> s31
- s16 --CALL--> s51
- s16 --BRANCH--> s33
- s16 --SIMPLE--> s35
- s16 --COMPOSIT--> s36
- s16 --UNOP--> s52
- s16 --BINOP--> s53
- s16 --FNAME--> s39
- s17 --COND--> s54
- s18 --token_t--> s22
- s18 --token_n--> s23
- s18 --token_v--> s25
- s18 --VNAME--> s55
- s18 --ATOMIC--> s56
- s18 --CONST--> s30
- s26 --token_v--> s25
- s26 --VNAME--> s57
- s27 --=--> s58
- s27 --<--> s59
- s28 --;--> s60
- s37 --(--> s61
- s38 --(--> s62
- s39 --(--> s63
- s41 --num--> s64
- s41 --void--> s21
- s41 --FUNCTIONS--> s65
- s41 --DECL--> s41
- s41 --HEADER--> s42
- s41 --FTYP--> s43
- s42 --{--> s13
- s42 --BODY--> s66
- s42 --PROLOG--> s44
- s43 --token_f--> s24
- s43 --FNAME--> s67
- s44 --num--> s45
- s44 --text--> s20
- s44 --VTYP--> s68
- s44 --LOCVARS--> s69
- s46 --begin--> s16
- s46 --ALGO--> s70
- s47 --token_v--> s25
- s47 --VNAME--> s71
- s49 --=--> s58
- s49 --<--> s59
- s50 --end--> s48
- s52 --(--> s61
- s53 --(--> s72
- s54 --then--> s73
- s57 --,--> s74
- s58 --not--> s3
- s58 --sqrt--> s4
- s58 --or--> s5
- s58 --and--> s6
- s58 --eq--> s7
- s58 --grt--> s8
- s58 --add--> s9
- s58 --sub--> s10
- s58 --mul--> s11
- s58 --div--> s12
- s58 --token_t--> s22
- s58 --token_n--> s23
- s58 --token_f--> s24
- s58 --token_v--> s25
- s58 --VNAME--> s55
- s58 --ATOMIC--> s75
- s58 --CONST--> s30
- s58 --CALL--> s76
- s58 --TERM--> s77
- s58 --OP--> s78
- s58 --UNOP--> s79
- s58 --BINOP--> s80
- s58 --FNAME--> s39
- s59 --input--> s81
- s60 --skip--> s1
- s60 --halt--> s2
- s60 --not--> s3
- s60 --sqrt--> s4
- s60 --or--> s5
- s60 --and--> s6
- s60 --eq--> s7
- s60 --grt--> s8
- s60 --add--> s9
- s60 --sub--> s10
- s60 --mul--> s11
- s60 --div--> s12
- s60 --end--> s48
- s60 --if--> s17
- s60 --print--> s18
- s60 --token_f--> s24
- s60 --token_v--> s25
- s60 --VNAME--> s49
- s60 --INSTRUC--> s82
- s60 --COMMAND--> s28
- s60 --ASSIGN--> s31
- s60 --CALL--> s51
- s60 --BRANCH--> s33
- s60 --SIMPLE--> s35
- s60 --COMPOSIT--> s36
- s60 --UNOP--> s52
- s60 --BINOP--> s53
- s60 --FNAME--> s39
- s61 --or--> s5
- s61 --and--> s6
- s61 --eq--> s7
- s61 --grt--> s8
- s61 --add--> s9
- s61 --sub--> s10
- s61 --mul--> s11
- s61 --div--> s12
- s61 --SIMPLE--> s83
- s61 --BINOP--> s84
- s62 --not--> s3
- s62 --sqrt--> s4
- s62 --or--> s5
- s62 --and--> s6
- s62 --eq--> s7
- s62 --grt--> s8
- s62 --add--> s9
- s62 --sub--> s10
- s62 --mul--> s11
- s62 --div--> s12
- s62 --token_t--> s22
- s62 --token_n--> s23
- s62 --token_v--> s25
- s62 --VNAME--> s55
- s62 --ATOMIC--> s85
- s62 --CONST--> s30
- s62 --OP--> s86
- s62 --ARG--> s87
- s62 --SIMPLE--> s88
- s62 --UNOP--> s79
- s62 --BINOP--> s89
- s63 --token_t--> s22
- s63 --token_n--> s23
- s63 --token_v--> s25
- s63 --VNAME--> s55
- s63 --ATOMIC--> s90
- s63 --CONST--> s30
- s67 --(--> s91
- s68 --token_v--> s25
- s68 --VNAME--> s92
- s69 --begin--> s16
- s69 --ALGO--> s93
- s70 --num--> s64
- s70 --void--> s21
- s70 --FUNCTIONS--> s94
- s70 --DECL--> s41
- s70 --HEADER--> s42
- s70 --FTYP--> s43
- s71 --,--> s95
- s72 --or--> s5
- s72 --and--> s6
- s72 --eq--> s7
- s72 --grt--> s8
- s72 --add--> s9
- s72 --sub--> s10
- s72 --mul--> s11
- s72 --div--> s12
- s72 --token_t--> s22
- s72 --token_n--> s23
- s72 --token_v--> s25
- s72 --VNAME--> s55
- s72 --ATOMIC--> s96
- s72 --CONST--> s30
- s72 --SIMPLE--> s88
- s72 --BINOP--> s84
- s73 --begin--> s16
- s73 --ALGO--> s97
- s74 --num--> s45
- s74 --text--> s20
- s74 --GLOBVARS--> s98
- s74 --VTYP--> s99
- s80 --(--> s100
- s83 --)--> s101
- s84 --(--> s102
- s85 --,--> s103
- s87 --,--> s104
- s88 --,--> s105
- s89 --(--> s106
- s90 --,--> s107
- s91 --token_v--> s25
- s91 --VNAME--> s108
- s92 --,--> s109
- s93 --}--> s14
- s93 --EPILOG--> s110
- s95 --num--> s45
- s95 --text--> s20
- s95 --GLOBVARS--> s98
- s95 --VTYP--> s47
- s96 --,--> s103
- s97 --else--> s111
- s99 --token_v--> s25
- s99 --VNAME--> s112
- s100 --not--> s3
- s100 --sqrt--> s4
- s100 --or--> s5
- s100 --and--> s6
- s100 --eq--> s7
- s100 --grt--> s8
- s100 --add--> s9
- s100 --sub--> s10
- s100 --mul--> s11
- s100 --div--> s12
- s100 --token_t--> s22
- s100 --token_n--> s23
- s100 --token_v--> s25
- s100 --VNAME--> s55
- s100 --ATOMIC--> s113
- s100 --CONST--> s30
- s100 --OP--> s86
- s100 --ARG--> s87
- s100 --UNOP--> s79
- s100 --BINOP--> s80
- s102 --token_t--> s22
- s102 --token_n--> s23
- s102 --token_v--> s25
- s102 --VNAME--> s55
- s102 --ATOMIC--> s96
- s102 --CONST--> s30
- s103 --token_t--> s22
- s103 --token_n--> s23
- s103 --token_v--> s25
- s103 --VNAME--> s55
- s103 --ATOMIC--> s114
- s103 --CONST--> s30
- s104 --not--> s3
- s104 --sqrt--> s4
- s104 --or--> s5
- s104 --and--> s6
- s104 --eq--> s7
- s104 --grt--> s8
- s104 --add--> s9
- s104 --sub--> s10
- s104 --mul--> s11
- s104 --div--> s12
- s104 --token_t--> s22
- s104 --token_n--> s23
- s104 --token_v--> s25
- s104 --VNAME--> s55
- s104 --ATOMIC--> s113
- s104 --CONST--> s30
- s104 --OP--> s86
- s104 --ARG--> s115
- s104 --UNOP--> s79
- s104 --BINOP--> s80
- s105 --or--> s5
- s105 --and--> s6
- s105 --eq--> s7
- s105 --grt--> s8
- s105 --add--> s9
- s105 --sub--> s10
- s105 --mul--> s11
- s105 --div--> s12
- s105 --SIMPLE--> s116
- s105 --BINOP--> s84
- s106 --not--> s3
- s106 --sqrt--> s4
- s106 --or--> s5
- s106 --and--> s6
- s106 --eq--> s7
- s106 --grt--> s8
- s106 --add--> s9
- s106 --sub--> s10
- s106 --mul--> s11
- s106 --div--> s12
- s106 --token_t--> s22
- s106 --token_n--> s23
- s106 --token_v--> s25
- s106 --VNAME--> s55
- s106 --ATOMIC--> s85
- s106 --CONST--> s30
- s106 --OP--> s86
- s106 --ARG--> s87
- s106 --UNOP--> s79
- s106 --BINOP--> s80
- s107 --token_t--> s22
- s107 --token_n--> s23
- s107 --token_v--> s25
- s107 --VNAME--> s55
- s107 --ATOMIC--> s117
- s107 --CONST--> s30
- s108 --,--> s118
- s109 --num--> s45
- s109 --text--> s20
- s109 --VTYP--> s119
- s110 --num--> s64
- s110 --void--> s21
- s110 --FUNCTIONS--> s40
- s110 --DECL--> s41
- s110 --HEADER--> s42
- s110 --FTYP--> s43
- s110 --SUBFUNCS--> s120
- s111 --begin--> s16
- s111 --ALGO--> s121
- s112 --,--> s122
- s114 --)--> s123
- s115 --)--> s124
- s116 --)--> s125
- s117 --,--> s126
- s118 --token_v--> s25
- s118 --VNAME--> s127
- s119 --token_v--> s25
- s119 --VNAME--> s128
- s120 --end--> s129
- s122 --num--> s45
- s122 --text--> s20
- s122 --GLOBVARS--> s98
- s122 --VTYP--> s130
- s126 --token_t--> s22
- s126 --token_n--> s23
- s126 --token_v--> s25
- s126 --VNAME--> s55
- s126 --ATOMIC--> s131
- s126 --CONST--> s30
- s127 --,--> s132
- s128 --,--> s133
- s130 --token_v--> s25
- s130 --VNAME--> s134
- s131 --)--> s135
- s132 --token_v--> s25
- s132 --VNAME--> s136
- s133 --num--> s45
- s133 --text--> s20
- s133 --VTYP--> s137
- s134 --,--> s95
- s136 --)--> s138
- s137 --token_v--> s25
- s137 --VNAME--> s139

## DFA Diagramn

```mermaid
stateDiagram-v2
    [*] --> s0

    % TRANSITIONS
    s0 --> s1: skip
    s0 --> s2: halt
    s0 --> s3: not
    s0 --> s4: sqrt
    s0 --> s5: or
    s0 --> s6: and
    s0 --> s7: eq
    s0 --> s8: grt
    s0 --> s9: add
    s0 --> s10: sub
    s0 --> s11: mul
    s0 --> s12: div
    s0 --> s13: {
    s0 --> s14: }
    s0 --> s15: main
    s0 --> s16: begin
    s0 --> s17: if
    s0 --> s18: print
    s0 --> s19: num
    s0 --> s20: text
    s0 --> s21: void
    s0 --> s22: token_t
    s0 --> s23: token_n
    s0 --> s24: token_f
    s0 --> s25: token_v
    s0 --> s26: VTYP
    s0 --> s27: VNAME
    s0 --> s28: COMMAND
    s0 --> s29: ATOMIC
    s0 --> s30: CONST
    s0 --> s31: ASSIGN
    s0 --> s32: CALL
    s0 --> s33: BRANCH
    s0 --> s34: OP
    s0 --> s35: SIMPLE
    s0 --> s36: COMPOSIT
    s0 --> s37: UNOP
    s0 --> s38: BINOP
    s0 --> s39: FNAME
    s0 --> s40: FUNCTIONS
    s0 --> s41: DECL
    s0 --> s42: HEADER
    s0 --> s43: FTYP
    s0 --> s44: PROLOG
    s15 --> s45: num
    s15 --> s20: text
    s15 --> s46: GLOBVARS
    s15 --> s47: VTYP
    s16 --> s1: skip
    s16 --> s2: halt
    s16 --> s3: not
    s16 --> s4: sqrt
    s16 --> s5: or
    s16 --> s6: and
    s16 --> s7: eq
    s16 --> s8: grt
    s16 --> s9: add
    s16 --> s10: sub
    s16 --> s11: mul
    s16 --> s12: div
    s16 --> s48: end
    s16 --> s17: if
    s16 --> s18: print
    s16 --> s24: token_f
    s16 --> s25: token_v
    s16 --> s49: VNAME
    s16 --> s50: INSTRUC
    s16 --> s28: COMMAND
    s16 --> s31: ASSIGN
    s16 --> s51: CALL
    s16 --> s33: BRANCH
    s16 --> s35: SIMPLE
    s16 --> s36: COMPOSIT
    s16 --> s52: UNOP
    s16 --> s53: BINOP
    s16 --> s39: FNAME
    s17 --> s54: COND
    s18 --> s22: token_t
    s18 --> s23: token_n
    s18 --> s25: token_v
    s18 --> s55: VNAME
    s18 --> s56: ATOMIC
    s18 --> s30: CONST
    s26 --> s25: token_v
    s26 --> s57: VNAME
    s27 --> s58: =
    s27 --> s59: <
    s28 --> s60: ;
    s37 --> s61: (
    s38 --> s62: (
    s39 --> s63: (
    s41 --> s64: num
    s41 --> s21: void
    s41 --> s65: FUNCTIONS
    s41 --> s41: DECL
    s41 --> s42: HEADER
    s41 --> s43: FTYP
    s42 --> s13: {
    s42 --> s66: BODY
    s42 --> s44: PROLOG
    s43 --> s24: token_f
    s43 --> s67: FNAME
    s44 --> s45: num
    s44 --> s20: text
    s44 --> s68: VTYP
    s44 --> s69: LOCVARS
    s46 --> s16: begin
    s46 --> s70: ALGO
    s47 --> s25: token_v
    s47 --> s71: VNAME
    s49 --> s58: =
    s49 --> s59: <
    s50 --> s48: end
    s52 --> s61: (
    s53 --> s72: (
    s54 --> s73: then
    s57 --> s74: ,
    s58 --> s3: not
    s58 --> s4: sqrt
    s58 --> s5: or
    s58 --> s6: and
    s58 --> s7: eq
    s58 --> s8: grt
    s58 --> s9: add
    s58 --> s10: sub
    s58 --> s11: mul
    s58 --> s12: div
    s58 --> s22: token_t
    s58 --> s23: token_n
    s58 --> s24: token_f
    s58 --> s25: token_v
    s58 --> s55: VNAME
    s58 --> s75: ATOMIC
    s58 --> s30: CONST
    s58 --> s76: CALL
    s58 --> s77: TERM
    s58 --> s78: OP
    s58 --> s79: UNOP
    s58 --> s80: BINOP
    s58 --> s39: FNAME
    s59 --> s81: input
    s60 --> s1: skip
    s60 --> s2: halt
    s60 --> s3: not
    s60 --> s4: sqrt
    s60 --> s5: or
    s60 --> s6: and
    s60 --> s7: eq
    s60 --> s8: grt
    s60 --> s9: add
    s60 --> s10: sub
    s60 --> s11: mul
    s60 --> s12: div
    s60 --> s48: end
    s60 --> s17: if
    s60 --> s18: print
    s60 --> s24: token_f
    s60 --> s25: token_v
    s60 --> s49: VNAME
    s60 --> s82: INSTRUC
    s60 --> s28: COMMAND
    s60 --> s31: ASSIGN
    s60 --> s51: CALL
    s60 --> s33: BRANCH
    s60 --> s35: SIMPLE
    s60 --> s36: COMPOSIT
    s60 --> s52: UNOP
    s60 --> s53: BINOP
    s60 --> s39: FNAME
    s61 --> s5: or
    s61 --> s6: and
    s61 --> s7: eq
    s61 --> s8: grt
    s61 --> s9: add
    s61 --> s10: sub
    s61 --> s11: mul
    s61 --> s12: div
    s61 --> s83: SIMPLE
    s61 --> s84: BINOP
    s62 --> s3: not
    s62 --> s4: sqrt
    s62 --> s5: or
    s62 --> s6: and
    s62 --> s7: eq
    s62 --> s8: grt
    s62 --> s9: add
    s62 --> s10: sub
    s62 --> s11: mul
    s62 --> s12: div
    s62 --> s22: token_t
    s62 --> s23: token_n
    s62 --> s25: token_v
    s62 --> s55: VNAME
    s62 --> s85: ATOMIC
    s62 --> s30: CONST
    s62 --> s86: OP
    s62 --> s87: ARG
    s62 --> s88: SIMPLE
    s62 --> s79: UNOP
    s62 --> s89: BINOP
    s63 --> s22: token_t
    s63 --> s23: token_n
    s63 --> s25: token_v
    s63 --> s55: VNAME
    s63 --> s90: ATOMIC
    s63 --> s30: CONST
    s67 --> s91: (
    s68 --> s25: token_v
    s68 --> s92: VNAME
    s69 --> s16: begin
    s69 --> s93: ALGO
    s70 --> s64: num
    s70 --> s21: void
    s70 --> s94: FUNCTIONS
    s70 --> s41: DECL
    s70 --> s42: HEADER
    s70 --> s43: FTYP
    s71 --> s95: ,
    s72 --> s5: or
    s72 --> s6: and
    s72 --> s7: eq
    s72 --> s8: grt
    s72 --> s9: add
    s72 --> s10: sub
    s72 --> s11: mul
    s72 --> s12: div
    s72 --> s22: token_t
    s72 --> s23: token_n
    s72 --> s25: token_v
    s72 --> s55: VNAME
    s72 --> s96: ATOMIC
    s72 --> s30: CONST
    s72 --> s88: SIMPLE
    s72 --> s84: BINOP
    s73 --> s16: begin
    s73 --> s97: ALGO
    s74 --> s45: num
    s74 --> s20: text
    s74 --> s98: GLOBVARS
    s74 --> s99: VTYP
    s80 --> s100: (
    s83 --> s101: )
    s84 --> s102: (
    s85 --> s103: ,
    s87 --> s104: ,
    s88 --> s105: ,
    s89 --> s106: (
    s90 --> s107: ,
    s91 --> s25: token_v
    s91 --> s108: VNAME
    s92 --> s109: ,
    s93 --> s14: }
    s93 --> s110: EPILOG
    s95 --> s45: num
    s95 --> s20: text
    s95 --> s98: GLOBVARS
    s95 --> s47: VTYP
    s96 --> s103: ,
    s97 --> s111: else
    s99 --> s25: token_v
    s99 --> s112: VNAME
    s100 --> s3: not
    s100 --> s4: sqrt
    s100 --> s5: or
    s100 --> s6: and
    s100 --> s7: eq
    s100 --> s8: grt
    s100 --> s9: add
    s100 --> s10: sub
    s100 --> s11: mul
    s100 --> s12: div
    s100 --> s22: token_t
    s100 --> s23: token_n
    s100 --> s25: token_v
    s100 --> s55: VNAME
    s100 --> s113: ATOMIC
    s100 --> s30: CONST
    s100 --> s86: OP
    s100 --> s87: ARG
    s100 --> s79: UNOP
    s100 --> s80: BINOP
    s102 --> s22: token_t
    s102 --> s23: token_n
    s102 --> s25: token_v
    s102 --> s55: VNAME
    s102 --> s96: ATOMIC
    s102 --> s30: CONST
    s103 --> s22: token_t
    s103 --> s23: token_n
    s103 --> s25: token_v
    s103 --> s55: VNAME
    s103 --> s114: ATOMIC
    s103 --> s30: CONST
    s104 --> s3: not
    s104 --> s4: sqrt
    s104 --> s5: or
    s104 --> s6: and
    s104 --> s7: eq
    s104 --> s8: grt
    s104 --> s9: add
    s104 --> s10: sub
    s104 --> s11: mul
    s104 --> s12: div
    s104 --> s22: token_t
    s104 --> s23: token_n
    s104 --> s25: token_v
    s104 --> s55: VNAME
    s104 --> s113: ATOMIC
    s104 --> s30: CONST
    s104 --> s86: OP
    s104 --> s115: ARG
    s104 --> s79: UNOP
    s104 --> s80: BINOP
    s105 --> s5: or
    s105 --> s6: and
    s105 --> s7: eq
    s105 --> s8: grt
    s105 --> s9: add
    s105 --> s10: sub
    s105 --> s11: mul
    s105 --> s12: div
    s105 --> s116: SIMPLE
    s105 --> s84: BINOP
    s106 --> s3: not
    s106 --> s4: sqrt
    s106 --> s5: or
    s106 --> s6: and
    s106 --> s7: eq
    s106 --> s8: grt
    s106 --> s9: add
    s106 --> s10: sub
    s106 --> s11: mul
    s106 --> s12: div
    s106 --> s22: token_t
    s106 --> s23: token_n
    s106 --> s25: token_v
    s106 --> s55: VNAME
    s106 --> s85: ATOMIC
    s106 --> s30: CONST
    s106 --> s86: OP
    s106 --> s87: ARG
    s106 --> s79: UNOP
    s106 --> s80: BINOP
    s107 --> s22: token_t
    s107 --> s23: token_n
    s107 --> s25: token_v
    s107 --> s55: VNAME
    s107 --> s117: ATOMIC
    s107 --> s30: CONST
    s108 --> s118: ,
    s109 --> s45: num
    s109 --> s20: text
    s109 --> s119: VTYP
    s110 --> s64: num
    s110 --> s21: void
    s110 --> s40: FUNCTIONS
    s110 --> s41: DECL
    s110 --> s42: HEADER
    s110 --> s43: FTYP
    s110 --> s120: SUBFUNCS
    s111 --> s16: begin
    s111 --> s121: ALGO
    s112 --> s122: ,
    s114 --> s123: )
    s115 --> s124: )
    s116 --> s125: )
    s117 --> s126: ,
    s118 --> s25: token_v
    s118 --> s127: VNAME
    s119 --> s25: token_v
    s119 --> s128: VNAME
    s120 --> s129: end
    s122 --> s45: num
    s122 --> s20: text
    s122 --> s98: GLOBVARS
    s122 --> s130: VTYP
    s126 --> s22: token_t
    s126 --> s23: token_n
    s126 --> s25: token_v
    s126 --> s55: VNAME
    s126 --> s131: ATOMIC
    s126 --> s30: CONST
    s127 --> s132: ,
    s128 --> s133: ,
    s130 --> s25: token_v
    s130 --> s134: VNAME
    s131 --> s135: )
    s132 --> s25: token_v
    s132 --> s136: VNAME
    s133 --> s45: num
    s133 --> s20: text
    s133 --> s137: VTYP
    s134 --> s95: ,
    s136 --> s138: )
    s137 --> s25: token_v
    s137 --> s139: VNAME

    % STARTING STATE
    q0 : "START"

    % ACCEPTING STATES
    s7 : "ACCEPT"
    s30 : "ACCEPT"
    s34 : "ACCEPT"
    s74 : "ACCEPT"
    s135 : "ACCEPT"
    s1 : "ACCEPT"
    s56 : "ACCEPT"
    s25 : "ACCEPT"
    s76 : "ACCEPT"
    s77 : "ACCEPT"
    s11 : "ACCEPT"
    s55 : "ACCEPT"
    s69 : "ACCEPT"
    s10 : "ACCEPT"
    s73 : "ACCEPT"
    s33 : "ACCEPT"
    s139 : "ACCEPT"
    s6 : "ACCEPT"
    s81 : "ACCEPT"
    s5 : "ACCEPT"
    s46 : "ACCEPT"
    s23 : "ACCEPT"
    s4 : "ACCEPT"
    s85 : "ACCEPT"
    s29 : "ACCEPT"
    s82 : "ACCEPT"
    s3 : "ACCEPT"
    s32 : "ACCEPT"
    s65 : "ACCEPT"
    s45 : "ACCEPT"
    s70 : "ACCEPT"
    s111 : "ACCEPT"
    s12 : "ACCEPT"
    s8 : "ACCEPT"
    s121 : "ACCEPT"
    s24 : "ACCEPT"
    s0 : "ACCEPT"
    s31 : "ACCEPT"
    s35 : "ACCEPT"
    s36 : "ACCEPT"
    s101 : "ACCEPT"
    s98 : "ACCEPT"
    s78 : "ACCEPT"
    s138 : "ACCEPT"
    s94 : "ACCEPT"
    s64 : "ACCEPT"
    s86 : "ACCEPT"
    s125 : "ACCEPT"
    s75 : "ACCEPT"
    s27 : "ACCEPT"
    s51 : "ACCEPT"
    s95 : "ACCEPT"
    s14 : "ACCEPT"
    s2 : "ACCEPT"
    s48 : "ACCEPT"
    s122 : "ACCEPT"
    s110 : "ACCEPT"
    s22 : "ACCEPT"
    s15 : "ACCEPT"
    s21 : "ACCEPT"
    s19 : "ACCEPT"
    s66 : "ACCEPT"
    s123 : "ACCEPT"
    s124 : "ACCEPT"
    s134 : "ACCEPT"
    s113 : "ACCEPT"
    s41 : "ACCEPT"
    s9 : "ACCEPT"
    s20 : "ACCEPT"
    s13 : "ACCEPT"
```
