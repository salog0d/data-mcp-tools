from mcp.server.fastmcp import FastMCP
from schemas import (QueryResponse, QueryRequest,
                     TableListRequest, TableListResponse, 
                     SchemaRequest, SchemaResponse, 
                     ExportQueryS3Request, ExportQueryS3Response,
                     S3ListRequest, S3ListResponse,
                     S3UploadRequest, S3DownloadRequest,
                     S3DeleteRequest, S3OperationResponse,
                     S3ShareRequest, ShareS3Response,
                     RunProcedureRequest, RunProcedureResponse,
                     BulkInsertRequest, BulkInsertResponse)

mcp = FastMCP("AWS Athena Tools")

"""
Athena tools
"""

@mcp.tool(name="Query Athena", description="Run safe queries using AWS Athena service")
def query_athena(request: QueryRequest) -> QueryResponse:
    pass

@mcp.tool(name="List Tables", description="List tables living in athena service")
def list_tables(request: TableListRequest) -> TableListResponse:
    pass

@mcp.tool(name="Get Schema", description="Gets the schema for an specific table")
def get_schema(request: SchemaRequest) -> SchemaResponse:
    pass

@mcp.tool(name="Export Query to S3", description="Exports query runs to a csv file in an S3 bucket")
def export_query_s3(request: ExportQueryS3Request) -> ExportQueryS3Response:
    pass


"""
S3 tools
"""

@mcp.tool(name= "List Objects", description= "List objects stored in an S3 instance")
def list_objects(request: S3ListRequest) -> S3ListResponse:
    pass

@mcp.tool(name= "Upload to S3", description= "Upload object to S3 instance")
def upload_object_s3(request: S3UploadRequest) -> S3OperationResponse:
    pass

@mcp.tool(name= "Download from S3", description="Download object from S3 instance")
def download_object_s3(request: S3DownloadRequest) -> S3OperationResponse:
    pass

@mcp.tool(name= "Delete from S3", description="Delete object from S3 instance")
def delete_object_s3(request: S3DeleteRequest) -> S3OperationResponse:
    pass

@mcp.tool(name= "Share S3 object", description="Share an S3 object through a temporal url")
def share_object_s3(request: S3ShareRequest) -> ShareS3Response:
    pass


"""
SQL tools
"""


@mcp.tool(name="Query SQL", description="Run safe queries using native sql connection")
def query_sql(request: QueryRequest) -> QueryResponse:
    pass

@mcp.tool(name="List Tables", description="List tables living in sql service")
def list_sql_tables(request: TableListRequest) -> TableListResponse:
    pass

@mcp.tool(name="Run Procedure", description="Run sql procedures")
def run_sql_procedures(request: RunProcedureRequest) -> RunProcedureResponse:
    pass

@mcp.tool(name="Insert Bulk", description="Insert bulk information")
def bulk_sql_insert(request: BulkInsertRequest) -> BulkInsertResponse:
    pass
