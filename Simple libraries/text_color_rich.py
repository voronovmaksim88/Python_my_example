from rich import print as rprint
from rich.console import Console
from rich.table import Table
console = Console()

nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(bool_list)


console.print("Hello, [bold magenta]World[/bold magenta]!")
console.print("Hello, [magenta]World[/magenta]!")
console.print("Hello, [bold white]World[/bold white]!")


table = Table(title="Sample Table")

table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Age", style="magenta")
table.add_column("City", justify="right", style="green")

table.add_row("John Doe", "30", "New York")
table.add_row("Jane Smith", "25", "Los Angeles")
table.add_row("Alice Brown", "28", "Chicago")

console.print(table)
