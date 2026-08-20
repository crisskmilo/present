# PRESENTE
### Digital Mental Health Accompaniment Initiative
**PRESENTE - AND REMEMBER YOU ARE NOT ALONE**  
*Initiative Proposal & MVP Technical Specification*  
**Author:** Cristian Camilo Rojas Estrada (Systems Engineer / Fullstack Developer)  
**Date:** August 2026  
**Proposed Institutional Partner:** Clínica San Juan de Dios (Manizales)  

---

## Introduction

Mental health is part of everyone's life.

Throughout life, we may experience anxiety, sadness, uncertainty, loneliness, grief, conflicts, major life transitions, family difficulties, or personal concerns that affect how we feel, think, and relate to our surroundings.

Each person experiences these moments uniquely. Some seek professional therapy; others find strength in family, community, or spirituality. Some do not know how to ask for help, while others have completed inpatient care and need to sustain their progress.

From this reality emerges **PRESENTE**: an independent digital platform designed to organize, produce, publish, and distribute mental health accompaniment content in a simple, accessible, and responsible manner.

**"PRESENTE - AND REMEMBER YOU ARE NOT ALONE."**

---

## 1. Initiative Origin

The initiative originates from reflections on post-care: **"What happens after finishing an inpatient cycle or therapeutic process?"**

Upon returning to daily routines, individuals need continuity, reminders of coping mechanisms, and support networks. PRESENTE expands this care to also reach individuals in isolation and families seeking guidance.

---

## 2. Concept of PRESENTE

Being present means meeting people where they are. It is not exclusively for diagnosed patients; it is open to all individuals looking to nurture their mental well-being.

---

## 3. Purpose

To build an accessible digital platform connecting individuals with mental health, well-being, and accompaniment content created and published by authorized professionals and contributors.

---

## 4. General Objective

Construct PRESENTE: a structured digital platform facilitating access to responsible mental health content with an architecture designed to organize and distribute multi-format resources.

---

## 5. Specific Objectives

- Deliver a functional, lightweight MVP.
- Provide multi-format access (video, audio, text, downloadable PDFs).
- Categorize content by topics, formats, and contributor profiles.
- Implement a role-based content management system (RBAC).
- Integrate multi-channel discovery (Web, YouTube, TikTok/Shorts).
- Ensure a low-friction, accessible UX for users with cognitive fatigue or anxiety.
- Promote awareness of the importance of professional therapy.
- Build a safe, moderated community around vetted content.

---

## 6. Technology as Added Value

PRESENTE is not merely a content creator; it is an independent digital infrastructure. A single core topic (e.g., a conversation between a psychologist and a pastoral leader) is re-purposed into:
- Full video episode (YouTube)
- Audio podcast (for commuting/listening)
- Short social clips (TikTok / Reels)
- Written summary and actionable guide (PDF)

---

## 7. Conceptual Architecture

- **Presentation Layer:** Responsive web interface (Mobile & Desktop).
- **Application Layer:** Backend managing authenticated users, catalogues, and workflows.
- **Data Layer:** Relational database storing structured content and metrics.
- **CMS & RBAC:** Granular role-based permissions (Admin, Authorized Publishers, Users).
- **Multimedia Integration:** YouTube embeds and cloud object storage.

---

## 8. Publishing Model & Access Control

- **Admin:** Full platform moderation, category management, content approval.
- **Authorized Publisher:** Psychologists, psychiatrists, pastoral leaders, occupational therapists.
- **User:** Browse, read, listen, watch, and download authorized materials. Unmoderated posting and raw file uploads are explicitly excluded in the MVP.

---

## 9. PRESENTE Community

A safe, curated digital space where users interact through moderated comments, reactions, and structured exercises.

---

## 10. Content Pillars

1. **Psychology & Mental Health:** Emotional regulation, sleep hygiene, crisis coping, recovery routines.
2. **Spirituality & Pastoral:** Life purpose, hope, reflection, interfaith respect.
3. **Well-being & Occupational Therapy:** Mindfulness, breathing exercises, healthy habits, creative expression.
4. **Family Guides & Lived Experiences:** Caregiver guidance and curated recovery stories.

---

## 11. Multimedia & Social Media Strategy

Social channels (TikTok, YouTube) act as discovery touchpoints, while the PRESENTE platform serves as the central hub for deep dives and tools.

---

## 12. User Experience (UX) Principles

Intent-based navigation (*"What are you looking for today?"*), minimal cognitive friction, high contrast, and mobile-first responsiveness.

---

## 13. Institutional Partnerships

**Clínica San Juan de Dios (Manizales)** serves as the incubator and initial collaborative space, while PRESENTE retains independent project governance.

---

## 14. Scope & Clinical Boundaries

PRESENTE provides accompaniment and psychoeducation. **It does NOT provide clinical diagnoses or replace emergency medical/psychiatric care.**

---

## 15. Phased Roadmap & Sustainability

Built in 6 progressive phases (Definition, MVP Development, Seed Content, Launch, Validation, Evolution). Initial operations run entirely on **$0 USD free-tier infrastructure**.

---
---

# 16. Detailed Technical Architecture, Multiplatform Ecosystem & Zero-Cost Deployment ($0 USD)

To guarantee technical excellence and complete financial transparency for **Clínica San Juan de Dios**, the system engineering specifications are outlined below:

---

### 16.1. Multiplatform Delivery: Web App and Hybrid Mobile App (Android & iOS)

Built with **Angular** and **Capacitor**, enabling three distribution channels from a single codebase:

1. **Responsive Web App / PWA:** Instant browser access without requiring device storage.
2. **Android Mobile App (.apk / .aab):** Native package for Android smartphones and tablets.
3. **iOS Mobile App (.ipa):** Native package for iPhone and iPad via TestFlight / App Store.

![Multiplatform Architecture](assets/multiplatform-web-app-diagram.jpg)

---

### 16.2. Software Architecture: Clean Architecture with Inversion of Control (IoC)

The backend is built in **Python (FastAPI)** following Clean Architecture principles:

- **1. Domain Core (`src/domain/`):** Pure enterprise entities, domain exceptions, and repository contracts (`abc.ABC`).
- **2. Application Layer (`src/application/`):** Use cases and input/output DTO validation schemas (`Pydantic`).
- **3. Infrastructure Layer (`src/infrastructure/`):** PostgreSQL database with async SQLAlchemy 2.0, storage adapters, and AI clients.
- **4. Presentation Layer (`src/api/`):** FastAPI REST routers with Inversion of Control (`Depends`) for dependency injection.

![Clean Architecture Diagram](assets/clean-architecture-diagram.jpg)

---

### 16.3. Cloud Server Hosting, Free PaaS & Institutional Financial Guarantee ($0 USD)

| Component | Free Provider | Cost | Operational Guarantee for the Clinic |
| :--- | :--- | :--- | :--- |
| **Frontend Web** | **Vercel / Cloudflare Pages** | **$0 USD (Free)** | Global CDN, automated SSL HTTPS, zero hosting fees. |
| **Backend API (PaaS)** | **Render.com / Oracle Always Free** | **$0 USD (Free)** | Modern PaaS alternative to Heroku running FastAPI without monthly charges. |
| **Database** | **Supabase (PostgreSQL)** | **$0 USD (Free)** | Managed relational database with 500 MB storage and automated backups. |
| **Artificial Intelligence** | **Google AI Studio (Gemini 2.0 Flash)** | **$0 USD (Free)** | 1M tokens/call free quota for therapeutic summaries and categorization. |
| **Multimedia Hosting** | **YouTube Embeds + Supabase** | **$0 USD (Free)** | Streaming video and audio without incurring server bandwidth costs. |

![Zero Cost Deployment Diagram](assets/zero-cost-deployment-diagram.jpg)

> [!IMPORTANT]
> **Financial Guarantee for Clínica San Juan de Dios:**  
> Clínica San Juan de Dios **assumes ZERO costs for servers, software licensing, databases, or technical maintenance**. The digital infrastructure is 100% self-sustained and independently managed.
