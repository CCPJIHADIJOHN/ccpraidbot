import os
import io
import random
import discord

FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commands", "files")

def get_random_path():
    if not os.path.isdir(FILES_DIR):
        return None
    paths = [os.path.join(FILES_DIR, f) for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
    return random.choice(paths) if paths else None

def load_all():
    files = []
    if not os.path.isdir(FILES_DIR):
        return files
    for f in os.listdir(FILES_DIR):
        path = os.path.join(FILES_DIR, f)
        if os.path.isfile(path):
            try:
                with open(path, "rb") as fp:
                    files.append((f, fp.read()))
            except:
                pass
    return files

def get_random_bytes():
    files = load_all()
    return random.choice(files) if files else (None, None)

async def send_with_file(interaction: discord.Interaction, content: str):
    name, data = get_random_bytes()
    if name and data:
        bio = io.BytesIO(data)
        await interaction.followup.send(content=content, file=discord.File(bio, filename=name))
        bio.close()
    else:
        await interaction.followup.send(content=content)
