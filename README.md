# FastAPI Project

A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

---

## 🚀 Features

- **Fast to code**: Increases development speed by about 200% to 300%
- **Fewer bugs**: Reduces human (developer) induced errors by about 40%
- **Intuitive**: Great editor support, completion everywhere, less debugging
- **Easy**: Designed to be simple to use and learn
- **Short**: Minimizes code duplication, multiple features per parameter declaration
- **Robust**: Production-ready code with automatic interactive documentation
- **Standards-based**: Fully compatible with OpenAPI and JSON Schema standards

---

## 🛠️ Installation

Install FastAPI and Uvicorn (ASGI server) via pip:

```bash
pip install fastapi uvicorn



.
├── main.py               # FastAPI app entry point
├── py_pydantic.py        # Pydantic models for data validation
├── py_types.py           # Custom type definitions
├── templating.py         # Template rendering utilities (if any)
├── tempCodeRunnerFile.py # Temporary files, can be removed
└── __pycache__/          # Compiled Python files (should be in .gitignore)

```
🚀 Running the app
To run the FastAPI application, use Uvicorn from the command line:
```
uvicorn main:app --reload

```
**main**: refers to the main.py file

**app**: the FastAPI instance inside main.py

**reload**: enables auto-reload on code changes (useful in development)

**Open your browser at :**
```
http://127.0.0.1:8000

