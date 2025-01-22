import requests

# Access Token and Page ID
ACCESS_TOKEN = ""
PAGE_ID = ""

def post_to_facebook(message, link=None):
    """Post content to Facebook Page using Graph API."""
    url = f"https://graph.facebook.com/v22.0/{PAGE_ID}/feed"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    # Post data
    data = {"message": message}
    if link:
        data["link"] = link

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        print("[SUCCESS] Post created:", response.json())
    except requests.exceptions.RequestException as e:
        print("[ERROR] Failed to create post:", e)
        print("[DEBUG] Response:", e.response.json() if e.response else "No response")

# Example Post
post_message = "Hello, world! This is a test post . Visit us at https://www.elcpp.com"
post_to_facebook(post_message)
