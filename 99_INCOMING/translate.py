import streamlit as st
from deep_translator import GoogleTranslator

st.title('Streamlit app translation')

st.header(':rainbow[Test app for deep_translator]')

st.subheader(':rainbow-background[Feasibility of automatic translation in Streamlit Apps]')

def translate_markdown(markdown_text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    
    # Split text into lines to preserve markdown structure
    lines = markdown_text.strip().split("\n")

    translated_lines = []
    for line in lines:
        if line.strip().startswith("#"):  # If it's a Markdown header, preserve #
            header_level = line.count("#")  # Count number of #
            text_without_hash = line.lstrip("#").strip()  # Remove leading #
            translated_text = translator.translate(text_without_hash)  # Translate only text
            translated_lines.append("#" * header_level + " " + translated_text)  # Re-add #
        else:
            translated_lines.append(translator.translate(line))  # Translate normally

    # Reconstruct the Markdown text
    translated_text = "\n\n".join(translated_lines)  # Ensure spacing for markdown

    return translated_text

# Example markdown text
Text1 = """
# 🍦 The Culture of Italian Gelato
Gelato is more than just ice cream in **Italy**—it is an essential part of daily life and a **symbol of Italian culture**. Unlike industrial ice cream, gelato is **crafted daily** in artisanal shops called _gelaterie_. 

Walking through Italian streets, you will see locals and tourists enjoying gelato at any time of day. Many Italians consider gelato a **social activity**, a perfect excuse to take a break, walk around, and enjoy a refreshing treat. 

## 🍨 The Differences Between Gelato and Ice Cream
Gelato is **not the same** as traditional ice cream. Some key differences include:
- **Less fat**: Gelato is made with more **milk** and less **cream**, making it lower in fat.
- **Denser texture**: It is churned at a **slower speed**, incorporating less air.
- **More intense flavor**: With less fat, flavors are more pronounced and natural.

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

## 📍 Where to Find the Best Gelato
The best gelato comes from _gelaterie artigianali_ (artisan gelato shops). Look for these signs of **high-quality gelato**:
- **Natural colors** (not overly bright or artificial)
- **Seasonal flavors** using fresh ingredients
- **Stored in covered metal containers** instead of high, colorful mountains

Famous gelaterie include:
- [Gelateria del Teatro](https://www.gelateriadelteatro.it/) (Rome 🇮🇹)
- [Grom](https://www.grom.it/) (Various locations)
- [La Carraia](https://www.lacarraiagroup.eu/) (Florence 🇮🇹)

## 🌍 The Worldwide Popularity of Gelato
Italian gelato has gained **global popularity**, with artisanal gelaterie opening in:
- 🇫🇷 **France** – Especially in Paris and the Riviera.
- 🇩🇪 **Germany** – Many Italian immigrants brought gelato culture.
- 🇺🇸 **United States** – Gelato shops are booming in major cities.
- 🇯🇵 **Japan** – Creative flavors like **matcha gelato** are a hit.

Whether in Italy or abroad, gelato remains a **beloved tradition** for people of all ages! 🍦✨
"""

# Language selection dropdown
languages = ['en', 'fr', 'es', 'it', 'ru', 'de']
target_lang = st.selectbox("Choose the target language", languages)

# Translate the text
Text1_t = translate_markdown(Text1, target_lang)

# Display the translated Markdown properly
st.markdown(Text1_t)
