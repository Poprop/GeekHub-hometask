# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

def unique_value_func(raw_dict):
    unique_wok = {}
    for key, value in raw_dict.items():
        if value not in unique_wok.values():
            unique_wok[key] = value
    return unique_wok


cod_names_wok = {2007: "mw1", 2009: "mw2", 2011: "mw3", 2019: "mw", 2022: "mw2", 2023: "mw3"}
print(unique_value_func(cod_names_wok))
