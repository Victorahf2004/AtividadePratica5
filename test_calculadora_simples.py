from calculadoraSimples import CalculadoraSimples
import pytest

@pytest.fixture
def calculadora():
    return CalculadoraSimples()

def test_somar(calculadora):
    assert calculadora.somar(2, 3) == 5

def test_subtrair(calculadora):
    assert calculadora.subtrair(3, 2) == 1

def test_multiplicar(calculadora):
    assert calculadora.multiplicar(2, 3) == 6

def test_ehPar(calculadora):
    assert calculadora.ehPar(4) is True

def test_potencia(calculadora):
    assert calculadora.potencia(2, 3) == 8