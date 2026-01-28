import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Landing", layout="wide")

# Obtenir le répertoire du script courant
script_dir = Path(__file__).parent

# Charger les fichiers avec des chemins absolus
html = (script_dir / "index.html").read_text(encoding="utf-8")
css = (script_dir / "styles" / "style.css").read_text(encoding="utf-8")

# Charger les images et les convertir en base64
images_dir = script_dir / "images"
image_path = images_dir / "cool-code-image.png"

if image_path.exists():
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode()
    # Remplacer le lien image par une image base64
    html = html.replace(
        'src="images/cool-code-image.png"',
        f'src="data:image/png;base64,{image_base64}"',
    )

st.components.v1.html(f"<style>{css}</style>{html}", height=1200, scrolling=True)
