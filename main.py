from engine.allocator import load_data, allocate_costs
import csv
import os


def write_detailed_csv(data, filepath):
    keys = ["team", "resource", "service", "usage_percent", "allocated_cost"]

    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def write_summary_csv(data, filepath):
    keys = ["team", "total_chargeback"]

    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def main():
    data = load_data("data/sample_shared_costs.json")
    detailed_results, summary_results = allocate_costs(data)

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Write CSV files
    write_detailed_csv(detailed_results, "output/detailed_allocation_report.csv")
    write_summary_csv(summary_results, "output/team_chargeback_summary.csv")

    print("\n✅ Reports generated in /output folder\n")


if __name__ == "__main__":
    main()