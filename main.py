ofrom kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# تحديد ألوان النيون المستقبلية
CLR_BG = get_color_from_hex("#010409") # أسود غامق للخلفية
CLR_NEON_CYAN = get_color_from_hex("#00FFFF") # أزرق نيون للحدود والعناوين
CLR_NEON_GREEN = get_color_from_hex("#0FFF50") # أخضر نيون للطوطال
CLR_GLASS = [0, 1, 1, 0.1] # لون زجاجي شفاف

class FuturisticInput(TextInput):
    """خانة إدخال بتصميم مستقبلي"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0,0,0,0] # إخفاء الخلفية الأصلية
        self.cursor_color = CLR_NEON_CYAN
        self.foreground_color = [1,1,1,1] # لون الكتابة أبيض
        self.input_filter = 'int'
        self.multiline = False
        self.padding = [10, 10]
        self.font_size = 18
        
        with self.canvas.before:
            Color(1, 1, 1, 0.05) # طبقة زجاجية خفيفة
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[5,])
            Color(0, 1, 1, 0.5) # حدود نيون زرقاء
            self.line = Line(rounded_rectangle=[self.x, self.y, self.width, self.height, 5], width=1)
            
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.line.rounded_rectangle = [self.x, self.y, self.width, self.height, 5]

class CafeDawdiApp(App):
    def build(self):
        # تغيير لون خلفية النافذة الأساسي
        Window.clearcolor = CLR_BG
        self.title = "Cafe Dawdi - Hologram Edition"
        
        self.prices = [7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.inputs = {}

        # الواجهة الرئيسية
        root = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # --- الهيدر الاحترافي ---
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        with header.canvas.before:
            Color(*CLR_GLASS) # خلفية زجاجية
            RoundedRectangle(pos=header.pos, size=header.size, radius=[0,0,15,15])
            Color(*CLR_NEON_CYAN) # خط سفلي نيون
            Line(points=[header.x, header.y, header.x + header.width, header.y], width=1.5)

        title_lbl = Label(text="CAFE DAWDI", font_size=35, bold=True, color=CLR_NEON_CYAN, font_name="Roboto")
        sub_title = Label(text="FUTURISTIC ACCOUNTING SYSTEM v1.0", font_size=12, color=[0.5, 0.5, 0.5, 1])
        header.add_widget(title_lbl)
        header.add_widget(sub_title)
        root.add_widget(header)

        # --- منطقة القائمة (Scroll) ---
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for price in self.prices:
            # كارت لكل ثمن
            item_box = BoxLayout(size_hint_y=None, height=70, padding=10, spacing=15)
            with item_box.canvas.before:
                Color(1, 1, 1, 0.03) # خلفية كارت شفافة
                RoundedRectangle(pos=item_box.pos, size=item_box.size, radius=[10,])

            # أيقونة دجيتال خيالية
            icon_lbl = Label(text="[color=00FFFF]🖩[/color]", markup=True, font_size=24, size_hint_x=None, width=40)
            item_box.add_widget(icon_lbl)

            lbl = Label(text=f"كأس {price} DH", font_size=18, halign='left', text_size=(None, None))
            lbl.bind(size=lambda s, w: s.setter('text_size')(s, (w[0], None))) # محاذاة اليسار
            item_box.add_widget(lbl)

            txt = FuturisticInput(hint_text="0", size_hint_x=None, width=120)
            item_box.add_widget(txt)
            
            self.inputs[price] = txt # تخزين الخانات
            grid.add_widget(item_box)

        scroll.add_widget(grid)
        root.add_widget(scroll)

        # --- منطقة النتائج (Holographic Total) ---
        result_box = BoxLayout(size_hint_y=None, height=80, padding=10)
        with result_box.canvas.before:
            Color(*CLR_NEON_GREEN[:3], 0.1) # توهج خلفي خفيف
            RoundedRectangle(pos=result_box.pos, size=result_box.size, radius=[15,])
            Color(*CLR_NEON_GREEN) # حدود مضيئة
            Line(rounded_rectangle=[result_box.x, result_box.y, result_box.width, result_box.height, 15], width=1.2)

        self.result_label = Label(text="TOTAL: 0 DH / 0 CUPS", font_size=22, bold=True, color=CLR_NEON_GREEN)
        result_box.add_widget(self.result_label)
        root.add_widget(result_box)

        # --- زر الحساب (The Execute Button) ---
        btn = Button(text="EXECUTE ACCOUNTING PROCESS", size_hint_y=None, height=60, font_size=16, bold=True)
        btn.background_color = [0,0,0,0] # إخفاء الخلفية
        with btn.canvas.before:
            Color(*CLR_NEON_CYAN[:3], 0.2) # توهج أزرق
            self.btn_rect = RoundedRectangle(pos=btn.pos, size=btn.size, radius=[10,])
            Color(*CLR_NEON_CYAN) # حدود نيون
            self.btn_line = Line(rounded_rectangle=[btn.x, btn.y, btn.width, btn.height, 10], width=1.5)
        btn.bind(pos=self.update_btn_ui, size=self.update_btn_ui)
        btn.bind(on_press=self.calculate_total)
        root.add_widget(btn)

        return root

    def update_btn_ui(self, instance, *args):
        self.btn_rect.pos = instance.pos
        self.btn_rect.size = instance.size
        self.btn_line.rounded_rectangle = [instance.x, instance.y, instance.width, instance.height, 10]

    def calculate_total(self, instance):
        total_money = 0
        total_cups = 0
        for price, input_field in self.inputs.items():
            if input_field.text:
                try:
                    num = int(input_field.text)
                    total_cups += num
                    total_money += num * price
                except ValueError:
                    pass
        
        # تحديث النتيجة بتأثير بصري (اختياري، هنا غيرنا النص فقط)
        self.result_label.text = f"TOTAL: {total_money} DH / {total_cups} CUPS"

if __name__ == '__main__':
    # لتجربة التطبيق في الحاسوب بنفس أبعاد التلفون (اختياري)
    # from kivy.config import Config
    # Config.set('graphics', 'width', '360')
    # Config.set('graphics', 'height', '640')
    CafeDawdiApp().run()

