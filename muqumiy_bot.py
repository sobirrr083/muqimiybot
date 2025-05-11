import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Set up logging with maximum detail
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            ["📚 Muqumiy haqida", "🎓 Stipendiya haqida"],
            ["📋 Ariza topshirish", "📞 Aloqa va takliflar"],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(
            "Assalomu alaykum! Men Muqumiy va uning nomidagi stipendiya haqida ma’lumot beruvchi botman.\n"
            "Quyidagi bo‘limlardan birini tanlang 👇",
            reply_markup=reply_markup
        )
        logger.info(f"User {update.effective_user.id} started the bot")
    except Exception as e:
        logger.error(f"Error in start command: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Muqumiy haqida
async def muqumiy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = (
            "📚 *Muqumiy (1850–1903)*\n\n"
            "Muqumiy – to‘liq ismi Hamad Alimxo‘ja Muqimiy, 1850-yilda Farg‘ona vodiysidagi Marg‘ilon shahrida tug‘ilgan\. "
            "U o‘zbek adabiyotining klassik vakillaridan biri bo‘lib, satirik va ijtimoiy mavzulardagi asarlari bilan mashhur\.\n\n"
            "🧠 U zamonasidagi ijtimoiy tengsizlik, zo‘ravonlik, riyokorlik kabi muammolarni ochiq tanqid qilgan\. "
            "Muqumiy she’rlari xalq orasida mashhur bo‘lgan va og‘zaki ijod bilan uyg‘unlashgan\. "
            "Satirasi, kulgi va hazil bilan yo‘g‘rilgan, ammo unda chuqur ijtimoiy mazmun mavjud\.\n\n"
            "🕊 1903-yilda Farg‘onada vafot etgan\. Uning merosi o‘zbek adabiyotida muhim o‘rin egallaydi\."
        )
        await update.message.reply_text(text, parse_mode="MarkdownV2")
        logger.info(f"User {update.effective_user.id} requested Muqumiy info")
    except TelegramError as te:
        logger.error(f"Telegram API error in muqumiy function: {te}", exc_info=True)
        await update.message.reply_text("Telegram xatoligi yuz berdi. Iltimos, qaytadan urinib ko‘ring.")
    except Exception as e:
        logger.error(f"Unexpected error in muqumiy function: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Stipendiya haqida
async def stipendiya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = (
            "🎓 *Muqumiy nomidagi Davlat stipendiyasi*\n\n"
            "Muqumiy stipendiyasi — O‘zbekiston Respublikasi Prezidentining qaroriga asosan ta'sis etilgan "
            "va adabiyot, san’at, jurnalistika yoki ijtimoiy-gumanitar fanlar yo‘nalishida iqtidorli talabalar uchun "
            "ajratiladigan nufuzli stipendiyadir\.\n\n"
            "📑 *Nizomga ko‘ra quyidagilar belgilangan:*\n"
            "1\. Stipendiya yilda bir marta tanlov asosida beriladi\.\n"
            "2\. Talaba bakalavriat yoki magistratura bosqichida bo‘lishi kerak\.\n"
            "3\. Nomzod fan yoki ijod sohasida yuksak natijalarga erishgan bo‘lishi shart\.\n"
            "4\. Har bir OTM alohida komissiya tuzadi va Oliy ta’lim vazirligiga tavsiyanoma yuboradi\.\n"
            "5\. G‘oliblar Respublika miqyosida tanlab olinadi\.\n\n"
            "💰 *Moliyaviy qo‘llab-quvvatlash:*\n"
            "Stipendiya miqdori har oyda maxsus belgilangan summa asosida to‘lab beriladi (aniq raqam har yili yangilanadi)\.\n\n"
            "🔍 Tanlov mezonlariga asosan ilmiy maqolalar, ijodiy ishlanmalar, tanlovlarda qatnashganlik e’tiborga olinadi\.\n\n"
            "📌 Muqumiy stipendiyasi talabalarga rag‘bat, hurmat va yuksak motivatsiya beradi\."
        )
        await update.message.reply_text(text, parse_mode="MarkdownV2")
        logger.info(f"User {update.effective_user.id} requested stipendiya info")
    except TelegramError as te:
        logger.error(f"Telegram API error in stipendiya function: {te}", exc_info=True)
        await update.message.reply_text("Telegram xatoligi yuz berdi. Iltimos, qaytadan urinib ko‘ring.")
    except Exception as e:
        logger.error(f"Unexpected error in stipendiya function: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Ariza topshirish
async def ariza(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = (
            "📋 *Muqumiy stipendiyasiga ariza topshirish*\n\n"
            "1️⃣ O‘zingiz o‘qiyotgan OTMda stipendiya komissiyasiga murojaat qiling\.\n"
            "2️⃣ Ilmiy yoki ijodiy ishingizni (maqola, loyiha, asar) taqdim eting\.\n"
            "3️⃣ OTM tomonidan tavsiyanoma oling\.\n"
            "4️⃣ Hujjatlarni Oliy ta’lim vazirligiga yuboring\.\n"
            "5️⃣ Tanlov natijalarini kuting\.\n\n"
            "🔍 Batafsil ma’lumot uchun: www\.edu\.uz"
        )
        await update.message.reply_text(text, parse_mode="MarkdownV2")
        logger.info(f"User {update.effective_user.id} requested ariza info")
    except TelegramError as te:
        logger.error(f"Telegram API error in ariza function: {te}", exc_info=True)
        await update.message.reply_text("Telegram xatoligi yuz berdi. Iltimos, qaytadan urinib ko‘ring.")
    except Exception as e:
        logger.error(f"Unexpected error in ariza function: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Aloqa va takliflar
async def aloqa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        logger.debug(f"User {update.effective_user.id} triggered aloqa function with text: '{update.message.text}'")
        text = (
            "📞 *Aloqa va takliflar*\n\n"
            "Botimizni yaxshilash bo‘yicha takliflaringiz bo‘lsa, iltimos, bizga yozing!\n"
            "📧 Email: muqumiy_bot@example\.com\n"
            "📱 Telegram: @MuqumiyBotAdmin\n\n"
            "Agar stipendiya bo‘yicha rasmiy ma’lumot kerak bo‘lsa, Oliy ta’lim vazirligiga murojaat qiling:\n"
            "🌐 Sayt: www\.edu\.uz\n"
            "📞 Telefon: \\+998 71 246-12-34"
        )
        try:
            await update.message.reply_text(text, parse_mode="MarkdownV2")
            logger.info(f"User {update.effective_user.id} successfully received aloqa info")
        except TelegramError as te:
            logger.warning(f"MarkdownV2 failed in aloqa: {te}. Falling back to plain text.")
            # Fallback to plain text
            plain_text = (
                "📞 Aloqa va takliflar\n\n"
                "Botimizni yaxshilash bo‘yicha takliflaringiz bo‘lsa, iltimos, bizga yozing!\n"
                "Email: muqumiy_bot@example.com\n"
                "Telegram: @MuqumiyBotAdmin\n\n"
                "Agar stipendiya bo‘yicha rasmiy ma’lumot kerak bo‘lsa, Oliy ta’lim vazirligiga murojaat qiling:\n"
                "Sayt: www.edu.uz\n"
                "Telefon: +998 71 246-12-34"
            )
            await update.message.reply_text(plain_text)
            logger.info(f"User {update.effective_user.id} received aloqa info in plain text")
    except TelegramError as te:
        logger.error(f"Telegram API error in aloqa function: {te}", exc_info=True)
        await update.message.reply_text("Telegram xatoligi yuz berdi. Iltimos, qaytadan urinib ko‘ring.")
    except Exception as e:
        logger.error(f"Unexpected error in aloqa function: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        logger.debug(f"Received message from user {update.effective_user.id}: '{text}'")
        text_lower = text.lower()
        if "muqumiy" in text_lower:
            await muqumiy(update, context)
        elif "stipendiya" in text_lower:
            await stipendiya(update, context)
        elif "ariza" in text_lower:
            await ariza(update, context)
        elif "aloqa" in text_lower or "taklif" in text_lower:
            await aloqa(update, context)
        else:
            await update.message.reply_text("Iltimos, menyudan foydalaning yoki aniqroq yozing.")
        logger.info(f"User {update.effective_user.id} sent message: '{text}'")
    except Exception as e:
        logger.error(f"Error in handle_message: {e}", exc_info=True)
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}", exc_info=True)
    if update and update.message:
        await update.message.reply_text("Xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

# Main function to run the bot
def main():
    try:
        if not TOKEN:
            logger.error("TELEGRAM_BOT_TOKEN is not set")
            raise ValueError("TELEGRAM_BOT_TOKEN is not set")
        
        app = Application.builder().token(TOKEN).build()

        # Command handlers
        app.add_handler(CommandHandler("start", start))

        # Message handlers for buttons
        app.add_handler(MessageHandler(filters.Regex("^📚 Muqumiy haqida$"), muqumiy))
        app.add_handler(MessageHandler(filters.Regex("^🎓 Stipendiya haqida$"), stipendiya))
        app.add_handler(MessageHandler(filters.Regex("^📋 Ariza topshirish$"), ariza))
        app.add_handler(MessageHandler(filters.Regex("^📞 Aloqa va takliflar$"), aloqa))

        # General message handler
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Error handler
        app.add_error_handler(error_handler)

        logger.info("Bot is starting...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}", exc_info=True)

if __name__ == "__main__":
    main()
