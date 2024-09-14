from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from bidi.algorithm import get_display  # To handle RTL text
from arabic_reshaper import reshape  # To reshape Farsi text

# Register the Farsi (Vazir) font
pdfmetrics.registerFont(TTFont('Vazir', '/Users/niotx/Developer/Web Development Projects/tmep/vazir-font-v16.1.0/Vazir.ttf'))  # Adjust the path to your font

# Create a PDF document
c = canvas.Canvas("resume.pdf", pagesize=A4)
c.setFont("Vazir", 12)

# Helper function to handle Farsi text correctly
def draw_text(text, x, y):
    reshaped_text = reshape(text)  # Reshape the Farsi text
    bidi_text = get_display(reshaped_text)  # Handle RTL with BiDi
    c.drawRightString(x, y, bidi_text)  # Draw text right-aligned

# Draw resume content
c.drawString(100, 800, "رزومه محمد متین ناصری")  # Title

draw_text("شماره تماس: ۰۹۰۲۵۸۳۱۱۲۴", 500, 780)
draw_text("ایمیل: mmnaseri4444@gmail.com", 500, 760)

c.drawString(100, 720, "خلاصه تخصصی:")
draw_text("دانشجوی کارشناسی مهندسی کامپیوتر با دوسال سابقه برنامه‌نویسی پایتون و سی‌پلاس‌پلاس،", 500, 700)
draw_text("یک سال تجربه در زمینه یادگیری ماشین، یادگیری عمیق و تحلیل داده‌ها. دارای تجربه در توسعه", 500, 680)
draw_text("سیستم‌های تعبیه‌شده و ساخت ربات‌های تلگرامی و وب‌اسکرپینگ.", 500, 660)

c.drawString(100, 620, "سوابق تحصیلی:")
draw_text("دانشگاه رازی - کارشناسی مهندسی کامپیوتر - ۱۴۰۰ تاکنون", 500, 600)
draw_text("دیپلم زبان انگلیسی - ۱۳۹۸", 500, 580)

c.drawString(100, 540, "مهارت‌ها:")
draw_text("برنامه‌نویسی: Python, C++", 500, 520)
draw_text("یادگیری ماشین و یادگیری عمیق: PyTorch, TensorFlow, Scikit-learn", 500, 500)
draw_text("تحلیل داده‌ها: Pandas, NumPy", 500, 480)
draw_text("مصورسازی داده‌ها: Matplotlib, Seaborn", 500, 460)
draw_text("توسعه سیستم‌های تعبیه‌شده: Arduino, ESP32", 500, 440)
draw_text("وب‌اسکرپینگ: BeautifulSoup, Selenium", 500, 420)
draw_text("ربات‌های تلگرامی: TeleBot", 500, 400)
draw_text("کنترل نسخه: Git", 500, 380)
draw_text("پایگاه داده: MySQL, SQLite", 500, 360)

c.drawString(100, 320, "سوابق کاری:")
draw_text("توسعه ربات‌های تلگرامی و وب‌اسکرپینگ (یک سال)", 500, 300)
draw_text("توسعه سیستم‌های تعبیه‌شده (شش ماه)", 500, 280)
draw_text("پروژه‌های یادگیری ماشین و یادگیری عمیق (یک سال)", 500, 260)

c.drawString(100, 220, "زبان‌ها:")
draw_text("فارسی: زبان مادری", 500, 200)
draw_text("انگلیسی: پیشرفته (درک مطلب و مهارت‌های نوشتاری)", 500, 180)

# Save the PDF
c.save()
