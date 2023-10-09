
---

# DevOps Script Generator

![GitHub stars](https://img.shields.io/github/stars/AashooSharmaTech/auto-create-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/AashooSharmaTech/auto-create-tool?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/AashooSharmaTech/auto-create-tool?style=social)

A command-line tool for generating DevOps-related scripts such as Dockerfiles and `docker-compose.yml` files based on user inputs.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive script generation.
- Support for Dockerfiles.
- Support for `docker-compose.yml` files.
- Customizable configuration options.
- Easy-to-use command-line interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- [pip](https://pip.pypa.io/en/stable/installation/) for installing Python packages.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AashooSharmaTech/auto-create-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd auto-create-tool
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate a Dockerfile

To generate a Dockerfile, run the following command:

```bash
python main.py
```

Follow the on-screen prompts to customize your Dockerfile, including the base image, instructions, and more. The generated Dockerfile will be saved in the `./my_files/` directory.

### Generate a `docker-compose.yml` file

To generate a `docker-compose.yml` file, choose option 2 when running the tool:

```bash
python main.py
```

Follow the on-screen prompts to configure your services, including container names, image names, environment variables, and more. The generated `docker-compose.yml` file will be saved in the project directory.

## Contributing

Contributions are welcome! Please feel free to fork this repository, make changes, and submit a pull request. If you encounter any issues or have suggestions for improvements, please create an [issue](https://github.com/AashooSharmaTech/your-repository/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a basic template that you can customize to fit your tool's specific details and usage instructions. Make sure to replace `your-username` and `your-repository` with the actual GitHub username and repository name where your tool is hosted.