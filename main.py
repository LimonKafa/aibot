import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}") # bilgisayarımız
            await ctx.send(f"{file_name} isimli resim kayıt edildi.") # discord
            # en önemli bölüm projenin beyni veya karar mekanizması
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name))
    else:
        await ctx.send("Resim yüklü değil !!!")

bot.run("")