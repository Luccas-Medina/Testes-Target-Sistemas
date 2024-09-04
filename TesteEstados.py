def calc_percentual(fat):
    total = sum(fat.values())
    return {k: (v / total) * 100 for k, v in fat.items()}

def main():
    fat = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    perc = calc_percentual(fat)
    
    print("Percentuais por estado:")
    for estado, pct in perc.items():
        print(f"{estado}: {pct:.2f}%")

if __name__ == "__main__":
    main()
