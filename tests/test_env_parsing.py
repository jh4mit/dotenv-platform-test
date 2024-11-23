import os
from dotenv import dotenv_values, load_dotenv

def test_env_parsing():
    # Simulate a problematic .env file
    content = """AZURE_SQL_SERVER=nonesuch.database.windows.net # comment
AZURE_SQL_DATABASE=nonesuch-database
AZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server # more comments
"""
    # Write to a temporary .env file
    with open("tmp.env", "w") as f:
        f.write(content)

    # Parse the .env file
    parsed = dotenv_values("tmp.env")
    assert parsed["AZURE_SQL_SERVER"] == "nonesuch.database.windows.net"
    assert parsed["AZURE_SQL_DATABASE"] == "nonesuch-database"
    assert parsed["AZURE_SQL_DRIVER"] == "ODBC Driver 18 for SQL Server"



def test_env_parsing_with_load():
    # Use an existing .env file
    load_dotenv()
    assert "AZURE_SQL_SERVER" in os.environ
    assert "AZURE_SQL_DATABASE" in os.environ
    assert "AZURE_SQL_DRIVER" in os.environ
    assert os.environ["AZURE_SQL_SERVER"] == "nonesuch.database.windows.net"
    assert os.environ["AZURE_SQL_DATABASE"] == "nonesuch-database"
    assert os.environ["AZURE_SQL_DRIVER"] == "ODBC Driver 18 for SQL Server"
    assert os.environ["AZURE_CREDENTIAL_SOURCE"] == "cli"