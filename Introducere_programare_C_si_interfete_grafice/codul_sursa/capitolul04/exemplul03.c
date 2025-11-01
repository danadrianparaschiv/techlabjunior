#include <stdio.h>

/*
Deci avem o buclă while în care testul este doar valoarea 1; aceasta este o valoare diferită de zero și, prin urmare, 
este întotdeauna adevărată. Dacă includeți cod în interiorul acoladelor după o instrucțiune while (1), 
bucla nu se va termina niciodată; va continua să ruleze pentru totdeauna.

Dar în acest caz am furnizat o modalitate alternativă de a termina bucla; testăm valoarea lui a în interiorul buclei în sine 
într-o instrucțiune if și, dacă a este egal cu 5, apelăm break. Acest lucru face ca bucla să se termine și execuția 
să continue cu instrucțiunea de după buclă. O instrucțiune break ca aceasta poate fi utilă pentru a părăsi 
o buclă în avans în cazul unei erori, de exemplu.
*/


int main (void) 
{ 
  int a = 0;
  
  while (1) 
  { 
    printf ("a este egal cu  %d\n", a); 
    a++; 
    
    if (a == 5)  
    { 
      break; 
    } 
  } 
  
  printf ("a este egal cu %d si am terminat \n", a); 
}