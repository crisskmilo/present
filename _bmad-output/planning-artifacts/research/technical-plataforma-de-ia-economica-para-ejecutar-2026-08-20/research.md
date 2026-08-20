---
title: 'technical research: Plataforma de IA económica para ejecutar BMAD en Antigravity para PRESENTE'
type: 'technical'
topic: 'Plataforma de IA económica para ejecutar BMAD en Antigravity para PRESENTE'
decision: 'Elegir la plataforma más económica y sostenible para desarrollar el MVP de PRESENTE con BMAD'
source: 'PRESENTE.docx y fuentes oficiales consultadas el 2026-08-20'
status: complete
preset: 'standard'
validation: normal
created: '2026-08-20'
updated: '2026-08-20'
---

# Investigación técnica: plataforma de IA económica para PRESENTE

**Decisión:** elegir la plataforma de IA para trabajar con BMAD y construir el MVP de PRESENTE sin comprometer recursos médicos esenciales.

## Resumen ejecutivo

**Recomendación principal: continuar con Antigravity usando la cuota gratuita de Google/Gemini, con Gemini Flash como modelo de trabajo y presupuestos explícitos por interacción.** Es la única opción evaluada que combina el entorno que ya tienes, ejecución de comandos, lectura y edición de archivos, web, contexto persistente y montaje de `AGENTS.md`/`.agents/skills`, que son precisamente las superficies que BMAD necesita [1].

La gratuidad no equivale a tokens garantizados ilimitados: Google define límites de tasa y cuota gratuitos sujetos a cambios. Las interacciones agénticas pueden hacer varios ciclos de razonamiento, herramientas y ejecución, por lo que una sola tarea compleja puede consumir mucho más que una respuesta de chat. La documentación permite fijar `max_total_tokens`, lo que debe ser una regla obligatoria para proteger el presupuesto [1].

**Alternativas:** GitHub Copilot Free es un buen complemento para autocompletado y tareas pequeñas, con 2.000 completions mensuales y Copilot CLI, pero sus datos publicados no lo presentan como una cuota amplia para sesiones BMAD agénticas [2]. OpenRouter ofrece modelos gratuitos y pagados, pero cambia disponibilidad por proveedor y modelo; además, sus términos trasladan al usuario la revisión de las prácticas de cada proveedor y algunos modelos gratuitos pueden permitir entrenamiento con entradas y salidas [3][4]. Por eso no es la primera opción para un proyecto relacionado con salud mental.

## Contexto de PRESENTE

El documento inicial plantea un MVP pequeño, administrado y progresivo: catálogo de contenidos, multimedia, recursos, perfiles de colaboradores, administración y roles. Excluye inicialmente diagnóstico, funciones clínicas, seguimiento de pacientes, chat privado, foro abierto y publicación libre. El equipo inicial es muy pequeño y la iniciativa busca minimizar infraestructura con servicios gratuitos o de bajo costo.

Esto cambia el criterio de selección: la IA debe ayudar a definir, diseñar, programar, probar y documentar; no debe recibir historias clínicas, testimonios identificables, nombres de pacientes, diagnósticos, audios de personas o cualquier dato sensible. La IA tampoco debe decidir contenido clínico ni sustituir revisión de profesionales.

## Requisitos de decisión

| Criterio | Tipo | Peso | Regla práctica |
|---|---:|---:|---|
| Compatibilidad con Antigravity/BMAD | Duro | 30% | Archivos, comandos, skills, reglas e iteración en repositorio |
| Costo actual | Duro | 30% | Comenzar en USD 0; pagar solo cuando exista presupuesto explícito |
| Capacidad para código y tareas largas | Preferencia | 20% | Contexto, herramientas, pruebas y continuidad |
| Privacidad y control | Duro | 15% | No enviar datos de salud; preferir uso sin entrenamiento o local |
| Portabilidad | Preferencia | 5% | Poder cambiar de proveedor sin rehacer el proyecto |

## Evaluación de finalistas

Puntuación orientativa sobre 5. No es un benchmark independiente; sintetiza las capacidades y condiciones publicadas por cada proveedor.

| Opción | Compatibilidad | Costo | Trabajo agéntico | Privacidad | Portabilidad | Lectura |
|---|---:|---:|---:|---:|---:|---|
| Antigravity + Gemini gratuito | 5 | 5 | 5 | 2 | 3 | Mejor ajuste para comenzar; requiere anonimización porque el uso no pagado puede ser usado para mejorar productos |
| GitHub Copilot Free | 3 | 5 | 2 | 3 | 3 | Complemento útil; 2.000 completions/mes y CLI, pero no es la cuota principal de BMAD |
| OpenRouter modelos `:free` | 2 | 4 | 3 | 1-3 | 5 | Respaldo experimental; límites, proveedores y términos cambian por modelo |
| ChatGPT/Claude gratuitos | 1-2 | 5 | 2 | 2-3 | 3 | Útiles para consultas manuales; no son la base integrada del repositorio Antigravity |

## Hallazgos por dimensión

### Integración y arquitectura

Antigravity ofrece ejecución de Bash, Python y Node, gestión de archivos, búsqueda web, URL context, contexto compacto para sesiones largas, MCP remoto y personalización mediante `AGENTS.md` y `.agents/skills` [1]. Esa combinación encaja directamente con BMAD: los artefactos viven en el repositorio y el agente puede ejecutar las verificaciones del proyecto.

Hay límites relevantes: la documentación marca el agente y la API como preview; no soporta entrada de audio, video ni documentos directamente, y algunas herramientas como `file_search` y `computer_use` no están disponibles [1]. Por tanto, el DOCX de requisitos debe convertirse a texto o Markdown para el trabajo de BMAD, y la multimedia de PRESENTE debe tratarse como contenido del producto, no como entrada automática del agente.

### Costo y límites

Google ofrece una capa gratuita con acceso a AI Studio y tokens de entrada/salida gratuitos para determinados modelos, pero con acceso limitado, límites de tasa y cuota que pueden cambiar [5]. El agente Antigravity se cobra según el consumo del modelo y las herramientas; la cuota gratuita incluye límites de uso, no una promesa de sesiones infinitas [1]. La opción de menor riesgo financiero es mantener facturación desactivada mientras se aprende y usar presupuestos bajos por tarea.

La API pagada de Gemini tiene una ventaja de privacidad: Google indica que no usa prompts ni respuestas para mejorar productos en Paid Services [6]. Sin embargo, esa ventaja solo importa si en el futuro existe presupuesto; no justifica activar facturación sin controles.

### Implementación real para BMAD

El flujo recomendado es:

1. Usar una sesión BMAD para una sola decisión o artefacto pequeño.
2. Leer primero `AGENTS.md`, el estado del sprint y el artefacto objetivo.
3. Pedir un plan corto antes de editar.
4. Fijar un `max_total_tokens` conservador en tareas agénticas y dividir tareas grandes.
5. Ejecutar pruebas o validaciones después de cada cambio.
6. Guardar los resultados en `_bmad-output` y no depender de la memoria del chat.
7. Cambiar a una tarea manual o esperar a que se renueve la cuota cuando el límite se alcance, sin abrir cuentas duplicadas ni intentar evadir límites.

### Ecosistema y riesgo de proveedor

OpenRouter permite seleccionar cientos de modelos y consultar precios y capacidades por API; los modelos gratuitos pueden desaparecer o cambiar [3]. Sus términos indican que el servicio no garantiza la disponibilidad de un modelo, que cada proveedor tiene términos propios y que algunos proveedores pueden usar entradas y salidas para entrenamiento [4]. Es útil como experimento con código sintético, pero no debe ser la ruta por defecto para información sensible o para un servicio futuro dirigido a personas vulnerables.

## Veredicto

### Ganador: Antigravity + Gemini gratuito

Gana por ajuste al flujo que ya tienes, no por ofrecer “tokens infinitos”. Es la opción que minimiza el costo de cambio y permite aprovechar BMAD con archivos, reglas, skills y comandos. La condición es operar en modo de desarrollo con datos sintéticos o anonimizados.

### Runner-up: GitHub Copilot Free

Gana cuando el trabajo sea autocompletado, pequeñas correcciones o consultas puntuales dentro de VS Code. No lo elegiría como motor principal de BMAD porque su oferta gratuita publicada se expresa en completions y acceso limitado, no en una capacidad amplia de agente multi-paso [2].

### Argumento más fuerte contra la recomendación

La cuota gratuita de Antigravity puede agotarse o cambiar, y el uso no pagado puede incluir revisión humana y uso de contenido para mejorar productos [6]. Si el proyecto llegara a manejar información personal o clínica, el modo gratuito no sería apropiado. La cobertura se mitiga manteniendo el contenido sensible fuera del repositorio de desarrollo, usando datos ficticios y, solo cuando exista financiación, evaluando un servicio pagado con controles contractuales.

## Plan de uso de costo cero

- **USD 0:** Antigravity/Gemini gratuito para BMAD, documentación, arquitectura, código y pruebas con datos ficticios.
- **USD 0:** YouTube para el primer contenido audiovisual y almacenamiento/distribución inicial según sus condiciones; separar esta decisión de la plataforma de IA.
- **USD 0:** GitHub público o privado según necesidad, verificando límites y evitando subir datos personales.
- **USD 0 opcional:** GitHub Copilot Free como complemento de completions.
- **No recomendado como ruta principal:** OpenRouter gratuito para código no sensible solamente, revisando proveedor por proveedor.
- **Cuando exista presupuesto:** activar pago solo con alertas, límite mensual y una cuenta/proyecto separado; comenzar con el modelo Flash/Lite y usar modelos Pro solo para decisiones complejas.

## Protección indispensable para PRESENTE

- No enviar a ninguna IA historias clínicas, nombres, teléfonos, correos, testimonios identificables, grabaciones, rostros, diagnósticos ni información de pacientes.
- No pedir a la IA diagnósticos, clasificación clínica, triage, tratamiento ni recomendaciones personalizadas.
- Mantener revisión humana de psicología/pastoral para todo contenido público.
- Separar el repositorio de desarrollo del futuro repositorio de contenidos y de cualquier base de usuarios.
- Añadir una política de datos y consentimiento antes de aceptar testimonios o comentarios.
- Tratar todo contenido generado por IA como borrador sujeto a revisión.

## Próximas acciones

1. Confirmar que Antigravity está usando una cuenta/proyecto sin facturación o con presupuesto máximo explícito.
2. Añadir o revisar `AGENTS.md` con reglas BMAD, privacidad y límites clínicos.
3. Convertir `PRESENTE.docx` a un artefacto Markdown de requisitos, sin adjuntar futuros datos personales.
4. Ejecutar BMAD primero sobre el alcance del MVP y la arquitectura, no sobre funcionalidades clínicas.
5. Medir durante una semana cuántas tareas y tokens consume el flujo real antes de decidir cualquier pago.

## Fuentes

[1] Google, “Antigravity agent”, documentación oficial, actualizado 2026-08-18. https://ai.google.dev/gemini-api/docs/antigravity-agent

[2] GitHub, “GitHub Copilot plans”, página oficial de precios, consultada 2026-08-20. https://github.com/features/copilot/plans

[3] OpenRouter, “Models”, documentación oficial y catálogo de modelos, consultado 2026-08-20. https://openrouter.ai/docs/guides/overview/models ; https://openrouter.ai/models?q=free

[4] OpenRouter, “Terms of Service” y “Privacy Policy”, actualizados 2026-07-29 y 2026-07-06. https://openrouter.ai/terms ; https://openrouter.ai/privacy

[5] Google, “Gemini Developer API pricing”, documentación oficial, actualizado 2026-08-13. https://ai.google.dev/gemini-api/docs/pricing

[6] Google, “Gemini API Additional Terms of Service”, efectivo 2026-03-23. https://ai.google.dev/gemini-api/terms

**Nota de frescura:** este informe debe revisarse antes de actuar si han pasado más de dos trimestres, o inmediatamente si Antigravity/Gemini cambia su esquema de cuota, modelos o términos de datos.
