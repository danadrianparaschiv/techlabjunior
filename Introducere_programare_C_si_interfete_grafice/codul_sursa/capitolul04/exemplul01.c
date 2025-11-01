#include <stdio.h>

/*
Bucla for nu este atât de diferită de o buclă while, dar tot controlul pentru buclă trăiește în parantezele rotunde după cuvântul cheie for. Aceasta conține trei instrucțiuni, separate prin punct și virgulă: în ordine, acestea sunt condiția inițială, testul și incrementul.

a = 0 este condiția inițială; variabila a este inițializată la 0 la începutul buclei.
a < 5 este testul, exact ca într-o buclă while. Acesta este verificat la fiecare iterație a buclei, și codul buclei este executat doar dacă testul evaluează ca adevărat; de îndată ce testul este fals, execuția continuă după acolada de la sfârșitul codului buclei.
a++ este incrementul; acesta este codul care este executat la sfârșitul fiecărei iterații a buclei, înainte ca testul să fie evaluat din nou. În acest caz, adaugă 1 la a.
*/

int main (void) 
{ 
  int a;
  
  for (a = 0; a < 5; a++) 
  { 
    printf ("a este  %d\n", a); 
  } 
  
  printf ("a este %d si am terminat \n", a); 
}