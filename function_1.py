import os

def select_base_image():
    print("Choose a base image for your Dockerfile:")
    print("[1] Python (latest)")
    print("[2] Node.js (latest)")
    print("[3] Ubuntu (latest)")
    print("[4] Other (provide a custom image name)")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        return "python:latest"
    elif choice == '2':
        return "node:latest"
    elif choice == '3':
        return "ubuntu:latest"
    elif choice == '4':
        return input("Enter the custom image name: ")
    else:
        print("Invalid choice. Using Python as the default base image (latest).")
        return "python:latest"

def generate_custom_dockerfile(app_name):
    base_image = select_base_image()

    dockerfile_contents = []

    while True:
        print("\nChoose a Dockerfile function to add (Enter 0 to finish):")
        print("[1] WORKDIR (Example: WORKDIR /app)")
        print("[2] COPY (Example: COPY . /app)")
        print("[3] RUN (Example: RUN apt-get update && apt-get install -y wget)")
        print("[4] EXPOSE (Example: EXPOSE 80)")
        print("[5] LABEL (Example: LABEL version=\"1.0\" maintainer=\"Your Name\")")
        print("[6] Comments")
        print("[7] ENV (Example: ENV MY_VARIABLE=my_value)")
        print("[8] ENTRYPOINT (Example: ENTRYPOINT [\"sh\", \"script.sh\"])")
        print("[9] VOLUME (Example: VOLUME /data)")
        print("[10] USER (Example: USER appuser)")
        print("[11] ARG (Example: ARG BUILD_ARG=default_value)")
        print("[12] CMD (Example: CMD [\"python\", \"app.py\"])")
        
        


           
        
        choice = input("Enter your choice (0-12): ")
        dockerfile_contents.append(f"\n")

        if choice == '0':
            break
        elif choice == '3':
            cmd = input("Enter the RUN command (e.g., apt-get update && apt-get install -y wget): ")
            dockerfile_contents.append(f"RUN {cmd}")
        elif choice == '12':
            cmd = input("Enter the CMD command (e.g., python app.py): ")
            dockerfile_contents.append(f"CMD {cmd}")
        elif choice == '1':
            path = input("Enter the WORKDIR path (e.g., /app): ")
            dockerfile_contents.append(f"WORKDIR {path}")
        elif choice == '2':
            source = input("Enter the COPY source (e.g., .): ")
            dest = input("Enter the COPY destination (e.g., /app): ")
            dockerfile_contents.append(f"COPY {source} {dest}")
        elif choice == '5':
            label = input("Enter the LABEL (e.g., version=\"1.0\" maintainer=\"Your Name\"): ")
            dockerfile_contents.append(f"LABEL {label}")
        elif choice == '4':
            port = input("Enter the EXPOSE port (e.g., 80): ")
            dockerfile_contents.append(f"EXPOSE {port}")
        elif choice == '7':
            env_var = input("Enter the ENV variable (e.g., MY_VARIABLE=my_value): ")
            dockerfile_contents.append(f"ENV {env_var}")
        elif choice == '8':
            entrypoint_cmd = input("Enter the ENTRYPOINT command (e.g., [\"sh\", \"script.sh\"]): ")
            dockerfile_contents.append(f"ENTRYPOINT {entrypoint_cmd}")
        elif choice == '9':
            volume = input("Enter the VOLUME (e.g., /data): ")
            dockerfile_contents.append(f"VOLUME {volume}")
        elif choice == '10':
            username = input("Enter the USER (e.g., appuser): ")
            dockerfile_contents.append(f"USER {username}")
        elif choice == '11':
            arg = input("Enter the ARG (e.g., BUILD_ARG=default_value): ")
            dockerfile_contents.append(f"ARG {arg}")
        elif choice == '6':
            comment = input("Enter a comment: ")
            dockerfile_contents.append(f"# {comment}")
        else:
            print("Invalid choice. Please select a valid option.")

    dockerfile = f"""\n# Dockerfile for {app_name}\nFROM {base_image}\n{"".join(dockerfile_contents)}"""
    
    print("\nGenerated Dockerfile:")
    print(dockerfile)

    # Create the Dockerfile and write the content to it
    dockerfile_path = "./my_files/Dockerfile"
    try:
        with open(dockerfile_path, "w") as dockerfile_file:
            dockerfile_file.write(dockerfile)
        print(f"\nDockerfile saved to {dockerfile_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    generate_custom_dockerfile("MyApp")
