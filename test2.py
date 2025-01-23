import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Facebook Access Token and Page ID
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
PAGE_ID = os.getenv("FB_PAGE_ID")

# Image file to upload
IMAGE_PATH = "elcpp.jpg"

def upload_media_and_create_post():
    print("[DEBUG] Starting media upload...")

    # URL to upload media
    media_url = f"https://graph.facebook.com/v22.0/{PAGE_ID}/photos"

    # Verify if the file exists
    if not os.path.exists(IMAGE_PATH):
        print(f"[ERROR] File not found: {IMAGE_PATH}")
        return

    # Step 1: Upload the image
    with open(IMAGE_PATH, "rb") as image_file:
        files = {
            "source": image_file
        }
        data = {
            "access_token": ACCESS_TOKEN,
            "caption": "ELCPP - Learn English in Phnom Penh! #ELCPP #IELTS"
        }

        try:
            response = requests.post(media_url, files=files, data=data)
            response.raise_for_status()
            media_response = response.json()
            print("[DEBUG] Media uploaded successfully!")
            print("[DEBUG] Media Response:", media_response)

            # Extract the media ID
            media_id = media_response.get("id")
            if not media_id:
                print("[ERROR] Failed to retrieve media ID.")
                return

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to upload media: {e}")
            if e.response is not None:
                print("[DEBUG] Response:", e.response.text)
            return

    # Step 2: Create a post using the uploaded media
    post_url = f"https://graph.facebook.com/v22.0/{PAGE_ID}/feed"
    post_data = {
        "access_token": ACCESS_TOKEN,
        "message": "Check out our latest update from ELCPP! Learn more about our English courses. #ELCPP #LearnEnglish",
        "attached_media[0]": f'{{"media_fbid":"{media_id}"}}'
    }

    try:
        post_response = requests.post(post_url, data=post_data)
        post_response.raise_for_status()
        post_result = post_response.json()
        print("[DEBUG] Post created successfully!")
        print("[DEBUG] Post Response:", post_result)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to create post: {e}")
        if e.response is not None:
            print("[DEBUG] Response:", e.response.text)

if __name__ == "__main__":
    print("[DEBUG] Running Facebook Media Upload and Post Test...")
    upload_media_and_create_post()
