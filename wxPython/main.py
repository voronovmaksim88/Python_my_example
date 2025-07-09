import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Нажми меня!", pos=(100, 50), size=(100, 50))

        # Привязываем обработчик события нажатия кнопки
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Создаём статусную строку внизу окна
        self.CreateStatusBar()
        self.SetStatusText("Готово к работе")

    def on_button_click(self, event):
        # Показываем диалоговое окно с сообщением
        wx.MessageBox("Вы нажали кнопку!", "Уведомление", wx.OK | wx.ICON_INFORMATION)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, "Пример wxPython")
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()