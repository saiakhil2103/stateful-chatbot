import os
import sys
import streamlit.web.cli as stcli

if __name__ == "__main__":
    # 📁 Ensure the project root is in the Python path
    sys.path.insert(0, os.path.dirname(__file__))
    
    # 🏃 Programmatically point Streamlit to our app file
    sys.argv = ["streamlit", "run", "src/app.py"]
    sys.exit(stcli.main())