import sys
from func_class import OlympicDataProcessor

def parse_arguments(args):
    if len(args) < 4:
        raise ValueError("Недостатньо аргументів. Мінімальна кількість: 4 (файл, команда, країна/рік).")
    
    file_path = args[1]
    command = args[2]
    
    if command == "-medals":
        if len(args) < 5:
            raise ValueError("Для -medals необхідно вказати країну та рік.")
        country = args[3]
        year = args[4]
        output_file = args[6] if len(args) > 6 and args[5] == "-output" else None
        return file_path, command, country, year, output_file
    
    elif command == "-total":
        if len(args) < 4:
            raise ValueError("Для команди -total необхідно вказати рік.")
        year = args[3]
        return file_path, command, None, year, None

    else:
        raise ValueError(f"Невідома команда: {command}")

def save_to_file(output_file, content):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    try:
        args = sys.argv
        file_path, command, country, year, output_file = parse_arguments(args)
        processor = OlympicDataProcessor(file_path)
        
        if command == "-medals":
            medalists, summary = processor.medals_per_country(country, year)
            result = "Медалісти:\n"
            result += "\n".join([f"{row['Name']} - {row['Event']} - {row['Medal']}" for row in medalists])
            result += "\n\nСумарна кількість медалей:\n"
            result += f"Gold: {summary['Gold']}, Silver: {summary['Silver']}, Bronze: {summary['Bronze']}\n"
            print(result)
            if output_file:
                save_to_file(output_file, result)

        elif command == "-total":
            summary = processor.total_medals_by_year(year)
            result = "Результати за країнами:\n"
            result += "\n".join([f"{team} - Gold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}" for team, medals in summary.items()])
            print(result)
        
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
