#include <stdio.h> 
#include <string.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "second"; 
  char str3[20];
  
  strcpy (str3, str1); 
  strcat (str3, str2);
  
  printf ("%s + %s = %s\n", str1, str2, str3); 
}