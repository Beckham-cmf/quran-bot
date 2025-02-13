import telebot
import os

# جلب التوكن من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")

# إنشاء البوت
bot = telebot.TeleBot(TOKEN)

# أمر /start للترحيب بالمستخدم
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "أهلاً بك في بوت متابعة ورد القرآن! \n\n أرسل لي اسم السورة ورقم الآية التي توقفت عندها.")

# تخزين تقدم المستخدم
users_progress = {}

@bot.message_handler(func=lambda message: True)
def track_quran(message):
    user_id = message.chat.id
    text = message.text.strip()

    # التحقق من تنسيق الرسالة
    try:
        surah, ayah = text.split()
        ayah = int(ayah)
        users_progress[user_id] = (surah, ayah)
        bot.send_message(user_id, f"📖 تم حفظ تقدمك عند:\n{surah} - آية {ayah}")
    except:
        bot.send_message(user_id, "❌ الرجاء إرسال البيانات بالشكل التالي:\n\n*اسم السورة رقم الآية*\n\nمثال: البقرة 5", parse_mode="Markdown")

# أمر /progress لعرض تقدم المستخدم
@bot.message_handler(commands=['progress'])
def get_progress(message):
    user_id = message.chat.id
    if user_id in users_progress:
        surah, ayah = users_progress[user_id]
        bot.send_message(user_id, f"📖 تقدمك الحالي:\n{surah} - آية {ayah}")
    else:
        bot.send_message(user_id, "❌ لم تسجل أي تقدم بعد! \n\n أرسل السورة والآية.")

# تشغيل البوت
bot.polling()
