test_name_space = {'global': ['v_01', {'ns1': ['v_10']}, 'v_04']}


def get(data: dict,
        name_space_fix: str,
        var_name: str,
        name_space: str) -> str:
    def search_in_list(lst, current_ns):
        for item in lst:
            if item == var_name:
                return f"variable {item} was found in namespace: {name_space_fix}"
            if isinstance(item, dict):
                result = search_in_dict(item)
                if result:
                    return result
        return None

    def search_in_dict(d):
        for key, value in d.items():
            print(f"ищем в словаре {key}")
            if isinstance(value, list):
                print(f"ищем в namespace {key}")
                result = search_in_list(value, key)
                if result:
                    return result
        return None

    if isinstance(data, dict):
        return search_in_dict(data)
    elif isinstance(data, list):
        return search_in_list(data, name_space)

    return "Variable not found"


print("get result:", get(test_name_space, 'global', 'v_04', ""))
