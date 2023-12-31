# ImageTextCaptions

A Python module to generate captions for images using Google AI's Vertex AI Platform.

## Overview

The `ImageTextCaptions` class provides an intuitive interface for generating textual captions for images. By simply passing a base64 encoded image, users can get insightful and accurate captions for their visual content.

## Features

- Easy integration with Google AI's Vertex AI Platform.
- Support for custom Google Cloud Project IDs.
- Flexibility to use either a Google Cloud credentials file or rely on `gcloud auth`.
- Option to set a custom base URL for the API endpoint.

## Installation

Ensure you have the required libraries:

```bash
pip install requests google-auth
```

To install ImageTextCaptions:

```bash
pip install ImageTextCaptions
```

## Usage

Convert Image to Base64:
```python
import base64

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
```

Generate Captions:

```python
from imagetext_captions import ImageTextCaptions

# Convert your image to base64
b64_image = convert_image_to_base64("path_to_your_image.jpg")

# Instantiate with your Google Cloud Project ID
captions = ImageTextCaptions("YOUR_PROJECT_ID")

# Define the number of responses you want and the language code
response_count = 1
language_code = "en"

# Generate captions
response = captions.caption(b64_image, response_count, language_code)

# Print the captions from the response
for caption in response["predictions"]:
    print(caption)
```

Using a Google Cloud Credentials File:

```python
captions = ImageTextCaptions("YOUR_PROJECT_ID", credentials_path="path_to_your_google_cloud_credentials.json")
```

Specifying a Custom Base URL:

```python
custom_url = "https://your_custom_base_url/v1/projects/{project_id}/locations/some_location/publishers/google/models/imagetext:predict"
captions = ImageTextCaptions("YOUR_PROJECT_ID", base_url=custom_url)
```

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
