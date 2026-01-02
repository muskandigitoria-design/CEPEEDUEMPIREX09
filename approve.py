import asyncio
import os
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string = os.getenv("STRING_SESSION")

bot = TelegramClient(StringSession(string), api_id, api_hash)

WELCOME_MESSAGE = """
✨ *WELCOME TO CE & PE EDUEMPIREX 📈*

Hum stock market me experienced team hain  
aur real-time market based guidance provide karte hain.

Best option choose karne ke liye  
please simple questions ka answer dijiye 👇
"""


MARKET_QUESTION = """
*✅ QUESTION 1: MARKET INTEREST*
1️⃣ Aap kis market me interested ho?
"""

SERVICE_QUESTION = """
*✅ QUESTION 2: SERVICE TYPE SELECTION*
2️⃣ Aap kaunsa option choose karoge?
"""

PREMIUM_PLANS = """
*✅ PREMIUM PLAN SELECTION*
4️⃣ Kaunsa premium plan choose karoge?
"""

ACCOUNT_CAPITAL = """
*✅ ACCOUNT HANDLING CAPITAL*
4️⃣ Kitna capital allocate kar sakte ho?
"""

FINAL_MESSAGE = """
🎉 *SPECIAL LIMITED TIME OFFER!*

Agar aap admin ko comment karte ho 👇  
👉 *ce&pe25*

Toh aapko premium plans par *50% discount* milega 🎁

📩 *NEXT STEP*
Admin ko message karein  
Team aapse directly connect karegi 😊
"""


# ================= AUTO APPROVE JOIN REQUEST =================
@bot.on(events.ChatJoinRequest)
async def approve(event):
    user = await event.get_user()
    name = user.first_name

    await event.approve()
    print(f"{name} Approved Automatically ✔️")

    # Send DM
    try:
        await bot.send_message(
            user.id,
            WELCOME_MESSAGE,
            buttons=[
                [
                    Button.url("⭐ Join Our Group", "https://t.me/+GiwKjDnCWNNhMGQ1"),
                    Button.url("📩 Contact Admin", "https://t.me/TRADEwithSHAANVii")
                ],
                [Button.inline("Continue ▶️", b"start")]
            ],
            parse_mode="markdown"
        )
    except:
        print("DM CLOSED ❌")


# ================= FLOW =================
@bot.on(events.CallbackQuery(data=b"start"))
async def q1(event):
    await event.edit(
        MARKET_QUESTION,
        buttons=[
            [Button.inline("📊 Stock Market", b"stock")],
            [Button.inline("💱 Forex Market", b"forex")]
        ]
    )


@bot.on(events.CallbackQuery(pattern=b"(stock|forex)"))
async def q2(event):
    await event.edit(
        SERVICE_QUESTION,
        buttons=[
            [Button.inline("📘 Premium Channel", b"premium")],
            [Button.inline("🤝 Account Handling", b"account")]
        ]
    )


@bot.on(events.CallbackQuery(data=b"premium"))
async def premium_plan(event):
    await event.edit(
        PREMIUM_PLANS,
        buttons=[
            [Button.inline("🔥 ₹3,999 Premium", b"p1")],
            [Button.inline("🔥 ₹7,999 Advanced", b"p2")],
            [Button.inline("⭐ ₹21,999 Lifetime", b"p3")]
        ]
    )


@bot.on(events.CallbackQuery(data=b"account"))
async def account(event):
    await event.edit(
        ACCOUNT_CAPITAL,
        buttons=[
            [Button.inline("💼 ₹25,000", b"c1")],
            [Button.inline("💼 ₹50,000", b"c2")],
            [Button.inline("💼 ₹1,00,000", b"c3")],
            [Button.inline("💼 ₹2,50,000", b"c4")]
        ]
    )


@bot.on(events.CallbackQuery())
async def final(event):
    await event.edit(
        FINAL_MESSAGE,
        buttons=[
            [
                Button.url("⭐ Join Our Group", "https://t.me/+GiwKjDnCWNNhMGQ1"),
                Button.url("📩 Contact Admin", "https://t.me/TRADEwithSHAANVii")
            ]
        ]
    )


async def main():
    print("Userbot Starting...")
    await bot.start()
    print("Auto Approve Bot LIVE 🚀")
    await bot.run_until_disconnected()

asyncio.run(main())
