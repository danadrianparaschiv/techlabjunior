#include <stdio.h> 
#include <string.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "fire"; 
  
  if (strcmp (str1, str2) == 0) 
  { 
    printf ("The two strings are identical.\n"); 
  } 
  else 
  { 
    printf ("The two strings are different.\n"); 
  } 
}