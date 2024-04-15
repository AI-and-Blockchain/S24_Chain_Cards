from openai import OpenAI

client = OpenAI()

# Define the message containing your prompt
prompt = "create 10 unique d&d characters with stats, equipment, weapon, and a backstory"

# Send the request to GPT-3.5 to generate the completion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract the generated response
generated_characters = response['choices'][0]['message']['content']
backstories = [character.split("Backstory: ")[1] for character in generated_characters]

# Print the generated characters
print(generated_characters)
print(backstories)


# Use backstories as prompts for DALL·E to generate images
images = []
for story in backstories:
    response = client.images.generate(
        model="dall-e-3",
        prompt=story,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    images.append(image_url)
    print("Generated Image URL:", image_url)