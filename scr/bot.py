import os
import asyncio
from facebook_scraper import get_posts
from discord.ext import commands, tasks

# Thay thế bằng token bot Discord của bạn
DISCORD_TOKEN = 'MTA5Njc3OTU5Mjg0NjU0NTA1Ng.Ggdbi4.FNn9DofcHJ1flmNoNgBWvXhAWDjaAeJNesmvBY'
# Thay thế bằng ID nhóm Facebook của bạn
FB_GROUP_ID = '957955702015040'
# Thay thế bằng ID kênh Discord mà bạn muốn gửi thông báo
DISCORD_CHANNEL_ID = 1106527441763184680

bot = commands.Bot(command_prefix='!')

latest_post_id = None

@bot.event
async def on_ready():
    print(f'{bot.user} đã kết nối với Discord!')
    check_new_posts.start()

@tasks.loop(minutes=5)
async def check_new_posts():
    print("Đang kiểm tra bài viết mới...")