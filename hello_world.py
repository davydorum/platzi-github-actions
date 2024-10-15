import os

def main():
    name = os.get_env("USERNAME")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
