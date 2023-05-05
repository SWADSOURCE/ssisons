from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ", url="https://t.me/source_av"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/TR_E2S_ON_MY_MOoN")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
البوت متخصص في استخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
َժٍᥱُ᥎ :- @source_av
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
╔━━━━━𓌹 ↱ ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╗  
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس افاتار
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/source_av)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @source_av
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
╚━━━━━𓌹 ↱ ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╝
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━𖠙ᥲ️᥎ᥲ️ƚᥲ️ᖇ𖠙━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس افـاتـار
╔━━━━━𓌹 ↱ ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╗  

⩩ السورس [ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ](https://t.me/source_av)

╚━━━━━𓌹 ↱ ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╝
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @source_av
⋖━━❲𖣂❳━━𖠙ᥲ️᥎ᥲ️ƚᥲ️ᖇ𖠙━━❲𖣂❳━━⋗
   """
