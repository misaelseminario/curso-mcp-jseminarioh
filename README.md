## Clase 2 — APIs de IA Generativa y memoria conversacional

### Conversación de 8 turnos (Paso 7)

Ver evidencia en `entregas/s02/evidencia/memoria.png`.

<pega aquí el texto de la salida de conversation.py; sirve el memoria.txt que guardaste>

### Por qué elegí ventana deslizante

La ventana deslizante es la estrategia más simple y barata: conserva solo los últimos
`MAX_TURNS` intercambios, así el costo por llamada no crece sin límite. Para una
conversación corta como esta (8 turnos, con `MAX_TURNS = 10`) no pierde nada. La desventaja
es que olvida el principio si la charla se alarga, y lo comprobé con `MAX_TURNS = 3`, donde
el modelo ya no supo el nombre de la mascota. Descarté el resumen progresivo, la memoria
selectiva y el almacenamiento externo porque añaden llamadas extra o infraestructura que este
caso no necesita.

### Límite de solicitudes provocado (Paso 9)

Ver evidencia en `entregas/s02/evidencia/rate_limit.png`.

<una línea confirmando que el error 429 se manejó con reintento y backoff, sin que el programa se cayera>

### Nota sobre el modelo

La guía indicaba `gemini-2.5-flash`, pero Google lo retiró para cuentas nuevas (error 404).
Usé `gemini-3.6-flash` y subí `max_output_tokens` de 200 a 1000, porque los modelos nuevos
gastan parte del presupuesto en razonar y con 200 la respuesta salía truncada.