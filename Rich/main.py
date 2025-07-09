from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.style import Style
import time

# Инициализация консоли
console = Console()

# 1. Простой вывод с форматированием
print("[bold red]Привет, мир![/bold red] :smiley:")
print("[italic blue]Это демонстрация[/italic blue] библиотеки [green]Rich[/green]")

# 2. Панели
print(Panel.fit("Это панель с закругленными углами", title="[b]Панель[/b]", subtitle="пример"))

# 3. Таблица
table = Table(title="Пример таблицы")
table.add_column("ID", style="cyan")
table.add_column("Название", style="magenta")
table.add_column("Статус", justify="right", style="green")

table.add_row("1", "Задача 1", "✅ Выполнено")
table.add_row("2", "Задача 2", "⏳ В процессе")
table.add_row("3", "Очень важная задача", "❌ Не начато")

console.print(table)

# 4. Прогресс-бар
with Progress() as progress:
    task1 = progress.add_task("[red]Загрузка...", total=100)
    task2 = progress.add_task("[green]Обработка...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        time.sleep(0.02)

# 5. Дерево
tree = Tree("Корневая папка", style="bold blue")
scripts = tree.add("Скрипты", style="bold green")
scripts.add("script1.py")
scripts.add("script2.py")
data = tree.add("Данные", style="bold red")
data.add("dataset1.csv")
data.add("dataset2.json")

console.print(tree)

# 6. Markdown
markdown_example = """
# Заголовок 1
## Заголовок 2

- Пункт 1
- Пункт 2
- Пункт 3

```python
print("Hello, World!")
"""
console.print(Markdown(markdown_example))


# 7. Синтаксис подсветка
code = """
def fibonacci(n):
if n <= 1:
return n
else:
return fibonacci(n-1) + fibonacci(n-2)
"""
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)


# 8. Стили
warning_style = Style(color="yellow", blink=True, bold=True)
console.print("Внимание! Это важное сообщение!", style=warning_style)