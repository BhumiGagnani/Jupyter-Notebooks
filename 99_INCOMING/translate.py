import streamlit as st
import re
import time
from deep_translator import GoogleTranslator

st.title('🌍 Streamlit App Translation')

st.header(':rainbow[Test app for deep_translator]')

st.subheader(':rainbow-background[Feasibility of automatic translation in Streamlit Apps]')

# Function to translate Markdown text while preserving bold/italic formatting
def translate_markdown(markdown_text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)

    # ✅ Step 1: Add spaces inside **bold** and *italic* before translation
    text_with_spaces = re.sub(r"(\*\*|\*)(\S.*?\S)(\*\*|\*)", r"\1 \2 \3", markdown_text)

    # ✅ Step 2: Split text into lines to preserve Markdown structure
    lines = text_with_spaces.strip().split("\n")

    translated_lines = []
    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith("#"):  # ✅ Preserve headers (even multiple ##)
            header_level = len(stripped_line) - len(stripped_line.lstrip("#"))  # Count #
            text_without_hash = stripped_line.lstrip("#").strip()  # Remove #
            translated_text = translator.translate(text_without_hash)  # Translate only text
            translated_lines.append("#" * header_level + " " + translated_text)  # Rebuild header
        else:
            translated_lines.append(translator.translate(stripped_line))

    translated_text = "\n\n".join(translated_lines)  # Ensure proper spacing

    # ✅ Step 3: Remove spaces inside **bold** and *italic* after translation
    final_text = re.sub(r"(\*\*|\*) (.*?) (\*\*|\*)", r"\1\2\3", translated_text)

    return final_text

# ✅ Split the long Markdown text into multiple sections
sections = [
    """
# 🍦 The Culture of Italian Gelato
Gelato is more than just ice cream in **Italy**—it is an essential part of daily life and a **symbol of Italian culture**.
Unlike industrial ice cream, gelato is **crafted daily** in artisanal shops called _gelaterie_.
    """,
    """
## 🍨 The Differences Between Gelato and Ice Cream
Gelato is **not the same** as traditional ice cream. Some key differences include:
- **Less fat**: Gelato is made with more **milk** and less **cream**, making it lower in fat.
- **Denser texture**: It is churned at a **slower speed**, incorporating less air.
- **More intense flavor**: With less fat, flavors are more pronounced and natural.
    """,
    """
## 🍧 Popular Gelato Flavors in Italy
Italy offers a wide variety of **classic and modern flavors**, including:

### **Classic Flavors**
- **Pistachio** (_Pistacchio_) 🌰
- **Hazelnut** (_Nocciola_) 🌰
- **Chocolate** (_Cioccolato_) 🍫
- **Lemon** (_Limone_) 🍋
- **Stracciatella** (vanilla with chocolate shavings) 🍦🍫

### **Modern & Creative Flavors**
- **Tiramisu** 🍰☕
- **Ricotta & Fig** 🧀🍯
- **Basil & Lemon** 🌿🍋
- **Salted Caramel** 🍯🧂
    """,
    """
## 📍 Where to Find the Best Gelato
The best gelato comes from _gelaterie artigianali_ (artisan gelato shops). Look for these signs of **high-quality gelato**:
- **Natural colors** (not overly bright or artificial)
- **Seasonal flavors** using fresh ingredients
- **Stored in covered metal containers** instead of high, colorful mountains

Famous gelaterie include:
- [Gelateria del Teatro](https://www.gelateriadelteatro.it/) (Rome 🇮🇹)
- [Grom](https://www.grom.it/) (Various locations)
- [La Carraia](https://www.lacarraiagroup.eu/) (Florence 🇮🇹)
    """,
    """
## 🌍 The Worldwide Popularity of Gelato
Italian gelato has gained **global popularity**, with artisanal gelaterie opening in:
- 🇫🇷 **France** – Especially in Paris and the Riviera.
- 🇩🇪 **Germany** – Many Italian immigrants brought gelato culture.
- 🇺🇸 **United States** – Gelato shops are booming in major cities.
- 🇯🇵 **Japan** – Creative flavors like **matcha gelato** are a hit.

Whether in Italy or abroad, gelato remains a **beloved tradition** for people of all ages! 🍦✨
    """
]

# ✅ Language selection dropdown
languages = ['fr', 'es', 'it', 'ru']
target_lang = st.selectbox("🌎 Choose the target language", languages)

# ✅ Create placeholders for streaming translation
placeholders = [st.empty() for _ in sections]

# ✅ Loop through each section and show it while translating
for i, section in enumerate(sections):
    placeholders[i].markdown(section)  # Show English text immediately
    time.sleep(1)  # Simulate delay to allow user to start reading

    translated_text = translate_markdown(section, target_lang)  # Translate section
    placeholders[i].markdown(translated_text)  # Replace with translated text
