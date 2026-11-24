import conn_func
import login_func

def main():
    conn_func.open_conn()
    curr_user = login_func.login()
    conn_func.close_conn()

if __name__ == "__main__":
    main()
