# Report Generation Logic

class ReportService:
    def generate_report(self, data):
        # Logic for generating the report
        report = f"Report generated with {len(data)} entries."
        return report

    def export_to_csv(self, data, filename):
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Entry ID', 'Description', 'Date'])  # Header
            for entry in data:
                writer.writerow(entry)
        return f"{filename} has been created with {len(data)} entries."