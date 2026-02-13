<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/zentrale-problematiken-hinsichtlich-webgestutzten-lehrens-und-lernens -->
<!-- slug: zentrale-problematiken-hinsichtlich-webgestutzten-lehrens-und-lernens -->
<!-- filename: 06_Zentrale_Problematiken_hinsichtlich_webgestuetzten_Lehrens_und_Lernens.md -->
<!-- title: Zentrale Problematiken hinsichtlich webgestützten Lehrens und Lernens -->

## Konzeption

Im konkreten Design von webbasiertem Lernen sind nach Arrigo (2005) technologische und methodologische Aspekte zur Sicherstellung der vollständigen Zugänglichkeit von Online-Lernumgebungen und -materialien zu berücksichtigen.

In **methodischer Hinsicht** steht an erster Stelle die Identifizierung der Ansprüche der Nutzergruppe an Barrierefreiheit und in einem zweiten Schritt die Identifizierung der Eigenschaften der Lernobjekte hinsichtlich Barrierefreiheit. Letztere sollten in standardisierten Beschreibungen formalisiert werden, um ein Matching der Lerninhalte mit den bevorzugten Einstellungen der Lernenden zu ermöglichen. Jeschke et al. (2008) empfehlen mittels semantischer Enkodierung die Auszeichnung nicht nur von Inhalten, sondern auch aller inhaltsverbundenen Aspekte, wie etwa der Navigation. Ziel ist es, präsentationsorientierte Informationen für die von den Benutzerinnen und Benutzern verwendeten Technologien zur Verfügung zu stellen, um die Inhalte passend darzustellen. Zur Umsetzung wird von ihnen die modellgetriebene Entwicklung von barrierefreien Lernangeboten, zum Beispiel auf der Basis der Unifying Modeling Language 2 (UML 2), vorgeschlagen.

In **technischer Hinsicht** identifizieren Karampiperis und Sampson (2005) zwei grundsätzliche Aspekte, die es bei der Umsetzung von webbasiertem Lernen zu berücksichtigen gilt: Einerseits die Entwicklung von zugänglichen Lerninhalten und andererseits die Entwicklung von zugänglichen Schnittstellen und Interfaces, um die Inhalte aufrufen zu können. Letzteres beinhaltet auch das Design des Lernmanagementsystems und seine Zugänglichkeit. Technologisch gesehen sind Webseiten die am häufigsten genutzte Möglichkeit, Informationen und webbasierte Lernmaterialien im Internet zur Verfügung zu stellen. Trotz WAI-Richtlinien, Design-for-All, Universal-Design-Prinzipien, ISO-Standards und Verordnungen beziehungsweise Richtlinien sind viele Webseiten aber noch immer unzugänglich für Menschen mit Behinderung (Arrigo, 2005).

## Lernplattformen und Lernumgebungen

Entwickler/innen von Lernplattformen und Lernumgebungen haben in vielen Fällen in den letzten Jahren große Anstrengungen hinsichtlich der Barrierefreiheit der von ihnen betreuten Produkte unternommen. Das Projekt VIP-Learn hat Leitlinien zur Begutachtung von Lernmanagement-Software erstellt, die für eine erste Begutachtung von Lernplattformen herangezogen werden können (URL: [http://www.bfw-dueren.de/projekte/abgeschlosseneprojekte/e-learn-vip/projekt-verffentlichungen/c4ea\_gl\_lms\_de.pdf](http://www.bfw-dueren.de/projekte/abgeschlosseneprojekte/e-learn-vip/projekt-verffentlichungen/c4ea_gl_lms_de.pdf)).

## Spezialfälle bei bestimmten Dateiformaten / Multimedia

Um die Vorteile von **multimedialen Lernelementen** auch für Menschen mit Behinderung zugänglich zu machen, sind Zugänglichkeitsüberlegungen schon beim Design und der Implementierung von multimedialen Inhalten zu berücksichtigen. CANnect, ein kanadisches Konsortium von Schulen und Philanthropen, identifiziert vier Aspekte, welche die Zugänglichkeit von multimedialen Inhalten negativ beeinflussen: unzugängliche Formate, fehlende Transkription von Audioinhalten, fehlende synchronisierte Untertitelung für Videodateien und fehlende Audiobeschreibung von Videodateien (CANnect, 2010). Darüber hinaus muss die Steuerung der Audio- und Videowiedergabe mittels Tastatur möglich und der Zugriff sowie die Verständlichkeit für Personen, die einen Screenreader verwenden, gegeben sein. Als Alternative zu kommerziellen Formaten bietet sich die Synchronized Multimedia Integration Language (SMIL) an. SMIL ist ein auf XML basierender, vom W3C entwickelter Standard für eine Auszeichnungssprache für zeitsynchronisierte, multimediale Inhalte und ermöglicht die Einbindung und Steuerung von Multimedia-Elementen wie Audio, Video, Text und Grafik in Webseiten.

CANnect nimmt einen klaren Standpunkt zu den folgenden Technologien ein: **Flash, Silverlight und JavaFX** sind Plattformen für die Entwicklung von Rich Internet Applications (RIAs) und beim derzeitigen Stand keine geeigneten Instrumente, um Textinhalte webbasiert anzubieten. Keine dieser Plattformen verfügt über die Möglichkeiten von HTML, Inhalte zu strukturieren und barrierefrei darzustellen (URL: [http://projectone.cannect.org/advice/non-html-dynamic.php](http://projectone.cannect.org/advice/non-html-dynamic.php)).

Die Konzeption des **Portable Document Format** (PDF), das Erscheinungsbild eines Dokuments auf allen Plattformen gleich aussehen zu lassen, widerspricht einem wichtigen Element von Barrierefreiheit: Die Darstellung von Inhalten sollte von Nutzerinnen und Nutzern an ihre individuellen Bedürfnisse angepasst werden können. Es empfiehlt sich vor der Erstellung eines PDF-Dokuments zu überlegen, ob nicht ein anderes Format, beziehungsweise bei Verwendung im Internet XML die bessere Alternative ist. Falls das PDF-Format verwendet werden muss, sollte ‚tagged PDF’ verwendet werden (erst dadurch wird das Dokument besser zugänglich), beziehungsweise eine Nachbesserung mit dem Softwareprogramm Adobe Acrobat Pro vorgenommen werden. Gute Ergebnisse hinsichtlich der Zugänglichkeit von PDF-Dokumenten lassen sich beispielsweise bei der Gestaltung des Dokuments in OpenOffice mit korrekter Strukturauszeichnung und dem PDF-Export erzielen. Die Verwendung von Lesezeichen fördert darüber hinaus die Navigation mit der Tastatur.

### In der Praxis: Prinzipien und Leitlinien der Web Content Accessibility Guidelines 2.0

</blockquote>

Vorbemerkung: Übersetzung der folgenden Prinzipien und Leitlinien der Web Content Accessibility Guidelines 2.0 ([http://www.barrierefreies-webdesign.de/wcag2/index.html](http://www.barrierefreies-webdesign.de/wcag2/index.html))

**Prinzip 1: Wahrnehmbarkeit**

Mit dem Prinzip Wahrnehmbarkeit soll sichergestellt werden, dass alle Funktionen und Informationen so präsentiert werden, dass sie von jeder Nutzerin und jedem Nutzer wahrgenommen werden können.

Konkret bedeutet das: Stellen Sie Textalternativen für alle Nicht-Text-Inhalte zur Verfügung, so dass diese in andere vom Benutzer benötigte Formen geändert werden können, wie zum Beispiel Großschrift, Braille, Symbole oder einfachere Sprache. Stellen Sie Alternativen für zeitbasierte Medien zur Verfügung. Erstellen Sie Inhalte, die auf verschiedene Arten dargestellt werden können (zum Beispiel anderes Layout), ohne dass Informationen oder Struktur verloren gehen.

Praktische Anwendungsbeispiele: Keine rein grafischen Navigationselemente verwenden, schriftliche Alternative zu allen akustischen Geräuschen anbieten, skalierbare Schriftgrößen, Möglichkeit der individuellen Farbeinstellungen, ausreichender Kontrast, zum Beispiel von Text und Hintergrundfarbe, keine Information allein durch Farbwechsel transportieren.

**Prinzip 2: Bedienbarkeit**

Zur Sicherstellung der Bedienbarkeit müssen die Interaktionselemente der Anwendung von jeder Nutzerin und jedem Nutzer bedienbar sein.

Richtlinien: Sorgen Sie dafür, dass alle Funktionalitäten per Tastatur zugänglich sind. Geben Sie den Benutzer/innen ausreichend Zeit, Inhalte zu lesen und zu benutzen. Gestalten Sie Inhalte nicht auf Arten, von denen bekannt ist, dass sie zu Anfällen führen. Stellen Sie Mittel zur Verfügung, um Benutzer dabei zu unterstützen zu navigieren, Inhalte zu finden und zu bestimmen, wo sie sich befinden.

Praktische Anwendungsbeispiele: Für die Verwendung sollen keine speziellen Eingabegeräte benötigt werden. Alle Funktionen sind über die Tastatur (ohne Maus) steuerbar. Es gibt keine Zeitbeschränkungen. Die Navigationsbereiche sind ausreichend groß bzw. weit genug auseinander positioniert. Zur Bedienung sollten keine bewegten Elemente (zum Beispiel Flash-Animationen) verwendet werden.

**Prinzip 3: Verständlichkeit**

Das Prinzip Verständlichkeit besagt, dass in einer Webseite die Inhalte so einfach wie möglich angeboten werden sollen. Zusätzlich sollen diese in einer intuitiv erfassbaren Struktur, in der die Orientierung leicht fällt, eingebunden werden.

Richtlinien: Machen Sie Inhalte lesbar und verständlich. Sorgen Sie dafür, dass Webseiten vorhersehbar aussehen und funktionieren. Helfen Sie den Benutzern dabei, Fehler zu vermeiden und zu korrigieren.

Praktische Anwendungsbeispiele: Komplexität der Inhalte an den Nutzer/innen ausrichten – möglichst ‚einfache’ Sprache verwenden. Visuelles Rauschen, zum Beispiel durch Farben, Ausrufezeichen, bestimmte Schrifttypen, vermeiden. Auf die wesentlichen Funktionen beschränken sowie auf umfangreiche Verwendung von Hintergrundinformationen und Zusatzfunktionen verzichten. Auf Fachausdrücke, Jargon, Anglizismen verzichten. Auf übersichtlichen Satzbau achten. Intuitive, logische Strukturierung der Inhalte oder der (Lern-)Umgebung vorsehen. Suchfunktion und Verlinkungen sinnvoll einsetzen. Symbole und Grafiken unterstützend einsetzen. Gegebenenfalls Gebärdensprachvideos anbieten.

**Prinzip 4: Robustheit**

Inhalte müssen robust genug sein, damit sie zuverlässig von einer großen Auswahl an Benutzeragenten einschließlich assistierender Techniken interpretiert werden können.

Richtlinie: Maximieren Sie die Kompatibilität mit aktuellen und zukünftigen Benutzeragenten, einschließlich assistierender Techniken.

Praktische Anwendungsbeispiele: Interoperabilität und Kompatibilität zu gängigen Produkten (zum Beispiel Vorlese- oder Vergrößerungssoftware) berücksichtigen. In der Planungsphase, zum Beispiel von Lernszenarien oder Online-Seminaren auf möglichen Zugang für assistive Technologien achten. Auf Weiterentwicklungen von Technologien achten, zum Beispiel hat sich die Zugänglichkeit von einigen Lernmanagementsystemen in den letzten Jahren stark verbessert.

Durch die Umsetzung des ISO-Standards ‚ISO 14289-1. Document management applications – Electronic document file format enhancement for accessibility – Part 1: Use of ISO 32000-1 (PDF/UA-1)’ in Softwareprodukten soll es Anwender/innen in Zukunft noch leichter möglich sein, zugängliche PDF-Dokumente zu erstellen. PDF/UA-1 definiert Anforderungen an barrierefreie PDF-Dokumente, die von Softwareherstellerinnen und -herstellern, Behörden und Unternehmen in zunehmend stärkerem Maß angewandt und in Software zur Erstellung von PDF-Dokumenten einfließen werden ([http://www.access-for-all.ch/en/accessibility/accessible-pdf/pdf-ua.html](http://www.access-for-all.ch/en/accessibility/accessible-pdf/pdf-ua.html)).

### In der Praxis: Accessibility Check

Mit dem PDF Accessibility Checker (PAC 2) können Sie PDF-Dateien rasch bezüglich Barrierefreiheit testen: [http://www.access-for-all.ch/ch/pdf-werkstatt/pdf-accessibility-checker-pac.html](http://www.access-for-all.ch/ch/pdf-werkstatt/pdf-accessibility-checker-pac.html).

</blockquote>
