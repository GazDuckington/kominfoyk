def dict_to_object(data: dict, cls):
    filtered_data = {
        key: value
        for key, value in data.items()
        if key in cls.__init__.__code__.co_varnames
    }
    return cls(**filtered_data)
