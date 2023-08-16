import requests
from google.auth import default
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

DEFAULT_BASE_URL = "https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models/imagetext:predict"

class ImageTextCaptions:
    def __init__(self, project_id, credentials_path=None, base_url=DEFAULT_BASE_URL):
        self.project_id = project_id
        self.base_url = base_url

        if credentials_path:
            creds = Credentials.from_authorized_user_file(credentials_path)
        else:
            # Get the default credentials set by gcloud auth
            creds, _ = default()

        if not creds.valid:
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())

        self.headers = {
            "Authorization": f"Bearer {creds.token}",
            "Content-Type": "application/json; charset=utf-8",
        }

    def caption(self, b64_image, response_count, language_code):
        """
        Generate a caption for an image using Google AI's Vertex AI Platform.

        Args:
            b64_image (str): Base64 encoded image string.
            response_count (int): Number of responses desired.
            language_code (str): Language code for the prediction.

        Returns:
            dict: Response from the VertexAI Platform.
        """

        data = {
            "instances": [
                {
                    "image": {
                        "bytesBase64Encoded": b64_image
                    }
                }
            ],
            "parameters": {
                "sampleCount": response_count,
                "language": language_code
            }
        }

        response = requests.post(
            self.base_url.format(project_id=self.project_id),
            headers=self.headers,
            json=data
        )

        if response.status_code != 200:
            raise ValueError(f"Error making the prediction: {response.text}")

        return response.json()
