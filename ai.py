import openai
inp=input("Enter the prompt: ")
openai.api_key = open("key.txt", "r").read ()
response = openai.Image.create(
prompt=inp,
n=5,
size="1024x1024"
)
image_url = response ['data'][0]['url']
print(response['data'])
print (image_url)