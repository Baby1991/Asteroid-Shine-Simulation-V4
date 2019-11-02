Kriva sjaja jeste funkcija po kojoj se figuriše intenzitet sjaja nekog osvjetljenog tela tokom
vremena. Razlikuje se u zavisnosti od oblika tela koje se posmatra ali i relativnog kretanja izvora
svetlosti i tačke iz koje se to telo posmatra.
Primarna ideja projekta je predstavljala simulaciju nekog dvodimenzionalnog objekta iz čije
geometrije se može izvući njegova kriva sjaja.

Kod za simulaciju asteroida napisan je ponovo u Python programskom jeziku, gde je implementiran efikasniji i tacniji nacin modelovanja. Umesto raycasting metodom, vidljivost se proverava pomocu geometrije linija, sto dozvoljava parcijalno osvetljene/vidjene linije, a i vecu rezoluciju sa boljim rezultatima. Linije se prvo poredjaju po udaljenosti od referentne tacke. Prva linija se uzima za vidljivu, i stavlja na listu vidljivih sektora (linija koja predstavlja pocetak i kraj vise linije koje se nastavljaju jedna na drugu). Svaka naredna linija se proverava da li je vidljiva (ili njen deo) u odnosu na vidljive sektore. Nakon testiranja svake od linija ona (ili njen deo) (ako je vidljiva) se dodaje na listu vidljivih sektora. Zatim se proverava povezanost sektora, i ako postoji, dodaje se nova sa pocetkom u pocetku jedne, a krajem u kraju druge. Originalne dve linije se brisu sa liste vidljivih sektora. Odredjivanje sjaja idalje nije implementirano, ali sa listom svih vidljivih linija (ili delova istih) koje vec imamo, mozemo geometrijski odrediti ove vrednosti.
 
Pored koda simulacije, sastavljen je kod za obradu slike, koji treba da ispiše krivu sjaja na osnovu
fotografija trodimenzionalnih modela asteroida od plastelina. Prvobitno je testiran na slikama
rotacije asteroid oblika takvog da se može poistovetiti sa nekim dvodimenzionalnim oblikom čija
je analitička formula poznata. Ova metoda je testirana na asteroidu oblika lopte - zbog
geometrije lopte, kriva sjaja bi trebala biti prava linija, a takav rezultat je i dobijen.
Postavku eksperimenta su činili rotirajuće postolje sa uglomerom na koje se postavlja model
asteroida od gline, crna pozadina, izvor svetlosti i kamera. Pomoću kamere u visini objekta,
snimljeno je nekoliko različitih modela, prvi put pod osvetljenjem blica telefona, a drugi put sa
sijalicom kao izvorom svetlosti. Pokazalo se da je rezultat je bio optimalniji kada je sijalica bila
izvor svetlosti, tako da su ti rezultati kasnije uzimani kao referentni za upoređivanje. Nakon
adaptiranja ekspozicije kamere, pomoću nje su uslikane faze rotacije modela asteroida koje su
iznosile po 10 stepeni.

Eksperiment je izvršen u cilju da se uporede krive sjaja iz simulacije sa krivama koje se dobijaju
na osnovu rotacije realnog objekta. Rezultati iz eksperimenta su služili kao provera i osnova za
poboljšanje simulacije.

Ono što bismo željeli da radimo dalje jeste da poboljšamo pojedine parametre prilikom
izvođenja eksperimenta, te da na kraju, po mogućnosti, u program implementiramo funkciju po
kojoj je definisan objekat nepravilnog oblika (za početak u 2D). Rezultate koje dobijemo ovom
metodom bismo mogli da upoređujemo sa eksperimentalnim rezultatima, te da na taj način
radimo na unapređivanju programa.

Pokušali smo da saznamo što više o eventualnim inverznim metodama, odnosno određivanje
oblika asteroida pomoću već poznate krive sjaja, međutim nismo naišli ni na kakav povezan a
ujedno I kompetentan članak/rad, ali naše pretpostavke su da se navedeno može izvesti uz
pomoć mašinskog učenja.
