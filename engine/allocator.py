import json
from collections import defaultdict


def load_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def allocate_costs(data):
    detailed_results = []
    team_totals = defaultdict(float)

    for item in data:
        resource = item["resource"]
        service = item["service"]
        total_cost = item["total_cost"]
        usage = item["usage"]

        for team, percent in usage.items():
            allocated_cost = total_cost * (percent / 100)

            detailed_results.append({
                "team": team,
                "resource": resource,
                "service": service,
                "usage_percent": percent,
                "allocated_cost": round(allocated_cost, 2)
            })

            team_totals[team] += allocated_cost

    summary_results = [
        {
            "team": team,
            "total_chargeback": round(total, 2)
        }
        for team, total in team_totals.items()
    ]

    return detailed_results, summary_results
