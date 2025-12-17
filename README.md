# Motion Controller

Gestové ovládání her pomocí webkamery a detekce pohybů těla. Transformujte pohyby těla na herní ovládání bez jakéhokoli dalšího hardwaru!

## Informace o projektu

**Předmět:** NI-CCC (Počítačové a komunikační sítě)  
**Univerzita:** České vysoké učení technické v Praze (ČVUT)  
**Rok:** 2025  
**Členové týmu:**
- Liudmila Taganashkina - [taganliu@fit.cvut.cz]
- Vladimir Efimov - [efimovla@fit.cvut.cz]

## Princip fungování

Aplikace zachycuje video z webkamery a pomocí neuronových sítí detekuje pozici těla v reálném čase. Systém analyzuje 33 klíčových bodů těla (landmarks) a na základě jejich pozice generuje příslušné vstupy klávesnice a myši.

### Zpracovatelský řetězec

1. **Snímaní video** - Zachycení snímku z webkamery (OpenCV)
2. **Detekce pózy** - Identifikace klíčových bodů těla pomocí MediaPipe
3. **Analýza gest** - Vyhodnocení pozice rukou a těla
4. **Mapování vstupů** - Převod pohybů na akce klávesnice/myši
5. **Simulace vstupů** - Odeslání příkazů do operačního systému

### Ovládací zóny

- **Levá ruka** - WASD pohybové ovládání
- **Pravá ruka** - Pohyb kurzoru myši a klikání
- **Tělo** - Skok, dřep a další akce

## Příklady her

Vyzkoušejte Motion Controller s těmito hrami:

### Hry pro klávesnici
- [Všechny hry pro klávesnici na Poki](https://poki.com/cz/kl%C3%A1vesnice)
- [Temple Run 2](https://poki.com/cz/g/temple-run-2) - Běžecká hra s ovládáním WASD a skokem
- [Subway Surfers](https://poki.com/cz/g/subway-surfers) - Klasická endless runner hra

### Hry pro myš
- [Fruit Ninja](https://poki.com/cz/g/fruit-ninja) - Klikací hra s pohybem myši

## Hlavní knihovny

### Počítačové vidění
- **OpenCV (4.8.1)** - Zpracování obrazu z kamery, vykreslování GUI
- **MediaPipe (0.10.8)** - Detekce pózy těla pomocí ML modelů od Google
- **NumPy (1.23.5)** - Matematické operace s maticemi a vektory

### Simulace vstupů
- **PyDirectInput (1.0.4)** - Přímé ovládání pro hry (primární)
- **PyAutoGUI (0.9.54)** - Univerzální simulace vstupu (záložní)

### Struktura projektu

```
Motion-Controller/
├── app.py                  # Hlavní vstupní bod aplikace
├── camera_utils.py         # Inicializace a správa kamery
├── config.py               # Konfigurační nastavení
├── gesture_controller.py   # Rozpoznávání gest a mapování
├── input_helpers.py        # Inicializace vstupního systému
├── ui_helpers.py           # Vykreslování UI a vizualizace
├── build_exe.py            # Skript pro vytvoření EXE souboru
└── requirements.txt        # Python závislosti
```

## Instalace

### Možnost 1: Vytvoření vlastního EXE

Pokud chcete vytvořit vlastní EXE soubor:

```bash
# Nainstalujte závislosti
pip install -r requirements.txt

# Spusťte build skript
python build_exe.py
```

EXE soubor najdete ve složce `dist/MotionController.exe`.

### Možnost 2: Instalace z kódu (pro vývojáře)

**Požadavky:**
- Python 3.8-3.10
- Webkamera
- Windows OS (pro podporu DirectInput)

**Postup:**

1. **Vytvořte virtuální prostředí:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Nainstalujte závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Spusťte aplikaci:**
   ```bash
   python app.py
   ```

4. **Ovládání:**
   - **ESC** - Ukončení aplikace
   - Postavte se před kameru
   - Sledujte instrukce na obrazovce

## Ovládací schéma

| Část těla | Pozice | Akce |
|-----------|--------|------|
| Levá ruka | Levá zóna | Pohyb doleva (A) |
| Levá ruka | Pravá zóna | Pohyb doprava (D) |
| Levá ruka | Horní zóna | Pohyb vpřed (W) |
| Levá ruka | Dolní zóna | Pohyb vzad (S) |
| Pravá ruka | Pohyb | Kurzor myši |
| Pravá ruka | U těla | Levé kliknutí |
| Tělo | Skok | Mezerník |

![Instructions](assets/instructions.png)
*Manuál ovládání*

## Konfigurace

Nastavení lze upravit v souboru [config.py](config.py):

```python
# Rozlišení obrazovky
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Citlivost ovládání
DEADZONE = 0.1
MOUSE_SMOOTHING = 0.3

# Spolehlivost detekce
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5
```

## Technické parametry

- **FPS:** 30 snímků za sekundu
- **Detekované body:** 33 landmarks těla
- **Latence:** < 50 ms
- **Normalizované souřadnice:** Nezávislé na rozlišení

## Řešení problémů

### Kamera není detekována
- Zkontrolujte připojení kamery
- Ověřte oprávnění v nastavení Windows

### Chyba MediaPipe
Použijte čistou instalaci:
```bash
pip uninstall opencv-python mediapipe -y
pip cache purge
pip install --no-cache-dir -r requirements.txt
```
---
*Vytvořeno v rámci projektu NI-CCC, České vysoké učení technické v Praze, 2025*
