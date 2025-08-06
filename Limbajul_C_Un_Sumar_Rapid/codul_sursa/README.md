# Cum sa compilezi si sa executi codul sursa

## Ubuntu (sau orice alta distributie majora de Linux)

Pentru a compila și rula cod C în Ubuntu, primul pas este instalarea unui compilator C. Cel mai popular și folosit este GCC (GNU Compiler Collection), care poate fi instalat prin comanda sudo apt update && sudo apt install build-essential. Pachetul build-essential include GCC, bibliotecile standard C și alte utilitare necesare pentru dezvoltare. După instalare, poți verifica că totul funcționează corect cu comanda gcc --version. Pentru a compila un program C simplu, salvezi codul în fișier cu extensia .c (de exemplu hello.c), apoi rulezi comanda gcc hello.c -o hello în terminal. Aceasta va crea un fișier executabil numit "hello" care poate fi rulat cu comanda ./hello.

În practică, există mai multe opțiuni utile pentru compilare care îmbunătățesc procesul de dezvoltare. Opțiunea -Wall activează majoritatea avertismentelor compilatorului (gcc -Wall hello.c -o hello), ajutându-te să identifici potențiale probleme în cod. Pentru debugging, poți adăuga flag-ul -g care include informații de debug în executabil, permițând folosirea debugger-ului GDB. Dacă lucrezi cu proiecte mai complexe cu mai multe fișiere sursă, poți compila toate fișierele odată: gcc -Wall file1.c file2.c file3.c -o program. Pentru optimizare, poți folosi flag-uri precum -O2 sau -O3 care îmbunătățesc performanța codului compilat. Alternativ, poți folosi editoare moderne precum VSCode cu extensii pentru C/C++ care oferă compilare și debugging integrat, făcând procesul mai accesibil pentru începători.

```
gcc --version
gcc hello-world.c -o hello-world
./hello-world
```
