def calculate_risk(open_ports):
    score = 0

    for p in open_ports:
        if p["port"] in [445, 139]:
            score += 30
        elif p["port"] < 1024:
            score += 10

    if score >= 60:
        return score, "HIGH"
    elif score >= 30:
        return score, "MEDIUM"
    else:
        return score, "LOW"
