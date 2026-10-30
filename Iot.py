import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Arduino vs Raspberry Pi | O'quv Portali",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Och ko'k asosiy fon va CHAP TARAFDAGI OCH YASHIL MENYU uchun CSS
st.markdown("""
<style>
    /* Butun sahifaning och ko'k foni */
    .stApp {
        background-color: #f0f7ff;
        background-image: 
            radial-gradient(at 0% 0%, rgba(186, 230, 253, 0.45) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(191, 219, 254, 0.45) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(224, 242, 254, 0.5) 0px, transparent 60%);
        background-attachment: fixed;
    }
    
    /* CHAP TARAFDAGI MENYU (SIDEBAR) OCH YASHIL FON */
    section[data-testid="stSidebar"] {
        background-color: #ecfdf5 !important;
        background-image: linear-gradient(180deg, #d1fae5 0%, #ecfdf5 100%) !important;
        border-right: 2px solid #a7f3d0 !important;
    }

    /* Chap tarafdagi menyu matnlari va sarlavhalari to'liq qora */
    section[data-testid="stSidebar"] * {
        color: #064e3b !important;
        font-weight: 600 !important;
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #047857 !important;
        font-weight: 800 !important;
    }
    
    /* Barcha asosiy matnlar to'liq qora va kontrastli */
    html, body, p, span, label, li {
        color: #0f172a !important;
        font-weight: 500 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-weight: 800 !important;
    }

    /* Test variantlari shrifti va rangi */
    div[role="radiogroup"] label p {
        color: #000000 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
    }

    /* Oq shaffof kartalar */
    .content-box {
        background-color: rgba(255, 255, 255, 0.96);
        border: 1px solid #bfdbfe;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(30, 58, 138, 0.05);
    }
    
    .author-badge {
        background: #ffffff;
        border: 2px solid #0284c7;
        padding: 10px 24px;
        border-radius: 9999px;
        display: inline-block;
        font-weight: 700;
        color: #000000 !important;
        box-shadow: 0 4px 10px rgba(2, 132, 199, 0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Muallif nishoni
st.markdown("""
<div style="text-align: center;">
    <div class="author-badge">
        👨‍🏫 Tuzuvchi: <span style="color: #0284c7; font-weight: 800;">Quljanova Shukurjon Zaribovna</span>
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

# Chap tarafdagi navigatsiya menyusi (Och yashil panel)
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
# 1-BO'LIM: NAZARIYA VA RASMLAR
# -----------------------------------------------------------------------------
if menu == "1. Nazariy Tushunchalar & Rasmlar":
    st.header("1. Fundamental Nazariy Tushunchalar va Uskunalar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("🔹 Arduino Uno (Mikrokontroller)")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/38/Arduino_Uno_-_R3.jpg", 
                 caption="Arduino Uno R3 mikrokontroller platasi", use_container_width=True)
        
        st.markdown("""
        * **Toifasi:** MCU (Microcontroller Unit) — Bare-Metal real-vaqt tizimi.
        * **Chip:** ATmega328P (8-bitli AVR RISC Garvard arxitekturasi).
        * **Xotira tuzilishi:** 32 KB Flash xotira (kod uchun), 2 KB SRAM (operativ) va 1 KB EEPROM.
        * **Vazifasi:** Datchiklar, motorlar va signallarni mikrosekund aniqlikda, kechikishsiz (deterministic) boshqarish.
        * **Energiya sarfi:** Atigi 40-50 mA; quvvat tejash rejimida mikroamper sarflaydi.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("🔸 Raspberry Pi 4 (Mini Kompyuter)")
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg", 
                 caption="Raspberry Pi 4 Model B mini kompyuteri", use_container_width=True)
        
        st.markdown("""
        * **Toifasi:** SBC (Single Board Computer) — to'laqonli ko'p vazifali kompyuter.
        * **Chip:** Broadcom BCM2711, 4 yadroli ARM Cortex-A72 (64-bit Fon-Neyman arxitekturasi).
        * **Xotira:** 2GB, 4GB yoki 8GB LPDDR4 operativ xotira, MicroSD kartada Linux OS (Raspberry Pi OS).
        * **Vazifasi:** Video oqimlarni tahlil qilish (OpenCV), sun'iy intellekt, veb-server va IoT shlyuzi.
        * **Energiya sarfi:** 600 mA dan 3000 mA gacha (5V / 3A Type-C manba talab qiladi).
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Garvard (Arduino) va Fon-Neyman (Raspberry Pi) Arxitekturalari")
    st.write("Arduino mikrokontrollerida dastur xotirasi (Flash) va ma'lumot xotirasi (RAM) bir-biridan alohida shinalarga ega (Garvard). Raspberry Pi kompyuterida esa dastur va ma'lumotlar bitta umumiy operativ xotirada joylashadi (Fon-Neyman).")
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
        pass
    time.sleep(2.0)""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4-BO'LIM: 25 TA TEST TIZIMI
# -----------------------------------------------------------------------------
elif menu == "4. 25 Savolli Imtihon Testi":
    st.header("4. 25 Savolli Imtihon Testi")
    st.markdown("""
        <div style="background-color: #ffffff; padding: 12px 20px; border-radius: 10px; border-left: 6px solid #0284c7; box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-bottom: 25px;">
            <strong style="color: #000; font-size: 1.05rem;">Test tuzuvchisi:</strong> <span style="color: #0284c7; font-weight: 800; font-size: 1.05rem;">Quljanova Shukurjon Zaribovna</span>
        </div>
    """, unsafe_allow_html=True)

    quiz_data = [
        {
            "q": "1. Garvard arxitekturasi Fon-Neyman arxitekturasidan nima bilan tubdan farq qiladi?",
            "options": [
                "A) Garvardda ma'lumotlar va dastur ko'rsatmalari uchun alohida xotira shinalari ishlatiladi",
                "B) Fon-Neymanda operativ xotira (RAM) bo'lmaydi",
                "C) Garvard faqat simsiz tarmoqda ishlaydi",
                "D) Ular o'rtasida apparat darajasida hech qanday farq yo'q"
            ],
            "correct": 0,
            "exp": "Garvard arxitekturasida dastur xotirasi (Flash) va ma'lumot xotirasi (SRAM) jismonan alohida shinalarga ega bo'ladi."
        },
        {
            "q": "2. Arduino Uno qaysi toifadagi hisoblash qurilmasi hisoblanadi?",
            "options": [
                "A) To'liq bir platalik kompyuter (SBC)",
                "B) Mikrokontroller platasi (MCU)",
                "C) Alohida grafik tezlatkich (GPU)",
                "D) Qattiq disk nazoratchisi"
            ],
            "correct": 1,
            "exp": "Arduino Uno — ATmega328P mikrokontrolleriga asoslangan bitta chipli boshqaruv platasidir."
        },
        {
            "q": "3. Arduino Uno GPIO pinlarining mantiqiy ishchi kuchlanishi qanchaga teng?",
            "options": [
                "A) 1.8V mantiqiy daraja",
                "B) 3.3V mantiqiy daraja",
                "C) 5.0V mantiqiy daraja",
                "D) 12.0V sanoat standarti"
            ],
            "correct": 2,
            "exp": "Arduino Uno platasi standart holda 5V mantiqiy sathda (TTL) ishlaydi."
        },
        {
            "q": "4. Raspberry Pi 4 mini kompyuteri qaysi quvvat manbai orqali barqaror ishlaydi?",
            "options": [
                "A) 3.3V, 100mA quvvat manbai",
                "B) 12V, 5A quvvat bloki",
                "C) Oddiy 1.5V soat batareyasi",
                "D) 5V, kamida 3A (15W) USB Type-C manbai"
            ],
            "correct": 3,
            "exp": "Raspberry Pi 4 to'liq yuklamada barqaror ishlashi uchun 5V / 3A USB-C quvvat manbai talab etiladi."
        },
        {
            "q": "5. 'Deterministik real-vaqt ijrosi' (Deterministic Real-time) xususiyati qaysi qurilmaga xos?",
            "options": [
                "A) Arduino mikrokontrolleriga",
                "B) Raspberry Pi (Linux OS) ga",
                "C) Har ikkala qurilmaga birdek",
                "D) Hech biriga xos emas"
            ],
            "correct": 0,
            "exp": "Arduino operatsion tizimsiz (bare-metal) ishlagani sababli buyruqlarni mikrosekund darajasidagi aniqlik bilan bajaradi."
        },
        {
            "q": "6. Raspberry Pi GPIO portiga to'g'ridan-to'g'ri 5V kuchlanish berilsa nima sodir bo'ladi?",
            "options": [
                "A) Tizim kuchlanishni avtomatik ravishda 3.3V ga pasaytiradi",
                "B) GPIO pini va SoC protsessori ishdan chiqadi (kuyadi)",
                "C) Hech narsa bo'lmaydi, chunki u 5V ga to'liq chidamli",
                "D) Faqat operatsion tizim qayta yuklanadi"
            ],
            "correct": 1,
            "exp": "Raspberry Pi GPIO pinlari faqat 3.3V ga mo'ljallangan. 5V berilsa ichki yarimo'tkazgichlar kuyadi."
        },
        {
            "q": "7. Raspberry Pi 4 qurilmasining markaziy protsessor arxitekturasi qanday?",
            "options": [
                "A) 8-bitli Garvard AVR",
                "B) 16-bitli PIC arxitekturasi",
                "C) 64-bitli ko'p yadroli ARM Cortex-A72",
                "D) 32-bitli x86 Intel arxitekturasi"
            ],
            "correct": 2,
            "exp": "Raspberry Pi 4 to'rt yadroli 64-bitli ARM Cortex-A72 arxitekturasidagi protsessorga ega."
        },
        {
            "q": "8. Arduino Uno'da yozilgan dastur kodi chipning qaysi qismida doimiy saqlanadi?",
            "options": [
                "A) Tashqi MicroSD fleshkada",
                "B) Dinamik RAM xotirasida",
                "C) Qattiq magnit diskda",
                "D) 32 KB li ichki Flash EEPROM xotirasida"
            ],
            "correct": 3,
            "exp": "Arduino kodi elektr o'chganda ham o'chib ketmaydigan 32 KB Flash xotirada saqlanadi."
        },
        {
            "q": "9. Arduino va Raspberry Pi o'rtasida ketma-ket (Serial) aloqa qaysi interfeys orqali eng oson ulanadi?",
            "options": [
                "A) UART (USB kabel orqali Serial port)",
                "B) Faqat optik tolali magistral",
                "C) Bluetooth 5.4 orqali simsiz",
                "D) Faqat audio AUX ulagichi"
            ],
            "correct": 0,
            "exp": "Ular USB kabel orqali UART (Serial) aloqa yordamida juda oson va ishonchli bog'lanadi."
        },
        {
            "q": "10. Arduino Uno platasida nechta apparat analog kirish (ADC) kanali mavjud?",
            "options": [
                "A) 2 ta kanal",
                "B) 6 ta kanal (A0 dan A5 gacha)",
                "C) 14 ta raqamli kanal",
                "D) Analog kanal mavjud emas"
            ],
            "correct": 1,
            "exp": "Arduino Uno platasida A0 dan A5 gacha belgilangan 6 ta 10-bitli ADC kanali mavjud."
        },
        {
            "q": "11. Raspberry Pi 4 platasining tezkor xotirasi (RAM) hajmi qanday bo'lishi mumkin?",
            "options": [
                "A) 2 KB SRAM",
                "B) 32 KB kesh",
                "C) 2 GB, 4 GB yoki 8 GB LPDDR4",
                "D) 128 MB SDRAM"
            ],
            "correct": 2,
            "exp": "Raspberry Pi 4 xaridor ehtiyojiga qarab 2GB, 4GB yoki 8GB operativ xotira bilan ishlab chiqariladi."
        },
        {
            "q": "12. Raspberry Pi to'satdan elektr tarmog'idan uzib qo'yilsa qanday xavf yuzaga keladi?",
            "options": [
                "A) Hech qanday xavf yuzaga kelmaydi",
                "B) Platadagi kvars rezonatori sinadi",
                "C) Butun plata darhol portlab ketadi",
                "D) MicroSD kartadagi operatsion tizim fayllari buziladi (corruption)"
            ],
            "correct": 3,
            "exp": "Linux doimiy yozuv amallarini bajargani sababli to'satdan uzilish MicroSD tizim fayllarini ishdan chiqarishi mumkin."
        },
        {
            "q": "13. Arduino Uno platasining markaziy takt chastotasi qanchaga teng?",
            "options": [
                "A) 16 MHz",
                "B) 1.5 GHz",
                "C) 100 MHz",
                "D) 500 kHz"
            ],
            "correct": 0,
            "exp": "Arduino Uno 16 megagersli (16 MHz) kvars rezonatori orqali taktlanadi."
        },
        {
            "q": "14. Raspberry Pi 4 platasida ichki analog kirishlar (ADC) bormi?",
            "options": [
                "A) Ha, 8 ta ichki ADC kanali mavjud",
                "B) Yo'q, analog signallarni o'qish uchun tashqi ADC chipi kerak",
                "C) Ha, barcha 40 ta pin analog ishlay oladi",
                "D) Ha, faqat GPIO 2 va GPIO 3 analog ishlaydi"
            ],
            "correct": 1,
            "exp": "Raspberry Pi platasida ichki ADC yo'q. Analog sensorlar uchun MCP3008 yoki ADS1115 kabi chiplar ulanadi."
        },
        {
            "q": "15. Arduino Uno'dagi analogRead() funksiyasi qanday sonlar oralig'ida natija qaytaradi?",
            "options": [
                "A) Faqat 0 yoki 1 (HIGH/LOW)",
                "B) 0 dan 255 gacha (8-bit)",
                "C) 0 dan 1023 gacha (10-bitli ADC)",
                "D) 0 dan 65535 gacha (16-bit)"
            ],
            "correct": 2,
            "exp": "Arduino Uno ADC moduli 10-bitli bo'lib, 0V dan 5V gacha kuchlanishni 0 dan 1023 gacha bo'lgan sonlarga aylantiradi."
        },
        {
            "q": "16. Kompyuter ko'rishi (OpenCV) va yuzni tanish tizimlarini qurishda qaysi qurilma to'g'ri tanlov?",
            "options": [
                "A) Arduino Uno",
                "B) ATmega328P alohida chipi",
                "C) PIC16F877A mikrokontrolleri",
                "D) Raspberry Pi 4 (SBC)"
            ],
            "correct": 3,
            "exp": "OpenCV, video oqimni qayta ishlash va neyron tarmoqlar yuqori protsessor quvvati va katta RAM talab qiladi."
        },
        {
            "q": "17. Arduino Uno'da nechta apparat PWM (impuls kengligi modulyatsiyasi) pini bor?",
            "options": [
                "A) 6 ta pin (3, 5, 6, 9, 10, 11)",
                "B) 2 ta pin",
                "C) 14 ta barcha raqamli pinlar",
                "D) PWM pini umuman yo'q"
            ],
            "correct": 0,
            "exp": "Arduino Uno'da yonida tilda (~) belgisi qo'yilgan 6 ta pin apparat PWM funksiyasini bajaradi."
        },
        {
            "q": "18. Nima sababdan sanoat motorlarini mikrosekundlik aniqlikda boshqarishda mikrokontroller afzal?",
            "options": [
                "A) Chunki Raspberry Pi motorlarni umuman aylantira olmaydi",
                "B) Linux operatsion tizimidagi ko'p vazifalilik sababli vaqt kechikishi (jitter) bo'ladi",
                "C) Chunki mikrokontrollerda quvvat juda yuqori bo'ladi",
                "D) Chunki Arduino faqat 220 voltda ishlaydi"
            ],
            "correct": 1,
            "exp": "Linux OS o'z jarayonlarini vaqt bo'yicha almashtirib turadi, bu esa millisekundlik noaniqliklarni keltirib chiqaradi."
        },
        {
            "q": "19. Arduino IDE dasturida kod yozish qaysi dasturlash tili sintaksisiga asoslangan?",
            "options": [
                "A) Python",
                "B) Pure Java",
                "C) C / C++",
                "D) HTML / CSS"
            ],
            "correct": 2,
            "exp": "Arduino dasturlash tili C/C++ tillari bazasida soddalashtirilgan kutubxonalar bilan yaratilgan."
        },
        {
            "q": "20. Sanoat IoT tizimlarida mikrokontroller va mini kompyuterning gibrid qo'llanilishi qanday bo'ladi?",
            "options": [
                "A) Biri ishlamay qolsa ikkinchisi zaxira bo'lib turishi uchun",
                "B) Tizimning umumiy tannarxini sun'iy oshirish uchun",
                "C) Faqat elektr tokini tejash maqsadida",
                "D) Arduino sensorlarni qat'iy vaqtda o'qiydi, Raspberry Pi esa bulutga tahliliy uzatadi"
            ],
            "correct": 3,
            "exp": "Gibrid arxitekturada mikrokontrollerning deterministik xususiyati va mini kompyuterning hisoblash quvvati birlashadi."
        },
        {
            "q": "21. Raspberry Pi 4'da bir vaqtning o'zida nechta mustaqil displey ulash mumkin?",
            "options": [
                "A) 2 ta 4K displey (ikkita micro-HDMI porti orqali)",
                "B) Faqat 1 ta oddiy monitor",
                "C) Displey umuman ulab bo'lmaydi",
                "D) 6 ta HDMI monitor"
            ],
            "correct": 0,
            "exp": "Raspberry Pi 4 ikkita micro-HDMI porti orqali 4K formatdagi ikkita monitorni mustaqil boshqara oladi."
        },
        {
            "q": "22. Raspberry Pi platasidagi 40 pinli ulagich rasman qanday ataladi?",
            "options": [
                "A) SATA Controller",
                "B) 40-pin GPIO Header",
                "C) PCI Express slot",
                "D) USB Header"
            ],
            "correct": 1,
            "exp": "Raspberry Pi platasining barcha tashqi ulanish pinlari guruhi 40-pin GPIO Header deb ataladi."
        },
        {
            "q": "23. Arduino mikrokontrolleridagi 'Bootloader' dasturining asosiy vazifasi nima?",
            "options": [
                "A) Murakkab 3D o'yinlarni boshqarish",
                "B) Operatsion tizimni internetdan tortib o'rnatish",
                "C) Yangi dastur kodini USB kabel orqali Flash xotiraga yozishni ta'minlash",
                "D) Kuchlanishni 5V dan 220V ga ko'tarish"
            ],
            "correct": 2,
            "exp": "Bootloader tashqi dasturlagichsiz yangi dasturni USB orqali mikrokontroller xotirasiga yozish imkonini beradi."
        },
        {
            "q": "24. Batareyada (masalan, kichik akkumulyatorda) uzoq muddat (oylab) avtonom ishlash uchun qaysi biri mos?",
            "options": [
                "A) Raspberry Pi 4",
                "B) Shaxsiy noutbuk",
                "C) Uy serveri",
                "D) Arduino Uno (quvvat tejash / Sleep rejimida)"
            ],
            "correct": 3,
            "exp": "Arduino uyqu rejimida atigi bir necha mikroamper tok sarflab, kichik batareyada bir necha oy ishlay oladi."
        },
        {
            "q": "25. Raspberry Pi o'z operatsion tizimini qayerdan yuklaydi?",
            "options": [
                "A) MicroSD kartadan yoki USB orqali ulangan SSD diskdan",
                "B) Ichki 32 KB Flash xotiradan",
                "C) Faqat internet bulutidan",
                "D) Protsessor ichidagi keshdan"
            ],
            "correct": 0,
            "exp": "Raspberry Pi bootloader orqali o'z tizimini MicroSD yoki USB orqali ulangan SSD diskdan yuklaydi."
        }
    ]

    # Javoblar holatini saqlash
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    correct_count = 0
    answered_count = len(st.session_state.user_answers)

    # Savollarni birma-bir chiqarish
    for idx, item in enumerate(quiz_data):
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
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
                st.info(f"💡 Tushuntirish: {item['exp']}")
        
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
    © 2026 Embedded Systems Portali | O'quv metodik majmua muallifi: <span style="color: #0284c7;">Quljanova Shukurjon Zaribovna</span>
</div>
""", unsafe_allow_html=True)
