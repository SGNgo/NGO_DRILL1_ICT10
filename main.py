# AREA OF A TRAPEZOID
from pyscript import display, document


def trapezoid_area(e):
    base1 = float(document.getElementById('base1').value)
    base2 = float(document.getElementById('base2').value)
    height = float(document.getElementById('height').value)

    area = ((base1 + base2) / 2) * height

    display(f'The area of a trapezoid with bases {base1}, {base2} and height {height} is {area}', target="output")

def reset(e):
    document.getElementById('base1').value = ""
    document.getElementById('base2').value = ""
    document.getElementById('height').value = ""
    document.getElementById('output').innerHTML = ""