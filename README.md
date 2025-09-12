# manara-repo
Manara Learning Path Graduation Project: Serverless To-Do List Application

# 📝 To-Do List Application – Manara Learning Path Graduation Project

| 🚀 Feature Request | 🐛 Bug Report | ❓ General Question |

**Note:** This project demonstrates a full-stack serverless To-Do List application. The frontend is a single HTML file (with CSS and JS) hosted on S3 and served via **CloudFront**, and the backend uses AWS API Gateway + Lambda (Python) + DynamoDB.

---

## Table of Contents

- [Solution Overview](#solution-overview)  
- [Architecture Diagram](#architecture-diagram)  
- [Frontend & Backend Setup](#frontend--backend-setup)  
- [Customizing the Solution](#customizing-the-solution)  
- [Prerequisites](#prerequisites)  
- [Deployment Steps](#deployment-steps)  
- [Screenshots](#screenshots)  
- [License](#license)  

---

## Solution Overview

The To-Do List application allows users to **add, update, delete, and view tasks**. It demonstrates a **serverless architecture** optimized for CRUD operations:

- **Frontend:** Single-page HTML, CSS, and JavaScript  
- **Backend:** AWS Lambda functions (Python) exposed via API Gateway REST API  
- **Database:** DynamoDB for persistent storage  
- **Hosting:** Frontend served via **S3 + CloudFront** for fast global delivery  

This project is suitable for learning **serverless application development** and **AWS cloud services integration**.

---

## Architecture Diagram

**Flow:**  
*CloudFront → S3 (frontend) → Browser → API Gateway → Lambda (Python CRUD) → DynamoDB*
     Web Browser (User)
        │
        ▼
  ┌─────────────┐
  │ CloudFront  │  ← Public-facing entry point
  └─────┬──────┘
        │
        ▼
  ┌─────────────┐
  │     S3      │  ← Stores index.html (frontend files)
  │  Static     │
  │  Website    │
  └─────┬──────┘
        │
        ▼
  ┌─────────────┐
  │ API Gateway │  ← Backend API endpoint
  │  REST API   │
  └─────┬──────┘
        │
        ▼
  ┌─────────────┐
  │   Lambda    │  ← Python CRUD
  └─────┬──────┘
        │
        ▼
  ┌─────────────┐
  │ DynamoDB    │
  │  Tasks Table│
  └─────────────┘



![Architecture Diagram](./docs/architecture.png)

---

## Frontend & Backend Setup

### Prerequisites

- AWS Account with appropriate permissions  
- AWS CLI installed and configured  
- Basic knowledge of Lambda and DynamoDB  

### Deployment Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/<houssem530>/<manara-repo>.git
cd <manara-repo>

Configure Frontend

Open index.html and update the API_BASE variable with your API Gateway URL:

const API_BASE = "https://abc123.execute-api.eu-west-3.amazonaws.com/prod";

3. Deploy Frontend to S3 + CloudFront<img width="642" height="249" alt="diagram-manara" src="https://github.com/user-attachments/assets/25082552-6516-42e3-b70a-8a4425fc8ff2" />


Create an S3 bucket (enable static website hosting)

Upload index.html

Create a CloudFront distribution pointing to the S3 bucket

Enable caching and HTTPS if desired

Access your app via the CloudFront URL

4. Deploy Backend

Deploy your Python Lambda functions for CRUD operations (create_task.py, read_tasks.py, update_task.py, delete_task.py)

Create an API Gateway REST API and connect each Lambda to its respective HTTP method

Ensure DynamoDB table (e.g., Tasks) exists with id as the primary key

Customizing the Solution

Update frontend design or styling in index.html

Modify Lambda logic for additional task features

Integrate with other AWS services (e.g., Cognito for authentication)

Screenshots

Include screenshots of the app UI in docs/screenshots/ for demonstration.

License

This project is licensed under the MIT License.


