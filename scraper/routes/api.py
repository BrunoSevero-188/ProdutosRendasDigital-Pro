from flask import Blueprint, jsonify
import json
import os

from config import OUTPUT_JSON_PATH
from core.kiwify_scraper import buscar_produtos_kiwify
from core.cakto_scraper import buscar_produtos_cakto

api_bp = Blueprint("api", __name__)

# TODO: troque por uma lista real de URLs de produto que você quer rastrear
URLS_KIWIFY = []
URLS_CAKTO = []


@api_bp.route("/atualizar-produtos", methods=["POST"])
def atualizar_produtos():
    produtos = []
    produtos += buscar_produtos_kiwify(URLS_KIWIFY)
    produtos += buscar_produtos_cakto(URLS_CAKTO)

    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok", "total_produtos": len(produtos)})


@api_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    if not os.path.exists(OUTPUT_JSON_PATH):
        return jsonify([])

    with open(OUTPUT_JSON_PATH, "r", encoding="utf-8") as arquivo:
        return jsonify(json.load(arquivo))
