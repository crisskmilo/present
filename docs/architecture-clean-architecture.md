# PRESENTE - Arquitectura Limpia y Diseño Técnico (Clean Architecture & $0 Cost Stack)

Este documento define la arquitectura técnica del proyecto **PRESENTE**, implementando el paradigma de **Clean Architecture (Onion / Hexagonal)** con **Inversión de Control (IoC)** en Python (**FastAPI**) + **Angular**, adaptado del modelo de referencia .NET del proyecto **Million**, y optimizado para ejecutarse en capas **100% gratuitas ($0 USD)**.

---

## 1. Topología del Ecosistema de Despliegue ($0 Cost Stack)

Para garantizar la viabilidad del proyecto sin generar costos operativos ni gastos mensuales en servidores o tokens de IA, se adopta la siguiente arquitectura de despliegue en capas gratuitas:

```mermaid
flowchart TB
    subgraph ClientLayer ["1. Frontend & CDN (100% Gratis)"]
        User["Usuario / Paciente / Acompañante"]
        AngularApp["Angular SPA (Vercel / Cloudflare Pages Free)"]
    end

    subgraph BackendLayer ["2. Backend API (100% Gratis)"]
        FastAPIApp["FastAPI Service (Render.com Free Web Service / Fly.io)"]
        Uvicorn["Uvicorn ASGI Engine"]
    end

    subgraph DataLayer ["3. Persistencia & Datos (100% Gratis)"]
        SupabaseDB[("PostgreSQL Gestionado (Supabase Free Tier - 500MB)")]
        MediaStorage["Supabase Storage / Cloudinary (Archivos & Audios Free)"]
    end

    subgraph AILayer ["4. Inteligencia Artificial & Agentes (100% Gratis)"]
        GeminiAPI["Google AI Studio (Gemini 2.0 Flash / 1.5 Flash - Free Tier)"]
        GroqAPI["Groq Cloud API (Llama 3.3 70B - Free Ultra Fast)"]
    end

    User -->|HTTPS| AngularApp
    AngularApp -->|REST API / JSON| FastAPIApp
    FastAPIApp --> Uvicorn
    FastAPIApp -->|Async SQLAlchemy| SupabaseDB
    FastAPIApp -->|S3 API| MediaStorage
    FastAPIApp -->|Async SDK| GeminiAPI
    FastAPIApp -.->|Fallback| GroqAPI
```

---

## 2. Diagrama de Capas: Clean Architecture (Onion Pattern)

La arquitectura sigue estrictamente la **Regla de Dependencia**: las capas externas conocen a las internas, pero el núcleo de Dominio nunca conoce librerías de infraestructura, frameworks ni bases de datos.

```mermaid
graph TD
    subgraph Presentation ["4. Capa de Presentación (WebApi / FastAPI)"]
        A1["Routers / Endpoints (v1)"]
        A2["Middlewares (CORS, Auth, Logs)"]
        A3["FastAPI Depends / IoC Wiring (deps.py)"]
    end

    subgraph Infrastructure ["2. Capa de Infraestructura (Infrastructure)"]
        I1["SQLAlchemy 2.0 Async Models"]
        I2["Repositorios Concretos (Postgres)"]
        I3["Clientes de IA (GeminiService / GroqClient)"]
        I4["Storage / YouTube API Adapter"]
    end

    subgraph Application ["3. Capa de Aplicación (Application)"]
        App1["Casos de Uso (Use Cases / Commands & Queries)"]
        App2["DTOs / Schemas de Entrada y Salida (Pydantic)"]
        App3["Interfaces de Servicios Externos"]
    end

    subgraph Domain ["1. Capa de Dominio (Domain Core)"]
        D1["Entidades de Negocio (Entities)"]
        D2["Interfaces de Repositorios (Contracts / abc.ABC)"]
        D3["Reglas & Excepciones de Dominio"]
        D4["Value Objects"]
    end

    Presentation --> Application
    Presentation --> Infrastructure
    Infrastructure --> Domain
    Infrastructure -.->|Implementa| D2
    Application --> Domain
    Application -.->|Define contratos| D2
```

---

## 3. Flujo de Inversión de Control (IoC) y Ciclo de Vida de una Petición

El siguiente diagrama de secuencia ilustra cómo la Inversión de Control desacopla la petición HTTP del acceso a datos, pasando por los casos de uso y resolviendo las dependencias en tiempo de ejecución:

```mermaid
sequenceDiagram
    autonumber
    actor Client as Cliente (Angular Frontend)
    participant Router as ContentRouter (api/routers/v1)
    participant IoC as IoC Container / Depends (api/deps.py)
    participant UseCase as GetContentByTopicUseCase (application)
    participant RepoInterface as IContentRepository (domain/interfaces)
    participant RepoImpl as ContentRepository (infrastructure/repositories)
    participant DB as Supabase PostgreSQL
    participant AI as Google AI Studio (Gemini 2.0)

    Client->>Router: GET /api/v1/contents?topic=ansiedad
    Router->>IoC: Resolver Dependencias (UseCase + Repo + Session)
    IoC->>RepoImpl: Instanciar ContentRepository(AsyncSession)
    IoC->>UseCase: Instanciar GetContentByTopicUseCase(IContentRepository)
    IoC-->>Router: Inyectar UseCase listo para ejecución

    Router->>UseCase: execute(topic="ansiedad")
    UseCase->>RepoImpl: get_by_topic("ansiedad")
    RepoImpl->>DB: SELECT * FROM contents WHERE topic = 'ansiedad'
    DB-->>RepoImpl: Rows de BD
    RepoImpl-->>UseCase: List[Content] (Entidades de Dominio)

    opt Enriquecimiento con IA (Recomendaciones / Resumen)
        UseCase->>AI: Gemini 2.0 Flash (Generar síntesis de apoyo)
        AI-->>UseCase: Resumen terapéutico / Recursos relacionados
    end

    UseCase-->>Router: ContentResponseDTO (Pydantic Schema)
    Router-->>Client: 200 OK + JSON Response
```

---

## 4. Tabla de Mapeo: .NET (`Million`) ➔ Python (`FastAPI`)

| Concepto Arquitectónico | Proyecto .NET (`Million`) | Proyecto Python (`Present`) | Rol / Responsabilidad |
| :--- | :--- | :--- | :--- |
| **Entidades de Dominio** | `Million.Domain.Entities/*.cs` | `src/domain/entities/*.py` | Modelos de negocio puros sin dependencias de ORM. |
| **Interfaces de Repositorio** | `Million.Domain.Interfaces/IRepository.cs` | `src/domain/interfaces/i_repository.py` | Contratos abstractos (`abc.ABC`) que definen operaciones de persistencia. |
| **Excepciones de Negocio** | `Million.Domain.Exceptions/*.cs` | `src/domain/exceptions/*.py` | Excepciones personalizadas para reglas de negocio. |
| **Casos de Uso / Servicios App** | `Million.Application.Services/*.cs` | `src/application/use_cases/*.py` | Orquestación de lógica de negocio por cada feature/acción. |
| **DTOs (Data Transfer Objects)** | `Million.Application.DTOs/*.cs` | `src/application/dtos/*.py` | Esquemas Pydantic para validar payloads de entrada y serializar salidas. |
| **Modelos de Base de Datos** | `Million.Infra.Data/Context/*.cs` | `src/infrastructure/database/models/*.py` | Modelos ORM de SQLAlchemy 2.0 mapeados a tablas de PostgreSQL. |
| **Implementación de Repositorios**| `Million.Infra.Data/Repositories/*.cs` | `src/infrastructure/repositories/*.py`| Implementaciones con consultas SQL async que cumplen `IRepository`. |
| **Inversión de Control (IoC)** | `Million.Infra.IoC/DependencyContainer.cs`| `src/core/container.py` + `src/api/deps.py` | Registro y resolución de dependencias (Singleton, Scoped, Factory). |
| **Controladores / Routers** | `Million.WebApi/Controllers/*.cs` | `src/api/routers/v1/*.py` | Endpoints HTTP con decoradores `@router.get/post`. |
| **Punto de Entrada & Middleware** | `Million.WebApi/Program.cs` | `src/api/main.py` | Configuración de FastAPI, CORS, Lifespan y Middlewares. |
| **Pruebas Unitarias & Integración**| `Million.Test/*.cs` (xUnit/NUnit) | `tests/unit/`, `tests/integration/` (pytest) | Suite de pruebas automatizadas con mocks de interfaces. |

---

## 5. Estructura de Directorios del Repositorio `present`

```
present/
├── .agents/                            # BMad Skills y Configuración de Agentes
├── _bmad/                              # Pipelines y Memlogs BMad
├── docs/                               # Documentación y Propuesta MVP
│   ├── present-mvp-proposal.md
│   └── architecture-clean-architecture.md
│
├── src/                                # Código Fuente Principal
│   ├── domain/                         # CAPA 1: DOMAIN
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── content.py              # Entidad de contenido multiformato
│   │   │   ├── user.py                 # Entidad de usuario y perfil
│   │   │   └── accompaniment.py        # Entidad de sesión de acompañamiento
│   │   ├── interfaces/
│   │   │   ├── i_content_repository.py # Contrato abstracto
│   │   │   └── i_user_repository.py
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   │
│   ├── application/                    # CAPA 3: APPLICATION
│   │   ├── __init__.py
│   │   ├── dtos/
│   │   │   ├── content_dto.py          # Schemas Pydantic In/Out
│   │   │   └── user_dto.py
│   │   ├── interfaces/
│   │   │   └── i_ai_service.py         # Contrato para servicios de IA
│   │   └── use_cases/
│   │       ├── get_contents.py
│   │       ├── create_content.py
│   │       └── generate_therapeutic_summary.py
│   │
│   ├── infrastructure/                 # CAPA 2: INFRASTRUCTURE
│   │   ├── __init__.py
│   │   ├── database/
│   │   │   ├── session.py              # Async Engine SQLAlchemy (Postgres)
│   │   │   └── models/
│   │   │       ├── content_model.py
│   │   │       └── user_model.py
│   │   ├── repositories/
│   │   │   ├── content_repository.py   # Implementa IContentRepository
│   │   │   └── user_repository.py
│   │   └── external/
│   │       ├── gemini_ai_client.py     # Integración Google AI Studio
│   │       └── supabase_storage.py
│   │
│   ├── core/                           # NÚCLEO TRANSVERSAL & IOC
│   │   ├── __init__.py
│   │   ├── config.py                   # Settings (pydantic-settings)
│   │   └── container.py                # Contenedor IoC
│   │
│   └── api/                            # CAPA 4: PRESENTATION (WEBAPI)
│       ├── __init__.py
│       ├── main.py                     # App FastAPI & Lifespan
│       ├── deps.py                     # Provider de dependencias (FastAPI Depends)
│       ├── middlewares/
│       │   └── error_handler.py
│       └── routers/
│           ├── __init__.py
│           └── v1/
│               ├── content_router.py
│               └── health_router.py
│
├── tests/                              # CAPA 5: PRUEBAS
│   ├── conftest.py
│   ├── unit/
│   └── integration/
│
├── .env.example                        # Plantilla de variables de entorno
├── pyproject.toml                      # Dependencias (Poetry / Pip / UV)
└── README.md
```

---

## 6. Estrategia de IA Gratuita (Tokens & Fallback)

Para operar la iniciativa de salud mental sin presupuesto de APIs:
1. **Google AI Studio (Gemini 2.0 Flash / 1.5 Flash)**:
   - Proveedor primario mediante API Key gratuita.
   - Ventana de contexto de 1,000,000 de tokens por llamada.
   - Capacidad multimodal (texto, audio, imagen, documentos).
2. **Groq Cloud (Llama 3.3 70B)**:
   - Proveedor secundario / fallback automático si se alcanza el rate limit por minuto.
   - Latencia < 500ms para generación de respuestas en tiempo real.
3. **Respaldo Local (Ollama)**:
   - Para desarrollo sin conexión a internet ejecutando modelos ligeros (Qwen 2.5 Coder o Llama 3.1).
