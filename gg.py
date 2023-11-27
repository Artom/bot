from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Готов!')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))


inline_btn_1 = InlineKeyboardButton('👥Весь список участников', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_btn_2 = InlineKeyboardButton('👥Показать список имперцев', callback_data='button2')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)

inline_btn_3 = InlineKeyboardButton('👥Показать список повстанцев', callback_data='button3')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)

inline_btn_4 = InlineKeyboardButton('👀Игроки', callback_data='btn4')
inline_kb4 = InlineKeyboardMarkup().add(inline_btn_4)

inline_btn_5 = InlineKeyboardButton('Показать🫰🏻', callback_data='btn5')
inline_kb5 = InlineKeyboardMarkup().add(inline_btn_5)

inline_btn_6 = InlineKeyboardButton('Показать🫰🏻', callback_data='btn6')
inline_kb6 = InlineKeyboardMarkup().add(inline_btn_6)

inline_btn_7 = InlineKeyboardButton('Готов!', callback_data='button7')
inline_kb7 = InlineKeyboardMarkup().add(inline_btn_7)

inline_btn_8 = InlineKeyboardButton('Показать🫰🏻', callback_data='btn8')
inline_kb8 = InlineKeyboardMarkup().add(inline_btn_8)

inline_btn_9 = InlineKeyboardButton('Показать🫰🏻', callback_data='btn9')
inline_kb9 = InlineKeyboardMarkup().add(inline_btn_9)

inline_kb_full = InlineKeyboardMarkup(raw_width=2).add(inline_btn_4)
inline_btn_5 = InlineKeyboardButton('🗣Имперцы', callback_data='btn5')
inline_btn_6 = InlineKeyboardButton('🗣Повстанцы', callback_data='btn6')
inline_kb_full.row(inline_btn_5, inline_btn_6)
inline_kb_full.add(InlineKeyboardButton('🔗Чат конкурса', url='https://t.me/MafiaWarChaos'))

inline_kb_dnd = InlineKeyboardMarkup(raw_width=2).add(inline_btn_4)
inline_btn_5 = InlineKeyboardButton('🗣Имперцы', callback_data='btn5')
inline_btn_6 = InlineKeyboardButton('🗣Повстанцы', callback_data='btn6')
inline_kb_dnd.row(inline_btn_5, inline_btn_6)
inline_kb_dnd.add(inline_btn_1)
inline_kb_dnd.add(inline_btn_2)
inline_kb_dnd.add(inline_btn_3)
inline_kb_dnd.add(InlineKeyboardButton('🔗Чат конкурса', url='https://t.me/MafiaWarChaos'))

##

inline_ff_1 = InlineKeyboardButton('Дон Капони', callback_data='A')
inline_ff_2 = InlineKeyboardButton('Comet', callback_data='D')
inline_a_1 = InlineKeyboardButton('Арматура', callback_data='G')
inline_a_2 = InlineKeyboardButton('Ая', callback_data='H')
inline_a_3 = InlineKeyboardButton('Nevill', callback_data='I')
inline_a_4 = InlineKeyboardButton('Amin a', callback_data='J')
inline_a_5 = InlineKeyboardButton('...', callback_data='K')
inline_a_6 = InlineKeyboardButton('Ляля', callback_data='L')
inline_a_7 = InlineKeyboardButton('Lemon', callback_data='M')
inline_a_8 = InlineKeyboardButton('Dasha', callback_data='N')
inline_a_9 = InlineKeyboardButton('леля', callback_data='O')
inline_b_1 = InlineKeyboardButton('~teftelka~', callback_data='P')
inline_b_2 = InlineKeyboardButton('Нiкiта', callback_data='Q')
inline_b_3 = InlineKeyboardButton('Arbie', callback_data='R')
inline_b_4 = InlineKeyboardButton('Beks', callback_data='S')
inline_b_5 = InlineKeyboardButton('AtacmsUA', callback_data='T')
inline_b_6 = InlineKeyboardButton('Diana', callback_data='Y')
inline_b_7 = InlineKeyboardButton('DARKSIDE', callback_data='V')
inline_b_8 = InlineKeyboardButton('Lady Cat', callback_data='W')
inline_b_9 = InlineKeyboardButton('Dina', callback_data='X')
inline_c_1 = InlineKeyboardButton('юлябасик', callback_data='Z')
inline_kb_dnd1 = InlineKeyboardMarkup(raw_width=2).add(inline_ff_1, inline_b_8)
inline_kb_dnd1.add(inline_a_1, inline_a_2)
inline_kb_dnd1.add(inline_a_3, inline_a_4)
inline_kb_dnd1.add(inline_a_5, inline_a_6)
inline_kb_dnd1.add(inline_a_7, inline_a_8)
inline_kb_dnd1.add(inline_a_9, inline_b_1)
inline_kb_dnd1.add(inline_b_2, inline_b_3)
inline_kb_dnd1.add(inline_b_4, inline_b_5)
inline_kb_dnd1.add(inline_b_6, inline_b_7)
inline_kb_dnd1.add(inline_b_9, inline_c_1)

inline_v_1 = InlineKeyboardButton('🏙Первый день', callback_data='IJ')
inline_v_2 = InlineKeyboardButton('🏙Второй день', callback_data='JK')
inline_kb_v = InlineKeyboardMarkup(raw_width=2).row(inline_v_1, inline_v_2)

inline_v_3 = InlineKeyboardButton('🗂Количество игр', callback_data='x1')
inline_v_4 = InlineKeyboardButton('🎯Побед', callback_data='x2')
inline_v_5 = InlineKeyboardButton('❌Проигрышей', callback_data='x3')
inline_v_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='x4')
inline_kb_v1 = InlineKeyboardMarkup(raw_width=2).add(inline_v_3)
inline_kb_v1.add(inline_v_4, inline_v_5)
inline_kb_v1.add(inline_v_6)

inline_v_7 = InlineKeyboardButton('🗂Количество игр', callback_data='x5')
inline_v_8 = InlineKeyboardButton('🎯Побед', callback_data='x6')
inline_v_9 = InlineKeyboardButton('❌Проигрышей', callback_data='x7')
inline_vv_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='x8')
inline_kb_v2 = InlineKeyboardMarkup(raw_width=2).add(inline_v_7)
inline_kb_v2.add(inline_v_8, inline_v_9)
inline_kb_v2.add(inline_vv_1)

##

inline_u_1 = InlineKeyboardButton('🏙Первый день', callback_data='GH')
inline_u_2 = InlineKeyboardButton('🏙Второй день', callback_data='HI')
inline_kb_u = InlineKeyboardMarkup(raw_width=2).row(inline_u_1, inline_u_2)

inline_u_3 = InlineKeyboardButton('🗂Количество игр', callback_data='w1')
inline_u_4 = InlineKeyboardButton('🎯Побед', callback_data='w2')
inline_u_5 = InlineKeyboardButton('❌Проигрышей', callback_data='w3')
inline_u_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='w4')
inline_kb_u1 = InlineKeyboardMarkup(raw_width=2).add(inline_u_3)
inline_kb_u1.add(inline_u_4, inline_u_5)
inline_kb_u1.add(inline_u_6)

inline_u_7 = InlineKeyboardButton('🗂Количество игр', callback_data='w5')
inline_u_8 = InlineKeyboardButton('🎯Побед', callback_data='w6')
inline_u_9 = InlineKeyboardButton('❌Проигрышей', callback_data='w7')
inline_uu_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='w8')
inline_kb_u2 = InlineKeyboardMarkup(raw_width=2).add(inline_u_7)
inline_kb_u2.add(inline_u_8, inline_u_9)
inline_kb_u2.add(inline_uu_1)

##

inline_t_1 = InlineKeyboardButton('🏙Первый день', callback_data='EF')
inline_t_2 = InlineKeyboardButton('🏙Второй день', callback_data='FG')
inline_kb_t = InlineKeyboardMarkup(raw_width=2).row(inline_t_1, inline_t_2)

inline_t_3 = InlineKeyboardButton('🗂Количество игр', callback_data='vb1')
inline_t_4 = InlineKeyboardButton('🎯Побед', callback_data='vb2')
inline_t_5 = InlineKeyboardButton('❌Проигрышей', callback_data='vb3')
inline_t_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='vb4')
inline_kb_t1 = InlineKeyboardMarkup(raw_width=2).add(inline_t_3)
inline_kb_t1.add(inline_t_4, inline_t_5)
inline_kb_t1.add(inline_t_6)

inline_t_7 = InlineKeyboardButton('🗂Количество игр', callback_data='vb5')
inline_t_8 = InlineKeyboardButton('🎯Побед', callback_data='vb6')
inline_t_9 = InlineKeyboardButton('❌Проигрышей', callback_data='vb7')
inline_tt_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='vb8')
inline_kb_t2 = InlineKeyboardMarkup(raw_width=2).add(inline_t_7)
inline_kb_t2.add(inline_t_8, inline_t_9)
inline_kb_t2.add(inline_tt_1)

##

inline_s_1 = InlineKeyboardButton('🏙Первый день', callback_data='CD')
inline_s_2 = InlineKeyboardButton('🏙Второй день', callback_data='DE')
inline_kb_s = InlineKeyboardMarkup(raw_width=2).row(inline_s_1, inline_s_2)

inline_s_3 = InlineKeyboardButton('🗂Количество игр', callback_data='u1')
inline_s_4 = InlineKeyboardButton('🎯Побед', callback_data='u2')
inline_s_5 = InlineKeyboardButton('❌Проигрышей', callback_data='u3')
inline_s_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='u4')
inline_kb_s1 = InlineKeyboardMarkup(raw_width=2).add(inline_s_3)
inline_kb_s1.add(inline_s_4, inline_s_5)
inline_kb_s1.add(inline_s_6)

inline_s_7 = InlineKeyboardButton('🗂Количество игр', callback_data='u5')
inline_s_8 = InlineKeyboardButton('🎯Побед', callback_data='u6')
inline_s_9 = InlineKeyboardButton('❌Проигрышей', callback_data='u7')
inline_ss_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='u8')
inline_kb_s2 = InlineKeyboardMarkup(raw_width=2).add(inline_s_7)
inline_kb_s2.add(inline_s_8, inline_s_9)
inline_kb_s2.add(inline_s_1)

##

inline_r_1 = InlineKeyboardButton('🏙Первый день', callback_data='AB')
inline_r_2 = InlineKeyboardButton('🏙Второй день', callback_data='BC')
inline_kb_r = InlineKeyboardMarkup(raw_width=2).row(inline_r_1, inline_r_2)

inline_r_3 = InlineKeyboardButton('🗂Количество игр', callback_data='t1')
inline_r_4 = InlineKeyboardButton('🎯Побед', callback_data='t2')
inline_r_5 = InlineKeyboardButton('❌Проигрышей', callback_data='t3')
inline_r_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='t4')
inline_kb_r1 = InlineKeyboardMarkup(raw_width=2).add(inline_r_3)
inline_kb_r1.add(inline_r_4, inline_r_5)
inline_kb_r1.add(inline_r_6)

inline_r_7 = InlineKeyboardButton('🗂Количество игр', callback_data='t5')
inline_r_8 = InlineKeyboardButton('🎯Побед', callback_data='t6')
inline_r_9 = InlineKeyboardButton('❌Проигрышей', callback_data='t7')
inline_rr_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='t8')
inline_kb_r2 = InlineKeyboardMarkup(raw_width=2).add(inline_r_7)
inline_kb_r2.add(inline_r_8, inline_r_9)
inline_kb_r2.add(inline_rr_1)

##

inline_q_1 = InlineKeyboardButton('🏙Первый день', callback_data='YY')
inline_q_2 = InlineKeyboardButton('🏙Второй день', callback_data='ZZ')
inline_kb_q = InlineKeyboardMarkup(raw_width=2).row(inline_q_1, inline_q_2)

inline_q_3 = InlineKeyboardButton('🗂Количество игр', callback_data='s1')
inline_q_4 = InlineKeyboardButton('🎯Побед', callback_data='s2')
inline_q_5 = InlineKeyboardButton('❌Проигрышей', callback_data='s3')
inline_q_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='s4')
inline_kb_q1 = InlineKeyboardMarkup(raw_width=2).add(inline_q_3)
inline_kb_q1.add(inline_q_4, inline_q_5)
inline_kb_q1.add(inline_q_6)

inline_q_7 = InlineKeyboardButton('🗂Количество игр', callback_data='s5')
inline_q_8 = InlineKeyboardButton('🎯Побед', callback_data='s6')
inline_q_9 = InlineKeyboardButton('❌Проигрышей', callback_data='s7')
inline_qq_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='s8')
inline_kb_q2 = InlineKeyboardMarkup(raw_width=2).add(inline_q_7)
inline_kb_q2.add(inline_q_8, inline_q_9)
inline_kb_q2.add(inline_qq_1)

##

inline_p_1 = InlineKeyboardButton('🏙Первый день', callback_data='WW')
inline_p_2 = InlineKeyboardButton('🏙Второй день', callback_data='XX')
inline_kb_p = InlineKeyboardMarkup(raw_width=2).row(inline_p_1, inline_p_2)

inline_p_3 = InlineKeyboardButton('🗂Количество игр', callback_data='rp1')
inline_p_4 = InlineKeyboardButton('🎯Побед', callback_data='rp2')
inline_p_5 = InlineKeyboardButton('❌Проигрышей', callback_data='rp3')
inline_p_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='rp4')
inline_kb_p1 = InlineKeyboardMarkup(raw_width=2).add(inline_p_3)
inline_kb_p1.add(inline_p_4, inline_p_5)
inline_kb_p1.add(inline_p_6)

inline_p_7 = InlineKeyboardButton('🗂Количество игр', callback_data='rp5')
inline_p_8 = InlineKeyboardButton('🎯Побед', callback_data='rp6')
inline_p_9 = InlineKeyboardButton('❌Проигрышей', callback_data='rp7')
inline_pp_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='rp8')
inline_kb_p2 = InlineKeyboardMarkup(raw_width=2).add(inline_p_7)
inline_kb_p2.add(inline_p_8, inline_p_9)
inline_kb_p2.add(inline_pp_1)

##

inline_o_1 = InlineKeyboardButton('🏙Первый день', callback_data='UU')
inline_o_2 = InlineKeyboardButton('🏙Второй день', callback_data='VV')
inline_kb_o = InlineKeyboardMarkup(raw_width=2).row(inline_o_1, inline_o_2)

inline_o_3 = InlineKeyboardButton('🗂Количество игр', callback_data='q1')
inline_o_4 = InlineKeyboardButton('🎯Побед', callback_data='q2')
inline_o_5 = InlineKeyboardButton('❌Проигрышей', callback_data='q3')
inline_o_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='q4')
inline_kb_o1 = InlineKeyboardMarkup(raw_width=2).add(inline_o_3)
inline_kb_o1.add(inline_o_4, inline_o_5)
inline_kb_o1.add(inline_o_6)

inline_o_7 = InlineKeyboardButton('🗂Количество игр', callback_data='q5')
inline_o_8 = InlineKeyboardButton('🎯Побед', callback_data='q6')
inline_o_9 = InlineKeyboardButton('❌Проигрышей', callback_data='q7')
inline_oo_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='q8')
inline_kb_o2 = InlineKeyboardMarkup(raw_width=2).add(inline_o_7)
inline_kb_o2.add(inline_o_8, inline_o_9)
inline_kb_o2.add(inline_oo_1)

##

inline_n_1 = InlineKeyboardButton('🏙Первый день', callback_data='SS')
inline_n_2 = InlineKeyboardButton('🏙Второй день', callback_data='TT')
inline_kb_n = InlineKeyboardMarkup(raw_width=2).row(inline_n_1, inline_n_2)

inline_n_3 = InlineKeyboardButton('🗂Количество игр', callback_data='oo1')
inline_n_4 = InlineKeyboardButton('🎯Побед', callback_data='oo2')
inline_n_5 = InlineKeyboardButton('❌Проигрышей', callback_data='oo3')
inline_n_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='oo4')
inline_kb_n1 = InlineKeyboardMarkup(raw_width=2).add(inline_n_3)
inline_kb_n1.add(inline_n_4, inline_n_5)
inline_kb_n1.add(inline_n_6)

inline_n_7 = InlineKeyboardButton('🗂Количество игр', callback_data='oo5')
inline_n_8 = InlineKeyboardButton('🎯Побед', callback_data='oo6')
inline_n_9 = InlineKeyboardButton('❌Проигрышей', callback_data='oo7')
inline_nn_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='oo8')
inline_kb_n2 = InlineKeyboardMarkup(raw_width=2).add(inline_n_7)
inline_kb_n2.add(inline_n_8, inline_n_9)
inline_kb_n2.add(inline_nn_1)

##

inline_m_1 = InlineKeyboardButton('🏙Первый день', callback_data='QQ')
inline_m_2 = InlineKeyboardButton('🏙Второй день', callback_data='RR')
inline_kb_m = InlineKeyboardMarkup(raw_width=2).row(inline_m_1, inline_m_2)

inline_m_3 = InlineKeyboardButton('🗂Количество игр', callback_data='l1')
inline_m_4 = InlineKeyboardButton('🎯Побед', callback_data='l2')
inline_m_5 = InlineKeyboardButton('❌Проигрышей', callback_data='l3')
inline_m_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='l4')
inline_kb_m1 = InlineKeyboardMarkup(raw_width=2).add(inline_m_3)
inline_kb_m1.add(inline_m_4, inline_m_5)
inline_kb_m1.add(inline_m_6)

inline_m_7 = InlineKeyboardButton('🗂Количество игр', callback_data='l5')
inline_m_8 = InlineKeyboardButton('🎯Побед', callback_data='l6')
inline_m_9 = InlineKeyboardButton('❌Проигрышей', callback_data='l7')
inline_mm_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='l8')
inline_kb_m2 = InlineKeyboardMarkup(raw_width=2).add(inline_m_7)
inline_kb_m2.add(inline_m_8, inline_m_9)
inline_kb_m2.add(inline_mm_1)

##

inline_l_1 = InlineKeyboardButton('🏙Первый день', callback_data='OO')
inline_l_2 = InlineKeyboardButton('🏙Второй день', callback_data='PP')
inline_kb_l = InlineKeyboardMarkup(raw_width=2).row(inline_l_1, inline_l_2)

inline_l_3 = InlineKeyboardButton('🗂Количество игр', callback_data='k1')
inline_l_4 = InlineKeyboardButton('🎯Побед', callback_data='k2')
inline_l_5 = InlineKeyboardButton('❌Проигрышей', callback_data='k3')
inline_l_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='k4')
inline_kb_l1 = InlineKeyboardMarkup(raw_width=2).add(inline_l_3)
inline_kb_l1.add(inline_l_4, inline_l_5)
inline_kb_l1.add(inline_l_6)

inline_l_7 = InlineKeyboardButton('🗂Количество игр', callback_data='k5')
inline_l_8 = InlineKeyboardButton('🎯Побед', callback_data='k6')
inline_l_9 = InlineKeyboardButton('❌Проигрышей', callback_data='k7')
inline_ll_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='k8')
inline_kb_l2 = InlineKeyboardMarkup(raw_width=2).add(inline_l_7)
inline_kb_l2.add(inline_l_8, inline_l_9)
inline_kb_l2.add(inline_ll_1)

##

inline_k_1 = InlineKeyboardButton('🏙Первый день', callback_data='MM')
inline_k_2 = InlineKeyboardButton('🏙Второй день', callback_data='NN')
inline_kb_k = InlineKeyboardMarkup(raw_width=2).row(inline_k_1, inline_k_2)

inline_k_3 = InlineKeyboardButton('🗂Количество игр', callback_data='j1')
inline_k_4 = InlineKeyboardButton('🎯Побед', callback_data='j2')
inline_k_5 = InlineKeyboardButton('❌Проигрышей', callback_data='j3')
inline_k_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='j4')
inline_kb_k1 = InlineKeyboardMarkup(raw_width=2).add(inline_k_3)
inline_kb_k1.add(inline_k_4, inline_k_5)
inline_kb_k1.add(inline_k_6)

inline_k_7 = InlineKeyboardButton('🗂Количество игр', callback_data='j5')
inline_k_8 = InlineKeyboardButton('🎯Побед', callback_data='j6')
inline_k_9 = InlineKeyboardButton('❌Проигрышей', callback_data='j7')
inline_kk_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='j8')
inline_kb_k2 = InlineKeyboardMarkup(raw_width=2).add(inline_k_7)
inline_kb_k2.add(inline_k_8, inline_k_9)
inline_kb_k2.add(inline_kk_1)

##

inline_i_1 = InlineKeyboardButton('🏙Первый день', callback_data='KK')
inline_i_2 = InlineKeyboardButton('🏙Второй день', callback_data='LL')
inline_kb_i = InlineKeyboardMarkup(raw_width=2).row(inline_i_1, inline_i_2)

inline_i_3 = InlineKeyboardButton('🗂Количество игр', callback_data='h1')
inline_i_4 = InlineKeyboardButton('🎯Побед', callback_data='h2')
inline_i_5 = InlineKeyboardButton('❌Проигрышей', callback_data='h3')
inline_i_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='h4')
inline_kb_i1 = InlineKeyboardMarkup(raw_width=2).add(inline_i_3)
inline_kb_i1.add(inline_i_4, inline_i_5)
inline_kb_i1.add(inline_i_6)

inline_i_7 = InlineKeyboardButton('🗂Количество игр', callback_data='h5')
inline_i_8 = InlineKeyboardButton('🎯Побед', callback_data='h6')
inline_i_9 = InlineKeyboardButton('❌Проигрышей', callback_data='h7')
inline_ii_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='h8')
inline_kb_i2 = InlineKeyboardMarkup(raw_width=2).add(inline_i_7)
inline_kb_i2.add(inline_i_8, inline_i_9)
inline_kb_i2.add(inline_ii_1)

##

inline_j_1 = InlineKeyboardButton('🏙Первый день', callback_data='II')
inline_j_2 = InlineKeyboardButton('🏙Второй день', callback_data='JJ')
inline_kb_j = InlineKeyboardMarkup(raw_width=2).row(inline_j_1, inline_j_2)

inline_j_3 = InlineKeyboardButton('🗂Количество игр', callback_data='f1')
inline_j_4 = InlineKeyboardButton('🎯Побед', callback_data='f2')
inline_j_5 = InlineKeyboardButton('❌Проигрышей', callback_data='3')
inline_j_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='f4')
inline_kb_j1 = InlineKeyboardMarkup(raw_width=2).add(inline_j_3)
inline_kb_j1.add(inline_j_4, inline_j_5)
inline_kb_j1.add(inline_j_6)

inline_j_7 = InlineKeyboardButton('🗂Количество игр', callback_data='f5')
inline_j_8 = InlineKeyboardButton('🎯Побед', callback_data='f6')
inline_j_9 = InlineKeyboardButton('❌Проигрышей', callback_data='f7')
inline_jj_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='f8')
inline_kb_j2 = InlineKeyboardMarkup(raw_width=2).add(inline_j_7)
inline_kb_j2.add(inline_j_8, inline_j_9)
inline_kb_j2.add(inline_jj_1)

##

inline_h_1 = InlineKeyboardButton('🏙Первый день', callback_data='GG')
inline_h_2 = InlineKeyboardButton('🏙Второй день', callback_data='HH')
inline_kb_h = InlineKeyboardMarkup(raw_width=2).row(inline_h_1, inline_h_2)

inline_h_3 = InlineKeyboardButton('🗂Количество игр', callback_data='e1')
inline_h_4 = InlineKeyboardButton('🎯Побед', callback_data='e2')
inline_h_5 = InlineKeyboardButton('❌Проигрышей', callback_data='e3')
inline_h_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='e4')
inline_kb_h1 = InlineKeyboardMarkup(raw_width=2).add(inline_h_3)
inline_kb_h1.add(inline_h_4, inline_h_5)
inline_kb_h1.add(inline_h_6)

inline_h_7 = InlineKeyboardButton('🗂Количество игр', callback_data='e5')
inline_h_8 = InlineKeyboardButton('🎯Побед', callback_data='e6')
inline_h_9 = InlineKeyboardButton('❌Проигрышей', callback_data='e7')
inline_hh_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='e8')
inline_kb_h2 = InlineKeyboardMarkup(raw_width=2).add(inline_h_7)
inline_kb_h2.add(inline_h_8, inline_h_9)
inline_kb_h2.add(inline_hh_1)

##

inline_g_1 = InlineKeyboardButton('🏙Первый день', callback_data='EE')
inline_g_2 = InlineKeyboardButton('🏙Второй день', callback_data='FF')
inline_kb_g = InlineKeyboardMarkup(raw_width=2).row(inline_g_1, inline_g_2)

inline_g_3 = InlineKeyboardButton('🗂Количество игр', callback_data='d1')
inline_g_4 = InlineKeyboardButton('🎯Побед', callback_data='d2')
inline_g_5 = InlineKeyboardButton('❌Проигрышей', callback_data='d3')
inline_g_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='d4')
inline_kb_g1 = InlineKeyboardMarkup(raw_width=2).add(inline_g_3)
inline_kb_g1.add(inline_g_4, inline_g_5)
inline_kb_g1.add(inline_g_6)

inline_g_7 = InlineKeyboardButton('🗂Количество игр', callback_data='d5')
inline_g_8 = InlineKeyboardButton('🎯Побед', callback_data='d6')
inline_g_9 = InlineKeyboardButton('❌Проигрышей', callback_data='d7')
inline_gg_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='d8')
inline_kb_g2 = InlineKeyboardMarkup(raw_width=2).add(inline_g_7)
inline_kb_g2.add(inline_g_8, inline_g_9)
inline_kb_g2.add(inline_gg_1)

##

inline_f_1 = InlineKeyboardButton('🏙Первый день', callback_data='CC')
inline_f_2 = InlineKeyboardButton('🏙Второй день', callback_data='DD')
inline_kb_f = InlineKeyboardMarkup(raw_width=2).row(inline_f_1, inline_f_2)

inline_f_3 = InlineKeyboardButton('🗂Количество игр', callback_data='c1')
inline_f_4 = InlineKeyboardButton('🎯Побед', callback_data='c2')
inline_f_5 = InlineKeyboardButton('❌Проигрышей', callback_data='c3')
inline_f_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='c4')
inline_kb_f1 = InlineKeyboardMarkup(raw_width=2).add(inline_f_3)
inline_kb_f1.add(inline_f_4, inline_f_5)
inline_kb_f1.add(inline_f_6)

inline_f_7 = InlineKeyboardButton('🗂Количество игр', callback_data='c5')
inline_f_8 = InlineKeyboardButton('🎯Побед', callback_data='c6')
inline_f_9 = InlineKeyboardButton('❌Проигрышей', callback_data='c7')
inline_ff_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='c8')
inline_kb_f2 = InlineKeyboardMarkup(raw_width=2).add(inline_f_7)
inline_kb_f2.add(inline_f_8, inline_f_9)
inline_kb_f2.add(inline_ff_1)

##

inline_e_1 = InlineKeyboardButton('🏙Первый день', callback_data='AAA')
inline_e_2 = InlineKeyboardButton('🏙Второй день', callback_data='BBB')
inline_kb_e = InlineKeyboardMarkup(raw_width=2).row(inline_e_1, inline_e_2)

inline_e_3 = InlineKeyboardButton('🗂Количество игр', callback_data='bb1')
inline_e_4 = InlineKeyboardButton('🎯Побед', callback_data='bb2')
inline_e_5 = InlineKeyboardButton('❌Проигрышей', callback_data='bb3')
inline_e_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='bb4')
inline_kb_e1 = InlineKeyboardMarkup(raw_width=2).add(inline_e_3)
inline_kb_e1.add(inline_e_4, inline_e_5)
inline_kb_e1.add(inline_e_6)

inline_e_7 = InlineKeyboardButton('🗂Количество игр', callback_data='bb5')
inline_e_8 = InlineKeyboardButton('🎯Побед', callback_data='bb6')
inline_e_9 = InlineKeyboardButton('❌Проигрышей', callback_data='bb7')
inline_ee_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='bb8')
inline_kb_e2 = InlineKeyboardMarkup(raw_width=2).add(inline_e_7)
inline_kb_e2.add(inline_e_8, inline_e_9)
inline_kb_e2.add(inline_ee_1)

##

inline_d_1 = InlineKeyboardButton('🏙Первый день', callback_data='AA')
inline_d_2 = InlineKeyboardButton('🏙Второй день', callback_data='BB')
inline_kb_a = InlineKeyboardMarkup(raw_width=2).row(inline_d_1, inline_d_2)

inline_d_3 = InlineKeyboardButton('🗂Количество игр', callback_data='aa1')
inline_d_4 = InlineKeyboardButton('🎯Побед', callback_data='aa2')
inline_d_5 = InlineKeyboardButton('❌Проигрышей', callback_data='aa3')
inline_d_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='aa4')
inline_kb_a1 = InlineKeyboardMarkup(raw_width=2).add(inline_d_3)
inline_kb_a1.add(inline_d_4, inline_d_5)
inline_kb_a1.add(inline_d_6)

inline_d_7 = InlineKeyboardButton('🗂Количество игр', callback_data='aa5')
inline_d_8 = InlineKeyboardButton('🎯Побед', callback_data='aa6')
inline_d_9 = InlineKeyboardButton('❌Проигрышей', callback_data='aa7')
inline_dd_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='aa8')
inline_kb_a2 = InlineKeyboardMarkup(raw_width=2).add(inline_d_7)
inline_kb_a2.add(inline_d_8, inline_d_9)
inline_kb_a2.add(inline_dd_1)

##

#Don Kaponi
inline_bob_3 = InlineKeyboardButton('🗂Количество игр', callback_data='bob3')
inline_bob_4 = InlineKeyboardButton('🎯Побед', callback_data='bob4')
inline_bob_5 = InlineKeyboardButton('❌Проигрышей', callback_data='bob5')
inline_bob_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='bob6')
inline_kb_dnd3 = InlineKeyboardMarkup(raw_width=2).add(inline_bob_3)
inline_kb_dnd3.add(inline_bob_4, inline_bob_5)
inline_kb_dnd3.add(inline_bob_6)

inline_f_7 = InlineKeyboardButton('🗂Количество игр', callback_data='b1')
inline_f_8 = InlineKeyboardButton('🎯Побед', callback_data='b2')
inline_f_9 = InlineKeyboardButton('❌Проигрышей', callback_data='b3')
inline_f_1 = InlineKeyboardButton('🔋Ресурсы', callback_data='b4')
inline_kb_dnd4 = InlineKeyboardMarkup(raw_width=2).add(inline_f_7)
inline_kb_dnd4.add(inline_f_8, inline_f_9)
inline_kb_dnd4.add(inline_f_1)

inline_bob_7 = InlineKeyboardButton('🏙Первый день', callback_data='B')
inline_bob_8 = InlineKeyboardButton('🏙Второй день', callback_data='C')
inline_kb_dnd2 = InlineKeyboardMarkup(raw_width=2).row(inline_bob_7, inline_bob_8)

##

#Comet
inline_ff_7 = InlineKeyboardButton('🏙Первый день', callback_data='E')
inline_ff_8 = InlineKeyboardButton('🏙Второй день', callback_data='F')
inline_kb_dnd5 = InlineKeyboardMarkup(raw_width=2).row(inline_ff_7, inline_ff_8)

inline_ff_3 = InlineKeyboardButton('🗂Количество игр', callback_data='aaa1')
inline_ff_4 = InlineKeyboardButton('🎯Побед', callback_data='aaa2')
inline_ff_5 = InlineKeyboardButton('❌Проигрышей', callback_data='aaa3')
inline_ff_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='aaa4')
inline_kb_dnd6 = InlineKeyboardMarkup(raw_width=2).add(inline_ff_3)
inline_kb_dnd6.add(inline_ff_4, inline_ff_5)
inline_kb_dnd6.add(inline_ff_6)

inline_f_3 = InlineKeyboardButton('🗂Количество игр', callback_data='aaa5')
inline_f_4 = InlineKeyboardButton('🎯Побед', callback_data='aaa6')
inline_f_5 = InlineKeyboardButton('❌Проигрышей', callback_data='aaa7')
inline_f_6 = InlineKeyboardButton('🔋Ресурсы', callback_data='aaa8')
inline_kb_dnd7 = InlineKeyboardMarkup(raw_width=2).add(inline_f_3)
inline_kb_dnd7.add(inline_f_4, inline_f_5)
inline_kb_dnd7.add(inline_f_6)

inline_res_1 = InlineKeyboardButton('🏙Первый день', callback_data='res1')
inline_res_2 = InlineKeyboardButton('🏙Второй день', callback_data='res2')
inline_res_3 = InlineKeyboardButton('🌄Всего', callback_data='res3')
inline_kb_res1 = InlineKeyboardMarkup(raw_width=2).add(inline_res_1, inline_res_2)
inline_kb_res1.add(inline_res_3)

inline_res_4 = InlineKeyboardButton('🏙Первый день', callback_data='res4')
inline_res_5 = InlineKeyboardButton('🏙Второй день', callback_data='res5')
inline_res_6 = InlineKeyboardButton('🌄Всего', callback_data='res6')
inline_kb_res2 = InlineKeyboardMarkup(raw_width=2).add(inline_res_4, inline_res_5)
inline_kb_res2.add(inline_res_6)

inline_res_7 = InlineKeyboardButton('Имперцы')
inline_res_8 = InlineKeyboardButton('Повстанцы')
inline_kb_res3 = InlineKeyboardMarkup(raw_width=2).add(inline_res_7, inline_res_8)
inline_kb_res3.add(inline_res_1, inline_res_4)
inline_kb_res3.add(inline_res_2, inline_res_5)
inline_kb_res3.add(inline_res_3, inline_res_6)