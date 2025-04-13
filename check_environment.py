import sys
import subprocess
import pkg_resources

def check_python_version():
    print("Verificando versão do Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 ou superior é necessário")
        print(f"Versão atual: {sys.version}")
        return False
    print(f"✅ Python {sys.version} - OK")
    return True

def check_pip():
    print("\nVerificando pip...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
        print("✅ pip está instalado - OK")
        return True
    except subprocess.CalledProcessError:
        print("❌ pip não está instalado ou não está funcionando corretamente")
        return False

def check_dependencies():
    print("\nVerificando dependências...")
    required = {
        'networkx': '3.1',
        'matplotlib': '3.7.1',
        'numpy': '1.24.3'
    }
    
    all_ok = True
    for package, version in required.items():
        try:
            pkg_resources.require(f"{package}=={version}")
            print(f"✅ {package} {version} - OK")
        except pkg_resources.VersionConflict as e:
            print(f"❌ {package}: versão incorreta - {e}")
            all_ok = False
        except pkg_resources.DistributionNotFound:
            print(f"❌ {package}: não instalado")
            all_ok = False
    
    return all_ok

def main():
    print("🔍 Verificando ambiente...\n")
    
    python_ok = check_python_version()
    pip_ok = check_pip()
    deps_ok = check_dependencies()
    
    print("\n📋 Resumo:")
    if python_ok and pip_ok and deps_ok:
        print("✅ Ambiente configurado corretamente!")
        print("Você pode executar o projeto com: python main.py")
    else:
        print("❌ Foram encontrados problemas no ambiente")
        print("\nSugestões:")
        if not python_ok:
            print("- Instale Python 3.8 ou superior")
        if not pip_ok:
            print("- Instale ou atualize o pip")
        if not deps_ok:
            print("- Execute: pip install -r requirements.txt")
            print("- Se o erro persistir, tente instalar cada pacote individualmente")

if __name__ == "__main__":
    main() 