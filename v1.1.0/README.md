# PATCH NOTES
- Nueva interfaz, mas "user-friendly".
- Se implementa casillero para especificar los threads del comprobador.
- Se cambia el titulo a "EXE-Proxy Scraper"
- Se agregan fuentes nuevas. Actualmente el scraper entrega 1900 proxies de los cuales el 70% son funcionales con un timeout de 500 (aproximadamente, depende de nuestra conexion tambien).
- Se implementa contador de proxies obtenidos, comprobados y que no funcionan.
- Se implementa 'Status', que refleja si el programa esta ejecutando un thread o esta esperando.
- Se implementa el boton "Reset stats" que permite dejar en 0 todos los contadores.
- Se agregaron todas las funciones de versiones anteriores.
- Ahora el programa tambien utlizara multi-threading para scrapear, actualmente usa 1 thread por cada fuenta de proxies.
- Se arreglo el bug que provocaba que los botones no se actualizaran despues de un error.

# BUGS
- El menu de arriba no es funcional: No es un bug, asi lo deje, ya que no le veo importancia para el programa.
- Aveces el programa no scrapea muchos proxies: esto es debido a que una de las fuentes tiene una proteccion basada en java. Para saltarse esta proteccion tube que hacer un ciclo que puede fallar. Es cosa de apretar "Scrape!" denuevo y listo.
- Error al apretar "Upload file...": Esto se debe porque no tienes el archivo en la raiz. Apreta "Save to file..." y luego funcionara.

# NOTAS

- Revisar notas de v1.0.2
- No hay novedades.
