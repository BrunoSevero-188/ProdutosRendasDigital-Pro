import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Onde o produtos.json final é salvo (pasta do frontend)
OUTPUT_JSON_PATH = os.path.join(BASE_DIR, "..", "frontend", "data", "produtos.json")

FONTES_ATIVAS = ["kiwify", "cakto"]

DIAS_VALIDADE_OFERTA = 15

HEADERS_PADRAO = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}
