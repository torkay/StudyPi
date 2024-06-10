import discord
import datetime
import asyncio

# Your schedule data
schedule = {
    "Monday, July 8, 2024": [
        {"time": "9:00AM - 12:00PM", "units": ["ICTPRG430", "ICTPRG549", "ICTPRG534"]},
        {"time": "1:00PM - 4:00PM", "units": ["ICTPRG430", "ICTPRG549", "ICTPRG534"]}
    ],
    # Add more days and their lessons here
}

# Function to check if there are lessons today
def check_lessons_today():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return today in schedule

# Function to get the details of today's lessons
def get_lessons_today():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return schedule[today]

# Function to format lesson details into an embed
def format_lesson_embed(lessons):
    embed = discord.Embed(title="Today's Lessons", color=0x00ff00)
    for lesson in lessons:
        time = lesson["time"]
        units = ", ".join(lesson["units"])
        embed.add_field(name=time, value=units, inline=False)
    return embed

# Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def lesson_notification():
    await client.wait_until_ready()
    while not client.is_closed():
        if check_lessons_today():
            lessons = get_lessons_today()
            embed = format_lesson_embed(lessons)
            channel = client.get_channel(YOUR_CHANNEL_ID)  # Replace YOUR_CHANNEL_ID with your channel ID
            await channel.send(embed=embed)
        await asyncio.sleep(7200)  # Check every 2 hours

client.loop.create_task(lesson_notification())
client.run('YOUR_TOKEN')  # Replace YOUR_TOKEN with your bot token
