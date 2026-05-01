from engine.allocator import load_data, allocate_costs

def main():
    data = load_data("data/sample_shared_costs.json")
    results = allocate_costs(data)

    print("\n--- Chargeback Report ---\n")

    for r in results:
        print(f"Team: {r['team']}")
        print(f"Resource: {r['resource']}")
        print(f"Service: {r['service']}")
        print(f"Allocated Cost: ${r['allocated_cost']}")
        print("------------------------")

if __name__ == "__main__":
    main()
