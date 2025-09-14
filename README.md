# AI Trip Planner

A project to build an AI-powered travel planning application using Python, LangChain, and HuggingFace.

## Getting Started

Follow these steps to set up your development environment and run the application.

### Prerequisites

- Python 3.11.13 (recommended)
- [uv](https://github.com/astral-sh/uv) package manager
- [pip](https://pip.pypa.io/en/stable/)
- [Streamlit](https://streamlit.io/)
- [Uvicorn](https://www.uvicorn.org/)

### Installation

1. **Check if `uv` is installed:**
    ```bash
    uv --version
    ```

2. **Check if `uv` is available in your PATH:**
    ```python
    import shutil
    print(shutil.which("uv"))
    ```

3. **Install `uv` (if not already installed):**
    ```bash
    pip install uv
    ```

4. **Initialize your project:**
    ```bash
    uv init AI_Travel_Planner
    ```

5. **List installed packages:**
    ```bash
    uv pip list
    ```

6. **List available Python versions:**
    ```bash
    uv python list
    ```

7. **Install Python 3.11.13 (if needed):**
    ```bash
    uv python install ypy-3.11.13-windows-x86_64-none
    ```

8. **List Python versions again to confirm installation:**
    ```bash
    uv python list
    ```

9. **Create a virtual environment:**
    ```bash
    uv venv env --python cpython-3.11.13-windows-x86_64-none
    ```

10. **Add required packages (example: pandas):**
    ```bash
    uv add pandas
    ```

11. **If using conda, deactivate it first:**
    ```bash
    conda deactivate
    ```

12. **Activate your virtual environment:**
    ```bash
    working_directory_path\AI_Trip_Planner\env\Scripts\activate.bat
    ```

### Running the Application

- **To start the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```

- **To run the FastAPI app with Uvicorn:**
    ```bash
    uvicorn main:app --reload --port 8000
    ```

---

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please open an issue on this repository.