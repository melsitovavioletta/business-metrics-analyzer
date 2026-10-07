import pandas as pd

def main():
    data = {
    "Месяц": ["Январь", "Февраль", "Март"],
    "Выручка": [120000, 150000, 135000],
    }
    
    df = pd.DataFrame(data)
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

def calculate_profitability(revenue: float, cost: float) -> float:
    if revenue == 0:
        return 0.0
    else: 
        return (revenue - cost) / revenue * 100

if __name__ == "__main__":
    main()
    print(calculate_profitability(30000, 10000))