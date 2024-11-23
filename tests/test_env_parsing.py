from dotenv import dotenv_values

def test_env_parsing():
    # Simulate a problematic .env file
    content = """AZURE_SQL_SERVER=nonesuch.database.windows.net # comment
AZURE_SQL_DATABASE=nonesuch-database
AZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server # more comments
"""
    # Write to a temporary .env file
    with open(".env", "w") as f:
        f.write(content)

    # Parse the .env file
    parsed = dotenv_values(".env")
    assert parsed["AZURE_SQL_SERVER"] == "nonesuch.database.windows.net"
    assert parsed["AZURE_SQL_DATABASE"] == "nonesuch-database"
    assert parsed["AZURE_SQL_DRIVER"] == "ODBC Driver 18 for SQL Server"
