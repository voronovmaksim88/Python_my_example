import win32com.client

# Создаем новое приложение Visio
visio = win32com.client.Dispatch("Visio.Application")
visio.Visible = True  # Делаем Visio видимым для пользователя

# Добавляем новый документ
doc = visio.Documents.Add("")

# Добавляем новую страницу
page = doc.Pages.Add()

# Нарисуем круг с помощью метода DrawOval
# Метод принимает координаты противоположных углов ограничивающего прямоугольника.
# Например, левый нижний угол (x1, y1) и правый верхний угол (x2, y2).
circle = page.DrawOval(2.0, 2.0, 6.0, 6.0)

# Сохраняем и закрываем документ, если это необходимо
doc.SaveAs(r"D:\YandexDisk\MyProg\MyGit\Python_my_example\YourVisioFile.vsd")
doc.Close()

# Закрываем приложение Visio
visio.Quit()
