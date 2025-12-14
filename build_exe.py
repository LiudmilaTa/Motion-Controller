"""
Skript pro vytvoření spustitelného EXE souboru Motion Controller aplikace.
Použití: python build_exe.py
"""

import os
import sys
import subprocess

def install_pyinstaller():
    """Nainstaluje PyInstaller, pokud není nainstalován."""
    print("🔧 Kontrola PyInstaller...")
    try:
        import PyInstaller
        print("✅ PyInstaller již nainstalován")
    except ImportError:
        print("📦 Instalace PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller nainstalován")

def build_exe():
    """Vytvoří EXE soubor pomocí PyInstaller."""
    print("\n🚀 Spouštím vytváření EXE souboru...")
    
    # PyInstaller parametry
    cmd = [
        "pyinstaller",
        "--name=MotionController",
        "--onefile",
        "--windowed",
        "--icon=NONE",
        "--add-data=config.py;.",
        "--hidden-import=mediapipe",
        "--hidden-import=cv2",
        "--hidden-import=pyautogui",
        "--hidden-import=pydirectinput",
        "--hidden-import=numpy",
        "--collect-all=mediapipe",
        "app.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ EXE soubor úspěšně vytvořen!")
        print("📁 Najdete ho v složce: dist/MotionController.exe")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Chyba při vytváření EXE: {e}")
        return False
    
    return True

def main():
    """Hlavní funkce."""
    print("=" * 60)
    print("🎮 Motion Controller - Vytváření EXE souboru")
    print("=" * 60)
    
    # Kontrola Python verze
    if sys.version_info < (3, 8):
        print("❌ Vyžaduje Python 3.8 nebo vyšší")
        sys.exit(1)
    
    # Instalace PyInstaller
    install_pyinstaller()
    
    # Vytvoření EXE
    if build_exe():
        print("\n" + "=" * 60)
        print("🎉 HOTOVO!")
        print("=" * 60)
        print("\n📝 Další kroky:")
        print("1. Najděte soubor: dist/MotionController.exe")
        print("2. Zkopírujte ho kamkoliv")
        print("3. Spusťte dvojklikem")
        print("\n⚠️  Poznámka: První spuštění může trvat déle")

if __name__ == "__main__":
    main()
