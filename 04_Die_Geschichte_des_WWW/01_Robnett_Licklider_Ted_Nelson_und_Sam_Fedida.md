<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/robnett-licklider-ted-nelson-und-sam-fedida -->
<!-- slug: robnett-licklider-ted-nelson-und-sam-fedida -->
<!-- filename: 01_Robnett_Licklider_Ted_Nelson_und_Sam_Fedida.md -->
<!-- title: Robnett Licklider, Ted Nelson und Sam Fedida -->

Die frühe Geschichte des Internets und der allmähliche Übergang von leitungsorientierten zu paketvermittelnden Systemen ist in der Literatur so ausführlich beschrieben, dass darauf hier nicht weiter eingegangen wird, sondern eher die Personen erwähnt werden, die die notwendigen vorangehenden geistigen Pionierleistungen erbrachten.

Zu selten wird dabei Joseph Carl Robnett Licklider (1915-1990) erwähnt, der schon in den fünfziger Jahren des vorigen Jahrhunderts vom Konzept des ‚„timesharing‘“ überzeugt war, dass also ein Computer viele Benutzerinnen und Benutzer gleichzeitig bedienen kann. Dies wurde damals von den meisten als zu wenig effizient, als Science-Fiction, abgetan. Einer der wenigen aktiven Unterstützer dieses Konzeptes war übrigens der kürzlich verstorbene Douglas Engelbart (1925-2013), der als Erfinder der Maus zu großen Ehren kam, obwohl seine größten Verdienste eher im konzeptionellen Bereich liegen. Dies ist ähnlich zu Licklider, die beide von der Mensch-Computer-Symbiose nicht nur träumten, sondern darüber schrieben und an Teilaspekten arbeiteten.

Licklider zeigte in einer erfolgreichen öffentlichen Vorführung 1957 das erste Time-Sharing-System auf einer PDP-1. Wenn man aber mit einem Rechner viele verteilte Benutzerinnen und Benutzer mit ihren Endgeräten innerhalb einer Firma gleichzeitig bedienen kann, dann erscheint mir der Sprung, über den Bereich eines Firmengeländes hinauszugehen, eher ein kleiner, ohne damit die Verdienste früher Pioniere von viel größeren Netzwerken wie es zum Beispiel das Internet wurde, allen voran natürlich Vint Cerf (geb. 1943) und Bob Kahn (geb. 1938), schmälern zu wollen.

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Der PDP-1 (Programmed Data Processor 1) war der erste von der Firma DEC im Jahr 1959 entwickelte Minicomputer. Er war so groß wie zwei Kühlschränke, konnte aber im Gegensatz zu den größeren IBM-Maschinen hochgefahren und gesteuert werden.

</blockquote>

Im Vergleich dazu erscheint mir die Betonung von Vannevar Bush (1890-1974) mit seinem Memex immer als überzeichnete Darstellung, da zumeist im englischen Sprachraum nicht bekannt ist, dass in vielen europäischen Bibliotheken bereits im 16. Jahrhundert mit mechanischen Buchautomaten experimentiert wurde, die ein automatisches Umblättern zu einer zugeordneten Seite eines anderen Buches ermöglichten. Abbildung 1 zeigt das ‚Buchrad‘ von Agostino Ramelli (1531-1610) aus dem Jahr 1588: Man konnte, während man eine Seite las, auf einer Tastatur beispielsweise 12378 tippen, wodurch dann automatisch die Seite 378 des Buches 12 aufgeschlagen wurde. Es gab viele, zum Teil sehr ausgefeilte Versionen solcher Buchräder: Trotz aller Einschränkungen (etwa die Anzahl der Bücher, die man verlinken konnte, und dass man sinnvollerweise bei Verweisen gleich die richtige Ziffernfolge, also hier 12378, in die Seite, von der man ‚verzweigen‘ wollte, eintrug) ist hier eine Informationsverlinkung gegeben, wie sie heute anstatt der Eingabe von einigen Ziffern durch einen Mausklick erledigt wird. Dies lässt Memex dann plötzlich nur noch als eine Neuaufwärmung einer uralten Idee mit etwas moderneren Mitteln erscheinen.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/01_Buchrad_von_Ramelli_1588_Keil_G_1990_Foto_aus_seiner_Habilitationsschrift_Paderb.png" alt="Abb. 1: Buchrad von Ramelli 1588 (Keil, G. (1990). Foto aus seiner Habilitationsschrift. Paderborn)">
  <figcaption>Abb. 1: Buchrad von Ramelli 1588 (Keil, G. (1990). Foto aus seiner Habilitationsschrift. Paderborn)</figcaption>
</figure></center>


Die Vision von Ted Nelson (geb. 1937) im Jahr 1960 hingegen scheint sehr bedeutungsvoll. Sein Xanadu-Projekt wird oft als konzeptionell wegbereitend für späterere Hypertext-Systeme gesehen (Nelson prägte auch den Begriff Hypertext), doch werden zahlreiche besonders wesentliche Aspekte seiner Vision selten erwähnt. Drei dieser Aspekte sind:

1. Links müssen bidirektional sein;
2. wenn mehrere ‚Fenster‘ geöffnet sind, muss es möglich sein, Elemente der beiden Fenster zum Beispiel mit einer Linie zu verbinden;
3. es muss Transklusion, also die Fähigkeit, andere Dokumente oder Abschnitte in sich selbst einzuschließen (‚einzubinden‘), möglich sein.

Der erste Aspekt (a) wird aus technischer Sicht noch später behandelt. Für Nelson war es aber wichtig, dass man in jedem Dokument feststellen kann, wer auf dieses verlinkt. Aspekt (b) ist bis heute noch immer in kein gängiges Betriebssystem implementiert, obwohl der Nutzen auf der Hand zu liegen scheint. So muss man sich zum Beispiel immer noch mit Screendumps, die man dann mit einem Grafikeditor bearbeitet, behelfen. Die fehlende Umsetzung von Aspekt (c) ist ebenso erstaunlich. Damit wäre es zum Beispiel einfach möglich, Links (entsprechen Sprungmarken, sogenannten GOTOs in der Programmierung) durch Unterprogrammaufrufe zu ersetzen. In der Programmierung sind GOTOs schon lange verpönt – in fast allen Hypertext-Systemen (auch den üblichen WWW-Anwendungen) wird hingegen noch immer mit Links eine Art ‚Spaghettiprogrammierung‘ (nach Robert Cailliau), anstelle vernünftiger Strukturen aufgebaut. Hingegen existier(t)en genug Systeme, die dies durchaus erlauben. Bei zweien war der Autor selbst involviert:

- HM-Card (Maurer & Sherbakov, 1995) und
- Hyperwave (Maurer, 1996).

Ein ähnliches System mit einer sehr hierarchischen Struktur ist das Gophersystem, das unter der Leitung von Marc McCahill (geb. 1956) an der Universität Minnesota um 1990 entwickelt wurde.

Während 1969, als das große Jahr des (langsamen) Starts des Internets überall erwähnt wird und vom WWW weit und breit noch nichts zu sehen war, hatte der englische Ingenieur Samuel Fedida schon 1968 die Vision ‘Viewdata‘ (und sogar ein Patent darauf), welche die aus funktionaler Sicht wichtigsten Elemente des WWW enthielt. Fedida betonte aber, dass er erst durch den durchaus spekulativen Beitrag „The Computer as a Communication Device“ von Licklider (Licklider & Taylor, 1968) auf die Idee kam und sehr zügig eine damals realistische Version implementierte. 1974, mehr als 15 Jahre vor dem WWW, ging sie als Prototyp in Betrieb und wurde noch in den 1970er Jahren im Vereinigten Königreich als kommerzieller Dienst (Fedida & Malik, 1979) angeboten. Der Dienst wurde später Prestel genannt, beziehungsweise in Deutschland und Österreich ‚Bildschirmtext‘ (BTX), wobei BTX in Deutschland 1977 erstmals auf der Internationalen Funkausstellung Berlin groß der Öffentlichkeit präsentiert wurde. Die Einführung als Pilotbetrieb beziehungsweise -dienst erfolgte dann etwas später, mit Beginn des Jahres 1981 auch in Österreich. Viele europäische Länder, aber auch zahlreiche außereuropäische, boten Varianten davon ab den 1980er Jahren als Dienst oder Pilotdienst an. Darüber wird im nächsten Kapitel berichtet.

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Prestel kann heute als Vormodell des WWW angesehen werden und wurde in den 1970er -Jahren bereits im Vereinigten Königreich als kommerzieller Dienst angeboten.

</blockquote>
