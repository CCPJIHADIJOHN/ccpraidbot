import discord
import asyncio

async def delete_safe(message):
    try:
        await message.delete()
    except:
        pass

async def send_ephemeral_delete(interaction: discord.Interaction, content: str, delay: float = 2.0):
    await interaction.response.send_message(content, ephemeral=True)
    msg = await interaction.original_response()
    
    async def delete_later():
        await asyncio.sleep(delay)
        await delete_safe(msg)
    
    asyncio.create_task(delete_later())

def format_urls(urls: list, min_count: int = 3, max_count: int = 5):
    import random
    amount = random.randint(min_count, max_count)
    chosen = random.sample(urls, k=min(amount, len(urls)))
    while True:
        text = "\n".join(f"{url} | [HIDE GIF]({url})" for url in chosen)
        if len(text) < 1999:
            break
        if not chosen:
            return None
        chosen.pop()
    return text if text.strip() else None
