"""
Script para obter o Student Performance Dataset diretamente da UCI ML Repository.

Duas opções:
  1) Via pacote oficial 'ucimlrepo' (recomendado - traz metadados e descrição das colunas)
  2) Via download direto do arquivo .zip do repositório da UCI

Requisitos:
  pip install ucimlrepo pandas requests --break-system-packages
"""

import pandas as pd

# ---------------------------------------------------------------------------
# OPÇÃO 1: pacote oficial ucimlrepo (mais simples e recomendado)
# ---------------------------------------------------------------------------
def baixar_via_ucimlrepo():
    from ucimlrepo import fetch_ucirepo

    # id=320 é o "Student Performance" no repositório da UCI
    dataset = fetch_ucirepo(id=320)

    X = dataset.data.features   # todas as variáveis preditoras
    y = dataset.data.targets    # G1, G2, G3 (as três notas)

    df = pd.concat([X, y], axis=1)
    df.to_csv("student_performance_full.csv", index=False)

    print("Metadados:", dataset.metadata.name)
    print("Descrição das variáveis:")
    print(dataset.variables)
    print(f"\nDataset salvo em student_performance_full.csv ({df.shape[0]} linhas, {df.shape[1]} colunas)")
    return df


# ---------------------------------------------------------------------------
# OPÇÃO 2: download direto do .zip oficial (student.zip contém student-mat.csv
# e student-por.csv, separados por matéria: Matemática e Português)
# ---------------------------------------------------------------------------
def baixar_via_zip_direto(pasta_destino="."):
    import requests, zipfile, io

    url = "https://archive.ics.uci.edu/static/public/320/student+performance.zip"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        # o zip principal contém um segundo zip "student.zip" lá dentro
        z.extractall(pasta_destino)

    print(f"Arquivos extraídos em: {pasta_destino}")
    print("Procure por student-mat.csv (Matemática) e student-por.csv (Português).")


if __name__ == "__main__":
    print("Tentando baixar via ucimlrepo...")
    try:
        baixar_via_ucimlrepo()
    except Exception as e:
        print(f"Falhou ({e}). Tentando download direto do .zip...")
        baixar_via_zip_direto()
