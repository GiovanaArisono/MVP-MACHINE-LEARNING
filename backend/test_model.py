import pytest
import requests

API_URL = "http://localhost:5000/predict"

test_cases = [
    {
        "name": "Flood",
        "input": {
            "year": 2020,
            "total_deaths": 100,
            "total_affected": 150000,
            "total_damage_usd_original": 75000000
        }
    },
    {
        "name": "Storm",
        "input": {
            "year": 2018,
            "total_deaths": 30,
            "total_affected": 250000,
            "total_damage_usd_original": 150000000
        }
    },
    {
        "name": "Earthquake",
        "input": {
            "year": 2015,
            "total_deaths": 9000,
            "total_affected": 8500000,
            "total_damage_usd_original": 1000000000
        }
    },
    {
        "name": "Wildfire",
        "input": {
            "year": 2018,
            "total_deaths": 85,
            "total_affected": 100000,
            "total_damage_usd_original": 16000000000
        }
    },
    {
        "name": "Landslide",
        "input": {
            "year": 2010,
            "total_deaths": 350,
            "total_affected": 30000,
            "total_damage_usd_original": 50000000
        }
    },
    {
        "name": "Volcanic activity",
        "input": {
            "year": 2021,
            "total_deaths": 180,
            "total_affected": 60000,
            "total_damage_usd_original": 220000000
        }
    },
    {
        "name": "Extreme temperature",
        "input": {
            "year": 2017,
            "total_deaths": 80000,
            "total_affected": 100000,
            "total_damage_usd_original": 3000000
        }
    },
    {
        "name": "Drought",
        "input": {
            "year": 2000,
            "total_deaths": 85000,
            "total_affected": 400000,
            "total_damage_usd_original": 15000000
        }
    }
]

@pytest.mark.parametrize("case", test_cases)
def test_predict(case):
    response = requests.post(API_URL, json=case["input"])
    assert response.status_code == 200, f"Erro na API: {response.text}"

    data = response.json()
    assert "predicted_class" in data, f"Resposta inválida: {data}"

    print(f"✔️  Testando {case['name']}: previsto -> {data['predicted_class']}")
