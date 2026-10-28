"""Environment check: imports the core libraries and prints their versions."""

import importlib
import sys

# nome usato in "import"  ->  nome usato in "pip install"
LIBRERIE = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "yfinance": "yfinance",
    "sklearn": "scikit-learn",
    "pytest": "pytest",
}


def controlla_libreria(nome_import: str) -> str | None:
    """Restituisce la versione della libreria, oppure None se non e' installata."""
    print(f"  ...controllo {nome_import}", end="\r", flush=True)
    try:
        modulo = importlib.import_module(nome_import)
    except ModuleNotFoundError:
        return None
    except Exception as errore:  # installata ma non si carica (es. DLL bloccata)
        return f"ERRORE -> {type(errore).__name__}: {errore}"
    return getattr(modulo, "__version__", "sconosciuta")


def main() -> None:
    print(f"Python {sys.version.split()[0]}  ->  {sys.executable}")
    in_venv = sys.prefix != sys.base_prefix
    print(f"Virtual environment attivo: {'SI' if in_venv else 'NO  (attivalo prima!)'}\n")

    mancanti = []
    for nome_import, nome_pip in LIBRERIE.items():
        versione = controlla_libreria(nome_import)
        if versione is None:
            print(f"  [MANCA] {nome_pip}")
            mancanti.append(nome_pip)
        else:
            stato = "[ERR]  " if versione.startswith("ERRORE") else "[OK]   "
            print(f"  {stato} {nome_pip:<13} {versione}")

    if mancanti:
        print(f"\nInstalla con:  python -m pip install {' '.join(mancanti)}")
    else:
        print("\nTutto pronto. Buon lavoro!")


if __name__ == "__main__":
    main()
