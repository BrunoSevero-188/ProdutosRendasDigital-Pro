"""
Scraper da Cakto — mesma lógica do kiwify_scraper.py: lista de URLs de
produto + extração via BeautifulSoup. Ajuste os seletores conforme o HTML
real da Cakto.
"""

from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

from config import HEADERS_PADRAO, DIAS_VALIDADE_OFERTA


def buscar_produtos_cakto(urls_produtos):
    produtos = []

    for url in urls_produtos:
        try:
            resposta = requests.get(url, headers=HEADERS_PADRAO, timeout=15)
            resposta.raise_for_status()
        except requests.RequestException as erro:
            print(f"[Cakto] Falha ao acessar {url}: {erro}")
            continue

        soup = BeautifulSoup(resposta.text, "html.parser")

        # TODO: ajustar os seletores conforme o HTML real da página de
        # checkout da Cakto.
        titulo_tag = soup.select_one("h1")
        imagem_tag = soup.select_one("meta[property='og:image']")
        preco_tag = soup.select_one("[class*='price']")

        titulo = titulo_tag.get_text(strip=True) if titulo_tag else ""
        imagem = imagem_tag["content"] if imagem_tag else ""
        preco_novo = preco_tag.get_text(strip=True) if preco_tag else ""

        if not titulo:
            continue

        produtos.append({
            "titulo": titulo,
            "imagem": imagem,
            "precoNovo": preco_novo,
            "precoAntigo": "",
            "link": url,
            "dataFim": str(date.today() + timedelta(days=DIAS_VALIDADE_OFERTA)),
        })

    return produtos
