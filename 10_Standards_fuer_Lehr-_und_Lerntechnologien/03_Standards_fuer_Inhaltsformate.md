<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/standards-fur-inhaltsformate -->
<!-- slug: standards-fur-inhaltsformate -->
<!-- filename: 03_Standards_fuer_Inhaltsformate.md -->
<!-- title: Standards für Inhaltsformate -->

Nicht nur für Metadaten zur Beschreibung von Lehr- und Lernressourcen sind Standards notwendig, sondern auch für die technische Repräsentation der Lehr- und Lernressourcen. Ohne die Definition und Einhaltung solcher Standards ist es nur eingeschränkt möglich, Ressourcen mit einem Autorensystem zu erstellen und über verschiedene Lernmanagementsysteme den Lernenden zur Verfügung zu stellen bzw. Ressourcen in verschiedenen Informationssystemen für Lehren und Lernen zu verwenden.

## Sharable Content Object Reference Model

Das Sharable Content Object Reference Model (SCORM) ist eine Sammlung von Standards zur Beschreibung von web-basierten Lehr- und Lernressourcen, also solchen Ressourcen, die den Lernenden im Web in der Regel über Lernmanagementsysteme zur Verfügung gestellt werden. Diese Sammlung wurde von der Advanced Distributed Learning Initiative veröffentlicht. Aktuell liegt der Standard in der Version 2004 vor (ADL, 2004); in Informationssystemen häufig realisiert ist zumeist die Version 1.2 (ADL, 2002).

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/10_Standards_fuer_Lehr-_und_Lerntechnologien/img/04_Bestandteile_des_SCORMStandards.jpg" alt="Abb. 4: Bestandteile des SCORM-Standards">
  <figcaption>Abb. 4: Bestandteile des SCORM-Standards</figcaption>
</figure></center>


SCORM besteht, wie in Abbildung 4 gezeigt, aus unterschiedlichen Teilen. Teil I gibt einen Überblick über den Standard und erläutert die Verwendung der anderen Teile. Teil II, das *Content Aggregation Model* (CAM), spezifiziert das Datenmodell (basierend auf XML) (#webtech), in welchem die Ressourcen zu erstellen, zu strukturieren, zusammenzufassen und mit Metadaten zu beschreiben sind. Als Metadatenformat wird wiederum LOM verwendet. Eine Lernressource nach SCORM kann letztendlich als gepackte Datei (ZIP-Datei) gespeichert und so zwischen verschiedenen Informationssystemen ausgetauscht werden.

Der dritte Teil mit Titel *Runtime Environment* (RTE) definiert ein Protokoll, welches Lernmanagementsysteme (#infosysteme) verwendet, um den Prozess des Lernens einzelner Lernenden mit einer nach dem CAM beschriebenen Lernressource zu dokumentieren. So speichert das Lernmanagementsystem unter anderem den Lernfortschritt, also zum Beispiel welche Seiten einer Lernressource ein/e Lernende/r bereits betrachtet hat oder welche Aufgaben er/sie erfolgreich bearbeitet hat. Teil IV, *Sequencing and Navigation* (SN), erlaubt es, beim Entwurf von Lernressourcen Regeln zu spezifizieren, mittels denen abhängig vom individuellen Lernergebnis innerhalb von Lernressourcen aber auch zwischen verschiedenen Lerneinheiten navigiert wird. Damit soll eine Anpassung der Präsentation einer Lernressource an den individuellen Lernfortschritt erreicht werden. SN ist erst seit der Version 2004 Bestandteil von SCORM und findet bisher kaum Verwendung.

## Question & Test Interoperability Specification

Wie das Content Aggregation Model von SCORM, so definiert auch die *Question & Test Interoperability Specification* (QTI) ein Datenmodell speziell für Testitems, das heißt Aufgaben, die den Lernenden entweder während der Bearbeitung einer Lerneinheit oder in einer elektronischen Prüfung gestellt werden (#assessment). QTI liegt aktuell in der Version 2.1 (IMS Global, 2012) vor. Die heute in Informationssystemen verbreitetste Version ist 1.2.

QTI erlaubt die Beschreibung von Aufgaben verschiedenster Typen. Über Einfach- und Mehrfachauswahl hinaus sind dies beispielsweise Zuordnungsaufgaben, Reihenfolgeaufgaben, Lückentexte, Freitexte oder die Bestimmung von Textteilmengen. In QTI lassen sich aber nicht nur Aufgaben definieren, sondern es lässt sich auch detailliert spezifizieren, wie und wie viele Punkte vergeben werden und wie das Informationssystem nach einer richtigen bzw. falschen Antwort agieren soll. Die Aufgaben werden, wie in Abbildung 5 dargestellt, mittels eines Autorenwerkzeuges erstellt. Mehrere Aufgaben lassen sich zu einem Test kombinieren. Ein solcher Test kann dann wiederum in eine Lerneinheit integriert werden oder in einem Prüfungssystem (E-Assessment-System) zur Durchführung einer Prüfung genutzt werden. Die Erstellung von Aufgaben und Test gehört häufig auch zu den Funktionalitäten eines Lernmanagementsystems oder eines Prüfungssystems, wobei erstere oftmals nur eine beschränkte Anzahl von Aufgabentypen unterstützen.

<center><figure>
  <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/10_Standards_fuer_Lehr-_und_Lerntechnologien/img/05_An_der_Erstellung_und_Nutzung_von_Aufgaben_und_Tests_beteiligte_Systeme.jpg" alt="Abb. 5: An der Erstellung und Nutzung von Aufgaben und Tests beteiligte Systeme">
  <figcaption>Abb. 5: An der Erstellung und Nutzung von Aufgaben und Tests beteiligte Systeme</figcaption>
</figure></center>


<blockquote style="background: #FFEBEE; border-left: 10px solid #F44336">

### ?

Erstellen Sie in dem auf diigo.com verlinkten onyx-Editor eine eigene Aufgabe nach dem QTI-Standard. Bei der Bearbeitung der Aufgabe werden Sie feststellen, wie vielen Möglichkeiten QTI bietet und wie aufwändig die Erstellung einer Aufgabe sein kann.

</blockquote>
