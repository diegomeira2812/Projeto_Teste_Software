# tests/test_funcionais_negativos.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import io
from unittest.mock import patch
import main


def test_opcao_invalida_no_menu():
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=["9", "0"]):
            try:
                main.main()
            except SystemExit:
                pass
    assert "Opção inválida!" in saida.getvalue()
