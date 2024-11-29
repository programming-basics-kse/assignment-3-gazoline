import csv

class OlympicDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_csv()

    def read_csv(self):
        with open(self.file_path, encoding="utf-8") as f:
            sample = f.read(1024)
            delimiter = '\t' if '\t' in sample else ','
            f.seek(0)
            reader = csv.DictReader(f, delimiter=delimiter)
            data = list(reader)
            if not data:
                raise ValueError("Помилка у файлі")
            return data

    def medals_per_country(self, country, year):
        filtered_data = [
            row for row in self.data
            if (row.get("Team") == country or row.get("NOC") == country)
            and row.get("Year") == year
            and row.get("Medal") != "NA"
        ]
        filtered_data.sort(key=lambda x: (x["Name"], x["Event"]))

        summary = {"Gold": 0, "Silver": 0, "Bronze": 0}
        for row in filtered_data:
            summary[row["Medal"]] += 1

        return filtered_data[:10], summary

    def total_medals_by_year(self, year):
        filtered_data = [row for row in self.data if row.get("Year") == year and row.get("Medal") != "NA"]
        summary = {}
        for row in filtered_data:
            team = row.get("Team", "Unknown")
            if team not in summary:
                summary[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            summary[team][row["Medal"]] += 1
        return summary
