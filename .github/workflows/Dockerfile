# Use a Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies and Python dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry install --no-root

# Install Playwright browsers
RUN poetry run playwright install

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set the environment variable for Poetry binary path
ENV PATH="$HOME/.local/bin:$PATH"

# Command to run your tests when the container starts
CMD ["poetry", "run", "pytest", "automation/tests/login_page_dertails_test/login_page_test_info.py "]
