# Natural Language Ocean Data Agent

## The Core Idea

Large-scale scientific datasets are fundamentally inaccessible to most. They require specialized tools and expertise to even ask a simple question. This project changes that.

It uses a large language model to create a **natural language interface** for complex oceanographic data. The system ingests raw scientific files (NetCDF, CSV), structures them into a queryable database, and deploys an agent that translates human questions into precise SQL. It's a direct pipeline from intent to execution, making vast data explorable through simple conversation.

## System Capabilities

* **Query with Language, Not Code:** The interface is natural language.
* **Handles Complex Formats:** Ingests and normalizes both NetCDF and CSV data.
* **Finds Signal in the Noise:** The agent intelligently locates the **nearest data point**, not just exact matches. This is crucial for working with gridded scientific data.
* **Local and Private:** Runs entirely on-device with Ollama. Your data and queries are never sent to the cloud.
* **Resilient by Design:** Built with LangGraph, the agent can reason, self-correct after errors, and rewrite its own queries to improve accuracy.

## How It Works

The process is two-fold: structuring and querying.

**Structuring:** A setup script reads the raw data file (`.nc` or `.csv`). It flattens the multi-dimensional data into a simple, two-dimensional SQL table and stores it in a local SQLite database. This one-time process makes the data computationally accessible.

**Querying:** When a question is posed, the agent executes a reasoning workflow:
1.  It first determines if the question is answerable given the database schema.
2.  It then translates the question into a SQL query, intelligently forming a nearest-point search.
3.  The query is executed. If it fails, the agent rewrites it and retries.
4.  Finally, the raw SQL result is translated back into a concise, human-readable sentence.

## Project Files
```bash
/
├── sql_csv.ipynb           # Main notebook for querying the CSV-based database.
├── sql_nc.ipynb            # Main notebook for querying the NetCDF-based database.
|
├── setup_csv_db.py         # Script to create the database from ocean_data.csv.
├── setup_db.py             # Script to create the database from the .nc file.
├── db_schema.py            # Connects the agent to the database file.
|
├── ocean_data.csv          # Raw data in CSV format.
├── *.nc                    # Raw data in NetCDF format.
|
└── ocean_csv_database.db   # The final SQLite database (created by setup scripts).