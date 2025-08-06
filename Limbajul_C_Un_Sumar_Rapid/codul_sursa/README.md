# Cum sa compilezi si sa executi codul sursa

## Windows 11

### Compilarea codului C în Windows 11
Cea mai populară opțiune gratuită de compilator este [MinGW-w64](https://www.mingw-w64.org), care poate fi instalat prin MSYS2 sau prin pachete standalone. Alternativ, poți folosi [Microsoft Visual Studio Community (gratuit)](https://visualstudio.microsoft.com/vs/community/) care vine cu compilatorul MSVC, sau doar Visual Studio Build Tools dacă preferi să lucrezi din linia de comandă. După instalare, deschizi Command Prompt sau PowerShell, navighezi la directorul unde ai fișierul sursă (de exemplu program.c), și folosești comanda gcc program.c -o program.exe pentru MinGW sau cl program.c pentru MSVC. Compilatorul va genera un fișier executabil (.exe) în același director.

### Rularea și depanarea
Pentru a rula programul compilat, pur și simplu tastezi numele executabilului în terminal: program.exe sau .\program.exe. Dacă programul are dependințe externe sau folosește biblioteci specifice, s-ar putea să fie nevoie să adaugi flag-uri suplimentare la compilare (cum ar fi -lm pentru biblioteca matematică). În caz de erori, compilatorul va afișa mesaje detaliate care te vor ajuta să identifici problemele din cod. Pentru proiecte mai complexe, poți folosi un IDE precum Code::Blocks, Dev-C++, sau chiar Visual Studio Code cu extensii pentru C, care oferă highlighting sintactic, auto-complete și debugging integrat, făcând procesul de dezvoltare mult mai eficient.

## Ubuntu (sau orice alta distributie majora de Linux)

Pentru a compila și rula cod C în Ubuntu, primul pas este instalarea unui compilator C. Cel mai popular și folosit este GCC (GNU Compiler Collection), care poate fi instalat prin comanda sudo apt update && sudo apt install build-essential. Pachetul build-essential include GCC, bibliotecile standard C și alte utilitare necesare pentru dezvoltare. După instalare, poți verifica că totul funcționează corect cu comanda gcc --version. Pentru a compila un program C simplu, salvezi codul în fișier cu extensia .c (de exemplu hello.c), apoi rulezi comanda gcc hello.c -o hello în terminal. Aceasta va crea un fișier executabil numit "hello" care poate fi rulat cu comanda ./hello.

În practică, există mai multe opțiuni utile pentru compilare care îmbunătățesc procesul de dezvoltare. Opțiunea -Wall activează majoritatea avertismentelor compilatorului (gcc -Wall hello.c -o hello), ajutându-te să identifici potențiale probleme în cod. Pentru debugging, poți adăuga flag-ul -g care include informații de debug în executabil, permițând folosirea debugger-ului GDB. Dacă lucrezi cu proiecte mai complexe cu mai multe fișiere sursă, poți compila toate fișierele odată: gcc -Wall file1.c file2.c file3.c -o program. Pentru optimizare, poți folosi flag-uri precum -O2 sau -O3 care îmbunătățesc performanța codului compilat. Alternativ, poți folosi editoare moderne precum VSCode cu extensii pentru C/C++ care oferă compilare și debugging integrat, făcând procesul mai accesibil pentru începători.

```
gcc --version
gcc hello-world.c -o hello-world
./hello-world
```

## MacOS

### Compilarea codului C în macOS
Pentru a compila și rula cod C pe macOS, cea mai simplă modalitate este să instalezi [Xcode Command Line Tools](https://developer.apple.com/xcode/resources/) executând comanda xcode-select --install în Terminal. Aceasta va instala compilatorul GCC (de fapt Clang) și toate instrumentele necesare pentru dezvoltare. Alternativ, poți instala Xcode complet din App Store dacă planifici să dezvolți aplicații pentru ecosistemul Apple. După instalare, deschizi Terminal, navighezi la directorul cu fișierul sursă folosind cd, și compilezi cu comanda gcc program.c -o program sau clang program.c -o program. Compilatorul va genera un fișier executabil (fără extensie .exe ca în Windows) în același director.

### Rularea și opțiuni suplimentare
Pentru a rula programul compilat, tastezi ./program în Terminal (prefixul ./ este necesar pentru a specifica că executabilul se află în directorul curent). macOS vine cu majoritatea bibliotecilor standard C deja instalate, dar pentru biblioteci suplimentare poți folosi manageri de pachete precum Homebrew (brew install nume_biblioteca). În caz de erori de compilare, Clang oferă mesaje foarte detaliate și sugestii utile pentru rezolvarea problemelor. Pentru un flux de lucru mai avansat, poți folosi editoare precum Visual Studio Code cu extensii pentru C, Xcode pentru proiecte mai mari, sau chiar vim/nano direct în Terminal pentru editări rapide.
