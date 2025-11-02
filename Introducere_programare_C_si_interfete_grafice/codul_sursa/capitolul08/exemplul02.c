#include <stdio.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "fire"; 
  char *ptr1 = str1, *ptr2 = str2;
  
  while (*ptr1 != 0 && *ptr2 != 0) 
  { 
    if (*ptr1 != *ptr2) 
    { 
      break; 
    } 
    ptr1++; 
    ptr2++; 
  }
  
  if (*ptr1 == 0 && *ptr2 == 0) 
  { 
    printf ("The two strings are identical.\n"); 
  } 
  else 
  { 
    printf ("The two strings are different.\n"); 
  } 
}