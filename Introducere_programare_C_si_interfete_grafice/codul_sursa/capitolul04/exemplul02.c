#include <stdio.h>

int main (void) 
{ 
  unsigned int a = 0;
  
  switch (a) 
  { 
    case 0 :    printf ("a este egal cu 0\n"); 
                break; 
    case 1 :    printf ("a este egal cu 1\n"); 
                break; 
    default :   printf ("a este mai mare decat 1\n");             
  } 

  /*
  Codul de mai sus este echivalent cu următorul cod folosind if...else:
  if (a == 0) 
  { 
    printf ("a este egal cu 0\n"); 
  } 
  else if (a == 1) 
  { 
    printf ("a este egal cu 1\n"); 
  } 
  else 
  { 
    printf ("a este mai mare decat 1\n"); 
  } 
  */
}