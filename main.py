import function_1
import function_2

def main():
    print("Choose the script you want to create:")
    print("[1] Dockerfile")
    print("[2] docker-compose.yml")
    
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        function_1.generate_custom_dockerfile("MyApp")
    elif choice == '2':
        function_2.generate_docker_compose_file("MyApp")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
