# Caso-3-Diseno-de-Software

## Members

## Description: Write a brief description of the system, highlighting its strengths

## Stack:

- Amazon Web Service as the designated Cloud Service

- Snowflake for data analytics and data processing, also for for MFA, IP whitelist and token validation (session validation)

Frontend:

    React Native 18.2.x – Provides high performance and scalability for web and mobile interactions.

Backend:

    Node.js 20.x: Handles all incoming REST requests. Connects to the PostgreSQL database. Implements general business logic (authentication, user management, file uploads, task creation) implementing external services such as AWS services.

    Express 4.x: Web framework for Node.js, used to handle REST, manage middleware, routing, and request/response lifecycle.

    REST: For structured, not state-dependant operation and service-oriented operations. Authentication and registration, use of AWS services, etc... 

Database:

    Snowflake --> Definir más 

AI & Machine Learning:

    Snowflake can be integrated with LLM's, in relation with the choosen model of the LLM a training for ETDL flow management is required. This AI will be used as well for documents revision.
    Reference Link: https://www.youtube.com/watch?app=desktop&v=9FejjGVZrPg&t=0s

Cloud & Hosting:   
 
    Amazon Web Services: Ensures good communication and compatbility with Snowflake and multiple useful services. 

DevOps & CI/CD:

    GitHub Actions: Automates integration and deployment workflows.

Quality Assurance:

  
## Frontend design specifications

## Data

## Third-Party 

## Cloud

## Protocols

## Backend

## Datalake

Buenas compañeros y 
@vsurak
 tengo ideas para el Data Lake, aqui hay un enlace para tener una definición concreta: https://www.geeksforgeeks.org/what-is-data-lake/
Este link trae casos de uso y comparativas:
https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-data-lake/'
A continuación hay varios de los puntos del apartado que investigue y trate de buscar soluciones:
La API debe desarrollarse en la misma tecnología cloud utilizada para los portales web del sistema.
Se puede utilizar lambda functions, cloud functions, azure functions.
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
Toda interacción con la API debe estar protegida por mecanismos de acceso como whitelist de IPs, validación de tokens y MFA.
Esto lo puede manejar snowflake https://docs.snowflake.com/en/user-guide/security-mfa
Las operaciones API deben cubrir: autenticación, validación de identidad, gestión de usuarios, operaciones sobre datasets, llaves de acceso, métricas, y procesos administrativos
AWS VPC endpoints sirven para whitelisting, etc
AWS secrets para validacion y segmentacion de info, credenciales, tokens
La lógica de negocio debe garantizar trazabilidad, cumplimiento legal, y control de cada transacción realizada dentro del sistema
Snowflake tiene historial por usuario, por rol, warehouse, etc. Son los query history de snowflake
Para la parte legal, hay que asegurar que todo el historial se guarda, que hay un warehouse especifico, desde un IP especifico....
Se deben incluir endpoints para gestionar accesos temporales, revocación de permisos, y control granular por rol y contexto.
Snowflake con aws, con middleware.
https://aws.amazon.com/financial-services/partner-solutions/snowflake/
Aunque se llame “datalake”, puede ser cualquier infraestructura moderna que permita almacenamiento, consulta y gestión masiva de datos
AWS para guardar los datos raw y luego en snowflake con los stages que jala los datos y los guarda. AWS Glue guarda todo raw y luego se pasa a snowflake ya que snowflake no puede almacenar datos raw, pasa por un proceso de ETL a snowflake, estructurado o semiestrucurado. Almacenamiento dentro de GLUE y gestion en snowflake
Debe soportar millones de registros, miles de usuarios concurrentes, y un crecimiento dinámico de la información.
Snowflake, warehouse mas grande = crecimiento vertical, mas clusters = crecimiento horizontal.
Usar inteligencia artificial para normalizar los modelos de datos, rediseñarlos según uso y relacionarlos automáticamente con datasets existentes
Snowflake for AI. https://www.snowflake.com/en/product/ai/
Detectar y evitar duplicidad de datos durante cargas y transferencias
bronce layer (Data raw), silver layer (Para los devs, ing de datos para manipular), gold layer (para el end user). Duplicidad en el silver layer tener un master antes de echar los datos al master del silver layer se verifica si ese dato ya existe y asi no se duplica. AI es una alternativa, pero tambien estan los orquestadores como Apache Airflow (recomendado porque es agnostica que sirve con snowflake), AWS tambien tiene.
Controlar y gestionar cargas delta, identificando diferencias entre cargas anteriores y actuales
Snowflake y tablas incrementales. Si se actualiza/manipula datos como manter la informacion intacta y no duplicada. Load data that hasn't been loaded yet. Snapshots anteriores, cargas las que van entrando. No es el orquestador. Snapshot de snowflake: https://docs.snowflake.com/en/sql-reference/sql/create-snapshot
dbt cargas delta: https://docs.getdbt.com/docs/build/incremental-models
Ser eficiente en operaciones de merge de datos, sin perder integridad ni contexto
De nuevo, Brance, silver y gold layer. Es conservar informacion relevante del goldlayer basicamente. Nulos, ceros, casos atipicos, incongruentes. Esto se maneja con reglas de negocios definidas entre nosotros y las instituciones, pero basicamente definidas anteriormente.
Llevar trazabilidad continua de datos usados, no usados, descartados y archivados
Trazabilidad de las capas. De la gold toma tablas de la silver y asi, por medio de nodos se puede ver cuales son usados, no usados, descartados y archivados. Gobernanza las lpersonas deben documentar bien que es lo que hacen. Es como un arbol con nodos e hijos.
DBT gestor de datos, sirve para esto con gobernanza
Tener monitoreo en tiempo real de estado, salud, tráfico, errores, cuellos de botella y uso por entidad o usuario
Entidad o usuario con snowflake sirve
salud, tráfico, errores, cuellos de botella con orquestadores (airflow)
Permitir múltiples niveles de acceso con control lógico, por usuario, entidad, o tipo de dato
Snowflake
Implementar RBAC (control de acceso basado en roles) y RLS (restricción a nivel de fila) para segmentación fina
Snowflake https://docs.snowflake.com/en/user-guide/security-access-control-overview
Toda la data sensible debe estar cifrada en reposo y en tránsito, y sus accesos siempre deben dejar registro auditable
Cualquier cosa que se haga en snowflake se registra y permite encriptacion
Restringir IP whitelist importante,
hacer el acceso a datos por warehouses para accceder a datos en particular solo en esas tablas y ya.
Limitacion o restricciones a nivel de rol. Por ultimo cifrado, encriptado, hashes, etc. https://docs.snowflake.com/en/sql-reference/functions/encrypt (edited) 
4:25
Cualquier corrección es bienvenida, gracias:saluting_face:


Buenas noches compañeros y 
@vsurak
.  A continuación voy a hacer una breve explicación de la investigación/análisis que he realizado en relación al diseño solución del caso 3 y algunas sugerencias hechas anteriormente por el profesor. A manera de aclaración la investigación tiene vinculo principalmente con la parte de "Pura Vida DataLake".
Primeramente, proporcionar dos videos que me parecieron de mucha utilidad para entender mejor Snowflake y como integrarlo a nuestro diseño:
1 - Getting Started - Architecture & Key Concepts: https://youtu.be/GtVwChmxdpw?si=4B9XBEY1BkyU4yK4
2- Getting Started: Introduction To Snowflake Virtual Warehouses: https://youtu.be/TeD5zshkdjY?si=9Vz-Y4WBu6H82gci
El segundo video se adentra en uno de los conceptos principales de SF, y el cual se describe en el primer video como una parte fundamental de su arquitectura. Ahora se presentarán algunas ideas para un par de puntos del diseño.
- Debe soportar millones de registros, miles de usuarios concurrentes, y un crecimiento dinámico de la información
Como se mencionó en observaciones pasadas SF solamente ofrece algoritmos y un diseño efectivo, por esto hay diferentes servicios de AWS que podrían servir. Se contempla AWS Lake Formation para construir, asegurar y administrar un data lake centralizado sobre Amazon S3 (Simple Storage Service), el cuál es sumamente escalable y no necesita predefinir limites de espacio.
Lo anterior se basa en separar responsabilidades para que el almacenamiento principal esté en cloud y SF se pueda centrar en otras cosas como análisis y procesamiento de datos a gran escala.
- El sistema estará basado inicialmente en servicios monolíticos con posibilidad de migrar a una arquitectura de microservicios en el futuro
Se tienen dos propuestas para este aspecto:
	1- Utilizar patrones como el "Modular Monolith", donde cada dominio (autenticación, compartición, 	visualización) se desarrolla como un módulo autónomo dentro del mismo despliegue.
	2- Implementar una arquitectura por capas separando handlers, servicios y repositorios.
- Se debe implementar versionamiento en los endpoints de la API y mantener compatibilidad hacia atrás en la medida posible
Hay diferentes prácticas como opciones en esté aspecto. Tanto el versionamiento en URL ó el versionamiento en headers son buenas prácticas pero se ven relacionadas a como se trabajará el backend, se debe de discutir más esto último con el equipo de trabajo.
Una referencia de versionamiento en URL (Norma en API´s REST): https://medium.com/@espinozajge/versionamiento-de-apis-rest-mejores-prácticas-y-consideraciones-4b5021dd0a11
Por último por el momento, para el tema del pricing de Snowflake se ha investigado también. Snowflake utiliza un modelo de pago por consumo, lo que significa que solamente se paga por lo que se usa. Entre las consideraciones de costos están los siguientes:
Almacenamiento de datos -> Se cobra por terabyte (TB) al mes, dependiendo de la región y proveedor de nube.
Fuerza de computación -> Se paga por uso mediante créditos Snowflake. Las unidades principales de cómputo son los "virtual warehouses", agrupados por tamaño.
Funciones Serverless
Servicios en la nubes -> Snowflake coordina autenticación, seguridad y compilación de consultas.
Es importante mencionar que hay diferentes ediciones que corresponden a diferentes perfiles de clientes, los créditos en cada edición cambian en su precio por ejemplo.
Toda la información viene de la guía oficial de SF sobre su pricing, a continuación el link:
https://www.snowflake.com/wp-content/uploads/2023/12/The-Simple-Guide-to-Snowflake-Pricing.pdf

YouTubeYouTube | Snowflake Developers
Getting Started - Architecture & Key Concepts 


YouTubeYouTube | Snowflake Developers
Getting Started: Introduction To Snowflake Virtual Warehouses 
