import yaml

def generate_docker_compose_file(app_name):
    services = {}

    while True:
        print("\nAdd a service to your docker-compose.yml (Enter 0 to finish):")
        service_name = input("Enter the service name: ")

        if service_name == '0':
            break

        container_name = input(f"Enter the container name for {service_name}: ")
        build_path = input(f"Enter the build path for {service_name} (e.g., '.'): ")
        image_name = input(f"Enter the image name for {service_name}: ")
        restart_policy = input(f"Enter the restart policy for {service_name} (e.g., 'unless-stopped'): ")
        env_file_path = input(f"Enter the env_file path for {service_name} (e.g., '.env'): ")
        database_client = input(f"Enter the DATABASE_CLIENT for {service_name}: ")
        database_host = input(f"Enter the DATABASE_HOST for {service_name}: ")
        database_port = input(f"Enter the DATABASE_PORT for {service_name}: ")
        database_name = input(f"Enter the DATABASE_NAME for {service_name}: ")
        database_username = input(f"Enter the DATABASE_USERNAME for {service_name}: ")
        database_password = input(f"Enter the DATABASE_PASSWORD for {service_name}: ")
        jwt_secret = input(f"Enter the JWT_SECRET for {service_name}: ")
        admin_jwt_secret = input(f"Enter the ADMIN_JWT_SECRET for {service_name}: ")
        app_keys = input(f"Enter the APP_KEYS for {service_name}: ")
        node_env = input(f"Enter the NODE_ENV for {service_name}: ")
        volumes = input(f"Enter the volume paths (comma-separated) for {service_name} (e.g., './config,./src'): ")
        port_mapping = input(f"Enter the port mapping for {service_name} (e.g., '1337:1337'): ")

        service_config = {
            'container_name': container_name,
            'build': build_path,
            'image': image_name,
            'restart': restart_policy,
            'env_file': env_file_path,
            'environment': {
                'DATABASE_CLIENT': database_client,
                'DATABASE_HOST': database_host,
                'DATABASE_PORT': database_port,
                'DATABASE_NAME': database_name,
                'DATABASE_USERNAME': database_username,
                'DATABASE_PASSWORD': database_password,
                'JWT_SECRET': jwt_secret,
                'ADMIN_JWT_SECRET': admin_jwt_secret,
                'APP_KEYS': app_keys,
                'NODE_ENV': node_env,
            },
            'volumes': volumes.split(','),
            'ports': [port_mapping],
        }

        services[service_name] = service_config

    # Generate the docker-compose.yml content
    docker_compose = {
        'version': '3',
        'services': services,
    }

    with open(f"{app_name}_docker-compose.yml", "w") as compose_file:
        compose_file.write(yaml.dump(docker_compose, default_flow_style=False))

if __name__ == '__main__':
    generate_docker_compose_file("MyApp")
