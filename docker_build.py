import subprocess
import sys

def build():
    try:
        subprocess.run(["docker-compose", "up", "--build"], check=True)
        print("✅ Docker build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Docker build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build()