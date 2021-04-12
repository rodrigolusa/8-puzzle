import pytest
from src.nodo import Nodo
from src.direcao import Direcao


@pytest.fixture
def estado_12345_678():
    return Nodo("1234_5678")


def test_vai_pra_cima_012345_6(estado_12345_678):
    estado = estado_12345_678
    proximo_estado = estado.faz_acao(Direcao.acima)
    assert proximo_estado == Nodo("1_3425678")


def test_vai_pra_baixo_012345_6(estado_12345_678):
    estado = estado_12345_678
    proximo_estado = estado.faz_acao(Direcao.abaixo)
    assert proximo_estado == Nodo("1234756_8")


def test_vai_pra_direita_012345_6(estado_12345_678):
    estado = estado_12345_678
    proximo_estado = estado.faz_acao(Direcao.direita)
    assert proximo_estado == Nodo("12345_678")


def test_vai_pra_esquerda_012345_6(estado_12345_678):
    estado = estado_12345_678
    proximo_estado = estado.faz_acao(Direcao.esquerda)
    assert proximo_estado == Nodo("123_45678")









