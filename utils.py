def get_query(f, cmd, value):
    data = map(lambda v: v.strip(), f)
    if cmd == "filter":
        data = filter(lambda v, text=value: text in v, data)
    elif cmd == "map":
        id_ = int(value)
        data = map(lambda v: v.split(" ")[id_], data)
    elif cmd == "unique":
        data = set(data)
    elif cmd == "sort":
        reverse = value == "desc"
        data = sorted(data, reverse=reverse)
    elif cmd == "limit":
        data = list(data)[:int(value)]
    return data
