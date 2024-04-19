# import sys
# sys.path.append('/home/mick/Documents/S24_Chain_Cards/backend/AI_comp')
# from ai import starter_pack
from easy_pil import Editor, Font
import textwrap


main = Font("/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/Vecna.otf", size=50)
desc =  Font("/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/Vecna.otf", size=35)
stats = Font("/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/Vecna Bold.otf", size=35)
# character = starter_pack[0]
character = {
    "Name": "Aurora Silverleaf",
    "Race": "Half-Elf",
    "Class": "Wizard",
    "Stats": {
        "STR": "8",
        "DEX": "14",
        "CON": "12",
        "INT": "20",
        "WIS": "10",
        "CHA": "16"
    },
    "Backstory": "Aurora was trained in the arcane arts by a powerful wizard, learning to harness the forces of magic to shape reality to her will. She now seeks out ancient secrets and forbidden knowledge, using her powers to unlock the mysteries of the universe.",
    "Equipment": " Robes, spellbook, arcane focus, components pouch\nWeapon: None"
}
background = Editor("/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/card_bg.png")
pfp = Editor("/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/pfp.png").resize((804,595))
background.paste(pfp.image, (83,158))
# square = Canvas((300, 300))
# square = Editor(canvas=square)

Class = Editor(f'/home/mick/Documents/S24_Chain_Cards/backend/testing/truffle/assets/{(character["Class"]).lower().strip(" ")}.png').resize((100,100))
background.paste(Class.image, (786,847))
background.text((80, 90), character["Name"], font=main, color="black")
background.text((80, 780), character["Race"], font=main, color="black")
background.text((85, 850), "Stats:", font=main, color="black")
background.text((85, 915), "STR:", font=stats, color="black")
background.text((160, 915), character["Stats"]["STR"], font=stats, color="black")
background.text((200, 915), "DEX:", font=stats, color="black")
background.text((275, 915), character["Stats"]["DEX"], font=stats, color="black")
background.text((315, 915), "CON:", font=stats, color="black")
background.text((390, 915), character["Stats"]["CON"], font=stats, color="black")
background.text((430, 915), "INT:", font=stats, color="black")
background.text((505, 915), character["Stats"]["INT"], font=stats, color="black")
background.text((545, 915), "WIS:", font=stats, color="black")
background.text((620, 915), character["Stats"]["WIS"], font=stats, color="black")
background.text((660, 915), "CHA:", font=stats, color="black")
background.text((735, 915), character["Stats"]["CHA"], font=stats, color="black")
background.text((85, 965), "Backstory:", font=main, color="black")
lines = textwrap.wrap(character["Backstory"], width=50)
i = 0;
for line in lines:
    width, height = desc.getsize(line)
    background.text((86, 1015+(33*i)), line, font=desc, color="red")
    i += 1;
background.show()