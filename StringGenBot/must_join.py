from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/46b4600cc41a592c4edd3.jpg", caption=f"» 📣 لا يمكنك استخدام البوت . [𝗦𝗼𝗨𝗿𝗖𝗲 ™𝗟𝗲𝗔𝗱𝗘𝗿]({link}) 🔘 الا بعد الاشتراك بقناة البوت . [𝗦𝗼𝗨𝗿𝗖𝗲 ™𝗟𝗲𝗔𝗱𝗘𝗿]({link}) 📡 اشترك بقناة بعدها ارسل /start .",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝗦𝗼𝗨𝗿𝗖𝗲 ™𝗟𝗲𝗔𝗱𝗘𝗿", url="https://t.me/V_P_N_8"),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
