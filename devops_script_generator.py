import click

@click.command()
@click.option('--platform', prompt='Enter the cloud platform (e.g., AWS, Azure, GCP)')
@click.option('--app-name', prompt='Enter the name of your application')
def generate_devops_script(platform, app_name):
    if platform.lower() == 'aws':
        generate_aws_script(app_name)
    elif platform.lower() == 'azure':
        generate_azure_script(app_name)
    elif platform.lower() == 'gcp':
        generate_gcp_script(app_name)
    else:
        click.echo(f"Unsupported platform: {platform}")

def generate_aws_script(app_name):
    # Generate AWS-specific script
    script = f"""#!/bin/bash
# Script to deploy {app_name} to AWS
# Add your AWS deployment commands here
"""
    print(script)

def generate_azure_script(app_name):
    # Generate Azure-specific script
    script = f"""#!/bin/bash
# Script to deploy {app_name} to Azure
# Add your Azure deployment commands here
"""
    print(script)

def generate_gcp_script(app_name):
    # Generate GCP-specific script
    script = f"""#!/bin/bash
# Script to deploy {app_name} to GCP
# Add your GCP deployment commands here
"""
    print(script)

if __name__ == '__main__':
    generate_devops_script()
