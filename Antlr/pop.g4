/*
BSD License

Copyright (c) 2020, Tom Everett
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of Tom Everett nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/* np_sub 16Feb2025
Notes regarding modification from the original (found here: https://github.com/antlr/grammars-v4/blob/master/vmf/vmf.g4)

The reference grammar was incorrect for the vmf file syntax. Everything, even keys, were being parsed as an atomicvalue because a + quantifier was erroneously added there.
  This has now been resolved.

The reference grammar also did not include source [$TOKEN] flag tokens.
  For purposes of popfiles, we ignore all of these flags.

The reference grammar also did not include #directive tokens.
  For purposes of popfiles, we only use #base, but this modified grammar will now allow others.

The reference grammar also did not include any form of comment syntax. Only // is used for vmf.
  This has now been added.

The reference grammar also did not consider periods being used in unquoted atomic values for use as float/decimal values
  This has now been added.
*/

grammar pop;

pop
    : directive* keyvalue* EOF
    ;

keyvalue
    : key (atomicvalue | listvalue+)
    ;

key
    : val
    ;

atomicvalue
    : val
    ;

val
    : QUOTEDSTRING
    | STRING
    ;

listvalue
    : '{' keyvalue* '}'
    ;
    
directive
    : '#' STRING val
    ;
    
COMMENT
    : '/' '/' ~( '\r' | '\n' )* -> skip
    ;

QUOTEDSTRING
    : '"' (~ ('"' | '\\' | '\r' | '\n') | '\\' ('"' | '\\'))* '"'
    ;

FLAG
    : '[' '$' STRING ']' -> skip
    ;

STRING
    : [a-zA-Z0-9()_$@<>[\]\-/.]+
    ;

WS
    : [ \t\r\n] -> skip
    ;