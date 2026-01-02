import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    ChatJoinRequest,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from aiogram.enums import ParseMode

# ================= ENV =================
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()

# ================= TEXTS (UNCHANGED) =================
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

# ================= KEYBOARDS =================
start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Continue ▶️", callback_data="start")]
])

market_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📊 Stock Market", callback_data="stock")],
    [InlineKeyboardButton(text="💱 Forex Market", callback_data="forex")]
])

service_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📘 Premium Channel", callback_data="premium")],
    [InlineKeyboardButton(text="🤝 Account Handling", callback_data="account")]
])

premium_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔥 ₹3,999 Premium", callback_data="p1")],
    [InlineKeyboardButton(text="🔥 ₹7,999 Advanced", callback_data="p2")],
    [InlineKeyboardButton(text="⭐ ₹21,999 Lifetime", callback_data="p3")]
])

account_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💼 ₹25,000", callback_data="c1")],
    [InlineKeyboardButton(text="💼 ₹50,000", callback_data="c2")],
    [InlineKeyboardButton(text="💼 ₹1,00,000", callback_data="c3")],
    [InlineKeyboardButton(text="💼 ₹2,50,000", callback_data="c4")]
])

final_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="⭐ Join Our Group",
            url="https://t.me/+GiwKjDnCWNNhMGQ1"
        ),
        InlineKeyboardButton(
            text="📩 Contact Admin",
            url="https://t.me/TRADEwithSHAANVii"
        )
    ]
])

# ================= AUTO APPROVE + DM =================
@dp.chat_join_request()
async def approve_user(req: ChatJoinRequest):
    await req.approve()

    try:
        await bot.send_message(
            req.from_user.id,
            WELCOME_MESSAGE,
            reply_markup=start_kb
        )
    except:
        pass

# ================= FLOW =================
@dp.callback_query(F.data == "start")
async def q1(cb: CallbackQuery):
    await cb.message.edit_text(MARKET_QUESTION, reply_markup=market_kb)

@dp.callback_query(F.data.in_(["stock", "forex"]))
async def q2(cb: CallbackQuery):
    await cb.message.edit_text(SERVICE_QUESTION, reply_markup=service_kb)

@dp.callback_query(F.data == "premium")
async def premium(cb: CallbackQuery):
    await cb.message.edit_text(PREMIUM_PLANS, reply_markup=premium_kb)

@dp.callback_query(F.data == "account")
async def account(cb: CallbackQuery):
    await cb.message.edit_text(ACCOUNT_CAPITAL, reply_markup=account_kb)

@dp.callback_query()
async def final(cb: CallbackQuery):
    await cb.message.edit_text(FINAL_MESSAGE, reply_markup=final_kb)

# ================= RUN =================
async def main():
    print("Bot started successfully")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
