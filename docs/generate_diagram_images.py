"""
Diagram Image Generator for PRESENTE Project.
Fetches rendered Mermaid diagrams as high-resolution JPEG images.
"""

import os
import base64
import urllib.request

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

DIAGRAMS = {
    "multiplatform-web-app-diagram.jpg": """
    graph TD
        subgraph ClientLayer ["1. Multiplatform Access for Patients & Families"]
            Web["Web App Responsive / PWA<br>(Instant access via browser without installation)"]
            Android["Android Mobile App<br>(Native .apk / Google Play)"]
            iOS["iOS Mobile App<br>(Native .ipa / App Store / TestFlight)"]
        end

        subgraph CoreApp ["2. Unified Frontend (Angular + Capacitor)"]
            UI["Accessible, Lightweight & Empathetic UI"]
            Offline["Local Guide Storage / Offline Mode"]
            Notifications["Push Notifications for Self-Care & Reflection"]
        end

        subgraph BackendAPI ["3. Cloud Backend API"]
            FastAPI["FastAPI REST Engine (Python)"]
        end

        Web --> CoreApp
        Android --> CoreApp
        iOS --> CoreApp
        CoreApp -->|HTTPS / JSON| FastAPI
    """,

    "clean-architecture-diagram.jpg": """
    graph TD
        subgraph Presentation ["4. Presentation Layer (WebApi / FastAPI)"]
            Routers["Routers & REST Controllers"]
            Middlewares["Middlewares (Security, CORS, RBAC)"]
            IoCDeps["Inversion of Control (FastAPI Depends / IoC Container)"]
        end

        subgraph Application ["3. Application Layer (Application Core)"]
            UseCases["Use Cases (Publish, Retrieve, Categorize)"]
            DTOs["Input/Output DTOs (Pydantic)"]
            AppInterfaces["External Service Interfaces"]
        end

        subgraph Domain ["1. Domain Layer (Enterprise Core)"]
            Entities["Business Entities (Content, Specialists, Resources)"]
            RepoInterfaces["Repository Contracts (abc.ABC)"]
            DomainRules["Domain Rules & Exceptions"]
        end

        subgraph Infrastructure ["2. Infrastructure Layer (Infrastructure)"]
            DBModels["SQLAlchemy 2.0 Async Models"]
            RepoImpl["Concrete Repositories (PostgreSQL)"]
            AIClient["AI Client (Google AI Studio / Gemini)"]
            StorageAdapter["Media Adapter & YouTube Embeds"]
        end

        Presentation --> Application
        Presentation --> Infrastructure
        Infrastructure --> Domain
        Application --> Domain
        Infrastructure -.->|Implements| RepoInterfaces
    """,

    "zero-cost-deployment-diagram.jpg": """
    flowchart TB
        subgraph FrontendHost ["Frontend Hosting (100% Free)"]
            Vercel["Vercel / Cloudflare Pages<br>(Global CDN, Automatic SSL HTTPS)"]
        end

        subgraph BackendHost ["Backend Server (Heroku-style Free PaaS)"]
            RenderPaaS["Render.com / Oracle Always Free VM<br>(Free PaaS alternative to Heroku for FastAPI)"]
        end

        subgraph DatabaseHost ["Managed Database (100% Free)"]
            Supabase["Supabase PostgreSQL<br>(Managed relational database, 500MB free)"]
        end

        subgraph AIHost ["Artificial Intelligence (100% Free)"]
            Gemini["Google AI Studio API<br>(Gemini 2.0 Flash - 1M tokens/call free)"]
        end

        subgraph MediaHost ["Multimedia Hosting"]
            YouTube["YouTube Embeds / Supabase Storage<br>(Streaming without server bandwidth cost)"]
        end

        Vercel -->|API Calls| RenderPaaS
        RenderPaaS -->|Async Connection| Supabase
        RenderPaaS -->|AI Assistance| Gemini
        Vercel -->|Media Playback| YouTube
    """
}


def generate_diagrams() -> None:
    """Renders Mermaid graphs into JPEG images and saves them in the assets directory."""
    for filename, code in DIAGRAMS.items():
        clean_code = "\n".join([line.strip() for line in code.strip().split("\n") if line.strip()])
        encoded = base64.b64encode(clean_code.encode('utf-8')).decode('ascii')
        url = f'https://mermaid.ink/img/{encoded}?type=jpeg&bgColor=FFFFFF'
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        destination = os.path.join(ASSETS_DIR, filename)
        try:
            with urllib.request.urlopen(request) as response, open(destination, 'wb') as file:
                file.write(response.read())
            print(f"Generated: {destination} ({os.path.getsize(destination)} bytes)")
        except Exception as error:
            print(f"Error generating {filename}: {error}")


if __name__ == "__main__":
    generate_diagrams()
