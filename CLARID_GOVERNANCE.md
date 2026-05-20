# ClarID Platform Governance

This repository builds ClarID — a portable, patient-controlled health identity and interoperability platform.

## 1. Architecture Principles

- Backend: FastAPI (Python 3.11+)
- Database: PostgreSQL with logical schemas: identity, clinical, audit
- ORM: SQLAlchemy 2.0
- Migrations: Alembic only; no Base.metadata.create_all in application startup
- Frontend: React + TypeScript + Tailwind
- Auth: JWT access token plus rotating HttpOnly refresh cookie
- Encryption: AES-256-GCM with RSA-OAEP key wrapping
- FHIR: US Core R4-compliant serializers
- CI: GitHub Actions required
- No secrets committed to repo

## 2. Database Structure

Schemas:

- identity
- clinical
- audit

Never collapse schemas.

## 3. Security Requirements

- HttpOnly refresh cookie
- Strict CORS using configured frontend origins
- Rate limiting on auth endpoints
- Structured logging
- Token rotation
- Audit logging for all patient access
- Encryption centralized in app/security/

## 4. FHIR Requirements

- All FHIR resources must declare US Core profile in meta.profile
- FHIR validation must run in CI when FHIR resources are implemented
- No custom schema that conflicts with US Core

## 5. Development Rules

- All database changes require Alembic migration
- All features require tests
- No wildcard CORS
- No inline secrets
- Follow 12-factor app principles

## 6. Deployment Target

- Initial hosting: Render
- Must remain AWS-migration compatible
- Container-friendly design

## 7. Milestone Order

Phase 1 – Infrastructure Hardening
Phase 2 – US Core FHIR Engine
Phase 3 – Encrypted Snapshot Engine
Phase 4 – Device-Bound Vault + PWA
Phase 5 – OAuth + SMART Scaffold
Phase 6 – AI Risk Engine
Phase 7 – Scale & Exit Readiness

Do not skip milestone order.
