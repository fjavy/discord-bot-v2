import discord
import random
import requests
import os
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import gen_emodji

with open("token.txt", "r") as f: #Membaca token dari file token.txt
    token = f.read() #Menyimpan token ke dalam variabel baru

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
async def passwd(ctx):
    await ctx.send(gen_pass(5))

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def mem(ctx):
    nama_images = random.choice(os.listdir('images'))
    with open(f'images/{nama_images}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah anjing (dog), program akan memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('fox')
async def fox(ctx):
    '''Setelah kita memanggil perintah rubah (fox), program akan memanggil fungsi get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

def get_pokemon_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('pokemon')
async def pokemon(ctx):
    '''Setelah kita memanggil perintah pokemon, program akan memanggil fungsi get_pokemon_image_url'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run(token)