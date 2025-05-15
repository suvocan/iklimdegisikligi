import discord
import random
from asyncio import TimeoutError
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='!', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  ! işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.


@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yardim(ctx):
    await ctx.send("IKON botuna hoş geldin! Benim komutlarım " \
    "!yardim,!olaylar. !olaylar komutunu yazdığında sana rastgele bir olay vereceğim. Sende bu olayın küresel ısınmanın sonucu olup olmadığını    (evet veya hayır). bende sana cevabının" \
        " doğru mu yanlış mı olduğunu söyleyeceğim. Eğer doğruysa seni tebrik edeceğim.")
    
@bot.command()
async def olay(ctx):
    olaylar = [
        ("Buzulların erimesi", ["evet","hayır"], "evet"),
        ("karbon salınımının artması.", ["evet","hayır"], "evet"),
        ("Sıcak hava dalgaları", ["evet","hayır"], "evet"),
        ("Kuraklık",["evet","hayır"], "evet"),
        ("Aşırı yağışlar",["evet","hayır"], "evet"),
        ("Hava kirliliği",["evet","hayır"], "evet"),
        ("Okyanus asitlenmesi",["evet","hayır"], "evet"),
        #küresel ısınmanın sonucu olmayanlar
        ("Yer altı su seviyelerinin yükselmesi",["evet","hayır"], "hayır"),
        ("Buzulların kalınlaşması",["evet","hayır"], "hayır"),
        ("Kar yağışlarının artması",["evet","hayır"], "hayır"),
        ("Sıcaklıkların düşmesi",["evet","hayır"], "hayır"),
        ("Yağışların azalması",["evet","hayır"], "hayır"),
        ("Hava sıcaklıklarının düşmesi",["evet","hayır"], "hayır"),
        ("Okyanus sıcaklıklarının düşmesi",["evet","hayır"], "hayır")
    ]
    soru, cevaplar, dogru_cevap = random.choice(olaylar)

    await ctx.send(f"Rastgele bir olay: {soru}")
    await ctx.send("Bu olayın küresel ısınmaya etkisi nedir? (evet/hayır)")
    def check(msg):
        return msg.author == ctx.author and msg.content.lower() in [cevap.lower() for  cevap in cevaplar]
    try:
        cevap = await bot.wait_for('message', check=check, timeout=13.0)
        if cevap.content.lower() == dogru_cevap.lower():
            await ctx.send("Cevabınız doğru!")
        else:
            await ctx.send("Cevabınız yanlış!")
    except TimeoutError:
            await ctx.send("Zaman aşımına uğradı! Lütfen daha hızlı yanıt verin.")

bot.run('your token here') 