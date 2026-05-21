# Azure Blob Storage File Manager

A simple cloud-based file management application built using **Python Flask** and **Azure Blob Storage**.

This application allows users to:

- Upload files
- View uploaded files
- Download files
- Delete files
- Generate secure temporary download links using SAS Token


# Features

✅ Upload files to Azure Blob Storage  
✅ View uploaded files  
✅ Download files  
✅ Delete files  
✅ Generate secure temporary links  
✅ Flask Web Interface  
✅ Azure Cloud Integration


# Technologies Used

## Frontend
- HTML
- Bootstrap 5

## Backend
- Python Flask

## Cloud Service
- Microsoft Azure Blob Storage

## Python Libraries
- Flask
- azure-storage-blob
- python-dotenv


# Azure Services Used

- Resource Group
- Storage Account
- Blob Container

---

# Project Structure

```text
azure-flask-storage-app/
│
├── .env
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md


# Installation

## 1. Clone Project

```bash
git clone https://github.com/Swosti-Makaju/Cloud_Computing.git
cd azure-flask-storage-app

## 2. Install Dependencies

```bash
pip install flask azure-storage-blob python-dotenv
```

Or:

```bash
pip install -r requirements.txt
```


# Azure Setup

## Step 1: Create Resource Group

Create a new Resource Group from Azure Portal.

## Step 2: Create Storage Account

- Select Resource Group
- Choose Region
- Performance → Standard
- Redundancy → LRS

## Step 3: Create Blob Container

Inside Storage Account:

- Go to Containers
- Create a container
- Set access level to Private

## Step 4: Copy Connection String

Storage Account → Access Keys → Connection String


# Environment Variables

Create a `.env` file in project root:

```env
AZURE_CONNECTION_STRING=your_connection_string
CONTAINER_NAME=files
```

# Run Application

```bash
python app.py
```

# Application Functions

## Upload File
Users can upload files to Azure Blob Storage.

## View Files
All uploaded files are displayed on the home page.

## Download File
Users can download files directly from Azure Blob Storage.

## Delete File
Users can remove files from Blob Storage.

## Secure Temporary Link
Generate SAS-based temporary secure links for file sharing.


# Security

- Blob container is private
- Secure access provided using SAS Token
- Temporary links expire automatically


# Learning Outcomes

After completing this project, I learned:

- Azure Blob Storage integration
- Flask web application development
- File handling in Python
- Cloud storage concepts
- Secure file sharing using SAS Tokens


# Future Improvements

- Authentication/Login
- File Search
- Metadata Support
- Upload Progress Bar
- Blob Storage Tier Management