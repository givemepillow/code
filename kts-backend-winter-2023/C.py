import json


def C(data):
    result = clear_json(data)
    return None if isinstance(result, (list, dict)) and len(result) == 0 else result


def clear_json(data):
    if isinstance(data, list):
        for i in range(len(data)):
            data[i] = clear_json(data[i])
        return [v for v in data if not isinstance(v, (list, dict)) or len(v) > 0]
    elif isinstance(data, dict):
        for k in data:
            data[k] = clear_json(data[k])
        return {k: v for k, v in data.items() if not isinstance(v, (list, dict)) or len(v) > 0}
    else:
        return data


print(C(data=json.loads(input())))
