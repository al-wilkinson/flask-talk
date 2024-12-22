import subprocess

def get_mi_token():
    command = "curl https://api.ipify.org"

    try:
        returned_output = subprocess.check_output(command)
        print(f"Output is: {returned_output}")
    except Exception as e:
        print(f"Something suboptimal occurred, {e}")


if __name__ == "__main__":
    get_mi_token()