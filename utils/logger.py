import logging

_logger = None

def configurar_logger(log_file: str = "stockmaster.log"):
    """Configura o logger principal do sistema."""
    global _logger
    _logger = logging.getLogger("StockMaster")
    _logger.setLevel(logging.INFO)

    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    if not _logger.handlers:
        _logger.addHandler(fh)

    return _logger

def get_logger():
# retorna o logger configurado
    global _logger
    if _logger is None:
        configurar_logger()
    return _logger
