
from openai import OpenAI
# Image,
class Character:
    def __init__(self, Name, Race, Class, Stats,  Backstory, Equipment):
        self.Name = Name
        self.Race = Race
        self.Class = Class
        self.Stats = Stats
        # self.Image = Image
        self.Backstory = Backstory
        self.Equipment = Equipment

    def __str__(self):
        return f"{self.Name} {self.Race} {self.Class} {self.Stats} {self.Backstory} {self.Equipment}"

# OpenAI.api_key api_key = OpenAI.api_key
client = OpenAI()

# Define the message containing your prompt
prompt = "create 10 unique d&d characters with stats, equipment, weapon, and a backstory"

# Send the request to GPT-3.5 to generate the completion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
)


chunk = str(response.choices[0].message.content)

generated_characters = chunk.split("\n\n")

# Extract the generated response
names = []
races = []
classes = []
stats = []
equipment = []
backstories = []

for character in generated_characters:
    names.append(character.split("Name: ")[1].split("\n")[0])
    races.append(character.split("Race: ")[1].split("\n")[0])
    classes.append(character.split("Class: ")[1].split("\n")[0])
    stats.append(character.split("Stats:")[1].split("\n")[0])
    equipment.append(character.split("Equipment:")[1].split("\nBackstory")[0])
    backstories.append(character.split("Backstory:")[1])

print("completed")
# Use backstories as prompts for DALL·E to generate images
# images = []
# for story in backstories:
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=story,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )
#     image_url = response.data[0].url
#     images.append(image_url)

# images[i],
starter_pack = []
for i in range(10):
    char = Character(names[i], races[i], classes[i], stats[i],  backstories[i], equipment[i])
    starter_pack.append(char)