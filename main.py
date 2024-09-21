import requests

def shorten_link(full_link):
    API_KEY = 'b0e03e47f670a29126f8931c2b68792165b79'
    BASE_URL = 'https://cutt.ly/api/api.php'

    # Ensure URL starts with http or https
    if not full_link.startswith(('http://', 'https://')):
        raise ValueError("The provided URL must start with 'http://' or 'https://'.")

    payload = {'key': API_KEY, 'short': full_link}
    response = requests.get(BASE_URL, params=payload)

    if response.status_code == 200:
        data = response.json()
        if data['url']['status'] == 7:
            return data['url']['shortLink']
        else:
            raise Exception(f"Error: {data['url']['status']} - {data['url']['title']}")
    else:
        raise Exception(f"Request failed with status code: {response.status_code} - {response.text}")

if __name__ == "__main__":
    link_to_shorten = input("Enter the URL to shorten: ")
    try:
        shortened_link = shorten_link(link_to_shorten)
        print(f"Shortened link: {shortened_link}")
    except Exception as e:
        print(f"An error occurred: {e}")
