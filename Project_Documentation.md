# 📘 Detailed Project Documentation: Showcase

This document provides a comprehensive technical breakdown of the Serverless To-Do List application, detailing each AWS service's role and configuration.

---

## 🎨 Frontend UI
**Purpose:** Provide a seamless, responsive user interface for task management.

### Implementation Details
- **Architecture:** Single-page application (SPA) model.
- **Technologies:** 
    - **HTML:** Semantic structure and core layout.
    - **CSS:** Custom styling for a modern, clean look.
    - **JavaScript:** Fetch API for asynchronous CRUD operations.
- **Deployment:** Optimized for static hosting on Amazon S3.

![Frontend UI](./Img/Thefrontend-app.png)

---

## ⚡ CloudFront (CDN)
**Purpose:** Global distribution and secure content delivery.

### Configuration
- **Origin:** S3 Bucket hosting the `index.html`.
- **Caching:** Configured with a 30-second TTL for frequent content updates.
- **Root Object:** `index.html`.
- **Protocols:** Enabled HTTP/1.1 and HTTP/2 for performance.
- **Security:** OAI (Origin Access Identity) integration for restricted S3 access.

![CloudFront Settings](./Img/cloudfront-setting.png)

---

## 📦 S3 Bucket (Storage)
**Purpose:** Secure storage for static frontend assets.

### Setup Highlights
- **Public Access:** Blocked (Public access is handled exclusively via CloudFront).
- **Static Hosting:** Enabled for the frontend file.
- **Permissions:** Restricted bucket policy allowing only CloudFront read access.

![S3 Policy](./Img/S3-policy.png)

---

## 🛡️ API Gateway
**Purpose:** Managed entry point and request routing for backend services.

### API Details
- **Type:** HTTP/REST API.
- **Integrations:** Direct proxy to AWS Lambda functions.
- **CORS Configuration:**
    - **Allowed Origins:** `*` (Configurable for production).
    - **Allowed Headers:** `Content-Type`, `Authorization`.
    - **Allowed Methods:** `GET`, `POST`, `PUT`, `DELETE`.

![API Gateway](./Img/Api_gateway.png)

---

## ⚙️ Lambda Functions
**Purpose:** Serverless execution of business logic for task CRUD operations.

### Function Registry
- **Language:** Python 3.x.
- **Operations:**
    - `createTask`: Handles new task creation in DynamoDB.
    - `getTasks`: Lists all existing tasks.
    - `updateTask`: Modifies task status or content.
    - `deleteTask`: Removes tasks from the database.
- **Environment:** Each function is isolated and triggered via API Gateway events.

![Lambda Overview](./Img/Lambda-fonctions.png)

---

## 🔄 End-to-End Execution Flow
1. **User Interaction:** User clicks "Add Task" on the CloudFront-hosted site.
2. **API Trigger:** Frontend sends a signed request to API Gateway.
3. **Logic Execution:** API Gateway triggers the `createTask` Lambda function.
4. **Data Persistence:** Lambda writes the task entry into Amazon DynamoDB.
5. **Response:** A success status is returned to the frontend, which updates the UI.

![Architecture Diagram](./Img/diagram-manara.png)

---
[⬅️ Back to README](./README.md)
