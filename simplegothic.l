%{
#include <iostream>
using namespace std;
%}
LETTER [A-Za-z]  
ID  {LETTER}*
EQ  =
SUM +
ASUM -
POW *
DIGIT [0-9]
ZNAK [A-Za-z0-9]
TEXT {ZNAK}*
NUMBER {DIGIT}*
TYPE int|double
ST string
CH char
 
NAMES suicide|Suicide
NAMEC defenestracja|Defenestracja
ONAW [(]
ZNAW [)]
SPACE [ ]






VAR {TYPE}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{NUMBER}{SPACE}*
CODES {NAMES}{SPACE}+{NUMBER}{SPACE}+{ONAW}{SPACE}*{HELPER}*{SPACE}*{ZNAW}{SPACE}*

CODEC {NAMEC}{SPACE}+{ONAW}{SPACE}*{TYPES}{SPACE}*{ZNAW}{SPACE}*
STRING {ST}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{TEXT}{SPACE}*
CHAR {CH}{SPACE}+{ID}{SPACE}*{EQ}{SPACE}*{ZNAK}{SPACE}*


unSu {VAR}|{CODEC}
TYPES {STRING}|{CHAR}|{VAR}
HELPER {CODEC}|{TYPES}

%s  INSIDE_COMMENT
%s  INSIDE_ONE_LINE_COMMENT



%%
{CODES}; {cout<< "Wykrylem petle"<<endl;}

{VAR}; {cout<< "Wykrylem deklaracje zmiennej: "<<yytext <<endl;}
{CHAR}; {cout<< "Wykrylem deklaracje znaku: "<<yytext <<endl;}
{STRING}; {cout<< "Wykrylem strumienn string: "<<yytext <<endl;}
{CODEC}; {cout<< "Wykrylem cout "<<yytext <<endl;}
\/\*      {cout<< "Pocz¹tek komentarza "<<yytext <<endl; BEGIN(INSIDE_COMMENT);}
\*\/      {cout<< "Koniec komentarza "<<yytext <<endl; BEGIN(INITIAL);}
\/\/      {cout<< "Pocz¹tek komentarza "<<yytext <<endl; BEGIN(INSIDE_ONE_LINE_COMMENT);}
<INSIDE_ONE_LINE_COMMENT>\n   {cout<< "Koniec komentarza w linii"<<yytext <<endl; BEGIN(INITIAL);}


<INITIAL>. {cout<< "B³¹d sk³adniowy w: "<<yytext <<endl;}
%%

int yywrap(void){}

int main()
{
	yylex();
	return 0;
}
