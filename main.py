from engine.allocator import load_data, allocate_costs


def main():
    data = load_data("data/sample_shared_costs.json")
    detailed_results, summary_results = allocate_costs(data)

    print("\n--- Detailed Allocation Report ---\n")

    for r in detailed_results:
        print(f"Team: {r['team']}")
        print(f"Resource: {r['resource']}")
        print(f"Service: {r['service']}")
        print(f"Usage %: {r['usage_percent']}%")
        print(f"Allocated Cost: ${r['allocated_cost']}")
        print("------------------------")

    print("\n--- Team Chargeback Summary ---\n")

    for r in summary_results:
        print(f"Team: {r['team']}")
        print(f"Total Chargeback: ${r['total_chargeback']}")
        print("------------------------")


if __name__ == "__main__":
    main()
