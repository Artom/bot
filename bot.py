from email import message
from random import randint, random
from sys import prefix

import telebot
from telebot import types

from aiogram import Bot, types
from aiogram.types import InputFile
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from telebot.apihelper import send_message

from config import TOKENSS
import gg as kb

bot = Bot(token='6953553307:AAFUhZI9IbzXRcuD7kzBGx4GjYqeJTJ-fe0', parse_mode="HTML")
dp = Dispatcher(bot)

##

@dp.callback_query_handler(lambda c: c.data == 'A')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Дон капон ', reply_markup=kb.inline_kb_dnd2)

@dp.callback_query_handler(lambda c: c.data == 'B')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Дон Капони', reply_markup=kb.inline_kb_dnd3)

@dp.callback_query_handler(lambda c: c.data == 'C')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Дон Капони', reply_markup=kb.inline_kb_dnd4)

@dp.callback_query_handler(lambda c: c.data == 'D')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Comet ', reply_markup=kb.inline_kb_dnd5)

@dp.callback_query_handler(lambda c: c.data == 'E')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Comet', reply_markup=kb.inline_kb_dnd6)

@dp.callback_query_handler(lambda c: c.data == 'F')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Comet', reply_markup=kb.inline_kb_dnd7)

@dp.callback_query_handler(lambda c: c.data == 'G')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Арматура ', reply_markup=kb.inline_kb_a)

@dp.callback_query_handler(lambda c: c.data == 'AA')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Арматура', reply_markup=kb.inline_kb_a1)

@dp.callback_query_handler(lambda c: c.data == 'BB')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Арматура', reply_markup=kb.inline_kb_a2)

@dp.callback_query_handler(lambda c: c.data == 'H')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Ая ', reply_markup=kb.inline_kb_e)

@dp.callback_query_handler(lambda c: c.data == 'AAA')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Ая', reply_markup=kb.inline_kb_e1)

@dp.callback_query_handler(lambda c: c.data == 'BBB')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Ая', reply_markup=kb.inline_kb_a2)

@dp.callback_query_handler(lambda c: c.data == 'I')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Nevill ', reply_markup=kb.inline_kb_f)

@dp.callback_query_handler(lambda c: c.data == 'CC')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Nevill', reply_markup=kb.inline_kb_f1)

@dp.callback_query_handler(lambda c: c.data == 'DD')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Nevill', reply_markup=kb.inline_kb_f2)

@dp.callback_query_handler(lambda c: c.data == 'J')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Amin a ', reply_markup=kb.inline_kb_g)

@dp.callback_query_handler(lambda c: c.data == 'EE')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Amin a', reply_markup=kb.inline_kb_g1)

@dp.callback_query_handler(lambda c: c.data == 'FF')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Amin a', reply_markup=kb.inline_kb_g2)

@dp.callback_query_handler(lambda c: c.data == 'K')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: ... ', reply_markup=kb.inline_kb_h)

@dp.callback_query_handler(lambda c: c.data == 'GG')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: ...', reply_markup=kb.inline_kb_h1)

@dp.callback_query_handler(lambda c: c.data == 'HH')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: ...', reply_markup=kb.inline_kb_h2)

@dp.callback_query_handler(lambda c: c.data == 'L')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Ляля', reply_markup=kb.inline_kb_j)

@dp.callback_query_handler(lambda c: c.data == 'II')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Ляля', reply_markup=kb.inline_kb_j1)

@dp.callback_query_handler(lambda c: c.data == 'JJ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Ляля', reply_markup=kb.inline_kb_j2)

@dp.callback_query_handler(lambda c: c.data == 'M')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Lemon', reply_markup=kb.inline_kb_i)

@dp.callback_query_handler(lambda c: c.data == 'KK')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Lemon', reply_markup=kb.inline_kb_i1)

@dp.callback_query_handler(lambda c: c.data == 'LL')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Lemon', reply_markup=kb.inline_kb_i2)

@dp.callback_query_handler(lambda c: c.data == 'N')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Dasha', reply_markup=kb.inline_kb_k)

@dp.callback_query_handler(lambda c: c.data == 'MM')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Dasha', reply_markup=kb.inline_kb_k1)

@dp.callback_query_handler(lambda c: c.data == 'NN')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Dasha', reply_markup=kb.inline_kb_k2)

@dp.callback_query_handler(lambda c: c.data == 'O')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: леля', reply_markup=kb.inline_kb_l)

@dp.callback_query_handler(lambda c: c.data == 'OO')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: леля', reply_markup=kb.inline_kb_l1)

@dp.callback_query_handler(lambda c: c.data == 'PP')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: леля', reply_markup=kb.inline_kb_l2)

@dp.callback_query_handler(lambda c: c.data == 'P')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: ~teftelka~', reply_markup=kb.inline_kb_m)

@dp.callback_query_handler(lambda c: c.data == 'QQ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: ~teftelka~', reply_markup=kb.inline_kb_m1)

@dp.callback_query_handler(lambda c: c.data == 'RR')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: ~teftelka~', reply_markup=kb.inline_kb_m2)

@dp.callback_query_handler(lambda c: c.data == 'Q')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Нiкiта', reply_markup=kb.inline_kb_n)

@dp.callback_query_handler(lambda c: c.data == 'SS')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Нiкiта', reply_markup=kb.inline_kb_n1)

@dp.callback_query_handler(lambda c: c.data == 'TT')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Нiкiта', reply_markup=kb.inline_kb_n2)

@dp.callback_query_handler(lambda c: c.data == 'R')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Arbie', reply_markup=kb.inline_kb_o)

@dp.callback_query_handler(lambda c: c.data == 'UU')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Arbie', reply_markup=kb.inline_kb_o1)

@dp.callback_query_handler(lambda c: c.data == 'VV')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Arbie', reply_markup=kb.inline_kb_o2)

@dp.callback_query_handler(lambda c: c.data == 'S')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Beks', reply_markup=kb.inline_kb_p)

@dp.callback_query_handler(lambda c: c.data == 'WW')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Beks', reply_markup=kb.inline_kb_p1)

@dp.callback_query_handler(lambda c: c.data == 'XX')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Beks', reply_markup=kb.inline_kb_p2)

@dp.callback_query_handler(lambda c: c.data == 'T')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: AtacmsUA', reply_markup=kb.inline_kb_q)

@dp.callback_query_handler(lambda c: c.data == 'YY')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: AtacmsUA', reply_markup=kb.inline_kb_q1)

@dp.callback_query_handler(lambda c: c.data == 'ZZ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: AtacmsUA', reply_markup=kb.inline_kb_q2)

@dp.callback_query_handler(lambda c: c.data == 'Y')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Diana', reply_markup=kb.inline_kb_r)

@dp.callback_query_handler(lambda c: c.data == 'AB')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Diana', reply_markup=kb.inline_kb_r1)

@dp.callback_query_handler(lambda c: c.data == 'BC')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Diana', reply_markup=kb.inline_kb_r2)

@dp.callback_query_handler(lambda c: c.data == 'V')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: DARKSIDE', reply_markup=kb.inline_kb_s)

@dp.callback_query_handler(lambda c: c.data == 'CD')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: DARKSIDE', reply_markup=kb.inline_kb_s1)

@dp.callback_query_handler(lambda c: c.data == 'DE')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: DARKSIDE', reply_markup=kb.inline_kb_s2)

@dp.callback_query_handler(lambda c: c.data == 'W')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Lady Cat', reply_markup=kb.inline_kb_t)

@dp.callback_query_handler(lambda c: c.data == 'EF')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Lady Cat', reply_markup=kb.inline_kb_t1)

@dp.callback_query_handler(lambda c: c.data == 'FG')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Lady Cat', reply_markup=kb.inline_kb_t2)

@dp.callback_query_handler(lambda c: c.data == 'X')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: Dina', reply_markup=kb.inline_kb_u)

@dp.callback_query_handler(lambda c: c.data == 'GH')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: Dina', reply_markup=kb.inline_kb_u1)

@dp.callback_query_handler(lambda c: c.data == 'HI')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: Dina', reply_markup=kb.inline_kb_u2)

@dp.callback_query_handler(lambda c: c.data == 'Z')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '🌇Выберите день\n \n<b>🎭Игрок</b>: юлябасик', reply_markup=kb.inline_kb_v)

@dp.callback_query_handler(lambda c: c.data == 'IJ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Первый день\n \n<b>🎭Игрок</b>: юлябасик', reply_markup=kb.inline_kb_v1)

@dp.callback_query_handler(lambda c: c.data == 'JK')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '📌<b>Статус</b>: Второй день\n \n<b>🎭Игрок</b>: юлябасик', reply_markup=kb.inline_kb_v2)

#юлябасик
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('x'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Diana
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('w'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Lady
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('vb'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#DARKSIDE
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('u'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Diana
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('t'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)


#AtacmsUA
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('s'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Beks
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('rp'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Arbie
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('q'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Hikita
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('oo'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

##
#teftelka
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('l'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 2 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 3/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛸Алантий - 700 \n🛡Нейраниум - 700 \n💫Сигли - 400',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - \nБронзиум - \nАлантий - \nНейраниум - \nСигли -',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#lelya
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('k'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр: 10/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - 3 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: 7/10',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Dasha
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('j'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 10/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 3 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 7/10',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 300 \nНейраниум - 300 \nСигли - 150',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Lemon
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('h'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 2/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 2 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 0/2',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 200 \nНейраниум - 200 \nСигли - 100',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Lyalya
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('f'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 2 \nмафия- 3 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 4/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 300 \nБронзиум - 300 \nАлантий - 200 \nНейраниум - 200 \nСигли - 250',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#...
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('e'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 7/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 3 \nмафия- 3 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 1/7',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 300 \nБронзиум - 300 \nАлантий - 300 \nНейраниум - 300 \nСигли - 300',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Amin a
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('d'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 7/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 2 \nмафия- 0 \nнейтральные - 1',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 4/7',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 300 \nБронзиум - 300 \nАлантий - 500 \nНейраниум - 500 \nСигли - 200',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Nevill
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('c'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 9/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 1 \nмафия- 2 \nнейтральные - 2',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 4/9',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 800 \nБронзиум - 800 \nАлантий - 700 \nНейраниум - 700 \nСигли - 350',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Aya
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bb'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 6/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 3 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 4/7',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 300 \nНейраниум - 300 \nСигли - 150',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

##


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '👥Список участников: \n💠Nevill \n💠Diana \n💠Дон Капони \n💠~teftelka~ \n💠AtacmsUA \n💠Ляля \n💠Ая \n💠лёля \n💠Amin a \n💠Арматура (бывший Norma) \n💠Нiкiта \n💠Beks (Bega) \n💠Dasha \n💠DARKSIDE \n💠Lemon \n💠Dina \n💠Arbie \n💠... \n💠Lady Cat')

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '👥Список имперцев: \n🔸Nevill \n🔸AtacmsUA \n🔸Ляля \n🔸Beks \n🔸Арматура \n🔸~teftelka~ \n🔸Ая \n🔸... \n🔸Lemon \n🔸Dina')

@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '👥Список повстанцев: \n🔹Dasha \n🔹Дон Капони \n🔹Diana  \n🔹Lady Cat \n🔹Amin a \n🔹лёля \n🔹Нiкiта \n🔹DARKSIDE \n🔹Arbie')

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Nevill , Diana, Дон Капони, ~teftelka~, AtacmsUA, Ляля, Ая, лёля, Арматура (бывший Norma), Amin a, Нiкiта, Lady Cat, Beks (Bega), Dasha, DARKSIDE, Lemon, Dina, Arbie, ...',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='🔸Nevill \n🔸AtacmsUA \n🔸Ляля \n🔸Beks \n🔸Арматура \n🔸~teftelka~ \n🔸Ая \n🔸... \n🔸Lemon \n🔸Dina',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='🔹Dasha \n🔹Amin a \n🔹Дон Капони \n🔹Diana \n🔹юлясрака \n🔹Lady Cat \n🔹лёля \n🔹Нiкiта \n🔹DARKSIDE \n🔹Arbie',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Don Kaponi
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bob'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 1/10',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 0 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 1/1',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 0 \nНейраниум - 0 \nСигли - 0',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Дон Капони
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('b'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    elif code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Арматура
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('aa'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 7/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 1 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 6/7',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 100 \nНейраниум - 100 \nСигли - 50',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)

#Comet
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('aaa'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='Количество игр: 7/10',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='Побед: \nмирные - 1 \nмафия- 0 \nнейтральные - 0',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='Проигрышей: 6/7',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \nБескар - 0 \nБронзиум - 0 \nАлантий - 100 \nНейраниум - 100 \nСигли - 50',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='📁Количество игр:',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='✔️Побед: \nмирные - \nмафия-  \nнейтральные -',
            show_alert=True)
    elif code == 7:
        await bot.answer_callback_query(
            callback_query.id,
            text='🚫Проигрышей: ',
            show_alert=True)
    elif code == 8:
        await bot.answer_callback_query(
            callback_query.id,
            text='Ресурсы: \n🔫Бескар - 0 \n👾Бронзиум - 0 \n🛸Алантий - 300 \n🛡Нейраниум - 300 \n💫Сигли - 150',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
##

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('res'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(
            callback_query.id,
            text='🛸Алантий - 2500 \n🔫Бескар - 2100 \n👾Бронзиум - 2100 \n🛡Нейраниум - 2500 \n💫Сигил - 1700',
            show_alert=True)
    elif code == 2:
        await bot.answer_callback_query(
            callback_query.id,
            text='хватит пялиться',
            show_alert=True)
    elif code == 3:
        await bot.answer_callback_query(
            callback_query.id,
            text='че над?',
            show_alert=True)
    elif code == 4:
        await bot.answer_callback_query(
            callback_query.id,
            text='🛸Алантий - 1800 \n🔫Бескар - 500 \n👾Бронзиум - 500 \n🛡Нейраниум - 1800 \n💫Сигил - 950',
            show_alert=True)
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Семки есть?',
            show_alert=True)
    elif code == 6:
        await bot.answer_callback_query(
            callback_query.id,
            text='А если найду?',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
##


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message, chat_id=None):
    await message.reply("Все возможные кнопки️",
                        reply_markup=kb.inline_kb_dnd)

@dp.message_handler(commands=['k'])
async def process_k_command(message: types.Message):
    await message.reply("❗️27.11.2023 в 19:00 вам в этом чате будут выставлены задания, необходимо, чтобы присутствовали все❗️",
                        reply_markup=kb.inline_kb_full)

@dp.message_handler(commands=['imperic'])
async def process_imperic_command(message: types.Message):
    await message.reply("📋Список имперцев ",
                        reply_markup=kb.inline_kb5)


@dp.message_handler(commands=['povstanic'])
async def process_povstanic_command(message: types.Message):
    await message.reply("📋Список повстанцев",
                        reply_markup=kb.inline_kb6)

@dp.message_handler(commands=['alls'])
async def process_alls_command(message: types.Message):
    await message.reply("📌Участники",
                        reply_markup=kb.inline_kb4)

@dp.message_handler(commands=['all'])
async def process_all_command(message: types.Message):
    await message.reply("📌Участники",
                        reply_markup=kb.inline_kb1)

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры",
                        reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['go'])
async def process_go_command(message: types.Message):
    await message.reply("<b>❗️Правила проведения❗️</b>\n \n<i>🚫Нельзя</i>: \n-спам командами \n-пытаться рандомно подобрать буквы \n<i>🔰Можно</i>:  \n-обсуждать в чате, тем самым разгадывая вместе \n🥷🏻Организатор вправе спросить у игрока как он решил ту или иную загадку, если не будет ответа ->предупреждение ->дисквалификация\n \n👻Если готов, то нажми кнопку ниже ГОТОВ",
                        reply_markup=kb.greet_kb2)

@dp.message_handler(commands=['stat'])
async def process_stat_command(message: types.Message):
    await message.reply("🕹Выберите игрока",
                        reply_markup=kb.inline_kb_dnd1)

@dp.message_handler(commands=['res_f_imper'])
async def process_res_f_imper_command(message: types.Message):
    await message.reply("♦️Ресурсы имперцев",
                        reply_markup=kb.inline_kb_res1)

@dp.message_handler(commands=['all_res'])
async def process_all_res_command(message: types.Message):
    await message.reply("♦️Ресурсы обеих команд",
                        reply_markup=kb.inline_kb_res3)

@dp.message_handler(commands=['res_g_povstanic'])
async def process_res_g_povstanic_command(message: types.Message):
    await message.reply("♦️Ресурсы повстанцев",
                        reply_markup=kb.inline_kb_res2)

@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок",
                        reply_markup=kb.markup3)


@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд",
                        reply_markup=kb.markup4)


@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок",
                        reply_markup=kb.markup5)


@dp.message_handler(commands=['hi6'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\n"
                        "Эти две кнопки не зависят друг от друга",
                        reply_markup=kb.markup_request)


@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Восьмое - все методы вместе",
                        reply_markup=kb.markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("👾Убираю шаблоны сообщений",
                        reply_markup=kb.ReplyKeyboardRemove())

##


@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка",
                        reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки",
                        reply_markup=kb.inline_kb_full)

help_message = text(
    "Доступные команды:\n",
    "/start - все позможные кнопки",
    "/k - кнопки с первым сообщением бота о дате головоломки",
    "/all - показывает список участников в лс с ботом",
    "/alls - показывает список участников поверх сообщения",
    "/imperic - показывает список имперцев поверх сообщения",
    "/povstanic - показывает список повстанцев поверх сообщения",
    "/go - для насала головоломки",
    sep="\n"
)


@dp.message_handler(commands=['команды'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)



if __name__ == '__main__':
    executor.start_polling(dp)