Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import streamlit as st

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Arduino vs Raspberry Pi | O'quv Portali",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Yashil, ko'k, sariq va qizil uyg'unligidagi ochiq fon uchun CSS
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        background-image: 
            radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.15) 0px, transparent 50%),
            radial-gradient(at 0% 100%, rgba(239, 68, 68, 0.12) 0px, transparent 50%);
        background-attachment: fixed;
    }
    
    .author-badge {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 8px 16px;
        border-radius: 9999px;
        display: inline-block;
        font-weight: 600;
        color: #1e293b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Muallif nishoni
st.markdown("""
<div style="text-align: center;">
    <div class="author-badge">
        👨‍🏫 Tuzuvchi: <span style="color: #059669; font-weight: 700;">Quljanova Shukurjon Zaribovna</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Asosiy sarlavha
st.markdown("""
<h1 style='text-align: center; color: #0f172a; margin-bottom: 0;'>
    Arduino Mikrokontrolleri va Raspberry Pi Mini Kompyuterlari
</h1>
<p style='text-align: center; color: #475569; font-size: 1.1rem; margin-top: 8px;'>
    Funksiyalarini o'rganish, apparat parametrlarini solishtirish va bilimlarni 25 ta test orqali sinash
</p>
""", unsafe_allow_html=True)

st.divider()

# Yon panel (Sidebar) navigatsiyasi
menu = st.sidebar.radio(
    "Bo'limni tanlang:",
    ["1. Nazariya va Tushunchalar", "2. Taqqoslash Matritsasi", "3. Amaliy Laboratoriyalar", "4. 25 Savolli Test"]
)

# -----------------------------------------------------------------------------
# 1-BO'LIM: NAZARIYA
# -----------------------------------------------------------------------------
if menu == "1. Nazariya va Tushunchalar":
    st.header("1. Fundamental Nazariy Tushunchalar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔹 Arduino Uno (Mikrokontroller)")
        st.info("**Toifasi:** MCU (Microcontroller Unit) | Bare-Metal Tizim")
        st.markdown("""
        * **Ichki tuzilishi:** Bitta chipda protsessor yadrosi, tezkor xotira (SRAM), dastur xotirasi (Flash EEPROM) va periferiya bloklari jamlangan.
        * **Arxitekturasi:** 8-bitli AVR RISC Garvard arxitekturasi (Ma'lumot va ko'rsatmalar shinalari ajratilgan).
        * **Deterministik ijro:** Operatsion tizim bo'lmagani sababli buyruqlar mikrosekund darajasidagi aniqlik bilan qat'iy ketma-ketlikda bajariladi.
        * **Energiya sarfi:** O'rtacha 40–50 mA (5V), uyqu rejimida mikroamper sarflaydi.
        """)

    with col2:
        st.subheader("🔸 Raspberry Pi 4 (Mini Kompyuter)")
        st.warning("**Toifasi:** SBC (Single Board Computer) | Ko'p vazifali Tizim")
        st.markdown("""
        * **Ichki tuzilishi:** To'liq SoC protsessori, gigabaytlab RAM va to'liq Linux operatsion tizimi (Raspberry Pi OS) bilan ishlaydi.
        * **Arxitekturasi:** 64-bitli ko'p yadroli ARM Cortex-A72 Fon-Neyman arxitekturasi.
        * **Time-slicing:** Linux operatsion tizimi yadro darajasida jarayonlarni almashtirib turadi, shu sababli millisekundlik kechikishlar yuzaga kelishi mumkin.
        * **Energiya sarfi:** 600 mA dan 3000 mA gacha (5V / 3A USB-C quvvat manbai talab etiladi).
        """)

# -----------------------------------------------------------------------------
# 2-BO'LIM: TAQQOSLASH MATRITSASI
# -----------------------------------------------------------------------------
elif menu == "2. Taqqoslash Matritsasi":
    st.header("2. Qiyosiy Texnik Parametrlar Matritsasi")
    
    comparison_data = {
        "Texnik Xususiyat": [
            "Qurilma toifasi",
            "Markaziy protsessor",
            "Takt chastotasi",
            "Tezkor xotira (RAM)",
            "Doimiy xotira (Storage)",
            "GPIO Mantiqiy Kuchlanishi",
            "Analog kirishlar (ADC)",
            "Operatsion tizim",
            "Video & Grafika"
        ],
        "Arduino Uno R3": [
            "Mikrokontroller (MCU)",
            "ATmega328P (8-bit)",
            "16 MHz",
            "2 KB SRAM",
            "32 KB Flash",
            "5V mantiqiy daraja",
            "Mavjud (6 ta 10-bitli ADC kanali)",
            "Yo'q (Dastur to'g'ridan-to'g'ri ishlaydi)",
            "Mavjud emas"
        ],
        "Raspberry Pi 4 Model B": [
            "Mini Kompyuter (SBC)",
            "Broadcom BCM2711, 4-yadro ARM (64-bit)",
            "1.5 GHz – 1.8 GHz",
            "2 GB / 4 GB / 8 GB LPDDR4",
            "MicroSD karta (16GB – 256GB)",
            "3.3V (5V berilsa port yonadi!)",
            "Mavjud emas (Tashqi ADC chip kerak)",
            "Raspberry Pi OS, Ubuntu",
            "2x micro-HDMI (4K 60fps)"
        ]
    }
    
    st.table(comparison_data)
    st.warning("⚠️ **Eslatma:** Raspberry Pi GPIO portlariga to'g'ridan-to'g'ri 5V signali berilsa, platadagi SoC chipi kuyadi. Har doim mantiqiy daraja moslagich (Logic Level Shifter) ishlating!")

# -----------------------------------------------------------------------------
# 3-BO'LIM: AMALIYOT VA KODLAR
# -----------------------------------------------------------------------------
elif menu == "3. Amaliy Laboratoriyalar":
    st.header("3. Amaliy Laboratoriya Mashg'ulotlari")
    
    tab1, tab2 = st.tabs(["Arduino: Potentsiometr va PWM", "Raspberry Pi: DHT22 Sensori"])
    
    with tab1:
        st.subheader("Laboratoriya 1: Arduino PWM va Analog Kirish")
        st.write("A0 analog portidan olingan 10-bitli qiymat D9 pin orqali 8-bitli PWM ga aylantirilib, LED yorug'ligi boshqariladi.")
        
        st.code("""// Arduino C++ KODI
const int potPin = A0;
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(potPin); 
  int pwmValue = map(sensorValue, 0, 1023, 0, 255);
  analogWrite(ledPin, pwmValue);
  delay(15);
}""", language="cpp")

    with tab2:
        st.subheader("Laboratoriya 2: Raspberry Pi va DHT22 Harorat/Namlik Sensori")
        st.write("DHT22 datchigi 3.3V kuchlanish orqali GPIO4 piniga ulanadi va Python kutubxonasi yordamida o'qiladi.")
        
        st.code("""# Python 3 (Raspberry Pi OS)
import time
import board
import adafruit_dht

dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temp = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Harorat: {temp:.1f}°C | Namlik: {humidity:.1f}%")
    except RuntimeError as err:
        pass
    time.sleep(2.0)""", language="python")

# -----------------------------------------------------------------------------
# 4-BO'LIM: 25 TA TEST TIZIMI
# -----------------------------------------------------------------------------
elif menu == "4. 25 Savolli Test":
    st.header("4. 25 Savolli Imtihon Testi")
    st.caption("Muallif: Quljanova Shukurjon Zaribovna")

    # 25 ta savol bazasi
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

    # Session state
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    correct_count = 0
    answered_count = len(st.session_state.user_answers)

    # Savollarni chiqarish
    for idx, item in enumerate(quiz_data):
        st.markdown(f"**{item['q']}**")
        
...         choice = st.radio(
...             "Javob variantini tanlang:",
...             item["options"],
...             key=f"q_{idx}",
...             index=None
...         )
... 
...         if choice is not None:
...             chosen_idx = item["options"].index(choice)
...             st.session_state.user_answers[idx] = chosen_idx
... 
...             if chosen_idx == item["correct"]:
...                 st.success(f"To'g'ri javob! {item['exp']}")
...                 correct_count += 1
...             else:
...                 st.error(f"Noto'g'ri! To'g'ri javob: {item['options'][item['correct']]}")
...                 st.info(f"Izoh: {item['exp']}")
...         
...         st.write("")
... 
...     # Natija paneli
...     st.divider()
...     res_col1, res_col2, res_col3 = st.columns(3)
...     res_col1.metric("Jami Savollar", 25)
...     res_col2.metric("Yechilgan", answered_count)
...     res_col3.metric("To'g'ri Javoblar", correct_count)
... 
...     if st.button("Testni Qayta Boshlash"):
...         st.session_state.user_answers = {}
...         st.rerun()
... 
... # Sahifa pastki qismi
... st.divider()
... st.markdown("""
... <div style='text-align: center; color: #64748b; font-size: 0.85rem;'>
...     © 2026 Embedded Systems Portali | O'quv metodik majmua muallifi: <strong>Quljanova Shukurjon Zaribovna</strong>
... </div>
