import subprocess

packages = [
    "annotated-types==0.7.0",
    "anyio==4.4.0",
    "appnope==0.1.4",
    "asttokens==2.4.1",
    "certifi==2024.6.2",
    "click==8.1.7",
    "comm==0.2.2",
    "debugpy==1.8.1",
    "decorator==5.1.1",
    "dnspython==2.6.1",
    "email_validator==2.2.0",
    "et-xmlfile==1.1.0",
    "executing==2.0.1",
    "fastapi==0.111.0",
    "fastapi-cli==0.0.4",
    "fastavro==1.9.4",
    "h11==0.14.0",
    "httpcore==1.0.5",
    "httptools==0.6.1",
    "httpx==0.27.0",
    "idna==3.7",
    "ipykernel==6.29.4",
    "ipython==8.25.0",
    "jedi==0.19.1",
    "Jinja2==3.1.4",
    "jupyter_client==8.6.2",
    "jupyter_core==5.7.2",
    "markdown-it-py==2.2.0",
    "MarkupSafe==2.1.5",
    "matplotlib-inline==0.1.7",
    "mdurl==0.1.2",
    "nest-asyncio==1.6.0",
    "numpy==2.0.0",
    "openpyxl==3.1.4",
    "orjson==3.10.5",
    "packaging==23.0",
    "pandas==2.2.2",
    "parso==0.8.4",
    "pexpect==4.9.0",
    "platformdirs==4.2.2",
    "prompt_toolkit==3.0.47",
    "psutil==6.0.0",
    "psycopg2-binary==2.9.6",
    "ptyprocess==0.7.0",
    "pure-eval==0.2.2",
    "pydantic==2.7.4",
    "pydantic_core==2.18.4",
    "Pygments==2.18.0",
    "python-dateutil==2.9.0.post0",
    "python-dotenv==1.0.1",
    "python-multipart==0.0.9",
    "pytz==2024.1",
    "PyYAML==6.0.1",
    "pyzmq==26.0.3",
    "rich==13.7.1",
    "shellingham==1.5.4",
    "six==1.16.0",
    "sniffio==1.3.1",
    "SQLAlchemy==2.0.31",
    "stack-data==0.6.3",
    "starlette==0.37.2",
    "tornado==6.4.1",
    "traitlets==5.14.3",
    "typer==0.12.3",
    "typing_extensions==4.12.2",
    "tzdata==2024.1",
    "ujson==5.10.0",
    "uvicorn==0.30.1",
    "watchfiles==0.22.0",
    "wcwidth==0.2.13",
    "websockets==12.0"
]

for package in packages:
    subprocess.run(["pip", "install", package])
