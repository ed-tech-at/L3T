<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/lernen-mit-informationssystemen-zusammenspiel-und-problempunkte -->
<!-- slug: lernen-mit-informationssystemen-zusammenspiel-und-problempunkte -->
<!-- filename: 05_Lernen_mit_Informationssystemen_Zusammenspiel_und_Problempunkte.md -->
<!-- title: Lernen mit Informationssystemen: Zusammenspiel und Problempunkte -->

Bei der Auswahl von Informationssystemen zum Lernen und Lehren müssen diese nicht nur einzeln einer Reihe von Anforderungen genügen, es sollte auch darauf geachtet werden, dass sie problemlos zusammen eingesetzt werden können. So sollte sich das Datenformat, das mit dem Autorentool exportiert wird, problemlos in das Lernmanagementsystem integrieren lassen. Inhalte dürfen nicht verzerrt dargestellt werden, nur weil das LMS eine bestimmte Fenstergröße dafür vorsieht. Ebenso sollte die Bewertung von Tests, die mit einem Autorenwerkzeug erstellt und beispielsweise als SCORM-Paket exportiert wurden, auch von den Bewertungswerkzeugen des Lernmanagementsystems verarbeitet werden.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/07_Informationssysteme/img/07_Zusammenspiel_von_Autorenystemen_und_Lernmanagementsystem.png" alt="Abb. 7: Zusammenspiel von Autorenystemen und Lernmanagementsystem">
  <figcaption>Abb. 7: Zusammenspiel von Autorenystemen und Lernmanagementsystem</figcaption>
</figure></center>


### In der Praxis: Praxisbeispiel eines laufenden Lernmanagementsystems

An der TU Graz (Ebner, 2008) wird die Open-Source-Software WBT-Master unter dem Namen TeachCenter eingesetzt (siehe Abbildung 8). Es handelt sich hier um eine Client-Server-Architektur, basierend auf einer AJAX-Lösung, als Programmiersprache kommt Java/JavaScript zum Einsatz. AJAX (Akronym für die WorteAsynchronousJavaScriptand XML) wird verwendet, wenn es darum geht, selektiv („nach und nach“, „je nach Bedarf“) Daten an den Browser zu senden, was mit klassischen Technologien immer ein Neuladen der gesamten Webseite und den damit verbundenen Zeitaufwand erfordern würde. DerVorteil dieser Architektur ist die Reduzierung der Datenmenge der Serverantworten (durch die Vorselektion) und damit zwangsläufig von Ladezeiten sowie die verstärkte Nutzung der Clients (Internetbrowser der jeweiligen Nutzer/innen). Besonders bei einem großen System mit hohen Nutzer/innen-Zahlen und deren parallele Aktivitäten ist dies von entscheidender Bedeutung. </blockquote>

An der TU Graz werden in etwa 20.000 Nutzerinnen und Nutzer verwaltet, die einen Datenverkehr von weit über 50GB pro Tag verursachen. Im Durchschnitt sind in den Kernzeiten 400 bis 500 Nutzer/innen parallel am System aktiv. Bei diesen Zahlen wird ersichtlich, dass die Performance ein wesentlicher Faktor eines LMS-Systems ist, da die Voraussetzung von zufriedenen Nutzer/innen von E-Learning-Inhalten akzeptable Reaktionszeiten des LMS sind (&lt;1 Sekunde nach einem Klick).

Das TeachCenter der TU Graz verwendet, wie die Mehrzahl der anderen Lernmanagementsysteme auch, eine Client-Server Architektur.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/07_Informationssysteme/img/08_Screenshot_einer_Kursseite_im_TeachCenter.png" alt="Abb. 8: Screenshot einer Kursseite im TeachCenter">
  <figcaption>Abb. 8: Screenshot einer Kursseite im TeachCenter</figcaption>
</figure></center>


Erstes, nachstehendes, Element wird ans Ende der vorherigen Seite gestellt

### In der Praxis: Überlegungen bei der Entscheidung für ein Lernmanagementsystem

Die folgende Beschreibung von Lernmanagementsystemen ist fiktiv, soll jedoch die Abwägung von Vor- und Nachteilen in der Praxis verdeutlichen. </blockquote>

**1. LernenMitSpaß – Die Open-Source-Lösung**  
Das LMS kann kostenlos heruntergeladen und selbst installiert werden. Das Basispaket bietet eine einfache Kurs- und Nutzer/innen-Verwaltung. Über eine Reihe von Plug-Ins, die von der Benutzer/innen-Community von LernenMitSpaß entwickelt wurden, können weitere Funktionalitäten hinzugefügt werden, wie beispielsweise ein komplexes Rollenmanagement, die Integration von Tests oder Statistiken zu Lernerfolgen. Darüber hinaus besteht durch die Open-Source-Lizenz die Möglichkeit, selbst Erweiterungen zu entwickeln.

**Vorteile**: sehr kostengünstig, erweiterbar, kann grundsätzlich an alle Bedürfnisse angepasst werden, Installation und Betrieb durch das Unternehmen selbst

**Nachteile**: eventuell zusätzlicher Personalbedarf, durch Anpassungen und Neuentwicklung von Erweiterungen durch Personalkosten eventuell sehr teuer </blockquote>

**2. LernenMitSystem– Die Standardlösung**  
Das LMS wird kommerziell angeboten und laufend weiterentwickelt. Es beinhaltet ein Kurs- und Nutzer/innen-Management, erlaubt die Erstellung und Auswertung von Tests und liefert kleine Statistiken zum Lernfortschritt der Mitarbeiterin bzw. des Mitarbeiters (Lernzeit, Durchschnitt der Lernergebnisse). Für die Kommunikation können E-Mails und Kursforen benutzt werden. Der Zugriff erfolgt über ein eigenes Programm, das auf dem Rechner der Mitarbeiter/innen installiert werden muss. Das LMS-Unternehmen übernimmt die Installation und Pflege des LMS auf einem Server Ihrer Firma, sowie kleine Anpassungen (zum Beispiel Verwendung des Firmenlogos und der Firmenfarben). Der Kaufpreis des LMS inkl. Installation, Einrichtung, 10 h Support und 1.000 Nutzer/innen-Lizenzen für die Zugriffsprogramme beträgt 15.000 Euro. Weitere Nutzer/innen-Lizenzen, Anpassungen, Supportstunden und Schulungen für Mitarbeiter/innen können bei Bedarf hinzugekauft werden. Hinzu kommen außerdem 1.500 Euro im Jahr für Wartung und Updates.

**Vorteile**: DieEinrichtung erfolgt durch ein kompetentesUnternehmen, es kann also ein ausreichender Funktionsumfang erwartet werden, das heißtbeispielsweise Skalierbarkeit, Zugriff über eigenes Programm (eventuell relevant für Firmen mit eingeschränkten Internetzugriff, da keine mühsame Freischaltung einzelner Seiten nötig ist, Daten auf dem eigenem Server liegen), einmaliger Kaufpreis etc.

**Nachteile**: Je nach Budget ist es eventuell zu teuer in der Anschaffung, je nach Anforderungskriterien besteht weiterer Anpassungsbedarf, fallen weitere Anschaffungskosten für einen eigenen Server an;dabei sind Anpassungen und Supportstunden schwer abschätzbar.

**3. LernenMitStrategie– Die Profi-Lösung**  
Das LMS wird kommerziell angeboten und laufend weiterentwickelt. Im Zentrum steht ein komplexes Kompetenzmanagement, dass die Planung der Weiterbildungsangebote für alle Mitarbeiter/innen an vorher definierten Personalentwicklungsplänen ausrichtet. Über Schnittstellen kann es an Personaldatenbanken und Dokumentenmanagementsysteme angebunden werden. Das LMS-Unternehmen übernimmt die Installation und Pflege des LMS auf einem seiner eigenen Server sowie besprochene Anpassungen, die Abbildung Ihrer Unternehmensstruktur auf die Nutzer/innen-Verwaltung und den Import der bereits bei Ihnen verfügbaren Personalentwicklungspläne und Lerninhalte. Der Mietpreis des LMS inkl. Installation, Einrichtung, Support und 1.000 Nutzer/innen-Accounts für den webbasierten Zugriff beträgt 40.000 Euro im Jahr. Weitere Nutzer/innen-Accounts, Anpassungen und Schulungen für Mitarbeiter/innen können bei Bedarf hinzugekauft werden.

**Vorteile**: Vollbetrieb durch kompetentes Unternehmen, individuell angepasster Funktionsumfang, skalierbar, hochkomplexe Nutzer/innen- und Lernprozessverwaltung

**Nachteile**: Jahresmiete, Daten auf fremden Server, eventuell für das Unternehmen zu komplex

Wie Sie gesehen haben, ist die Entscheidung zwischen Open-Source und kommerziellen Produkten immer eine individuelle Antwort auf eine offene Fragestellung und muss auf die einzelne Situation angepasst werden.
