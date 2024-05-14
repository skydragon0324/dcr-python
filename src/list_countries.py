from collections import defaultdict
import json
from db import Country

class ListCountries:
    def run(self):
        regions = defaultdict(lambda: {"number_countries": 0, "total_population": 0})
        for country in Country.list_all():
            region_name = country.data["region_name"]
            regions[region_name]["number_countries"] += 1
            regions[region_name]["total_population"] += int(country.data["population"])
        output = {"regions": []}
        for region_name, data in regions.items():
            output["regions"].append({
                "name": region_name,
                "number_countries": data["number_countries"],
                "total_population": data["total_population"]
            })
        print(json.dumps(output, indent=4))
if __name__ == "__main__":
    ListCountries().run()