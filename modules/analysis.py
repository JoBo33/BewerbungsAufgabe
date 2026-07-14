import json
import calculator
import ai_analysis


if __name__ == "__main__":
    with open('data.json', 'r') as f:
        data = json.load(f)

    res_dict = calculator.calc_pv_values(data)
    res_dict["ai_analysis"] = ai_analysis.ai_analysis(data)
    print(json.dumps(res_dict))


