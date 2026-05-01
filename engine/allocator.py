import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def allocate_costs(data):
    results = []

    for item in data:
        resource = item["resource"]
        service = item["service"]
        total_cost = item["total_cost"]
        usage = item["usage"]

        for team, percent in usage.items():
            allocated_cost = total_cost * (percent / 100)

            results.append({
                "team": team,
                "resource": resource,
                "service": service,
                "allocated_cost": round(allocated_cost, 2)
            })

    return results
