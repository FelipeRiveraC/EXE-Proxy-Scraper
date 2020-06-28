# INFO
Tenemos version final. No planeo hacer mas updates ya que el programa es exactamente lo que tenia en mente desde el minuto 1. El objetivo de este programa, mas que obtener proxies y algo mas personal era mejorar mis tecnicas de scrapear y obtener datos de un sitio web utilizando python, junto a manejar de mejor manera los threads (tanto QThreads como threads normales). Despues de las patch notas voy a dejar las cosas que he aprendido.
- Instalar fuente Sketch 3D: para un correcto funcionamiento.
# Patch Notes
- Se agregan muchas mas fuentes y de gran calidad.
- Se arregla el checker, haciendolo un 200% mas preciso.
- Ahora cada fuente de proxies se ejecuta en paralelo y no responden a una lista madre, sino que cada una recibe una señal a la cual emite los proxies a medida que los obtiene.
- Se elimino lineas de codigo que eran innesesarias para la ejecucion del programa.
- Ahora la ventana se adapta a la resolucion del monitor, gracias al modulo OS.
- No se actualizara denuevo el programa.

# Projecto: Cosas aprendidas & perfecionadas
- PyQT5: Signals, Designer, QThreads, crear una GUI desde cero y conectar botones a QThreads, hacer texto con colores.
- Threads: aprendi a usar correctamente los threads en python, aprovechando todo el poder de nuestros computadores para ejecutar el script.
- Selenium: Ejecutar el webdriver con argumentos (como el headless), a "capearse" proteccion anti bots de sitios web.
- bs4: Aprendi a mezclar bs4 junto a selenium para hacer el programa mas rapido.
- En terminos generales este proyecto me sirvio mucho para tener un codigo mas estructurado y ordenado. Ademas el programa final tiene un valor real en el mercado, actualmente programas como este se pueden llegar a vender en $10 USD por licencia, sin embargo mi decicion es hacer este repositorio publico para que otras personas puedan aprender lo mencionado con este ejemplo.
