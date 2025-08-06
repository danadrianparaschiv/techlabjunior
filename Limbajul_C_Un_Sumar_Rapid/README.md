# Esențialul limbajului C / Limbajul C Un sumar rapid


## Din editia originala in limba engleza
© Nick Parlante, 1996. Gratuit pentru uz necomercial.

Acest document rezumă practic toate caracteristicile majore ale limbajului C. Nu explică cum funcționează lucrurile în detaliu, dar oferă suficiente informații pentru a fi, sperăm, util. A fost bazat inițial pe un document al lui Mike Cleron și acum este un fel de proiect în desfășurare al meu. Am făcut numeroase modificări și îmbunătățiri de-a lungul anilor în timp ce am predat CS107. Vă rog să trimiteți orice feedback la nick@cs.stanford.edu.

## Istoria Limbajului C

Limbajul de programare C a fost dezvoltat între 1969 și 1973 la Laboratoarele Bell de către Dennis Ritchie, ca o evoluție a limbajului B creat de Ken Thompson. Ritchie a dorit să creeze un limbaj care să combine eficiența limbajelor de nivel scăzut cu flexibilitatea limbajelor de nivel înalt. Numele "C" vine natural după "B", fiind următoarea literă din alfabet. Prima versiune funcțională a fost finalizată în 1972, iar în 1978 Ritchie și Brian Kernighan au publicat cartea legendară "The C Programming Language", care a devenit standardul de facto și a fost cunoscută sub numele de "K&R C".

Succesul limbajului C a fost strâns legat de sistemul de operare UNIX, care a fost rescris aproape în întregime în C în 1973. Această decizie a fost revoluționară pentru epoca respectivă, când majoritatea sistemelor de operare erau scrise în limbaj de asamblare. Portabilitatea rezultată a făcut ca UNIX să poată fi adaptat pe diverse arhitecturi hardware, iar C să devină limbajul preferat pentru programarea de sistem. Filosofia "write once, run anywhere" a avut origini în această perioadă, cu decenii înainte de Java.

În 1989, American National Standards Institute (ANSI) a standardizat limbajul C cu standardul ANSI C (cunoscut și ca C89), urmat de standardul ISO C90 în 1990. Aceste standarde au stabilit regulile precise ale limbajului și au asigurat portabilitatea codului între diferite platforme. Mai târziu au urmat alte revizii importante: C99 (1999), C11 (2011), C17 (2018) și cel mai recent C23, fiecare aducând îmbunătățiri și funcționalități noi, dar păstrând compatibilitatea inversă și spiritul original al limbajului.

Impactul limbajului C asupra programării moderne este imens - a inspirat dezvoltarea unor limbaje precum C++, Java, C#, JavaScript și multe altele. Astăzi, după peste 50 de ani, C rămâne unul dintre cele mai folosite limbaje de programare, fiind esențial în sistemele embedded, kernel-uri de sisteme de operare, compilatoare și aplicații unde performanța și controlul direct asupra hardware-ului sunt critice.
