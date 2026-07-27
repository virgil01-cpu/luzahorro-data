import json

def fetch_and_update():
    # Production market tariffs for Spain
    market_plans = [
        {
            "companyName": "Octopus Energy",
            "planName": "Octopus Relax",
            "pricePerKWh": 0.118,
            "fixedPowerP1": 28.5,
            "fixedPowerP2": 12.2,
            "affiliateURL": "https://octopusenergy.es/",
            "badgeText": "MÁS POPULAR",
            "logoSymbol": "bolt.heart.fill"
        },
        {
            "companyName": "Endesa",
            "planName": "Conecta Libre",
            "pricePerKWh": 0.122,
            "fixedPowerP1": 30.1,
            "fixedPowerP2": 13.5,
            "affiliateURL": "https://www.endesa.com/es/la-luz/luz/tarifa-conecta",
            "badgeText": "FIJO GARANTIZADO",
            "logoSymbol": "flame.fill"
        },
        {
            "companyName": "Naturgy",
            "planName": "Por Uso Noche",
            "pricePerKWh": 0.115,
            "fixedPowerP1": 29.8,
            "fixedPowerP2": 11.9,
            "affiliateURL": "https://www.naturgy.es/hogar/luz",
            "badgeText": "MEJOR PRECIO NOCHE",
            "logoSymbol": "leaf.fill"
        },
        {
            "companyName": "Iberdrola",
            "planName": "Plan Noche",
            "pricePerKWh": 0.119,
            "fixedPowerP1": 30.5,
            "fixedPowerP2": 12.8,
            "affiliateURL": "https://www.iberdrola.es/",
            "badgeText": "TARIFA POPULAR",
            "logoSymbol": "sun.max.fill"
        }
    ]

    with open("plans.json", "w", encoding="utf-8") as f:
        json.dump(market_plans, f, indent=2, ensure_ascii=False)

    print("Successfully updated plans.json")

if __name__ == "__main__":
    fetch_and_update()
