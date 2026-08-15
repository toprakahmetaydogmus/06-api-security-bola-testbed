# API Security & Broken Object Level Auth (BOLA / IDOR) Defense

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI Quality Gate](https://github.com/toprakahmetaydogmus/06-api-security-bola-testbed/actions/workflows/ci.yml/badge.svg)](https://github.com/toprakahmetaydogmus/06-api-security-bola-testbed/actions)
[![OWASP API](https://img.shields.io/badge/OWASP-API1%3A2023%20BOLA-red.svg)](#)

Geliştirici: **Toprak Ahmet Aydoğmuş**

FastAPI ile geliştirilmiş, OWASP API Top 10 (özellikle API1:2023 BOLA) açıklarını gösteren ve ABAC (Attribute-Based Access Control) ile güvenli hale getiren testbed.

---

## 🏗️ Karşılaştırmalı API Güvenlik Mimarisi

```mermaid
graph LR
    Client[Client Request: doc_102] --> Vulnerable["/vulnerable/documents/doc_102<br/>(No Authorization Check)"]
    Vulnerable -->|200 OK| LeakedData[Unauthorized Bob Private Data Leaked]

    Client --> Secure["/secure/documents/doc_102<br/>(JWT + ABAC Validator)"]
    Secure -->|403 Forbidden| Blocked[BOLA Violation Blocked & Logged]
```

---

## ⚡ Hızlı Başlangıç & Test

```bash
git clone https://github.com/toprakahmetaydogmus/06-api-security-bola-testbed.git
cd 06-api-security-bola-testbed

python -m unittest discover tests/
```

---

## 📜 Lisans
MIT License - **Toprak Ahmet Aydoğmuş**
