import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()

# Добавляем узлы
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Добавляем связи между узлами
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "A")

# Рисуем граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=500, font_size=16, font_weight='bold')

# Добавляем метки к ребрам
edge_labels = {("A", "B"): "1", ("B", "C"): "2",
               ("C", "D"): "3", ("D", "A"): "4"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Показываем график
plt.axis('off')
plt.tight_layout()
plt.show()