import os
import json
import requests
from datetime import time
from dotenv import load_dotenv
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, JobQueue
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API = os.getenv("WEATHER_API")
EARTHQUAKE_API = os.getenv("EARTHQUAKE_API")

# File penyimpanan
USERS_FILE = "users.json"
HISTORY_FILE = "history.json"

def load_json(file):
    if not os.path.exists(file):
        return {}
    try:
        with open(file, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except Exception:
        return {}

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

users = load_json(USERS_FILE)
history = load_json(HISTORY_FILE)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌦 Cuaca", callback_data="cuaca"),
         InlineKeyboardButton("🌍 Gempa", callback_data="gempa")],
        [InlineKeyboardButton("📊 Statistik", callback_data="statistik"),
         InlineKeyboardButton("🗺 Peta", callback_data="peta")],
        [InlineKeyboardButton("🔮 Forecast", callback_data="forecast"),
         InlineKeyboardButton("🌫 AQI", callback_data="aqi")],
        [InlineKeyboardButton("🔔 Subscribe", callback_data="subscribe"),
         InlineKeyboardButton("🚫 Unsubscribe", callback_data="unsubscribe")],
        [InlineKeyboardButton("⚠️ Alert Gempa", callback_data="alert"),
         InlineKeyboardButton("🌐 Bahasa", callback_data="language")],
        [InlineKeyboardButton("ℹ️ Tentang", callback_data="tentang"),
         InlineKeyboardButton("👨‍💻 Credit", callback_data="credit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Selamat datang di *Weather & Info Bot*!\nSilakan pilih menu:", 
                                    parse_mode="Markdown", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "cuaca":
        await query.edit_message_text("📌 Gunakan perintah: `/cuaca <kota>`", parse_mode="Markdown")
    elif query.data == "gempa":
        await query.edit_message_text("📌 Gunakan perintah: `/gempa`", parse_mode="Markdown")
    elif query.data == "statistik":
        await query.edit_message_text("📊 Gunakan perintah: `/statistik <kota>`", parse_mode="Markdown")
    elif query.data == "peta":
        await query.edit_message_text("🗺 Gunakan perintah: `/peta <kota>`", parse_mode="Markdown")
    elif query.data == "forecast":
        await query.edit_message_text("🔮 Gunakan perintah: `/forecast <kota>`", parse_mode="Markdown")
    elif query.data == "aqi":
        await query.edit_message_text("🌫 Gunakan perintah: `/aqi <kota>`", parse_mode="Markdown")
    elif query.data == "subscribe":
        await query.edit_message_text("🔔 Gunakan perintah: `/subscribe <kota>`", parse_mode="Markdown")
    elif query.data == "unsubscribe":
        await query.edit_message_text("🚫 Gunakan perintah: `/unsubscribe`", parse_mode="Markdown")
    elif query.data == "alert":
        await query.edit_message_text("⚠️ Gunakan perintah: `/alert`", parse_mode="Markdown")
    elif query.data == "language":
        await query.edit_message_text("🌐 Gunakan perintah: `/language <kode_bahasa>`", parse_mode="Markdown")
    elif query.data == "tentang":
        await query.edit_message_text("🤖 Bot ini dibuat untuk info cuaca, gempa & lingkungan.\nData dari API Ferdev & BMKG.")
    elif query.data == "credit":
        await query.edit_message_text(
            "👨‍💻 *Credit:*\n"
            "Development: Eko Muhammad M\n"
            "💰 Donasi: saweria.co/eko\n"
            "📸 Instagram: instagram.com/eko\n"
            "💻 Github: github.com/eko",
            parse_mode="Markdown"
        )

async def cuaca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("❌ Contoh: `/cuaca jakarta`", parse_mode="Markdown")
        return
    kota = context.args[0]
    url = f"{WEATHER_API}&kota={kota}"
    try:
        r = requests.get(url, timeout=10).json()
        if r.get("success"):
            d = r["data"]
            msg = (
                f"🌦 *Cuaca {d['kota']}*\n"
                f"🌡 Suhu: {d['suhu']}\n"
                f"☁️ Kondisi: {d['kondisi']}\n"
                f"💧 Kelembapan: {d['kelembapan']}\n"
                f"🌬 Angin: {d['angin']}\n"
                f"🌧 Curah Hujan: {d['curah_hujan']}"
            )
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Kota tidak ditemukan atau API error!")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

async def gempa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get(EARTHQUAKE_API, timeout=10).json()
        if r.get("success"):
            d = r["data"]
            msg = (
                f"🌍 *{d['title']}*\n"
                f"🕒 Waktu: {d['waktu']}\n"
                f"📍 Lokasi: {d['wilayah']}\n"
                f"📐 Lintang/Bujur: {d['lintang']}, {d['bujur']}\n"
                f"💥 Magnitudo: {d['magnitudo']}\n"
                f"📏 Kedalaman: {d['kedalaman']}"
            )
            await update.message.reply_photo(photo=d["map"], caption=msg, parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Data gempa tidak tersedia!")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

# Dummy fitur lain (bisa dikembangkan pakai API tambahan)
async def statistik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Statistik sementara hanya menampilkan cuaca rata-rata.\nContoh: `/statistik jakarta`")

async def peta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗺 Fitur peta akan menampilkan peta cuaca/gempa.\nContoh: `/peta jakarta`")

async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Forecast akan menampilkan prediksi cuaca 3-7 hari.\nContoh: `/forecast jakarta`")

async def aqi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌫 AQI akan menampilkan indeks kualitas udara.\nContoh: `/aqi jakarta`")

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 Fitur subscribe aktif.\nBot akan kirim update harian.")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚫 Kamu berhenti langganan update.")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ Alert gempa akan mengirim notifikasi otomatis jika ada gempa.")

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌐 Fitur multi-bahasa.\nContoh: `/language en` untuk English.")

async def send_daily_weather(context: ContextTypes.DEFAULT_TYPE):
    for uid in users:
        await context.bot.send_message(uid, "🌦 Update cuaca harian (dummy).")

def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.add_handler(CommandHandler("cuaca", cuaca))
    app.add_handler(CommandHandler("gempa", gempa))
    app.add_handler(CommandHandler("statistik", statistik))
    app.add_handler(CommandHandler("peta", peta))
    app.add_handler(CommandHandler("forecast", forecast))
    app.add_handler(CommandHandler("aqi", aqi))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))
    app.add_handler(CommandHandler("alert", alert))
    app.add_handler(CommandHandler("language", language))

    # Kirim update harian jam 07:00
    job_queue: JobQueue = app.job_queue
    job_queue.run_daily(send_daily_weather, time=time(hour=7, minute=0))

    app.run_polling()

if __name__ == "__main__":
    main()