"""
Script to print Python path and interpreter information.
"""

import sys
import os
import site

def main():
    """
    Print Python path and interpreter information.
    """
    print("=== Python Interpreter Information ===")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    print("\n=== Python Path (sys.path) ===")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")
    
    print("\n=== Site Packages ===")
    try:
        site_packages = site.getsitepackages()
        for i, path in enumerate(site_packages):
            print(f"{i+1}. {path}")
    except Exception as e:
        print(f"Error getting site packages: {e}")
    
    print("\n=== Environment Variables ===")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', 'Not set')}")
    
    print("\n=== Installed Packages ===")
    try:
        import pkg_resources
        installed_packages = sorted([f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set])
        print(f"Total installed packages: {len(installed_packages)}")
        print("First 10 packages:")
        for i, pkg in enumerate(installed_packages[:10]):
            print(f"{i+1}. {pkg}")
    except ImportError:
        print("pkg_resources not available")

if __name__ == "__main__":
    main() 