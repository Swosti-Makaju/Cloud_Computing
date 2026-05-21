from flask import Flask, render_template, request, redirect, url_for, send_file
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pathlib import Path
import os
import io

# Load .env file from the project directory
env_path = Path(__file__).with_name(".env")
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

# Azure Configuration
connection_string = os.getenv("AZURE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")
if not connection_string or not container_name:
    raise RuntimeError(
        "Missing AZURE_CONNECTION_STRING or CONTAINER_NAME. "
        "Set them in .env or the environment before running the app."
    )

# Debug check
print("Connection String Loaded:", connection_string)
print("Container Name:", container_name)

# Azure Blob Client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)


# Home Page
@app.route('/')
def index():
    blobs = container_client.list_blobs()
    files = [blob.name for blob in blobs]

    return render_template('index.html', files=files)


# Upload File
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file:
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file, overwrite=True)

    return redirect(url_for('index'))


# Download File
@app.route('/download/<filename>')
def download_file(filename):
    blob_client = container_client.get_blob_client(filename)

    stream = io.BytesIO()
    download_stream = blob_client.download_blob()

    stream.write(download_stream.readall())
    stream.seek(0)

    return send_file(
        stream,
        as_attachment=True,
        download_name=filename
    )


# Delete File
@app.route('/delete/<filename>')
def delete_file(filename):
    blob_client = container_client.get_blob_client(filename)

    blob_client.delete_blob()

    return redirect(url_for('index'))


# Generate Secure Temporary Link
@app.route('/generate-link/<filename>')
def generate_link(filename):

    sas_token = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=filename,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(minutes=10)
    )

    blob_url = (
        f"https://{blob_service_client.account_name}.blob.core.windows.net/"
        f"{container_name}/{filename}?{sas_token}"
    )

    return f"""
    <h3>Temporary Secure Link</h3>
    <a href="{blob_url}" target="_blank">{blob_url}</a>
    """


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)