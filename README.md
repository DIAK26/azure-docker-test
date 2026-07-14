# 🐱 Meine erste Web-Seite auf Azure

Ein einfaches Lernprojekt: Eine mit Flask gebaute Index-Seite, 
containerisiert mit Podman und auf einer Azure VM deployed.

![Python](https://img.shields.io/badge/Python-3.x-green)
![Flask](https://img.shields.io/badge/Flask-2.x-orange)
![Podman](https://img.shields.io/badge/Podman-rootless-blue)
![Azure](https://img.shields.io/badge/Azure-VM-0078D4)
![License](https://img.shields.io/badge/License-none-lightgrey)

---

## 📋 Inhaltsverzeichnis

- [Über das Projekt](#-über-das-projekt)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Projektstruktur](#-projektstruktur)
- [✅ Voraussetzungen](#-voraussetzungen)
- [🚀 Lokale Ausführung](#-lokale-ausführung)
- [☁️ Deployment auf Azure VM](#️-deployment-auf-azure-vm)
- [📜 Projektverlauf](#-projektverlauf)
- [🎓 Was ich gelernt habe](#-was-ich-gelernt-habe)

---

## 🏠 Über das Projekt

Dieses Projekt ist im Rahmen meiner IT-Einstiegsreise entstanden. 
Ziel war es, eine einfache Webseite von der lokalen Entwicklung 
bis zur Live-Schaltung auf einer Cloud-VM vollständig selbst 
aufzubauen und zu verstehen.

---

## 🛠️ Tech Stack

| Komponente     | Technologie              |
|----------------|--------------------------|
| Backend        | Python / Flask           |
| Container      | Podman (rootless)        |
| VM             | Debian (Azure)           |
| Versionskontrolle | Git & GitHub          |
| Webserver      | Flask Dev Server         |

---

## 📁 Projektstruktur

```
/
├── app.py              → Flask-Server mit Inline-HTML
├── requirements.txt    → Python-Abhängigkeiten
└── Containerfile       → Build-Anleitung für Podman
```

✅ Voraussetzungen
Python 3.x installiert
Flask (pip install flask)
Podman (alternativ Docker)
Azure Konto mit aktiver VM
Git
🚀 Lokale Ausführung
# Repository klonen
git clone https://github.com/DIAK70/azure-docker-test.git
cd DEIN-REPO

# Abhängigkeiten installieren
pip install -r requirements.txt

# Server starten
python app.py

→ Im Browser öffnen: http://localhost:5000

☁️ Deployment auf Azure VM
1. Container bauen
podman build -t meine-webseite .

2. Container starten
podman run -d -p 80:5000 meine-webseite

3. erreichbar unter
(http://commonsky.australiaeast.cloudapp.azure.com/)
📜 Projektverlauf
Phase	Was passiert ist
🟢 Phase 1	Lokale Entwicklung: Flask-App mit reinem Text gestartet
🟡 Phase 2	Erste VM: Auf Ubuntu mit Docker deployt
🟠 Phase 3	Migration: Wechsel auf Debian VM, Umstieg von Docker → Podman (rootless)
🔵 Phase 4	Live: DNS-Name vergeben, Design verbessert, Hintergrundbild hinzugefügt
ℹ️ Der Wechsel von Docker zu Podman bewusst gewählt, um Container ohne Root-Rechte laufen zu lassen.

🎓 Was ich gelernt habe
🔹 Wie Flask als Webserver funktioniert
🔹 Unterschied zwischen HTML (Inhalt) und Python (Logik)
🔹 Containerisierung mit Docker und Podman
🔹 Deployment auf einer Cloud-VM
🔹 Versionskontrolle mit Git & GitHub
🔹 DNS-Konfiguration in Azure
📝 Lizenz
Keine – reines Lernprojekt. Freut sich aber über Feedback! 😊
