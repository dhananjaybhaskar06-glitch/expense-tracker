def auto_category(desc):
    desc = desc.lower()
    if "food" in desc:
        return "Food"
    elif "uber" in desc:
        return "Transport"
    elif "amazon" in desc:
        return "Shopping"
    elif "movie" in desc:
        return "Entertainment"
    else:
        return "Others"