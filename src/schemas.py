from pydantic import BaseModel
from typing import List, Dict, Optional

"""
Schemas definition for MCP tools requests and responses
"""
class QueryRequest(BaseModel):
    query: str
    database: str

class QueryResponse(BaseModel):
    success: bool
    query: str
    database: str
    rows: List[Dict[str, str]]

class TableListRequest(BaseModel):
    database: str
class TableListResponse(BaseModel):
    database: str
    tables: Dict[str, str]

class SchemaRequest(BaseModel):
    database: str

class SchemaResponse(BaseModel):
    database: str
    tables: List[str]

class ExportQueryS3Request(BaseModel):
    query: str
    database: str
    bucket: str

class ExportQueryS3Response(BaseModel):
    success: bool
    query: str
    bucket: str
    output_location: str

class S3ListRequest(BaseModel):
    bucket: str
    prefix: Optional[str] = None   

class S3UploadRequest(BaseModel):
    bucket: str
    key: str             
    local_path: str      

class S3DownloadRequest(BaseModel):
    bucket: str
    key: str              
    local_path: str       

class S3DeleteRequest(BaseModel):
    bucket: str
    key: str              

class S3ShareRequest(BaseModel):
    bucket: str
    key: str              
    expiration: int = 3600

class S3ListResponse(BaseModel):
    bucket: str
    objects: List[str]


class S3OperationResponse(BaseModel):
    success: bool
    bucket: str
    object_name: str

class ShareS3Response(BaseModel):
    success: bool
    bucket: str
    object_name: str
    url: str

class RunProcedureRequest(BaseModel):
    database: str
    procedure: str                 
    params: Optional[Dict[str, str]] = None  


class RunProcedureResponse(BaseModel):
    success: bool
    database: str
    procedure: str
    rows: List[Dict[str, str]]

class BulkInsertRequest(BaseModel):
    database: str
    table: str
    file_path: str                 
    file_type: str 

class BulkInsertResponse(BaseModel):
    success: bool
    database: str
    table: str
    inserted_rows: int