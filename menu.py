from telebot import types


# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🔎 Выбрать город', callback_data='catalog')
)

main_menu.add(
    types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='👥 Рефералы', callback_data='referral_web')
)

main_menu.add(
    types.InlineKeyboardButton(text='👨‍💻 Поддержка', callback_data='info'),
    types.InlineKeyboardButton(text='🛒 Мои покупки', callback_data='purchases')
)

main_menu.add(
    types.InlineKeyboardButton(text='💸 Пополнить баланс', callback_data='repenish_balance'),
)

# Admin menu
admin_menu = types.InlineKeyboardMarkup(row_width=1)
admin_menu.add(types.InlineKeyboardButton(text='Управление городами', callback_data='catalog_control'))
admin_menu.add(types.InlineKeyboardButton(text='Управление товаром', callback_data='section_control'))
admin_menu.add(types.InlineKeyboardButton(text='Изменить баланс', callback_data='give_balance'))
admin_menu.add(types.InlineKeyboardButton(text='Рассылка', callback_data='admin_sending_messages'))
admin_menu.add(types.InlineKeyboardButton(text='Топ рефералов(доходы)', callback_data='admin_top_ref'))
admin_menu.add(
    types.InlineKeyboardButton(text='Информация', callback_data='admin_info'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_admin_menu')
)

# Admin control
admin_menu_control_catalog = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_catalog.add(
    types.InlineKeyboardButton(text='Добавить город в каталог', callback_data='add_section_to_catalog'),
    types.InlineKeyboardButton(text='Удалить город из каталога', callback_data='del_section_to_catalog'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Admin control section
admin_menu_control_section = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_section.add(
    types.InlineKeyboardButton(text='Добавить товар в раздел', callback_data='add_product_to_section'),
    types.InlineKeyboardButton(text='Удалить товар из раздела', callback_data='del_product_to_section'),
    types.InlineKeyboardButton(text='Загрузить товар', callback_data='download_product'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Back to admin menu
back_to_admin_menu = types.InlineKeyboardMarkup(row_width=1)
back_to_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_to_admin_menu')
)

btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)

replenish_balance = types.InlineKeyboardMarkup(row_width=3)
replenish_balance.add(
    types.InlineKeyboardButton(text='🔄 Проверить', callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel_payment')
)

to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)

card_balance = types.InlineKeyboardMarkup(row_width=3)
card_balance.add(
    types.InlineKeyboardButton(text="🔄 Проверить", callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel_payment')
)


renish_balance = types.InlineKeyboardMarkup(row_width=3)
renish_balance.add(
    types.InlineKeyboardButton(text="🔄 Проверить", callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel_payment')
)

repenish_balance = types.InlineKeyboardMarkup(row_width=2)
repenish_balance.add(
          types.InlineKeyboardButton(text='🥝 Qiwi', callback_data='replenish_balance'),
          types.InlineKeyboardButton(text='💵 Карта', callback_data='card_balance'),
          types.InlineKeyboardButton(text='🅱️ BTC', callback_data='renish_balance'),
          types.InlineKeyboardButton(text='❌ Выйти', callback_data='to_close')
)






