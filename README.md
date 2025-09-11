# Data Tools MCP Server

A set of **MCP tools** for working with **AWS Athena, S3, and SQL databases**.  
Provides a unified interface to run queries, manage schemas, and move data across cloud services.

---

##  Objective
The objective of this repository is to expose **data tools** through an MCP server, making it easier to:
- Query AWS Athena securely
- Manage tables, schemas, and exports
- Interact with Amazon S3 (upload, download, share, list, delete)
- Run SQL procedures and perform bulk inserts

---

##  Installation

Clone the repo:

```bash
git clone https://github.com/<your-org-or-user>/data-mcp-toolkit.git
cd data-mcp-toolkit
````

Install requirements:

```bash
pip install -r requirements.txt
```

---

##  Usage

Start the MCP server:

```bash
python server.py
```


---
