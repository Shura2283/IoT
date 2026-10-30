import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Arduino vs Raspberry Pi | O'quv Portali",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Yashil, ko'k, sariq va qizil uyg'unligidagi ochiq fon va QORA MATNLAR uchun CSS
st.markdown("""
<style>
    /* Ochiq rangli fon */
    .stApp {
        background-color: #f8fafc;
        background-image: 
            radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.16) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.16) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.16) 0px, transparent 50%),
            radial-gradient(at 0% 100%, rgba(239, 68, 68, 0.13) 0px, transparent 50%);
        background-attachment: fixed;
    }
    
    /* BARCHA MATNLARNI TO'LIQ QORA VA ANIQLASHTIRISH */
    html, body, p, span, label, li {
        color: #0f172a !important;
        font-weight: 500 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-weight: 800 !important;
    }

    /* Radio tugmalar va variantlar yozuvlari */
    div[role="radiogroup"] label p {
        color: #000000 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
    }

    /* Oq rangli kartalar */
    .content-box {
        background-color: rgba(255, 255, 255, 0.95);
        border: 1px solid #cbd5e1;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07);
    }
    
    .author-badge {
        background: #ffffff;
        border: 2px solid #059669;
        padding: 10px 24px;
        border-radius: 9999px;
        display: inline-block;
        font-weight: 700;
        color: #000000 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Muallif nishoni
st.markdown("""
<div style="text-align: center;">
    <div class="author-badge">
        👨‍🏫 Tuzuvchi: <span style="color: #059669; font-weight: 800;">Quljanova Shukurjon Zaribovna</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Bosh sarlavha
st.markdown("""
<h1 style='text-align: center; margin-bottom: 5px;'>
    ARDUINO MIKROKONTROLLERI VA RASPBERRY PI MINI KOMPYUTERLARI
</h1>
<p style='text-align: center; font-size: 1.2rem; color: #1e293b !important; margin-bottom: 25px;'>
    Funksiyalarini o'rganish, apparat parametrlarini solishtirish va bilimlarni 25 ta test orqali sinash
</p>
""", unsafe_allow_html=True)

st.divider()

# Chap tarafdagi navigatsiya menyusi
st.sidebar.title("📌 Menyu")
menu = st.sidebar.radio(
    "Bo'limni tanlang:",
    [
        "1. Nazariy Tushunchalar & Rasmlar", 
        "2. Qiyosiy Taqqoslash Matritsasi", 
        "3. Amaliy Laboratoriya Mashg'ulotlari", 
        "4. 25 Savolli Imtihon Testi"
    ]
)

# -----------------------------------------------------------------------------
# 1-BO'LIM: NAZARIYA VA INTERNET RASMLARI
# -----------------------------------------------------------------------------
if menu == "1. Nazariy Tushunchalar & Rasmlar":
    st.header("1. Fundamental Nazariy Tushunchalar va Uskunalar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("🔹 Arduino Uno (Mikrokontroller)")
        # Internetdan olingan aniq rasm (Arduino Uno Wikimedia)
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/38/Arduino_Uno_-_R3.jpg", 
                 caption="Arduino Uno R3 mikrokontroller platasi", use_container_width=True)
        
        st.markdown("""
        * **Toifasi:** MCU (Microcontroller Unit) — Bare-Metal real-vaqt tizimi.
        * **Chip:** ATmega328P (8-bitli AVR RISC Garvard arxitekturasi).
        * **Xotira tuzilishi:** 32 KB Flash xotira (dastur kodi uchun), 2 KB SRAM (operativ xotira) va 1 KB EEPROM.
        * **Vazifasi:** Datchiklar, rele, servomotorlar va signallarni mikrosekund aniqlikda, kechikishsiz (deterministic) boshqarish.
        * **Energiya sarfi:** Atigi 40-50 mA; quvvat tejamkor rejimda mikroamper sarflaydi.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("🔸 Raspberry Pi 4 (Mini Kompyuter)")
        # Internetdan olingan aniq rasm (Raspberry Pi 4 Wikimedia)
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg", 
                 caption="Raspberry Pi 4 Model B mini kompyuteri", use_container_width=True)
        
        st.markdown("""
        * **Toifasi:** SBC (Single Board Computer) — to'laqonli ko'p vazifali kompyuter.
        * **Chip:** Broadcom BCM2711, 4 yadroli ARM Cortex-A72 (64-bit Fon-Neyman arxitekturasi).
        * **Xotira:** 2GB, 4GB yoki 8GB LPDDR4 operativ xotira, MicroSD kartada Linux operatsion tizimi (Raspberry Pi OS).
        * **Vazifasi:** Video oqimlarni tahlil qilish (OpenCV), sun'iy intellekt modellarini ishga tushirish, veb-server va IoT shlyuzi.
        * **Energiya sarfi:** 600 mA dan 3000 mA gacha (5V / 3A Type-C quvvat talab qiladi).
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Arxitektura taqqoslash rasmi
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Garvard (Arduino) va Fon-Neyman (Raspberry Pi) Arxitekturalari")
    st.write("Arduino mikrokontrollerida dastur xotirasi (Flash) va ma'lumot xotirasi (RAM) bir-biridan alohida shinalarga ega (Garvard arxitekturasi). Raspberry Pi kompyuterida esa dastur va ma'lumotlar umumiy operativ xotirada joylashadi (Fon-Neyman arxitekturasi).")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Von_Neumann_Architecture.svg/800px-Von_Neumann_Architecture.svg.png", 
             caption="Fon-Neyman arxitekturasi: Umumiy xotira va shina tizimi", width=550)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2-BO'LIM: SOLISHTIRUV MATRITSASI
# -----------------------------------------------------------------------------
elif menu == "2. Qiyosiy Taqqoslash Matritsasi":
    st.header("2. Qiyosiy Texnik Parametrlar Matritsasi")
    
    st.markdown("""
    <div class="content-box">
        <h4 style="color:#000000; margin-top:0;">Arduino Uno R3 va Raspberry Pi 4 Model B solishtirmasi</h4>
    """, unsafe_allow_html=True)
    
    comparison_table = {
        "Texnik Xususiyat": [
            "Qurilma toifasi",
            "Markaziy protsessor",
            "Takt chastotasi",
            "Operativ xotira (RAM)",
            "Doimiy xotira (Storage)",
            "GPIO Mantiqiy Kuchlanishi",
            "Analog kirishlar (ADC)",
            "Operatsion tizim",
            "Displey chiqishlari",
            "Asosiy dasturlash tili"
        ],
        "Arduino Uno R3": [
            "Mikrokontroller (MCU)",
            "ATmega328P (8-bit)",
            "16 MHz",
            "2 KB SRAM",
            "32 KB Flash",
            "5V mantiqiy daraja",
            "Mavjud (6 ta 10-bitli ADC)",
            "Yo'q (Bare-metal)",
            "Yo'q",
            "C / C++ (Arduino IDE)"
        ],
        "Raspberry Pi 4 Model B": [
            "Mini Kompyuter (SBC)",
            "Broadcom BCM2711 4-yadro (64-bit)",
            "1.5 GHz – 1.8 GHz",
            "2 GB / 4 GB / 8 GB LPDDR4",
            "MicroSD karta (16GB - 256GB)",
            "3.3V (5V berilsa port kuyadi!)",
            "Yo'q (Tashqi chip kerak)",
            "Linux (Raspberry Pi OS, Ubuntu)",
            "2x micro-HDMI (4K 60fps)",
            "Python, Bash, C++, JavaScript"
        ]
    }
    
    st.table(comparison_table)
    st.markdown("""
        <div style="background-color: #fee2e2; border-left: 6px solid #ef4444; padding: 12px; border-radius: 6px; margin-top: 15px;">
            <strong style="color: #991b1b;">⚠️ OGOHLANTIRISH:</strong> 
            <span style="color: #7f1d1d;">Raspberry Pi GPIO pinlariga hech qachon 5V kuchlanish bermang! Arduino 5V kuchlanishda, Raspberry Pi esa 3.3V kuchlanishda ishlaydi. Ular birga ulanganda albatta <strong>Logic Level Shifter</strong> (mantiqiy daraja moslagich) ishlatilishi shart.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3-BO'LIM: AMALIY LABORATORIYA MASHG'ULOTLARI
# -----------------------------------------------------------------------------
elif menu == "3. Amaliy Laboratoriya Mashg'ulotlari":
    st.header("3. Amaliy Laboratoriya Mashg'ulotlari va Sxemalar")
    
    lab_tab1, lab_tab2 = st.tabs(["1-Laboratoriya: Arduino PWM", "2-Laboratoriya: Raspberry Pi Sensor"])
    
    with lab_tab1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Arduino: Analog Potentsiometr va PWM LED")
        st.write("Ushbu laboratoriyada A0 analog portidan 10-bitli (0–1023) ma'lumot o'qilib, 9-raqamli PWM pin orqali LED yorug'ligi silliq boshqariladi.")
        
        # Arduino va potentsiometr ulanish sxemasi (Internetdan)
        st.image("https://docs.arduino.cc/static/a38e8ec43685bc1f6186411dd78a3c89/read-analog-voltage.png", 
                 caption="Arduino analog kirish va potentsiometr ulanish sxemasi", width=550)
        
        st.markdown("**Arduino C++ Dastur Kodi:**")
        st.code("""// Arduino C++ KODI
const int potPin = A0;  // Potentsiometr o'rta oyog'i
const int ledPin = 9;   // LED anodi (220 Om rezistor orqali)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(potPin);          // 0 dan 1023 gacha o'qish
  int pwmValue = map(sensorValue, 0, 1023, 0, 255); // 0-255 diapazonga o'tkazish
  analogWrite(ledPin, pwmValue);                 // PWM signal uzatish
  delay(15);
}""", language="cpp")
        st.markdown('</div>', unsafe_allow_html=True)

    with lab_tab2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Raspberry Pi: DHT22 Raqamli Harorat va Namlik Sensori")
        st.write("DHT22 datchigi 3.3V quvvat va 4-raqamli GPIO piniga ulanadi. Linux muhitida Python yordamida o'qiladi.")
        
        # Raspberry Pi GPIO pinout xaritasi (Internetdan)
        st.image("https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png", 
                 caption="Raspberry Pi 40-pin GPIO xaritasi (Pin 1 = 3.3V, Pin 7 = GPIO4)", width=650)
        
        st.markdown("**Python Dastur Kodi:**")
        st.code("""# Python 3 (Raspberry Pi OS)
import time
import board
import adafruit_dht

# GPIO4 piniga ulangan DHT22 sensori
dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temp = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Harorat: {temp:.1f}°C | Namlik: {humidity:.1f}%")
    except RuntimeError as err:
        # Sensor o'qish xatolarini o'tkazib yuborish
        pass
    time.sleep(2.0)""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4-BO'LIM: 25 TA TEST TIZIMI
# -----------------------------------------------------------------------------
elif menu == "4. 25 Savolli Test":
    st.header("4. 25 Savolli Imtihon Testi")
    st.markdown("""
        <div style="background-color: #f1f5f9; padding: 10px 18px; border-radius: 8px; border-left: 5px solid #059669; margin-bottom: 20px;">
            <strong style="color: #000;">Test tuzuvchisi:</strong> <span style="color: #059669; font-weight: 800;">Quljanova Shukurjon Zaribovna</span>
        </div>
    """, unsafe_allow_html=True)

    quiz_data = [
        {"q": "1. Arduino Uno qaysi toifadagi hisoblash qurilmasi hisoblanadi?", "options": ["To'liq bir platalik kompyuter (SBC)", "Mikrokontroller platasi (MCU)", "Grafik tezlatkich (GPU)", "Qattiq disk nazoratchisi"], "correct": 1, "exp": "Arduino Uno — bu ATmega328P mikrokontrolleriga asoslangan bitta chipli boshqaruv platasidir."},
        {"q": "2. Raspberry Pi 4 qurilmasining arxitekturasi qanday?", "options": ["8-bitli Garvard AVR", "16-bitli PIC", "64-bitli ko'p yadroli ARM Cortex-A72", "32-bitli x86 Intel"], "correct": 2, "exp": "Raspberry Pi 4 to'rt yadroli 64-bitli ARM Cortex-A72 protsessoriga ega."},
        {"q": "3. Arduino Uno GPIO pinlarining mantiqiy ishchi kuchlanishi qanchaga teng?", "options": ["1.8V", "3.3V", "5.0V", "12.0V"], "correct": 2, "exp": "Arduino Uno standart holda 5V mantiqiy darajada ishlaydi."},
        {"q": "4. Raspberry Pi GPIO portiga to'g'ridan-to'g'ri 5V kuchlanish berilsa nima sodir bo'ladi?", "options": ["Tizim avtomatik 5V ni 3.3V ga tushiradi", "GPIO pini va SoC protsessor kuyishi mumkin", "Hech narsa bo'lmaydi, u 5V ga chidamli", "Faqat tizim qayta yuklanadi"], "correct": 1, "exp": "Raspberry Pi GPIO pinlari 3.3V tolerantli. 5V berish portni va protsessorni kuydiradi."},
        {"q": "5. Arduino Uno platasida nechta apparat analog kirish (ADC) kanali mavjud?", "options": ["2 ta", "6 ta (A0 dan A5 gacha)", "14 ta", "Mavjud emas"], "correct": 1, "exp": "Arduino Uno'da 6 ta 10-bitli ADC kanali mavjud."},
        {"q": "6. Raspberry Pi 4 platasida ichki analog kirishlar (ADC) bormi?", "options": ["Ha, 8 ta ichki ADC mavjud", "Yo'q, analog signallar uchun tashqi ADC chipi kerak", "Ha, faqat GPIO 2 va GPIO 3 analog ishlaydi", "Ha, barcha pinlar analog ishlay oladi"], "correct": 1, "exp": "Raspberry Pi faqat raqamli signallarni qabul qiladi. Analog signal uchun MCP3008 yoki ADS1115 kerak."},
        {"q": "7. Arduino Uno platasida mikrokontroller qanday takt chastotada ishlaydi?", "options": ["1.5 GHz", "16 MHz", "100 MHz", "500 kHz"], "correct": 1, "exp": "Arduino Uno 16 MHz chastotali kvars rezonatori orqali ishlaydi."},
        {"q": "8. Raspberry Pi 4 platasining tezkor xotirasi (RAM) qancha bo'lishi mumkin?", "options": ["2 KB SRAM", "32 KB", "2 GB, 4 GB yoki 8 GB LPDDR4", "128 MB"], "correct": 2, "exp": "Raspberry Pi 4 modellariga qarab 2GB, 4GB yoki 8GB operativ xotiraga ega bo'ladi."},
        {"q": "9. Arduino Uno'da yozilgan dasturlar qayerda saqlanadi?", "options": ["MicroSD fleshkada", "32 KB li ichki Flash xotirada", "RAM da", "Qattiq diskda"], "correct": 1, "exp": "Arduino kodi chip ichidagi 32 KB Flash xotirada doimiy saqlanadi."},
        {"q": "10. Raspberry Pi o'z operatsion tizimini (OS) qayerdan yuklaydi?", "options": ["Ichki 32 KB Flash xotiradan", "MicroSD kartadan yoki USB orqali ulangan SSD diskdan", "Protsessor keshidan", "Bios chipidan"], "correct": 1, "exp": "Raspberry Pi bootloader orqali MicroSD yoki USB drayverdagi operatsion tizimni yuklaydi."},
        {"q": "11. 'Deterministik real-vaqt ijrosi' (Deterministic Real-time) qaysi qurilmaga xos?", "options": ["Arduino mikrokontrolleriga", "Raspberry Pi (Linux) ga", "Har ikkalasiga teng", "Hech biriga"], "correct": 0, "exp": "Arduino operatsion tizimsiz (bare-metal) ishlagani sababli buyruqlarni mikrosekund aniqlikda bajaradi."},
        {"q": "12. Nima sababdan Raspberry Pi sanoat motorlarini boshqarishda mikrokontroller o'rnini to'liq bosa olmaydi?", "options": ["Raspberry Pi kuchi yetmaydi", "Linux ko'p vazifali bo'lgani uchun vaqt kechikishlari (jitter) yuzaga keladi", "Raspberry Pi elektr tokini o'tkazmaydi", "Unda Python tili ishlamaydi"], "correct": 1, "exp": "Ko'p vazifali operatsion tizimlarda vaqtni taqsimlash real vaqt talablariga to'liq javob bermaydi."},
        {"q": "13. Arduino Uno platasida nechta PWM (kenglik-impuls modulyatsiyasi) pini bor?", "options": ["2 ta", "6 ta (3, 5, 6, 9, 10, 11)", "14 ta", "PWM mavjud emas"], "correct": 1, "exp": "Arduino Uno platasida '~' belgisi bo'lgan 6 ta pin apparat PWM ni qo'llab-quvvatlaydi."},
        {"q": "14. Qaysi vazifada Raspberry Pi Arduino'dan ancha ustun va to'g'ri tanlov hisoblanadi?", "options": ["Oddiy tugma bosilganda LED yoqish", "Kompyuter ko'rishi (OpenCV orqali yuzni aniqlash)", "Releyni har 5 sekundda ochib yopish", "Suv sathini o'lchash"], "correct": 1, "exp": "OpenCV va neyron tarmoqlar yuqori chastota, katta RAM va video drayverlarni talab qiladi."},
        {"q": "15. Arduino Uno batareyada (masalan, 9V yoki Li-ion) qancha vaqt ishlashi mumkin?", "options": ["Ko'pi bilan 10 minut", "Kam energiya sarfi sabab oylardan yillargacha (uyqu rejimida)", "Batareyada umuman ishlamaydi", "Faqat 1 soat"], "correct": 1, "exp": "Arduino 'Deep Sleep' rejimida mikroamper sarflab oylab xizmat qiladi."},
        {"q": "16. Raspberry Pi 4 ni to'liq yuklama ostida ishlatish uchun qanday quvvat manbai kerak?", "options": ["3.3V, 100mA", "5V, kamida 3A (15W) USB Type-C", "12V, 10A", "Oddiy soat batareyasi"], "correct": 1, "exp": "Raspberry Pi 4 to'liq ishlashi uchun 5V / 3A USB-C quvvat bloki shart."},
        {"q": "17. Garvard arxitekturasi Fon-Neyman arxitekturasidan nima bilan farq qiladi?", "options": ["Garvardda ma'lumotlar va dastur ko'rsatmalari uchun alohida xotira shinalari ishlatiladi", "Fon-Neymanda operativ xotira bo'lmaydi", "Garvard faqat simsiz tarmoqda ishlaydi", "Ular o'rtasida hech qanday farq yo'q"], "correct": 0, "exp": "Garvard arxitekturasida Flash va SRAM jismonan alohida shinalarga ega."},
        {"q": "18. Arduino IDE dasturida yozilgan kod qaysi til oilasiga kiradi?", "options": ["Python", "C / C++", "Java", "HTML / CSS"], "correct": 1, "exp": "Arduino C/C++ tillari asosida soddalashtirilgan kutubxonalar bilan dasturlanadi."},
        {"q": "19. Raspberry Pi 4'da nechta monitor ulash imkoniyati bor?", "options": ["Faqat 1 ta VGA", "2 ta 4K monitor (ikkita micro-HDMI orqali)", "Monitor ulab bo'lmaydi", "4 ta"], "correct": 1, "exp": "Raspberry Pi 4 ikkita micro-HDMI porti orqali 4K formatdagi ikkita monitorni boshqaradi."},
        {"q": "20. Arduino Uno'dagi analogRead() funksiyasi qanday diapazondagi qiymat qaytaradi?", "options": ["0 dan 1 gacha (faqat HIGH/LOW)", "0 dan 255 gacha", "0 dan 1023 gacha (10-bit ruxsat)", "0 dan 65535 gacha"], "correct": 2, "exp": "Arduino Uno ADC'si 10-bitli bo'lgani sababli qiymat 0 dan 1023 gacha o'zgaradi."},
        {"q": "21. Raspberry Pi'dagi 40 pinli ulagichning rasmiy nomi nima?", "options": ["USB Header", "40-pin GPIO Header", "SATA port", "PCI Express"], "correct": 1, "exp": "Ushbu interfeys rasman 40-pin GPIO Header deb yuritiladi."},
        {"q": "22. Qaysi aloqa interfeysi Arduino va Raspberry Pi o'rtasida ma'lumot almashish uchun eng qulay?", "options": ["UART (Serial / USB) yoki I2C", "Bluetooth 5.4", "Faqat optik tolali shina", "Faqat audio kabel"], "correct": 0, "exp": "Ular odatda USB orqali Serial (UART) yoki mantiqiy daraja moslagich orqali I2C da bog'lanadi."},
        {"q": "23. Raspberry Pi to'satdan elektrdan uzib qo'yilsa qanday xavf yuzaga keladi?", "options": ["Hech narsa bo'lmaydi", "MicroSD kartadagi fayl tizimi buzilishi (data corruption) mumkin", "Protsessor darhol yonib ketadi", "Xotirasi butunlay o'chib ketadi"], "correct": 1, "exp": "Linux doimiy ravishda diskka yozuvlarni amalga oshirgani sababli to'satdan uzilish fayllarni shikastlaydi."},
        {"q": "24. Arduino'da 'Bootloader' nima vazifani bajaradi?", "options": ["Murakkab o'yinlarni boshqaradi", "Dastur kodini USB orqali Flash xotiraga yozishni ta'minlaydi", "Kuchlanishni 220V ga ko'taradi", "Wi-Fi signallarini tutadi"], "correct": 1, "exp": "Bootloader yangi dasturni tashqi dasturlagichsiz to'g'ridan-to'g'ri yuklashga imkon beruvchi dasturdir."},
        {"q": "25. Sanoat IoT tizimlarida nima sababdan Arduino va Raspberry Pi birgalikda ishlatiladi?", "options": ["Narxini oshirish uchun", "Arduino real vaqtli sensorlarni xavfsiz o'qiydi, Raspberry Pi esa tahlil qilib bulutga uzatadi", "Biri ishlamasa ikkinchisi o'z-o'zidan yonadi", "Faqat tashqi ko'rinish uchun"], "correct": 1, "exp": "Gibrid arxitekturada mikrokontrollerning real-vaqt kuchi va mini kompyuterning hisoblash quvvati birlashtiriladi."}
    ]

    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    correct_count = 0
    answered_count = len(st.session_state.user_answers)

    # Savollarni chiqarish
    for idx, item in enumerate(quiz_data):
        st.markdown(f'<div class="content-box">', unsafe_allow_html=True)
        st.markdown(f"### {item['q']}")
        
        choice = st.radio(
            "Javob variantini tanlang:",
            item["options"],
            key=f"q_{idx}",
            index=None
        )

        if choice is not None:
            chosen_idx = item["options"].index(choice)
            st.session_state.user_answers[idx] = chosen_idx

            if chosen_idx == item["correct"]:
                st.success(f"✅ To'g'ri javob! {item['exp']}")
                correct_count += 1
            else:
                st.error(f"❌ Noto'g'ri! To'g'ri javob: {item['options'][item['correct']]}")
                st.info(f"💡 Izoh: {item['exp']}")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Natijalar ko'rsatkichi
    st.divider()
    res_col1, res_col2, res_col3 = st.columns(3)
    res_col1.metric("Jami Savollar", 25)
    res_col2.metric("Javob Berilgan", answered_count)
    res_col3.metric("To'g'ri Javoblar", correct_count)

    if st.button("🔄 Testni Qayta Boshlash"):
        st.session_state.user_answers = {}
        st.rerun()

# Pastki qism (Footer)
st.divider()
st.markdown("""
<div style='text-align: center; color: #000000 !important; font-size: 0.95rem; font-weight: 700;'>
    © 2026 Embedded Systems Portali | O'quv metodik majmua muallifi: <span style="color: #059669;">Quljanova Shukurjon Zaribovna</span>
</div>
""", unsafe_allow_html=True)
