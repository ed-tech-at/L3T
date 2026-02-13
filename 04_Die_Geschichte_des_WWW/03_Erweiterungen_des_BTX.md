<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/erweiterungen-des-btx -->
<!-- slug: erweiterungen-des-btx -->
<!-- filename: 03_Erweiterungen_des_BTX.md -->
<!-- title: Erweiterungen des BTX -->

In Kanada versuchte man besonders die komplexen Mosaik-Grafiken zu vereinfachen und programmierte den Decoder so, dass er automatisch gewisse geometrische Objekte zeichnen konnte. Statt zum Beispiel einen roten Kreis annähernd und aufwendig aus Mosaiksteinchen zusammenzusetzen, schickte man einen Code, der im Wesentlichen besagte: „Zeichne einen rot gefüllten Kreis mit Radius r und Zentrum (x,y).“ Diese Entwicklung von „geometrischer Grafik“ unter dem Namen „Telidon“ wurde dann von AT+T unter ‚NAPLPS‘ weiterverfolgt, ohne aber einen entscheidenden Durchbruch auszulösen.

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Telidon und NAPLPS waren grafische Beschreibungssprachen für Video- und Bildschirmtext-Systeme.

</blockquote>

In Japan setzte man mit dem Videotext-System ‚CAPTAIN‘ nur auf pixelorientierte Bilder, weil man so gleich auch japanische Schriftzeichen erzeugen konnte. Da es aber zu dieser Zeit noch kein Komprimierungsverfahren gab (wie zum Beispiel heute unter anderem bei Bildern im Format .jpeg in Verwendung), waren die Übertragungszeiten unangenehm lang. In Europa wurde von allen damaligen Kommunikationsmonopolbetreibern 1985 eine neue Norm, ‘CEPT II, Level 2 und 3‘ (Level 2 dabei verpflichtend), beschlossen, wodurch eine Umstellung bei den Benutzern und Benutzerinnen, bei den Serverbetreibenden und den Decoderherstellenden notwendig war und damit mit Sicherheit auch die Weiterentwicklung verlangsamt statt beschleunigt wurde.

Level 2 der Norm sollte ein verbessertes BTX sein: 4096 Farben, 32 verschiedene Blinkfrequenzen, frei definierbare Zeichensätze (dynamically redefinable charactersets, DRCS) u. Ä. erlaubten zwar die Erstellung sehr schöner Bilder, jedoch mit erheblichem Aufwand. Level 3 beinhaltete geometrische Grafik, war jedoch nicht verpflichtend in der Umsetzung und wurde eigentlich nur in Österreich aktiv verfolgt.

Es ist inzwischen so viel Zeit vergangen, dass man heute ungestraft erklären darf, warum Europa eine so eigene komplexe europäische Grafiknorm für BTX einführte: Man konnte damit die ersten am Horizont sichtbaren Heimcomputer aus Japan oder den USA aus Europa schlicht und einfach fern halten, denn ohne spezielle Hardware waren die eigentümlichen Anforderungen der Grafik erst mit sehr hochwertigen Heimcomputern und daher erst zehn Jahre später (mit dem ‚Amiga‘ von Commodore als erstem) möglich. Kurzum, die Norm war in Wahrheit ein Schutzschirm gegen Importe nach Europa. Im Schutze dieses Schirms hoffte man, eigene europäische Geräte erzeugen und anbieten zu können.

Zwei der wichtigsten europäischen Mitunterzeichnenden dieser Regelung kümmerten sich aber von Anfang an nicht um die neue Norm. Das Vereinigte Königreich machte mit dem anfänglichen BTX (‚Prestel‘) weiter wie gehabt, mäßig erfolgreich. Die Franzosen bauten mit einer gewissen Verzögerung einen S/W-Bildschirm mit alphabetischer Tastatur in das Telefon ein. Dieses Minitel war zwar meilenweit von der CEPT-II-Norm entfernt, aber ideal, um es als elektronisches Telefonbuch, Nachschlagewerk, Buchungsinstrument oder für Nachrichtendienste zu verwenden. Im Laufe der Zeit benutzten immerhin 30% der französischen Haushalte (6 Millionen) ein Minitel. Im Jahr 1996 war der mit Minitel erzielte Umsatz in Frankreich noch größer als jener mit dem Internet in den flächen- und einwohnermäßig wesentlich größeren USA. Die Verbreitung der Geräte in Frankreich wurde insofern unterstützt, als dass man anfangs Haushalten, die auf gedruckte Telefonbücher verzichteten, das Minitel gratis zur Verfügung stellte.

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Minitel ist ein 1982 in Frankreich eingeführter Onlinedienst, der dem deutsch/österreichischen BTX sehr ähnlich war. Wesentlicher Unterschied ist, dass Minitel auf eigene Terminals setzte und keine Nutzung von Fernsehgeräten als Bildschirm benötigte.

</blockquote>

Deutschland und einige Nachbarländer setzten auf den Level-2-Standard, wobei Österreich von Anfang an, also schon zu den Beginnzeiten des BTX, eine neue Idee verfolgte, die auf meinen damaligen Mitarbeiter und heutigen CIO der Regierung, Prof. Posch, und den Verfasser zurückging. Wenn Fernsehgeräte mit Elektronik nachgerüstet werden, wieso verwendet man nicht gleich programmierbare Computer, die natürlich nicht nur Level 3 unterstützen konnten, sondern die man auch ohne Telefonverbindung als Kleincomputer einsetzen konnte? Da insbesondere externe Speicher (wie Kassettenlaufwerke) langsam und unzuverlässig waren, beschlossen wir, alle Daten und Programme mit Ausnahme eines Kernbetriebssystems in den BTX-Zentralrechnern abzuspeichern. Im unveränderbaren ROM (Read Only Memory) des Gerätes, des MUPID (Mehrzweck Universell Programmierbarer Intelligenter Decoder - der wie Insider wissen: ‚Maurer Und Posch Intelligenter Decoder‘), befand sich Software zur Anzeige von Daten, für Interaktionen mit den BTX-Zentralen, für das Editieren und für das Programmieren (in einer Grafikversion der Programmiersprache BASIC).

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

BASIC steht für **B**eginner's **A**ll-purpose **S**ymbolic **I**nstruction **C**ode und ist eine imperative Programmiersprache. Neben der einfachen Erlernbarkeit zeichnete diese Sprache in den Anfängen die Verwendung von Zeilennummern und Sprungbefehlen (GOTO) aus. Der Höhepunkt der Sprache kann mit Ende der 1970er, Anfang der 1980er Jahre datiert werden, als viele Heimcomputer mit einem BASIC-Interpreter ausgeliefert wurden.

</blockquote>

Alle Daten und selbst programmierte oder komplexe zusätzliche Programme konnte man in den BTX-Zentralen ablegen und jederzeit abrufen - ähnlich, wie man es heute mit Smartphone-Apps macht oder über Cloud-Computing redet, nur nannte man es damals Teleprogramme und Zentralrechner. Die Programmierbarkeit des MUPIDS (der 1985 an den CEPT-Standard angepasst wurde) erweiterte die Möglichkeiten ungemein. Sehr erfolgreiche Berechnungen, Mehrpersonenspiele, Informationsverwaltungsprogramme, die ersten ‚Social Networks‘ entstanden und vieles mehr. Abbildung 4 zeigt den Stichtag 15. April 1982, als wir den ersten MUPID der damals tatsächlich staunenden Welt (auch Fachwelt) vorführten.

Der Siegeszug des MUPID im wichtigsten Absatzmarkt Deutschland wurde durch Interventionen der deutschen Post zu Gunsten deutscher Firmen gebremst, sodass die Gesamtproduktion 50.000 Geräte nicht überschritt, mit 40% Absatz in Österreich.

Natürlich wurde mit der Kombination MUPID/ BTX auch erstmals (landesweit) vernetztes Lernen und Lehren möglich, so dass im Laufe der Zeit über 300 einstündige Unterrichtseinheiten mit Bildern, Animationen, Frage/Antwortspielen usw. entwickelt wurden. Bei der IFIP Weltkonferenz 1986 wurde dies im Aufsatz über „Nationwide teaching through a network of microcomputers“ (Maurer, 1986) dargestellt. Das Projekt selbst nannte sich COSTOC (Computer Supported Teaching of Computer Science) und wurde an Dutzenden Universitäten weltweit eingesetzt. Eine partielle Liste findet sich auch in den Links zum Kapitel auf diigo.com.  
Es gab Kurse in Deutsch und Englisch, einige von hochrangigen Wissenschaftlern wie Arto Salomaa, Thomas Ottmann oder Ian Witten verfasst.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/04_MUPID_vorgestellt_am_1541982_in_Wien.png" alt="Abb. 4: MUPID, vorgestellt am 15.4.1982 in Wien">
  <figcaption>Abb. 4: MUPID, vorgestellt am 15.4.1982 in Wien</figcaption>
</figure></center>


<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Bildmaterial und andere Informationen zu MUPID, COSTOC, BTX, Autool (dem Editierwerkzeug für COSTOC), Hyper-G, Hyperwave, Harmony, Amadeus, HM-Card, GENTLE usw. finden sich unter [http://much.iicm.edu/projects](http://much.iicm.edu/projects/costoc_2/3.htm/).

</blockquote>

Mit MUPID waren auch schon Pixelbilder leicht generierbar und anzeigbar. Die fehlenden guten Bildkomprimierungsmethoden und langsamen Leitungen führten jedoch dazu, dass der Einsatz anfangs recht beschränkt war. Abbildung 5 zeigt, dass man BTX sogar verwendete, um den Prozess der Digitalisierung zu erklären.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/05_Mit_MUPID_und_Videokamera_war_eine_direkte_Bildabspeicherung_möglich.png" alt="Abb. 5: Mit MUPID und Videokamera war eine direkte Bildabspeicherung möglich.">
  <figcaption>Abb. 5: Mit MUPID und Videokamera war eine direkte Bildabspeicherung möglich.</figcaption>
</figure></center>


Abbildung 6 zeigt die Anwendung MUPID-Teleschach. Damit konnte man synchron und asynchron mit mehreren Personen Schach spielen. Selbst eine Chat-Komponente war implementiert. Selbst wenn kein Spieler am System war, konnte man (ohne das vielleicht zu wissen) gegen ein Schachprogramm spielen, das sogar mit Eliza-ähnlichen Methoden am Chat teilnahm.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/06_Teleschach_Der_Eintrag_2_KOMM_für_Kommunikation_aktivierte_einen_Chat.png" alt="Abb. 6: Teleschach. Der Eintrag ‚2 KOMM.‘ für Kommunikation aktivierte einen Chat.">
  <figcaption>Abb. 6: Teleschach. Der Eintrag ‚2 KOMM.‘ für Kommunikation aktivierte einen Chat.</figcaption>
</figure></center>


Nach all diesen erfreulichen Entwicklungen drängt sich nun die Frage auf, warum BTX in Kombination mit Geräten (Heimcomputern) nicht ein wirklicher Erfolg wurde, sondern dies anderen Systemen vorbehalten blieb, so dass nach 2001 allmählich alle BTX-Systeme eingestellt wurden, in Frankreich 2006 am spätesten. Die Antwort ist nicht für jedes Land gleich. Der relativ große Erfolg in Frankreich beispielsweise führte dazu, dass das WWW dort erst sehr spät eingeführt wurde, was für Frankreich einige Jahre lang sogar nachteilig war.

Im Folgenden eine Schilderung der Situation in Österreich, die in Variationen auch für andere Länder zutrifft. Die BTX-Zentralen waren teure und zunehmend schlecht wartbare bzw. modifizierbare Geräte. Die Strukturierung der Daten in einer einfachen Datenbank über Links war nicht gut genug. Die Protokolle waren zu wenig ausgefeilt, die Benutzbarkeit der Zentralen und der damit verbundenen ‚externen‘ Rechner war schwierig. Aber am schlimmsten waren die Kosten für die Benutzerinnen und Benutzer. Die Geräte konnten zwar recht preiswert von der damaligen Post gemietet und damit auch gratis gewartet werden, aber Telefonortsgespräche in Österreich kosteten pro Stunde ATS 40.-, was vermutlich heute etwa 20 Euro entsprechen würde. Wenn also ein Österreicher bzw. eine Österreicherin täglich 20 Minuten BTX benutzte, dann kosteten die reinen Telefongebühren für das BTX pro Monat zusätzlich 200 Euro. Dies zu einer Zeit, wo man in den USA pro Monat nur einen Pauschalbetrag von etwa 10 Euro für beliebig lange Telefongespräche zahlte.

Es wurde den technisch mit BTX-Beschäftigten, die zunehmend günstigen Zugriff auf das entstehende weltweite Internet hatten, augenscheinlich, dass man auf neue Großrechner (in vielen Fällen unter dem Betriebssystem UNIX), auf bessere Protokolle und auf vernünftige und ohnehin immer mehr verfügbare Personalcomputer zurückgreifen würde müssen.

Von den größeren Bestrebungen seien vor allem drei, die sich fast zeitgleich entwickelten, erwähnt:

- Das Projekt Gopher, das in erster Linie von Mark McCahill an der Universität Minnesota vorangetrieben wurde,
- das Projekt WWW, das eine Vierergruppe am CERN leitete, und
- das Projekt Hyper-G (später Hyperwave), welches auf mehrere Väter wie Ivan Tomek, Fritz Huber, Frank Kappe und den Verfasser selbst zurück geht.

Alle drei Systeme bauten auf dem Internet mit etwas verschiedenen Protokollen auf. Gopher war, im Hinblick auf Endgeräte und Serverkonfigurationen, sehr liberal und unterstützte auch die meisten gängigen Terminals bzw. PCs. Es erlaubte Links, Textsuche und eine hierarchische Gliederung der Daten, war also ein gut durchdachtes System, das 1990 vorgestellt wurde.

Im selben Jahr erschien der erste Zeitschriftenartikel über Hyper-G (Maurer & Tomek, 1990). Hyper-G bot statt der starren hierarchischen Gliederung eine flexiblere DAG-Gliederung (Directed Acyclic Graph) an, darüber hinaus auch Links, eine Suche und vor allem ‚Daten über Daten‘ (die man heute als ‚Metadaten‘ bezeichnen würde und nach denen man auch suchen, aber auch Rechte für Nutzerinnen und Nutzer vergeben kann). Damit kann ein und dasselbe Angebot für verschiedene Benutzerinnen und Benutzer ganz verschieden aussehen. Weitere Datenstrukturen wie Cluster und Sequenzen erleichterten die Datenablagerung und Auffindung. Sämtlich Links waren bidirektional und nicht Teil des Dokuments, d.h., wenn ein Dokument seinen Ort (seine URL) ändert, kann es alle darauf hinweisenden Links auf anderen Servern automatisch korrigieren. Dadurch war in einem Netzwerk von Hyperwave-Servern die Meldung „es gibt diese Seite nicht mehr“ bei einem Klick auf einen Link nicht möglich.

Es ist ein eigentümlicher Zufall, dass im selben Jahr am CERN der Vorschlag gemacht wird, ein System für wissenschaftliche Artikel anzulegen, welche für die ganze Welt über das Internet abrufbar sind. Es ist dabei zu beachten, dass Interaktivität jenseits von Abrufen und E-Mails nicht als wesentlich oder vorrangig betrachtet wurde, denn neben Suchfunktionen würden Links und Menüs für den Zugriff voll ausreichen. Ein Auszug der Originalmail ist in Abbildung 7 zu sehen:

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/07_Der_Vorschlag_eine_erste_Version_eines_vernetzten_Hypertextsystems_zu_implementi.png" alt="Abb. 7: Der Vorschlag, eine erste Version eines vernetzten Hypertextsystems zu implementieren.">
  <figcaption>Abb. 7: Der Vorschlag, eine erste Version eines vernetzten Hypertextsystems zu implementieren.</figcaption>
</figure></center>


Mir erscheint dieses E-Mail darum so wesentlich, weil es belegt, dass nicht Tim Berners-Lee das WWW allein vorantrieb, sondern ein Team, dessen zweitwichtigster Mann Robert Cailliau war, und den Berners-Lee, sobald es bequem erschien, immer ‚vergaß‘ zu erwähnen. Dies und nachfolgende Aktionen von Berners-Lee werden von Insidern als nicht besonders vornehm angesehen und haben Cailliau veranlasst, seine Version in dem Buch „How the Web was Born“ (Gilles & Cailliau, 2000) festzuhalten. Nur wird auch dieses Buch immer wieder verschwiegen. Die Welt hat eben abgestimmt, dass Bernes-Lee der große Erfinder des WWWs ist, und obwohl das nur sehr bedingt die Wahrheit ist, wird es immer mehr zur Wahrheit, da anders lautenden Aussagen immer mehr vergessen werden.

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Mehr zur Abbildung 7, nämlich der gesamte Vorschlag, kann auf https://www.diigo.com/ nachgelesen werden.

</blockquote>

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/04_Die_Geschichte_des_WWW/img/08_Das_Editiersystem_Harmony_in_Hyperwave_mit_einer_viel_mächtigeren_Markupsprache_.png" alt="Abb. 8: Das Editiersystem Harmony in Hyperwave mit einer viel mächtigeren Markupsprache als HTML, die aus Kompatibilitätsgründen aufgegeben werden musste.">
  <figcaption>Abb. 8: Das Editiersystem Harmony in Hyperwave mit einer viel mächtigeren Markupsprache als HTML, die aus Kompatibilitätsgründen aufgegeben werden musste.</figcaption>
</figure></center>


Die drei Systeme WWW, Gopher und Hyperwave laufen 1991 als erste Versionen. Von den Systemen ist das WWW zweifelsohne das einfachste, denn es ist einfach zu installieren und kostenlos. Gopher ist doch deutlich komplexer und dass die Administration der Universität bei den meist ohnehin kostenlosen Lizenzen eingreift, ist bremsend. Hyperwave ist am weitaus mächtigsten, aber auch am kompliziertesten, und obwohl Bildungsinstitutionen das System gratis erhalten, zahlen große Konzerne (für die es als Wissensmanagementsystem fast noch immer eine Geheimwaffe ist) schon größere Beträge an die Firma Hyperwave.com. Abbildung 8 zeigt das mächtige Mehr-Fenster-Editierwerkzeuge ‚Harmony‘ von Hyper-G im Einsatz.
