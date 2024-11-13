import discord
from discord.ext import commands
Repl.it
# إعداد البوت
bot = commands.Bot(command_prefix="!")

# التأكد من تشغيل البوت
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# أمر لحساب الضريبة وتوزيعها
@bot.command()
async def tax(ctx, total: float):
    # حساب 10% للشخص الأول والثاني
    person_one_share = total * 0.10
    person_two_share = total * 0.10
    # الباقي يذهب للشخص الثالث
    person_three_share = total - (person_one_share + person_two_share)

    # عرض النتائج
    await ctx.send(f"Total Amount: {total}")
    await ctx.send(f"Person 1 Share (10%): {person_one_share}")
    await ctx.send(f"Person 2 Share (10%): {person_two_share}")
    await ctx.send(f"Person 3 Share (Remaining): {person_three_share}")

# تشغيل البوت باستخدام التوكن
bot.run("Y_8MUHbWzgWUqEyX28YDU-5KmtwChIMf")

