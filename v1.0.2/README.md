# PATCH NOTES
- Se implementaron nuevas fuentes, de algunas de ellas se extraen los datos usando selenium. Por ende se añade una nueva dependencia.
- Se aumento la cantidad de threads. De la cantidad de threads que tiene el procesador que ejecuta el programa a 50 threads. 
- El comprobador aumento considerablemente de velocidad. aproximadamente puede comprobar 2000 proxies en 45 segundos.
- Nuevo archivo: chromedriver.exe. Es nesesario para la ejecucion correcta del programa. Sin el, solo funcionaria el comprobador.
- El programa vuelve a depender de otro archivo: proxies.py.
- El comprobador ahora revisa dos veces los proxies muertos, para rescatar algunos de ellos. (a coste de velocidad).

# BUGS
- Al apretar scrape, se congela el programa: El programa corre con multriples QThreads, sin embargo al usar selenium, el Main loop se bloquea. Estoy trabajando para buscar solucion a este problema, pero no afecta la funcionalidad del programa.
- El contador de proxies comprobados y obtenidos no se resetea solo: Este problema es porque no he asignado correctamente una señal, se va a arreglar cuando cambie la interfaz (cosa que planeo hacer pronto).
- No se puede detener el comprobador de proxies: Esta funcionalidad esta en mi lista de cosas por hacer.

# NOTAS
- Al ejecutar el programa se abria la consola de chromedriver, enconte solucion al editar el archivo encontrado en : Python\Lib\site-packages\selenium\webdriver\common\service.py.
  Se realizo el siguiente cambio:
  
  ```python
  # DE ESTO
  self.process = subprocess.Popen(cmd, env=self.env, close_fds=platform.system() != 'Windows', stdout=self.log_file, stderr=self.log_file, stdin=PIPE)
  # A ESTO
  self.process = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE ,stderr=PIPE, shell=False, creationflags=0x08000000)
  ```
  
  Por ende para hacer el ejecutable con pyinstaller, deben primero hacer este cambio. Pueden escribirme y yo les puedo enviar el ejecutable, ya que es muy pesado para subirlo a github.
