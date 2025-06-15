import wx
import numpy as np
import time
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class RealTimePlot(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Özelleştirilebilir Gerçek Zamanlı Grafik", size=(900, 600))

        self.panel = wx.Panel(self)

        # Matplotlib setup
        self.figure = Figure()
        self.canvas = FigureCanvas(self.panel, -1, self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Gerçek Zamanlı Sinüs Dalga Grafiği")
        self.ax.set_xlabel("Zaman (s)")
        self.ax.set_ylabel("Genlik")

        self.x_data = []
        self.y_data = []

        self.line, = self.ax.plot([], [], lw=2, color='blue')

        # Zamanlayıcı
        self.timer = wx.Timer(self)
        self.timer.Start(50)
        self.Bind(wx.EVT_TIMER, self.update_plot, self.timer)

        self.start_time = time.time()

        # Kontrol paneli (yan panel)
        control_panel = wx.Panel(self.panel)
        control_sizer = wx.BoxSizer(wx.VERTICAL)

        # Frekans girişi
        control_sizer.Add(wx.StaticText(control_panel, label="Frekans (Hz):"), flag=wx.TOP | wx.LEFT, border=10)
        self.freq_text = wx.TextCtrl(control_panel, value="1.0")
        control_sizer.Add(self.freq_text, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Genlik girişi
        control_sizer.Add(wx.StaticText(control_panel, label="Genlik:"), flag=wx.TOP | wx.LEFT, border=10)
        self.amp_text = wx.TextCtrl(control_panel, value="1.0")
        control_sizer.Add(self.amp_text, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Çizgi kalınlığı slider
        control_sizer.Add(wx.StaticText(control_panel, label="Çizgi Kalınlığı:"), flag=wx.TOP | wx.LEFT, border=10)
        self.width_slider = wx.Slider(control_panel, value=2, minValue=1, maxValue=10)
        control_sizer.Add(self.width_slider, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Renk seçimi
        control_sizer.Add(wx.StaticText(control_panel, label="Çizgi Rengi:"), flag=wx.TOP | wx.LEFT, border=10)
        self.color_choice = wx.Choice(control_panel, choices=['blue', 'red', 'green', 'orange', 'purple'])
        self.color_choice.SetSelection(0)
        control_sizer.Add(self.color_choice, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Duraklat / devam ettir butonu
        self.pause_button = wx.Button(control_panel, label="Duraklat")
        control_sizer.Add(self.pause_button, flag=wx.ALL | wx.EXPAND, border=10)

        control_panel.SetSizer(control_sizer)

        # Ana layout
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.canvas, proportion=3, flag=wx.EXPAND | wx.ALL, border=5)
        main_sizer.Add(control_panel, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(main_sizer)

        # Buton olay bağlama
        self.pause_button.Bind(wx.EVT_BUTTON, self.on_pause)

        self.paused = False

        self.Show()

    def update_plot(self, event):
        if self.paused:
            return

        try:
            freq = float(self.freq_text.GetValue())
            amp = float(self.amp_text.GetValue())
        except ValueError:
            freq = 1.0
            amp = 1.0

        width = self.width_slider.GetValue()
        color = self.color_choice.GetStringSelection()

        now = time.time() - self.start_time
        value = amp * np.sin(2 * np.pi * freq * now)

        self.x_data.append(now)
        self.y_data.append(value)

        self.x_data = self.x_data[-200:]
        self.y_data = self.y_data[-200:]

        self.line.set_data(self.x_data, self.y_data)
        self.line.set_linewidth(width)
        self.line.set_color(color)

        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def on_pause(self, event):
        self.paused = not self.paused
        self.pause_button.SetLabel("Devam Ettir" if self.paused else "Duraklat")


if __name__ == "__main__":
    app = wx.App(False)
    frame = RealTimePlot()
    app.MainLoop()
