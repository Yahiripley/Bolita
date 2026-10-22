import pytest

from main import calcular_area_triangulo

def test_area_triangulo():
    #resultado obtenido (real)
    actual_result = calcular_area_triangulo(13., 6)

    #assert (estamos asegurando o verificando) que el resultado obtenido es igual al resultado esperado (19.5)
    assert actual_result == pytest.approx(19.5, abs=0.01) 