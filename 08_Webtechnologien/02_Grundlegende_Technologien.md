<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/grundlegende-technologien -->
<!-- slug: grundlegende-technologien -->
<!-- filename: 02_Grundlegende_Technologien.md -->
<!-- title: Grundlegende Technologien -->

Das Internet ist eine weltweite Verknüpfung von Datennetzen, welche Ende der 1960er Jahre in den USA von der vom DARPA (Defense Advanced Research Projects Agency) initiiert wurde und aus dem daraus entstandenen ARPANET (Advanced Research Projects Agency Network) hervorging (Cerf et al., 2012).

<blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">

### !

Der Begriff Internet als solcher bezeichnet das entstehende „interconnected network“ zwischen unabhängigen und weltweit verteilten Computernetzen.

</blockquote>

Die Kommunikation in einem Computernetzwerk wird über **Protokolle** geregelt. Ein Protokoll ist eine Regelvorschrift, welche den Datenaustausch und die Kommunikation zwischen Computern detailliert beschreibt. In der Netzwerkkommunikation hat sich eine Aufteilung der Verantwortung auf einzelne aufeinander aufbauende Protokolle als sinnvoll erwiesen. Diese Aufteilung kann man über das OSI-Schichtenmodell (Open System Interconnection) der internationalen Standardisierungsgesellschaft ISO (International Standardization Organisation), in dem Protokolle einer Ebene nur jeweils mit Protokollen der benachbarten Ebenen in Kontakt treten müssen, einheitlich beschreiben.

Die Ebenen des OSI-Schichtenmodells (siehe Tabelle 1) beschreiben die Kommunikation in verschiedenen Abstraktionsstufen. So beschäftigt sich die unterste Schicht (1) mit der physikalischen Übertragung, während sich die oberste Schicht (7) mit Anwendungen auseinandersetzt. Grob werden diese Schichten in anwendungs- und transportorientierte Schichten unterteilt. In den anwendungsorientierten Schichten finden sich Protokolle, welche dieeigentliche Benutzer/innen-Interaktion in (Web-)Anwendungen beschreibt. Die transportorientierten Schichten bilden die eigentlichen „Schienen“ des darunterliegenden Datenverkehrs. Im Rahmen dieses Kapitels werden wir uns nur mit anwendungsorientierten Protokollen beschäftigen. Die Kommunikation vieler Programme auf der Anwendungsschicht erfolgt nach dem Client-Server-Prinzip (siehe #infosysteme).

| | **Schicht** | **Ebene** | **Protokolle** |
| --- | --- | --- | --- |
| 7 | Anwendungsschicht | Anwendungsorientierte Schichten | HTTP(S) |
| 6 | Darstellungsschicht | FTP |
| 5 | Kommunikationsschicht | POP, SMTP |
| 4 | Transportschicht | Transportorientierte Schichten | TCP UDP |
| 3 | Vermittlungsschicht | IP |
| 2 | Sicherungsschicht | Ethernet |
| 1 | Physikalische Schicht | |

Tab. 1: OSI-Schichtenmodell

Basierend auf dem Internet als Verbindung unterschiedlicher Computernetze ermöglichen diverse Protokolle den Zugriff auf eine Vielzahl von Anwendungen. Die wohl prominenteste dieser Anwendungen ist das World Wide Web.
