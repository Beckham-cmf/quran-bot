import telebot
import os

# جلب التوكن من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")

# التأكد من أن التوكن ليس فارغًا
if not TOKEN:
    print("❌ خطأ: التوكن غير موجود! تأكد من ضبط متغير البيئة BOT_TOKEN.")
    exit(1)  # إنهاء البرنامج

print(f"✅ التوكن المستعمل: {TOKEN[:10]}********")  # طباعة جزء من التوكن لحماية الخصوصية

# إنشاء كائن البوت
bot = telebot.TeleBot(TOKEN)

# أمر /start للترحيب بالمستخدم
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "أهلاً بك! البوت يعمل بنجاح 🎉")

# طباعة الأخطاء إذا حصلت
try:
    print("🚀 بدء تشغيل البوت...")
    bot.polling(none_stop=True, timeout=60)
except Exception as e:
    print(f"❌ حصل خطأ أثناء تشغيل البوت: {e}")
