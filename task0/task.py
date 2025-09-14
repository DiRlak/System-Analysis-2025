import pandas as pd
import numpy as np


def read_csv_to_string(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.to_csv(index=False)
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"


def main(file_path):
    str = read_csv_to_string(file_path)

    cleaned_string = str.replace(',', ' ').replace('\n', ' ')
    parts = cleaned_string.split()
    if not parts:
        print('Пустое содержимое файла')
        return None
    numbers_of_edges = [int(p) for p in parts]
    print(numbers_of_edges)
    n = max(numbers_of_edges)
    adjacency_matrix = np.zeros((n, n), dtype=int)

    for k in range(0, len(numbers_of_edges), 2):
        i = numbers_of_edges[k]-1
        j = numbers_of_edges[k+1]-1
        adjacency_matrix[i, j] = 1

    print(adjacency_matrix)
    return adjacency_matrix

if __name__ == "__main__":
    main('task0.csv')