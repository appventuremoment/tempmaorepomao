# Stability AI API
import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/3d/stable-fast-3d",
    headers={
        "authorization": f"Bearer sk-APIKEY",
    },
    files={
        "image": open("./man_image_testing.jpg", "rb")
    },
    data={},
)

if response.status_code == 200:
    print('Success!')
    with open("./3d-cat-statue.glb", 'wb') as file:
        file.write(response.content)
        print('Writing to file')
else:
    raise Exception(str(response.json()))