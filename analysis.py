def recommend_career(technical_avg, soft_avg):
    if technical_avg >= 80:
        return "Software / IT field"
    elif soft_avg >= 80:
        return "Management / HR"
    else:
        return "General skill-based career"

