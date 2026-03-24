# 📝 Serverless To-Do List Application

[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Serverless](https://img.shields.io/badge/Serverless-platform-FD5750?style=flat&logo=serverless)](https://www.serverless.com/)

A modern, high-performance **Serverless To-Do List** application built as a graduation project for the **Manara Learning Path**. This project showcases a robust full-stack architecture leveraging AWS cloud-native services for scalability, security, and global delivery.

---

## 🚀 Overview

This application allows users to seamlessly manage tasks through a clean, responsive web interface. By utilizing a serverless approach, the solution minimizes operational overhead while ensuring high availability and low latency.

### Key Features
- **CRUD Operations:** Create, Read, Update, and Delete tasks with real-time feedback.
- **Global Delivery:** Hosted on S3 and served via CloudFront for lightning-fast loading worldwide.
- **RESTful API:** Securely exposed via Amazon API Gateway.
- **Scalable Backend:** Event-driven Python Lambda functions handle business logic.
- **NoSQL Storage:** Amazon DynamoDB provides persistent, high-speed storage.

---

## 🛠️ Tech Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript | Modern, responsive UI |
| **Hosting** | Amazon S3 & CloudFront | Static hosting & CDN delivery |
| **API Layer** | Amazon API Gateway | RESTful interface management |
| **Compute** | AWS Lambda (Python) | Serverless business logic |
| **Database** | Amazon DynamoDB | Scalable NoSQL database |
| **Security** | IAM Roles & Policies | Least-privileged access control |

---

## 📐 Architecture

The application follows a best-practice serverless architecture:

1.  **Request Flow:** User triggers an action in the browser.
2.  **Frontend Delivery:** CloudFront serves the static frontend from an S3 bucket.
3.  **API Interaction:** The frontend sends a REST request to API Gateway.
4.  **Compute:** API Gateway triggers the relevant AWS Lambda function.
5.  **Data Persistence:** Lambda interacts with DynamoDB to store or retrieve data.

![Architecture Diagram](./Img/diagram-manara.png)

---

## 📂 Project Structure

```text
.
├── Backend/                # Serverless compute logic
│   ├── createTask/         # Lambda: Create new tasks
│   ├── deleteTask/         # Lambda: Delete tasks
│   ├── getTasks/           # Lambda: Retrieve all tasks
│   └── update_task/        # Lambda: Modify existing tasks
├── Frontend/               # Web interface
│   └── index.html          # Combined HTML, CSS, and JS
├── Img/                    # Documentation assets & screenshots
├── LICENSE                 # MIT License
├── Project_Documentation.md # Detailed technical specifications
└── README.md               # Project overview & entry point
```

---

## ⚙️ Deployment & Setup

### Prerequisites
- [AWS Account](https://aws.amazon.com/free/) with administrative access.
- [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- Python 3.x for local Lambda testing (optional).

### 1. Backend Configuration
1.  **DynamoDB:** Create a table named `Tasks` with `id` as the Primary Key (Type: String).
2.  **Lambda:** Deploy the Python scripts located in the `Backend/` directory.
3.  **API Gateway:** Create a REST API and map the HTTP methods (POST, GET, PUT, DELETE) to their respective Lambda functions.

### 2. Frontend Configuration
Open `Frontend/index.html` and update the `API_BASE` constant with your deployed API Gateway endpoint:

```javascript
const API_BASE = "https://your-api-id.execute-api.region.amazonaws.com/prod";
```

### 3. S3 & CloudFront Setup
1.  Create an S3 bucket and upload the `Frontend/index.html` file.
2.  Create a CloudFront distribution pointing to your S3 bucket.
3.  Update bucket permissions to allow access from the CloudFront Origin Access Identity (OAI).

---

## 📸 UI Showcase

| Main Dashboard | Architecture View |
| :---: | :---: |
| ![Frontend UI](./Img/Thefrontend-app.png) | ![Flow Diagram](./Img/diagram-manara.png) |

---

## 🗺️ Roadmap
- [ ] **Authentication:** Integrate Amazon Cognito for User Login/Sign-up.
- [ ] **Notifications:** Add AWS SNS for task reminders.
- [ ] **PWA Support:** Enable offline functionality.
- [ ] **Multi-language:** Add I18n support.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🤝 Acknowledgments
- **Manara Learning Path** for the mentorship and project guidance.
- The AWS Community for providing excellent documentation.

---
<p align="center">Made with ❤️ by Houssem Rezgui</p>

