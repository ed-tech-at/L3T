<!-- URL: https://l3t.ed-tech.app/books/l3t-lehrbuch-fur-lernen-und-lehren-mit-technologien/page/datenkompression-bei-multimedialen-materialien -->
<!-- slug: datenkompression-bei-multimedialen-materialien -->
<!-- filename: 03_Datenkompression_bei_multimedialen_Materialien.md -->
<!-- title: Datenkompression bei multimedialen Materialien -->

Mit Multimedia ist unweigerlich das Problem der Datenkompression verbunden. Bedenkt man, dass sämtliche Daten möglichst in Echtzeit bei den Lernenden ankommen beziehungsweise am Bildschirm auf Knopfdruck erscheinen sollten, sah man sich besonders in den Anfängen des World Wide Web mit großen Problemen konfrontiert.

Mit einem damals in Privathaushalten verfügbarem Modem war eine Übertragungsrate von 14.400 Bits pro Sekunde möglich. Eine nicht komprimierte Bilddatei mit einer Größe von 1024 * 768 Pixel erreicht bei einer angenommenen Farbtiefe von 24 Bits (24 Bits = 3 Bytes) je Pixel bereits 1024 * 768 * 24 Bits, also 18.874.368 Bits. Dies ergäbe bei Verwendung obigen Modems im Idealfall eine Übertragungszeit von 1.311 Sekunden oder circa 22 Minuten. Eine Steigerung der Übertragungsrate auf 28.800 Bits pro Sekunde oder sogar 56.000 Bits pro Sekunde schaffte nur bedingt Abhilfe. Nachdem ein Video nur die schnelle Abfolge von vielen Einzelbildern darstellt, wurde das Problem nur noch weiter verschärft.

Somit wurden verlustfreie (Informationen aus dem Datenbestand werden unter Vermeidung von Redundanzen neu strukturiert) und verlustbehaftete (dabei wird in der Regel ein Kompromiss zwischen einer möglichst hohen Datenkompression und einem möglichst kleinen Qualitätsverlust angestrebt) Datenkompressionsverfahren entwickelt, um, je nach Einsatzzweck, die zu übertragende und zu speichernde Datenmenge zu reduzieren. Wenn bei den erstellten Lehrmaterialien eine möglichst hohe Qualität sowie eine spätere Bearbeitung gewünscht werden, wird man sich für eine verlustfreie Datenkompression entscheiden; sollen die Materialien ‚nur’ konsumiert werden können, dann ist oftmals eine verlustbehaftete Datenkompression geeigneter.

Zur Kompression/Dekompression von Multimediadaten, im speziellen Audio- und Videodaten, kommt ein sogenannter Codec (als Abkürzung für ‚coder’ und ‚decoder’) zum Einsatz. Dieser kann in Software- oder Hardwareform vorliegen. Bei lizenzpflichtigen Verfahren sind diese beiden Teile auch manchmal getrennt: Der Kompressor ist gebührenpflichtig, während der Dekompressor frei zugänglich ist.

## Datenkompression von Bildern

Im Laufe der Jahre entstanden unterschiedliche Kodierungsverfahren, die heute von verschiedenen Bildformaten verwendet werden. JPG, PNG, GIF, SVG, BMP, TIFF, WMF, Postscript, PDF sind die bekanntesten Formate. Wie im vorhergehenden Abschnitt dargestellt, besteht beim Bild ein Zusammenhang zwischen der Bildauflösung (Anzahl der Bildpunkte), der Anzahl der verwendeten Farben (Farbtiefe) sowie der Art des Bildes (Vektor- oder Pixelgrafik) und gegebenenfalls auch der Anzahl der unterschiedlichen Ebenen (Layer) eines Bildes.

In den Anfängen kam im World Wide Web vor allem das GIF-Format zur Anwendung, da es bei geringer Farbtiefe auch Transparenz und kleine Animationen zuließ. Des Weiteren wurde es in die HTML-Spezifikation aufgenommen. Auf Grund von Lizenzproblemen greifen viele (Firmen) allerdings auf die heute gängigen JPEG- oder PNG-Formate zurück.

JPEG-Kompression eignet sich sehr gut für fotorealistische Bilder bei ausgezeichneten Kompressionsraten, jedoch bilden sich bei harten Übergängen Artefakte und bei mehrmaliger Kompression verändert sich die Qualität des Bildes stark. JPEG ist zwar für Darstellungen im Web geeignet, aber nicht für die Bildbearbeitung. In den letzten Jahren setzte sich immer stärker das PNG-Format durch, wie auch das Vektorgrafikformat SVG, das in modernen Webbrowsern verlustfrei dargestellt werden kann.

## Datenkompression von Audio

Audiokompression ist heute sehr stark durch das MP3-Format geprägt, welches auch auf einem sehr einfachen Prinzip beruht: Zur Kompression von Audio-Signalen speichert man unwichtige Informationen nicht ab. Basierend auf Studien über das menschliche Gehör entscheidet der so genannte Encoder, welche Informationen wichtig sind und welche nicht. Beim Menschen ist es prinzipiell nicht viel anders: Bevor ein Klang ins Bewusstsein dringt, haben Ohr und Gehirn ihn schon auf seine Kernelemente reduziert. Die psychoakustische Reduktion der Audiodaten nimmt diesen Vorgang teilweise vorweg. Der Schlüssel zur Audiokompression besteht darin, auch solche Elemente zu beseitigen, die nicht redundant, aber irrelevant sind. Dabei geht es um diejenigen Teile des Signals, die die menschlichen Zuhörerinnen und Zuhörer ohnehin nicht wahrnehmen würden.

Ähnlich wie bei Bildern und Videos gibt es eine hohe Anzahl an verschiedenen Kompressionsverfahren. Hierzu seien exemplarisch das quelloffene Format OGG Vorbis oder auch das auf MPEG aufsetzende AAC-Format genannt. Ein verlustfreies Format ist zum Beispiel FLAC.

## Datenkompression von Videos

Digitale Videotechnik nimmt aufgrund der verfügbaren Endgeräte einen immer höheren Stellenwert in unserem Alltag ein. Sie bleibt aber aufgrund der notwendigen Datenmenge nicht unproblematisch – selbst hochwertige Computer sind bei der Verarbeitung derartiger Daten gefordert. Um die Speichermengen zu verdeutlichen, gehen wir davon aus, dass eine digitale Videokamera mit einer Auflösung von 800.000 Pixeln arbeitet. Bei voller Farbtiefe benötigt dieses Bild circa 2,3 Megabyte. Um eine realistische Bewegtbildfolge zu erhalten, sind 24 bis 30 Bilder pro Sekunde nötig. Das führt, je nach Bildrate, zu einem Datenstrom von ca. 60 Megabyte pro Sekunde. Ein abendfüllender Film (120 Minuten) würde nichtkomprimiert also 422 Gigabyte an Daten produzieren. Ohne Datenkompression wäre eine Übertragung im Internet undenkbar und es wurde daher eine große Anzahl unterschiedlicher (Komprimierungs-)**Codecs** entwickelt. Die wichtigsten Codecs sind Cinepak, Indeo, Video-1, MS-RLE, MJPEG und Codecs nach H.261, H.263 und MPEG.

Ähnlich den Bildern und Audiofiles können verschiedene Dateiformate durchaus verschiedene Codecs unterstützen, sodass man keinen direkten Schluss aus dem Dateiformat auf den verwendeten Codec ziehen kann. Bekannte Beispiele sind das von Apples Quicktime verwendete MOV-Format und das von Windows angebotene WMF- oder ASF-Format.
