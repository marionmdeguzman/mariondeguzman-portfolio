# Marion De Guzman — Portfolio

Personal portfolio website built with Flask, showcasing 8+ years of engineering experience across Cloud Infrastructure, Observability, SaaS, and Telco platforms.

## About Marion

**Marion De Guzman** is a Senior Engineering Professional based in Manila, Philippines, currently working as a **Senior Support Engineer at Coralogix** — an international Observability SaaS platform. He is the first Filipino to hold this role at Coralogix, representing excellence for Filipino engineers in the global cloud industry.

With a background spanning Telco operations, AWS cloud architecture, Kubernetes administration, and Observability stacks, Marion operates at the intersection of deep technical expertise and customer success engineering.

### Key Credentials

| Credential | Detail |
|---|---|
| 🎓 B.S. Electronics Engineering | Adamson University, 2011–2017 |
| 🌐 CCNA | Cisco Certified Network Associate, 2019 |
| 🐧 RHCSA | Red Hat Certified System Administrator, 2022 |
| ☁️ AWS SAA | Solutions Architect Associate, 2023 |
| ☸️ CKA | Certified Kubernetes Administrator, 2026 |
| 📜 Licensed ECE | Philippine Electronics Engineer Licensure |

### Career Highlights

- **First Filipino Senior Support Engineer at Coralogix** — pioneering role in APAC
- **2025 Outstanding Support Engineer — Coralogix APAC** — year-end commendation for exceptional customer satisfaction and regional leadership
- **Part-Time ECE Professor** — Adamson University, 2020 (Electronic Devices & Circuit Theory, Electronics Circuits & Design Lab)
- **Technical Speaker** — Cisco & Linux presenter at Adamson University

## Tech Stack

**Cloud & Infra:** AWS (EKS, ECS, EC2, S3, Lambda, Firehose, CloudWatch), Kubernetes, Terraform  
**Observability:** OpenTelemetry, Prometheus, PromQL, ELK Stack, Lucene, Grafana, Coralogix  
**Languages & Tools:** Python, Shell Scripting, Flask, Django, APIs & SDKs  
**Telco:** 3GPP Standards, 4G LTE, Load Balancing, Tier-1 Platform Operations  
**Agents:** FluentD, Filebeat, AlertManager  

## Personal Projects

### Terraform AI Debugger & Deployment Lab
> Internal initiative built for Coralogix

AI-powered Flask web application that assists engineers in diagnosing Terraform errors and managing deployment workflows. Built to reduce operational toil and accelerate infrastructure delivery.

**Stack:** Python, Flask, Terraform, AI/LLM integration  
**Repo:** [TF_Debugger_Deployment_Tool](https://github.com/marionmdeguzman/TF_Debugger_Deployment_Tool) *(currently private — internal project)*

---

### Simple Microservice APM Instrumentation
> Internal lab for APM simulation at Coralogix

Demonstrates end-to-end OpenTelemetry instrumentation of a Python microservice stack with full integration into Coralogix APM — covering distributed tracing, metrics, and log correlation.

**Stack:** Python, OpenTelemetry, Coralogix APM  
**Repo:** [simple_microservice_apm_instrumentation](https://github.com/marionmdeguzman/simple_microservice_apm_instrumentation) *(currently private — internal lab)*

---

### Django EHR MVP
> Personal project

A Django-based Electronic Health Record (EHR) system designed for small clinics and private physicians. Covers patient management, consultation records, prescriptions, and appointment scheduling.

**Stack:** Django, Python, PostgreSQL  
**Repo:** [IMS_2024](https://github.com/marionmdeguzman/IMS_2024) *(currently private — contains personal/patient data)*

---

## Running Locally

```bash
# Clone the repo
git clone https://github.com/marionmdeguzman/mariondeguzman-portfolio.git
cd mariondeguzman-portfolio

# Create virtualenv and install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run Flask (note: macOS AirPlay uses port 5000 — use a different port if needed)
flask run --port 5001
# or
python app.py
```

> **macOS port conflict:** If port 5000 is in use, disable **AirPlay Receiver** in System Settings → General → AirDrop & Handoff, or run on port 5001 with `flask run --port 5001`.

---

**Contact:** deguzmancaptain@gmail.com · Manila, Philippines  
**GitHub:** [github.com/marionmdeguzman](https://github.com/marionmdeguzman)
