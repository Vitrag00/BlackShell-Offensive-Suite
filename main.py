import argparse
import os

def run_module(module, script, target):
    module_path = f"modules/{module}/{script}"
    if os.path.exists(module_path):
        if module_path.endswith(".sh"):
            os.system(f"bash {module_path} {target}")
        elif module_path.endswith(".py"):
            os.system(f"python3 {module_path} {target}")
        elif module_path.endswith(".pl"):
            os.system(f"perl {module_path} {target}")
        elif module_path.endswith(".awk"):
            os.system(f"awk -f {module_path} {target}")
        else:
            print("Unsupported script type.")
    else:
        print(f"Module {script} not found in {module}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BlackShell - Offensive Toolkit")
    parser.add_argument("module", choices=["recon", "scan", "vulnscan", "exploit", "report"])
    parser.add_argument("script", help="Script to run within the module")
    parser.add_argument("target", help="Target IP, domain or URL")

    args = parser.parse_args()
    run_module(args.module, args.script, args.target)
