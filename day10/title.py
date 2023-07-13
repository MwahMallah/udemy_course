def format_name(f_name: str, l_name: str) -> str:
    new_f_name = f_name.lower().title()
    new_l_name = l_name.lower().title()
    name = new_f_name + " " + new_l_name
    return name

f_name_1 = "anGeLa"
l_name_1 = "MaAKSIm"

print(format_name(f_name_1, l_name_1))


def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

