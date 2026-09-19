import logging
import conversor
import pytest

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'test_conversor.log',
    filemode =  'w'
)

@pytest.mark.system
@pytest.mark.unit
def test_celsius_a_fahrenheit():
    resultado = conversor.celsius_a_fahrenheit(25)
    assert resultado == 77

@pytest.mark.system
@pytest.mark.multi
@pytest.mark.parametrize("quantity, expected", [(10, 6.21371),(50, 31.06855),(1000000000, 621371000)])
def test_km_a_mi(quantity, expected):
    resultado = conversor.km_a_mi(quantity)
    assert resultado == expected

@pytest.mark.system
@pytest.mark.aprox
def test_pesomex_a_dolar():
    resultado = conversor.pesomex_a_dolar(172.30)
    assert resultado == pytest.approx(10)

@pytest.mark.system
@pytest.mark.decimal
def test_celsius_a_fahrenheit_decimal():
    resultado = conversor.celsius_a_fahrenheit(23.4)
    assert resultado == 74.12

