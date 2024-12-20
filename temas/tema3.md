# Servidores de aplicaciones

## Introducción

Un servidor de aplicaciones es un marco mixto de software que permite tanto la creación de aplicaciones web como un entorno de servidor para ejecutarlas.

A menudo puede ser una pila compleja de diferentes elementos computacionales que ejecutan tareas específicas que necesitan trabajar como uno solo para alimentar múltiples nubes y software y aplicaciones basadas en la web.

Situado entre el servidor web y el nivel de backend del servidor de bases de datos, el servidor de aplicaciones es esencialmente un intermediario para el servidor de bases de datos y los usuarios de las aplicaciones empresariales o de consumo que soporta mediante el uso de varios protocolos e interfaces de programación de aplicaciones (API).

Es habitual que se utilice junto con un servidor web o que contenga un servidor web, por lo que ambos pueden converger y denominarse servidor de aplicaciones web. También es lo suficientemente versátil como para ser utilizado con otros servidores de aplicaciones simultáneamente.

Los servidores de aplicaciones también pueden contener sus propias interfaces gráficas de usuario para su gestión a través de PC, pero también pueden ocuparse de sus propios recursos, así como del procesamiento de transacciones, la mensajería, la agrupación de recursos y conexiones, y la realización de tareas de seguridad.

## Servidor de aplicaciones

Las aplicaciones vienen en todas las formas, tamaños y casos de uso. En un mundo en el que dependemos de una serie de procesos empresariales críticos, los servidores de aplicaciones son los ordenadores de gran potencia que proporcionan recursos de aplicaciones a los usuarios y clientes web.

Los servidores de aplicaciones, como ya hemos dicho, se sitúan física o virtualmente entre los servidores de bases de datos que almacenan los datos de las aplicaciones y los servidores web que se comunican con los clientes. Los servidores de aplicaciones y el middleware afín son los sistemas operativos que soportan el desarrollo y la entrega de una aplicación. Ya sea una aplicación de escritorio, móvil o web, los servidores de aplicaciones desempeñan un papel fundamental en la conexión de un mundo de dispositivos.

## Terminología de los servidores de aplicaciones

| Término           | Descripción                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Servidor web      | Responsable de almacenar, procesar y entregar los datos de E/S de las páginas web                     |
| Cliente web       | Punto final que intenta acceder a los recursos de la web o de la aplicación                           |
| HTTPS             | Protocolo de comunicación seguro entre el servidor web y los clientes web                             |
| JSON              | Lenguaje para el intercambio entre los servidores web y de aplicaciones                               |
| Lógica de negocio | Reglas para el almacenamiento de datos y la transferencia de recursos de la aplicación                |
| Aplicación        | Un programa de software o un sitio web unido a una base de datos                                      |

## El papel del servidor de aplicaciones en la arquitectura de servicios

Cuando los usuarios de las aplicaciones, ya sea usuarios físicos o los clientes web, solicitan acceso a una aplicación, el servidor de aplicaciones suele hacer el trabajo pesado en el backend para almacenar y procesar las solicitudes dinámicas de las aplicaciones.

## ¿Por qué necesitamos servidores de aplicaciones?

Miles de millones de clientes web hacen peticiones HTTP cada día, esperando un acceso instantáneo a la aplicación en cuestión. Headspace durante la rutina de la mañana, Google Docs para el informe extenso, Twitter durante la pausa para el café, no importa la aplicación en uso, está siendo consultada en un servidor de aplicaciones y devuelta a través de un servidor web.

Los servidores web se encargan de servir a los clientes web peticiones HTTP con respuestas HTTP. A diferencia de los servidores de aplicaciones, el diseño del servidor web es lo suficientemente ligero como para procesar las solicitudes de datos estáticos de varias aplicaciones (o sitios web), manteniendo la seguridad. Las peticiones dinámicas, a menudo en forma de aplicaciones, requieren asistencia adicional.

### Los servidores de aplicaciones optimizan el tráfico y añaden seguridad

Para conseguir una agilidad óptima del servidor web, no sirve gestionar tanto las peticiones HTTP de los clientes web como pasar o almacenar recursos de múltiples sitios web. Los servidores de aplicaciones llenan este vacío con un diseño de alta potencia construido para manejar las solicitudes de contenido web dinámico.

Los servidores de aplicaciones también proporcionan redundancia de programas y una capa adicional de seguridad. Una vez desplegado entre una base de datos y un servidor web, el trabajo de preservar y duplicar la arquitectura de la aplicación a través de la red es más factible. El paso adicional entre las potenciales comunicaciones web maliciosas y las joyas de la corona en el servidor de base de datos añade una capa de seguridad adicional. Dado que los servidores de aplicaciones pueden procesar solicitudes de lógica empresarial, un intento de inyección SQL es también mucho más difícil.

Las organizaciones pueden proteger aún más sus datos con un servidor proxy inverso colocado delante de sus bases de datos. Los servidores proxy y las VPN pueden hacer maravillas para anonimizar y encriptar la comunicación para proteger a los usuarios y los datos de la empresa.

## ¿Cómo funcionan los servidores de aplicaciones?

Pongamos como ejemplo un servidor de aplicaciones Java.

### ¿Qué son los servlets?

Un servlet es un programa Java que se ejecuta en un servidor Web y construye o sirve páginas web. De esta forma se pueden construir páginas dinámicas, basadas en diferentes fuentes variables: datos proporcionados por el usuario, fuentes de información variable (páginas de noticias, por ejemplo), o programas que extraigan información de bases de datos.

Comparado con un CGI, un servlet es más sencillo de utilizar, más eficiente (se arranca un hilo por cada petición y no un proceso entero), más potente y portable. Con los servlets podremos, entre otras cosas, procesar, sincronizar y coordinar múltiples peticiones de clientes, reenviar peticiones a otros servlets o a otros servidores u otros.

Como la mayoría de los servidores de hoy en día, los servidores de aplicaciones contienen características de seguridad, transacciones, servicios, clustering, diagnósticos y bases de datos. En lo que se diferencian los servidores de aplicaciones es en su capacidad para procesar peticiones de servlets (programas Java) desde un servidor web.

1. El cliente abre un navegador y solicita acceso a un sitio web
2. El servidor web recibe la petición HTTP y responde con la página web deseada
3. El servidor web gestiona las peticiones de datos estáticos, pero el cliente quiere utilizar una herramienta interactiva
4. Al tratarse de una petición de datos dinámicos, el servidor web transfiere la petición a un servidor de aplicaciones
5. El servidor de aplicaciones recibe la petición HTTP y la convierte en una petición de servlet
6. El servlet llega al servidor de la base de datos, y el servidor de aplicaciones recibe una respuesta del servlet
7. El servidor de aplicaciones traduce la respuesta del servlet al formato HTTP para el acceso del cliente

| Servidor de aplicaciones | Servidor web |
|--------------------------|--------------|
| Sirve peticiones HTTP y de otra lógica de negocio | Sirve peticiones HTTP |
| Almacena y proporciona lógica de negocio | Contenido web estático |
| La utilización de los recursos es pesada | Ligera |
| Soporta transacciones distribuidas y Enterprise JavaBeans (EJB) | Soporta Servlets, Java Server Pages (JSP) y JSON |

## Servidores de aplicaciones en la década de 2020

El mercado de los servidores de aplicaciones espera crecer a una CAGR del 13,2%, pasando de cerca de 17.000 millones de dólares en 2020 a 41.000 millones en 2026. El crecimiento continuo no es una sorpresa, ya que la conectividad a Internet y la dependencia de las aplicaciones crece.

La migración a las plataformas y servicios en la nube y el auge de los dispositivos IoT son dos impulsores clave en el mercado de infraestructura de aplicaciones y middleware moderno. A esto hay que añadir un movimiento hacia las políticas BYOD (Bring Your Own Device) y una fuerza de trabajo remota que depende de una mayor conectividad y eficiencia operativa.

## Servidores de aplicaciones: El mejor amigo de un servidor web

Los servidores de aplicaciones son fundamentales para las exigencias actuales de interconexión. Las empresas, en última instancia, están al servicio de los intereses de los clientes por lo que sin una conexión escalable y estable a los recursos de las aplicaciones, los clientes modernos huirán sin mirar atrás.

Los servidores de aplicaciones asumen el papel de conector y mejor amigo de los servidores web. Cuando los servidores web tienen una petición del cliente que es demasiado para soportar, los servidores de aplicaciones hacen posible mantener la comunicación sin problemas con el contenido web dinámico.

## ¿Qué es el despliegue de aplicaciones web?

El despliegue en el desarrollo de software y web significa pasar los cambios o actualizaciones de un entorno de funcionamiento a otro. Al configurar un sitio web, siempre se tendrá el sitio web en vivo, que se llama el entorno en vivo o entorno de producción.

Si se quiere tener la capacidad de hacer cambios sin afectar a un sitio web en producción, se puede (y se debe) añadir entornos adicionales. Estos entornos se llaman entornos de desarrollo o entornos de despliegue. Los entornos de desarrollo adicionales suelen ser un entorno local, un entorno de desarrollo y un entorno de preparación o preproducción.

Aunque los modelos de despliegue pueden variar, el más común es el clásico modelo de despliegue "de izquierda a derecha" cuando se trabaja con múltiples entornos de despliegue.

## ¿De qué pasos consta el proceso despliegue?

El flujo del proceso de despliegue consta de 5 pasos: **Planificación, desarrollo, pruebas, despliegue y supervisión**.

1. **Recordar tener un plan de despliegue de software**: Para asegurarse de que el proceso de despliegue se desarrolle con la mayor fluidez posible, lo mejor es tener un plan de despliegue que se siga en todo momento. Al tener un plan nos aseguramos de que todo se haga de la misma manera cada vez que se realicen cambios. Esto es especialmente útil cuando varios usuarios trabajan en el mismo proyecto.

Un plan de despliegue debe incluir reglas sobre cuándo desplegar desde los entornos locales a los sitios de desarrollo o de puesta en escena, así como horarios para cuando los nuevos cambios pueden ir a un entorno en vivo. Al tener un plan establecido, se reduce el riesgo de conflictos entre los diferentes cambios y se asegura que el proceso de despliegue sea lo más fácil y fluido posible. Si se está trabajando en un proyecto de código abierto, también da la oportunidad de hacer Release Candidates y dejar que la comunidad lo pruebe para detectar cualquier error que se pueda haber pasado por alto.

Además de un plan general, también es importante planificar cada uno de los cambios que se vaya a realizar. Este proceso será muy rápido para los cambios menores, pero debería ser mucho más extenso para los grandes cambios. Si se planifica con mucha antelación, se estará mucho más preparado para tener un proceso de despliegue sin problemas.

2. **Definir las dependencias**: Una vez que se tenga el plan en marcha, es el momento de realizar el desarrollo real. Para garantizar que cualquier desarrollo pueda realizarse simultáneamente y sin romper nada, es importante trabajar únicamente en entornos locales o de desarrollo. Una vez que el proceso de desarrollo está hecho, es el momento de empezar a probar y desplegar los cambios a través de la configuración de su entorno.

3. **Automatización del proceso de despliegue**: Probar los cambios es crucial para garantizar que no haya errores en el entorno de producción final. Pero las pruebas no pueden completarse sin desplegar los cambios en nuevos entornos.

Una vez que se haya comprobado que todos los cambios funcionan en el entorno local o de desarrollo, es el momento de desplegar los cambios en el siguiente entorno. Esto debe hacerse hasta el entorno de preproducción, donde se deben realizar las pruebas finales de control de calidad. Si todo está correctamente probado y funciona en un entorno parecido al entorno real, es el momento de desplegarlo en vivo.

Si se descubren errores por el camino en cualquier entorno, es importante tener un plan para manejarlos. Por lo general, cualquier cambio que no pase las pruebas en el entorno de ensayo debe ser enviado de nuevo a la fase de desarrollo y -una vez corregido- volver a trabajar en los entornos.

4. **Desplegar primero en entornos de desarrollo y prueba**: Una vez que se han realizado todas las pruebas en los entornos anteriores y se han corregido los errores, es el momento de desplegar los cambios en el entorno real. Esto debería ser algo bastante seguro, pero todos los que han trabajado en el desarrollo de software saben que algo puede salir mal.

Así que, aunque es fácil detenerse aquí, es importante incluir el último paso del proceso: la monitorización.

5. **Supervisar los cambios**: Una vez que los nuevos cambios estén en marcha y los usuarios reales utilicen activamente el sitio web o la aplicación, es importante supervisar que todo funcione según lo previsto. Independientemente de la planificación realizada, existe la posibilidad de que los usuarios se encuentren con problemas o realicen acciones que usted no había previsto durante la planificación y el desarrollo.

Un buen consejo para la monitorización es planificar los lanzamientos para los momentos en los que la menor cantidad de usuarios lo noten y en los que se tengan recursos de desarrollo listos en caso de que haya que arreglar algo. De este modo, el número de usuarios afectados por cualquier error será mínimo y se tendrá gente preparada para arreglarlo o revertir los cambios si es necesario.

Si se han de revertir los cambios, es importante mantener la calma y tener un proceso para manejarlo con la misma minuciosidad con la que se manejan los despliegues.

# Tipos de Despliegue

Cuando se trata del despliegue en entornos, este suele dividirse en dos categorías principales: despliegue de metadatos y despliegue de contenido. Cada uno tiene distintos impactos en el entorno de destino y debe gestionarse de forma diferente para garantizar un proceso de despliegue fluido y sin problemas.

## Despliegue de Metadatos

Los metadatos incluyen cambios en el código fuente, plantillas, hojas de estilo, archivos y otras configuraciones estructurales de la aplicación. Este tipo de despliegue generalmente requiere una validación rigurosa entre los entornos para identificar y resolver posibles conflictos. Muchas herramientas de despliegue ofrecen mecanismos de verificación de consistencia que pueden guiar al equipo en caso de encontrar conflictos de fusión u otras incompatibilidades.

## Despliegue de Contenido

El contenido, que incluye textos, imágenes, videos y otros activos multimedia, es más sencillo de transferir entre entornos en comparación con los metadatos. Debido a su menor complejidad, muchas herramientas de despliegue permiten que los editores de contenido gestionen el despliegue de contenido sin necesidad de la intervención de desarrolladores. Esto facilita que los equipos de contenido puedan enviar actualizaciones sin depender de un equipo técnico para publicar nuevos materiales.

# Mejores Prácticas de Despliegue

Tener un plan de despliegue claro y consistente en el equipo es fundamental. A continuación, se enumeran algunas prácticas recomendadas para asegurar un proceso de despliegue eficiente y sin errores.

### 1. Utilizar Git

Usar un sistema de control de versiones como Git es esencial para cualquier flujo de trabajo de despliegue, especialmente cuando se trabaja en equipo. Git permite mantener un historial de versiones, facilita la colaboración y permite revertir cambios cuando sea necesario, reduciendo el riesgo de errores y mejorando la trazabilidad del código.

### 2. Trabajar en Ramas

Trabajar en ramas independientes permite desarrollar múltiples funcionalidades o corregir errores sin que interfieran entre sí. Esto ayuda a que los desarrolladores puedan trabajar en paralelo y facilita las pruebas antes de fusionar los cambios en la rama principal. En caso de surgir errores, se pueden crear ramas específicas para corregirlos sin afectar al resto del proyecto.

### 3. Utilizar un Entorno Local para el Desarrollo

Trabajar en un entorno local permite una mayor rapidez en la iteración de cambios, pruebas y correcciones sin tener que desplegar en un servidor remoto. Esto ahorra tiempo y reduce la necesidad de constantes actualizaciones en entornos de desarrollo o pruebas hasta que el código esté listo para ser revisado y probado exhaustivamente.

### 4. Revisar las Diferencias Antes del Despliegue en Producción

Antes de desplegar en el entorno de producción, es importante revisar las diferencias entre el código de producción actual y el nuevo que se está desplegando. Esta revisión permite identificar posibles problemas antes de que afecten a los usuarios y facilita tomar decisiones informadas sobre el momento adecuado para realizar el despliegue.

### 5. Control de Permisos para Despliegues en Producción

Restringir el acceso a los despliegues en producción para desarrolladores senior puede mejorar la seguridad y control sobre los cambios realizados en el entorno real. Aunque este control puede ralentizar un poco el proceso, también reduce el riesgo de errores en producción y asegura que al menos un desarrollador experimentado esté supervisando los cambios.

### 6. Mantener la Calma en Caso de Problemas

Si un despliegue resulta en problemas en producción, es importante actuar con calma y verificar si una reversión solucionará el problema o si existen otros métodos para corregir el fallo. Evitar reacciones apresuradas permite gestionar mejor la situación y evitar daños mayores.

### 7. Desplegar en Horas de Menor Actividad

Para minimizar el impacto en los usuarios, los despliegues deben realizarse durante horarios de menor actividad. A través de herramientas de análisis, como Google Analytics, se puede determinar cuándo hay menos usuarios activos y elegir el mejor momento para realizar el despliegue. También es importante que haya desarrolladores disponibles para monitorizar y resolver problemas que puedan surgir durante el despliegue.

# Ventajas de los Entornos de Despliegue Múltiples

- **Reducción del Riesgo**: Utilizar entornos de desarrollo y pruebas permite realizar cambios sin afectar el entorno de producción, reduciendo el riesgo de interrupciones.
- **Ahorro de Tiempo**: Trabajar en entornos locales o de prueba optimiza el flujo de trabajo, permitiendo realizar cambios y pruebas sin afectar el sitio en vivo.
- **Gestión de Contenido Sensible al Tiempo**: Con entornos de despliegue múltiples, los equipos pueden preparar campañas y contenidos para lanzarlos en un momento específico, lo que facilita la gestión de contenido programado sin complicaciones.

# Despliegue de Aplicaciones Java

### Introducción

En aplicaciones JavaEE, los componentes dinámicos que manejan las solicitudes HTTP en el servidor suelen ser los **servlets** y **JSPs**. Estos procesan las solicitudes, ejecutan la lógica de negocio y devuelven la respuesta al cliente. Los servlets son programas Java que generan contenido dinámico en función de las peticiones del cliente, procesan la información y la devuelven al servidor web, que la envía al cliente.

### Componentes del Despliegue de Aplicaciones Java

1. **Servlets**: Programas que ejecutan lógica de negocio para responder dinámicamente a las solicitudes de los usuarios.
2. **JSPs (Java Server Pages)**: Páginas que mezclan código HTML y Java para generar contenido dinámico.
3. **EJBs (Enterprise Java Beans)**: Componentes empresariales que gestionan la lógica de negocio compleja y las transacciones.
4. **Bases de Datos**: Almacenan los datos y permiten su acceso y manipulación a través de consultas desde los servlets o EJBs.

El flujo de despliegue en una aplicación Java sigue los siguientes pasos:

1. El cliente realiza una solicitud al servidor a través de su navegador.
2. El servidor web gestiona la solicitud y la dirige al servidor de aplicaciones.
3. El servidor de aplicaciones ejecuta los servlets o JSPs, que procesan la lógica de negocio y realizan consultas a la base de datos.
4. El servidor de aplicaciones convierte la respuesta en un formato HTTP y la envía de vuelta al servidor web.
5. El servidor web entrega la respuesta al cliente, completando la solicitud.

# Conclusión

Los diferentes tipos de despliegue y el uso de entornos de despliegue múltiples ofrecen una estrategia efectiva para gestionar cambios en las aplicaciones sin afectar a los usuarios. Siguiendo prácticas recomendadas, como el uso de control de versiones y la configuración de permisos, se puede minimizar el riesgo de errores y asegurar una transición fluida entre versiones en producción. Además, para aplicaciones Java, el uso de componentes como servlets y JSPs permite un manejo efectivo de contenido dinámico y procesos de backend, facilitando el despliegue de aplicaciones robustas y escalables.


# Estructura de una aplicación Java

Una aplicación web JavaEE que utilice servlets o páginas JSP debe tener una estructura de ficheros y directorios determinada:

- En el directorio raíz de la aplicación se colocan las páginas HTML o JSP (podemos dividirlas también en directorios si queremos).
  
- Colgando del directorio inicial de la aplicación, se tiene un directorio `WEB-INF`, que contiene la información Web relevante para la aplicación.
  
- El resto de elementos de la aplicación (imágenes, etc.) podemos estructurarlos como nos convenga.

Esta estructura estará contenida dentro de algún directorio, que será el directorio correspondiente a la aplicación Web, y que podremos, si lo hacemos convenientemente, copiar en el servidor que nos convenga. Es decir, cualquier servidor Web JavaEE soporta esta estructura en una aplicación Web, sólo tendremos que copiarla en el directorio adecuado de cada servidor.

Cada aplicación web JavaEE es un contexto, una unidad que comprende un conjunto de recursos, clases Java y su configuración. Cuando hablemos de contexto, nos estaremos refiriendo a la aplicación web en conjunto.

## Empaquetamiento

Una forma de distribuir aplicaciones Web es empaquetar toda la aplicación (a partir de su directorio inicial) dentro de un fichero WAR (de forma parecida a como se hace con un TAR o un JAR), y distribuir dicho fichero. Podemos crear un fichero WAR de la misma forma que creamos un JAR, utilizando la herramienta JAR.

Estos ficheros WAR son un estándar de JavaEE, por lo que podremos utilizarlos en los diferentes servidores de aplicaciones JavaEE existentes.

## Despliegue de archivos WAR

Los archivos WAR son un tipo especial de JAR utilizado para distribuir los artefactos o contenido de las aplicaciones Web en tecnología JEE: páginas Web HTML o JSP, clases Java, servlets Java, archivos XML, librerías de etiquetas (tag libraries) y otros recursos.

El empaquetamiento en archivos WAR es algo estándar, pero no así el proceso de despliegue, que es dependiente del servidor. No obstante, la mayoría de servidores JavaEE funcionan en este aspecto de modo similar: permiten desplegar las aplicaciones desde una consola de administración y también "dejando caer" el fichero en determinado directorio.

## Maven

Maven es una herramienta open-source, que se creó en 2001 con el objetivo de simplificar los procesos de build (compilar y generar ejecutables a partir del código fuente).

Antes de existir Maven, si queríamos compilar y generar ejecutables de un proyecto, teníamos que analizar qué partes de código se debían compilar, qué librerías utilizaba el código, dónde incluirlas, qué dependencias de compilación había en el proyecto…

En el mejor de los casos, se empleaban unos pocos minutos para saber cómo hacer una build del proyecto. En el peor de los casos, el proceso de build era tan complejo que un desarrollador podía tardar horas en saber cómo compilar y generar los ejecutables a partir del código.

Ahora, la build de cualquier proyecto Maven, independientemente de sus módulos, dependencias o librerías, consiste simplemente en ejecutar el comando `mvn install`.

Por otra parte, antes de Maven, cada vez que salía una nueva versión de un analizador estático de código, de un framework de pruebas unitarias (como JUnit) o cualquier librería, había que parar todo el desarrollo para reajustar el proceso de build a las nuevas necesidades.

Y… ¿cómo se ejecutaban las pruebas? ¿Cómo se generaban informes? Sin Maven, en cada proyecto esto se hacía de distinta manera.

Lo cierto es que Maven es mucho más que una herramienta que hace builds del código.

Podríamos decir que Maven es una herramienta capaz de gestionar un proyecto software completo, desde la etapa en la que se comprueba que el código es correcto, hasta que se despliega la aplicación, pasando por la ejecución de pruebas y generación de informes y documentación.

Para ello, en Maven se definen tres ciclos de build del software con una serie de etapas diferenciadas. Por ejemplo, el ciclo por defecto tiene las etapas de:

1. **Validación (validate)**: Validar que el proyecto es correcto.
2. **Compilación (compile)**.
3. **Test (test)**: Probar el código fuente usando un framework de pruebas unitarias.
4. **Empaquetar (package)**: Empaquetar el código compilado y transformarlo en algún formato tipo .jar o .war.
5. **Pruebas de integración (integration-test)**: Procesar y desplegar el código en algún entorno donde se puedan ejecutar las pruebas de integración.
6. **Verificar (verify)**: Verificar que el código empaquetado es válido y cumple los criterios de calidad.
7. **Instalar (install)**: Instalar el código empaquetado en el repositorio local de Maven, para usarlo como dependencia de otros proyectos.
8. **Desplegar (deploy)**: Desplegar el código a un entorno.

Para poder llevar a cabo alguna de estas fases en nuestro código, tan solo tendremos que ejecutar `mvn` y el nombre de la fase (la palabra que puse entre paréntesis). Además, van en cadena, es decir, si empaquetamos el código (package), Maven ejecutará desde la fase de validación (validate) a empaquetación (package). Así de simple.

Por otra parte, con Maven la gestión de dependencias entre módulos y distintas versiones de librerías se hace muy sencilla. En este caso, solo tenemos que indicar los módulos que componen el proyecto, o qué librerías utiliza el software que estamos desarrollando en un fichero de configuración de Maven del proyecto llamado `POM` (Project Object Module).

Además, en el caso de las librerías, no tienes ni tan siquiera que descargarlas a mano. Maven posee un repositorio remoto (Maven central) donde se encuentran la mayoría de librerías que se utilizan en los desarrollos de software, y que la propia herramienta se descarga cuando sea necesario.

Digamos que Maven aporta una semántica común al proceso de build y desarrollo del software.

Incluso, establece una estructura común de directorios para todos los proyectos. Por ejemplo, el código estará en `${raíz del proyecto}/src/main/java`, los recursos en `${raíz del proyecto}/src/main/resources`. Los tests están en `${raíz del proyecto}/src/test`.

## Despliegue de aplicaciones Node.js con Express

### ¿Qué es Node.js?

Node JS es un entorno de ejecución de JavaScript rápido que utilizamos para construir aplicaciones del lado del servidor, pero por sí mismo no sabe cómo servir archivos, manejar peticiones ni métodos HTTP, así que aquí es donde entra en juego Express JS.

Node.js no es un lenguaje de programación. Más bien, es un entorno de ejecución que se utiliza para ejecutar JavaScript fuera del navegador.

Node.js tampoco es un framework (una plataforma para desarrollar aplicaciones de software). El tiempo de ejecución de Node.js se construye sobre un lenguaje de programación -en este caso, JavaScript- y ayuda a la ejecución de los propios frameworks.

En resumen, Node.js no es un lenguaje de programación ni un marco de trabajo; es un entorno para ellos.

### ¿Qué es Express?

Express JS es un framework de Node.js diseñado para construir aplicaciones web de APIs y aplicaciones móviles multiplataforma de forma rápida y hacer que Node.js sea fácil.

### ¿Qué es npm?

NPM responde a las siglas de Node Package Manager o manejador de paquetes de node, es la herramienta por defecto de JavaScript para la tarea de compartir e instalar paquetes.

Tal como reza su documentación, npm se compone de al menos dos partes principales:

- Un repositorio online para publicar paquetes de software libre para ser utilizados en proyectos Node.js.
  
- Una herramienta para la terminal (command line utility) para interactuar con dicho repositorio que te ayuda a la instalación de utilidades, manejo de dependencias y la publicación de paquetes.

Así pues, NPM es un gestor de paquetes para Javascript. Es una especie de Maven para paquetes Javascript, es decir, sirve para instalar y gestionar versiones de paquetes y librerías js.

NPM lleva mucho tiempo siendo el referente en cuanto a gestores de paquetes javascript, pero desde hace un tiempo le ha salido un competidor: Yarn. Los de yarn aseguran que su gestor de librerías js es mucho más rápido y potente, pero de momento el uso de NPM es mayoritario.

### package.json

Cada proyecto en JavaScript puede enfocarse como un paquete npm con su propia información de paquete y su archivo `package.json` para describir el proyecto.

`package.json` se generará cuando se ejecute `npm init` para inicializar un proyecto JavaScript/Node.js, con los siguientes metadatos básicos proporcionados por los desarrolladores:

- **name**: el nombre de la librería/proyecto JavaScript.
- **version**: la versión del proyecto.
- **description**: la descripción del proyecto.
- **license**: la licencia del proyecto.

### NPM scripts

`package.json` también soporta la propiedad `scripts` que puede definirse para ejecutar herramientas de línea de comandos que se instalan en el contexto local del proyecto. Por ejemplo, la porción de scripts de un proyecto npm puede tener un aspecto similar a este:

```json
{
  "scripts": {
    "build": "tsc",
    "format": "prettier --write **/*.ts",
    "format-check": "prettier --check **/*.ts",
    "lint": "eslint src/**/*.ts",
    "pack": "ncc build",
    "test": "jest",
    "all": "npm run build && npm run format && npm run lint && npm run pack && npm test"
  }


```

Con eslint, prettier, ncc, jest no necesariamente instalados como ejecutables globales sino como locales de tu proyecto dentro de node_modules/.bin/.

