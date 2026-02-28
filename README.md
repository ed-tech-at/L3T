# 📖 L3T Backend – Dokumentation

## 📌 Überblick

**Zugang zum Lehrbuch im Frontend: [L3T-Bookstack](https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien)**


Dieses Repository dient als Backend für das Buch **„L3T – Lehrbuch für Lernen und Lehren mit Technologien“**. Änderungen werden kollaborativ über dieses Repo verwaltet und nach einer manuellen Prüfung ins [L3T-BookStack](https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien) synchronisiert.

Aktuell ist das Lehrbuch sehr veraltet und muss dringend aktualisiert werden. Änderungen von jeder Person sind jederzeit willkommen. Unter Einhaltung der geforderten Konventionen (siehe weiter unten) werden Änderungen gerne in das Lehrbuch aufgenommen.

## 🛠 Struktur im Repository

Das Repo folgt einer gewissen Struktur und sieht wie folgt aus:

- Jedes Kapitel hat einen eigenen Ordner mit

	- Einem File `00_*.md`, welches die Inhalte des Kapitels inkl. Beschreibung beinhaltet.
	- Diverse fortlaufend nummerierte Markdown-Files (`*.md`), welche die einzelnen Seiten eines Kapitels bilden.
	- Einem Literaturverzeichnis (`99_Literatur.md`) mit Quellenangaben.
    - Einem `img`-Ordner für Bilder.
- Der Ordner `00_L3T` enthält Buch-Administrationsdateien und darf nicht geändert werden.

## 📝 Richtlinien zur Bearbeitung

Du möchtest aktiv am **L3T**-Lehrbuch mitwirken? Sehr gerne! Das Lehrbuch als öffentliche Bildungsressource (OER) lebt von der kollaborativen Zusammenarbeit und freut sich über regelmäßige Unterstützung von freiwilligen Personen, die das Lehrbuch aktuell halten.

Beachte bitte folgende Richtlinien, um die Qualität der Inhalte im Lehrbuch aufrecht zu erhalten:

### 🔹 GitHub Workflow

> 💡 **Tipp**: Falls du mit der Verwendung von Git bzw. Github nicht vertraut bist, sieh dir z.B. [diese Einführung](https://www.datacamp.com/de/tutorial/github-and-git-tutorial-for-beginners) an!

1. **Forke das Repository** [hier](https://github.com/ed-tech-at/L3T/fork) *(eigener GitHub-Account erforderlich!).*
2. Nimm Änderungen an den Markdown-Dateien im eigenen Fork vor.
3. Erstelle einen **Pull-Request (PR)**, um deine Änderungen zur Überprüfung einzureichen.
    > 💡 **Tipp**: Falls du unsicher bist, wie man einen PR erstellt, sieh dir [diese Anleitung](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) an!

    - Beschreibe im Pull-Request in Kürze, welche Änderungen du vorgenommen hast.
    - Gib ggf. auch an, welche Issues diese Änderung behebt.
4. Die Inhalte werden geprüft:
    - Automatisiert: Beim Erstellen werden die vorgenommenen Änderungen automatisch auf viele typische Fehlerquellen überprüft (Details siehe weiter unten).
        - Fehler müssen behoben werden, damit der PR akzeptiert wird.
        - Warnungen sollten behoben werden, blockieren den PR aber nicht.
    - Manuell: Eine weitere manuelle Prüfung der Änderungen wird von den Administratoren bzw. Autoren vorgenommen.
        - Falls in Ordnung: PR wird akzeptiert und ins [L3T-BookStack](https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien) übertragen. 
        - Falls weitere Anpassungen nötig: Wird mit Kommentar zurückgewiesen.

### 🔹 Automatische Überprüfung

Bei jedem Pull-Request werden **automatische Checks** durchgeführt, die häufige Fehler erkennen:

**✅ Was wird geprüft:**
- **Metadaten:** filename, title, authors, tags, revisors, slugs, url (Format & Vollständigkeit)
- **Bilder:** GitHub-URLs, alt-Tags & figcaptions (müssen identisch sein!), Zentrierung
- **Blockquotes:** Korrekte Farben und Stil (blau/rot/grün für verschiedene Typen)
- **Figurennummerierung:** Fortlaufende Nummerierung (Abb. 1, 2, 3...) pro Kapitel
- **APA-Zitierungen:** Fehlende Jahre, fehlerhafte URLs, Zugriffsdaten, Einheitlichkeit
- **Dateistruktur:** Nur erlaubte Dateitypen (.md, Bilder), korrekte Ordnerstruktur
- **Markdown-Links:** Fehlende oder fehlerhafte Links
- **Tabellen:** Konsistente Spaltenanzahl

**⚠️ Fehler vs. Warnungen:**
- **Fehler (rot):** Müssen behoben werden, bevor der PR akzeptiert werden kann
- **Warnungen (gelb):** Hinweise auf mögliche Probleme, blockieren den PR nicht

Die Check-Ergebnisse erscheinen direkt im PR unter "Checks" mit detaillierter Auflistung aller gefundenen Probleme.

### 🔹 Formatierung & Inhalt

- **Markdown** wird für die meisten Inhalte genutzt. Einige Elemente (Bilder, Blockquotes) müssen jedoch als HTML eingebunden werden.

    > 💡 **Tipp**: Falls du neu in Markdown bist, schau dir z.B. [diese Einführung](https://www.markdownguide.org/) an!

- **Metadaten:** 
    - Jede Markdown-Datei enthält **Header-Kommentare** (`<!-- [...] -->`):
    
        - `filename`: Muss  **genau**  dem realen Dateinamen entsprechen und sollte nur - wenn unbedingt notwendig - geändert werden. Der Dateiname darf bei Änderung **keine Lehrzeichen**, **Umlaute**, **Sonderzeichen**, o.ä. beinhalten!
        - `title`: Titel des Kapitel bzw. der Unterseite. Darf ohne Einschränkungen angepasst werden.
        - Beispiel:
            ```
            <!-- filename: 01_L3T_-_die_zweite_Auflage.md -->
            <!-- title: L3T – die zweite Auflage -->
            ```
    -  Kapitel-Files (``00_*.md``) enthalten zusätzliche Infos:
    
        - `slug`: Eindeutige URL-Kennung für die Seite (wird automatisch vom Sync-Script generiert und sollte nicht manuell geändert werden, bzw. bei Sync automatisch überschrieben).
        - `URL`: Vollständige URL zur Seite in Bookstack (wird automatisch vom Sync-Script generiert und sollte nicht manuell geändert werden, bzw. bei Sync automatisch überschrieben).
        - `tags`: Tags für das Kapitel, scheinen in Bookstack in der Seitenleiste auf. Dürfen ohne Einschränkungen angepasst werden.
        - `authors`: Autoren des jeweiligen Kapitels. Kommagetrennte Liste.
        - `revisors` (optional): Überarbeiter des Kapitels. Kommagetrennte Liste. *Füge deinen eigenen Namen hinzu, wenn du Änderungen am Kapitel vorgenommen hast!*
        - Beispiel: 
            ```
            <!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/chapter/einleitung -->
            <!-- slug: einleitung -->
            <!-- filename: 00_Einleitung.md -->
            <!-- title: Einleitung -->
            
            <!-- tags: #einleitung,#einfuehrung,#l3t -->
            <!-- authors: Martin Ebner, Sandra Schön, Jennifer Frey -->
            <!-- revisors: Bernd Grabner --> 
            ```
        
- **Bilder:** 
    - Gehören vorab in den `img`-Ordner des Kapitels hochgeladen.
    - Werden im **HTML-Format** eingebunden (für Bildunterschriften).
    - Sind zentriert innerhalb einer Figure (`<center><figure> [...] </figure></center>`) mit `alt`-Tag und Bildunterschrift `figcaption`.
        - **Pfad** - RAW-GitHub-URL: `https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/<Kapitel>/img/<Bilddatei>`
        - `alt`-Tag und  `figcaption` sollen gleich sein und eine fortlaufende Nummer beinhalten.
    - Zum Beispiel:
        ```
        <center>
        <figure>
          <img src="https://raw.githubusercontent.com/ed-tech-at/L3T/refs/heads/main/03_Von_der_Kreidetafel_zum_Tablet/img/05_Epiprojektor.jpg" alt="Abb. 5: Epiprojektor">
          <figcaption>Abb. 5: Epiprojektor</figcaption>
        </figure>
        </center>
        ```
    
- **Blockquotes:** 
    - Um Wichtiges hervorzuheben, zusätzliche Informationen zu geben, Übungen anzubieten oder praxisnahe Beispiele zu zeigen. 
    - Werden im **HTML-Format** angegeben.
    - Folgen demselben Format mit unterschiedlichen Farben je nach Typ
         ```
        <blockquote style="background: <HEX-Farbcode>; border-left: 10px solid <HEX-Farbcode>"> [...] </blockquote>`
        ```
    - Es gibt 3 Arten:
    
        |               | `!`                                           | `?`                 | `In der Praxis`     |
        | ------------: | :-------------------------------------------: | :-----------------: | :-----------------: |
        | Verwendet für | **Wichtiges** & **zusätzliche Informationen** | **Übungen**         | **Praxisbeispiele** |
        | Farbe         | 🟦 **Blau**                                   | 🟥 **Rot**          | 🟩 **Grün**         |
        | Hintergrund   | `#B3E5FC`                                     | `#FFEBEE`           | `#E8F5E9`           |
        | Akzent        | `#039BE5`                                     | `#F44336`           | `#4CAF50`           |

    - Beispiel
        ```
        <blockquote style="background: #B3E5FC; border-left: 10px solid #039BE5">
        
        ### !
        
        Als Vorteil der Kreidetafel [...] angepasst ist.
        
        </blockquote>
        ```
            
- **Tabellen:**
    - Werden im **Markdown-Format** geschrieben.
    - Mögliche (Darstellungs-)Fehler könnten durch die Datenübernahme entstanden sein und sollten manuell korrigiert werden.

### 🔹 Zitierweise

Die korrekte **APA-Zitierweise** ist einzuhalten:

> 💡 **Tipp**: Die hier angegebenen Zitierungen verstehen sich als Beispiele. Eine tiefgreifendere Beschreibung der APA-Zitierung findest du z.B. [auf dieser Webseite](https://www.scribbr.at/category/apa-standard-at).
- **Im Text:** 

    - (In)Direktes Zitat: `(<Autor:innen>, <Jahr>)`, z.B. 
        > (Ebner & Schön, 2013)
    - Im Fließtext: `<Autor:innen> (<Jahr>)`, z.B.
        > Ebner & Schön (2013)
- **Im Literaturverzeichnis:**

    - Bücher: `<Autor:innen> (<Jahr>). <Titel> (<Auflage>). <Verlagsort>: <Verlag>.`, z.B. 
        > Ebner, M. & Schön, S. (2013). *Lehrbuch für Lernen und Lehren mit Technologien* (2. Aufl.). Berlin: epubli.
    - Webseiten:`<Autor:innen> (<Jahr>). <Titel>. <Name der Webseite>. <URL> [<Abrufdatum>].`, z.B. 
        > Ebner, M., Schön, S. & Nagler, W. (2011). *Einführung - Das Themenfeld "Lernen und Lehren mit Technologien".* Lehrbuch für Lernen und Lehren mit Technologien. URL: http://l3t.tugraz.at/index.php/LehrbuchEbner10/article/view/88 [Abgerufen am 01.01.2025].

- Die Datei mit den Literaturangaben (`99_Literatur.md`) soll nicht umbenannt werden.

## ⚠️ Wichtige Hinweise

- **Veraltete Inhalte:** Das Buch enthält überholte Informationen. Offene [**Issues auf GitHub**](https://github.com/ed-tech-at/L3T/issues) zeigen die zu überabeitenden Stellen (Vollständige Liste in Arbeit).
- **Fehler durch die Datenübernahme:** Fehlerhafte Tabellen, Links, Blockquotes, Bilder, etc. könnten vorhanden sein. Die Dateien sollten daher mit der **[PDF-Version des Buches](https://l3t.tugraz.at/index.php/LehrbuchEbner10/index)** abgeglichen und ggf. manuell korrigiert werden werden.
- **Manuelle Verarbeitung:** PRs werden **nicht automatisch** in BookStack hochgeladen, sodass eine Aktualisierung Zeit braucht.

## 📩 **Fragen oder Probleme?** 
- Erstelle ein [Issue auf GitHub](https://github.com/ed-tech-at/L3T/issues).
- Sende eine Nachricht auf Discord: [@16grabnb](https://discord.com/).
- Schreib eine [E-Mail](mailto:bernd.grabner@edu.uni-graz.at).

