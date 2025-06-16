import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer sk-APIKEY",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Old man with scoliosis slouching and standing still while wearing a beanie and holding a walking stick",
        "output_format": "png",
    },
)

if response.status_code == 200:
    print('Success!')
    with open("./old_man_test.png", 'wb') as file:
        file.write(response.content)
        print(response.content[:100])
        print('Written')
        file.close()
else:
    print('Failure!')
    raise Exception(str(response.json()))


# Stability AI API
import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/3d/stable-fast-3d",
    headers={
        "authorization": f"Bearer sk-APIKEY",
    },
    files={
        "image": open("./old_man_test.png", "rb")
    },
    data={},
)

if response.status_code == 200:
    print('Success!')
    with open("./output.glb", 'wb') as file:
        file.write(response.content)
        print('Writing to file')
        file.close()
else:
    raise Exception(str(response.json()))