%{
#include <iostream>
using namespace std;
%}
LETTER [A-Za-zπÊÍ≥ÒÛúøü• ∆èØå£—”]  
ID  {LETTER}*
EQ  =
SUM +
ASUM -
POW *
DIGIT [0-9]
NUMBER {DIGIT}*
TYPE int|double
NAMES suicide|Suicide
NAMEC defenestracja|Defenestracja
ONAW [(]
ZNAW [)]
SPACE [ ]
CODE {CODEZ}|{CODEC}|{CODES}
COMMAND {CODE};


CODEZ {TYPE}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{NUMBER}{SPACE}*
CODES {NAMES}{SPACE}+{NUMBER}{SPACE}+{ONAW}{SPACE}*{CODE}{SPACE}*{ZNAW}{SPACE}*;
CODEC {NAMEC}{SPACE}+{ONAW}{SPACE}*{CODEZ}{SPACE}*{ZNAW}{SPACE}*





CODESx {NAMES}{SPACE}+{NUMBER}{SPACE}+{ONAW}{SPACE}*{TYPE}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{NUMBER}{SPACE}*{ZNAW}{SPACE}*
CODECx {NAMEC}{SPACE}+{ONAW}{SPACE}*{TYPE}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{NUMBER}{SPACE}*{ZNAW}{SPACE}*


%s  INSIDE_COMMENT
%s  INSIDE_ONE_LINE_COMMENT



%%
<INITIAL>{CODEZ} {cout<< "Wykrylem deklaracje zmiennej: "<<yytext <<endl;}
<INITIAL>{CODES} {cout<< "Wykrylem petle"<<yytext <<endl;}
<INITIAL>{CODEC} {cout<< "Wykrylem cout "<<yytext <<endl;}
\/\*      {cout<< "Poczπtek komentarza "<<yytext <<endl; BEGIN(INSIDE_COMMENT);}
\*\/      {cout<< "Koniec komentarza "<<yytext <<endl; BEGIN(INITIAL);}
<INSIDE_COMMENT>{COMMAND} {cout<< "UWAGA instrukcja "<< yytext << " w komentarzu, potencjalny b≥πd czystego kodu"<<endl;}
<INSIDE_ONE_LINE_COMMENT>{COMMAND} {cout<< "UWAGA instrukcja "<< yytext << " w komentarzu, potencjalny b≥πd czystego kodu"<<endl;}
\/\/      {cout<< "Poczπtek komentarza "<<yytext <<endl; BEGIN(INSIDE_ONE_LINE_COMMENT);}
<INSIDE_ONE_LINE_COMMENT>\n   {cout<< "Koniec komentarza w linii"<<yytext <<endl; BEGIN(INITIAL);}
%%

int yywrap(void){}

int main()
{
	yylex();
	return 0;
}
