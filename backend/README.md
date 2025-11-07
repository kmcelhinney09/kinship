# Backend

This directory contains the backend for the Kinship application, built with FastAPI and SQLite.

## Technologies Used

*   **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints.
*   **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
*   **SQLAlchemy**: The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
*   **uv**: A fast Python package installer and resolver, written in Rust.

## Getting Started

### Installation

The dependencies are managed with `uv`. To install them, run the following command in the root of the project:

```bash
uv pip install -r backend/pyproject.toml
```

### Running the Server

To run the development server, use the following command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

When using the dev container, the server will be started automatically for you.
