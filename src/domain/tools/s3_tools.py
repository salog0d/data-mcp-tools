from typing import List
from src.schemas.s3_schemas import (
    S3ListRequest, S3ListResponse, S3Object, S3UploadRequest, S3OperationResponse,
    S3DownloadRequest, S3DeleteRequest, S3ShareRequest, ShareS3Response,
)
from src.domain.s3_client import S3Client


class S3Tools:
    """Operaciones de conveniencia sobre S3."""

    @staticmethod
    def list_objects(request: S3ListRequest) -> S3ListResponse:
        s3 = S3Client().client
        params = {"Bucket": request.bucket}
        if request.prefix:
            params["Prefix"] = request.prefix
        if request.max_keys:
            params["MaxKeys"] = request.max_keys
        if request.continuation_token:
            params["ContinuationToken"] = request.continuation_token
        if request.start_after:
            params["StartAfter"] = request.start_after

        response = s3.list_objects_v2(**params)
        contents = response.get("Contents", []) or []

        objects: List[S3Object] = [
            S3Object(
                key=obj["Key"],
                size=obj["Size"],
                last_modified=obj["LastModified"].isoformat(),
            )
            for obj in contents
        ]
        return S3ListResponse(bucket=request.bucket, objects=objects)

    @staticmethod
    def upload_object(request: S3UploadRequest) -> S3OperationResponse:
        s3 = S3Client().client
        s3.upload_file(request.local_path, request.bucket, request.object_name)
        return S3OperationResponse(
            success=True,
            bucket=request.bucket,
            object_key=request.object_name,
        )

    @staticmethod
    def download_object(request: S3DownloadRequest) -> S3OperationResponse:
        s3 = S3Client().client
        s3.download_file(request.bucket, request.object_key, request.local_path)
        return S3OperationResponse(
            success=True,
            bucket=request.bucket,
            object_key=request.object_key,
        )

    @staticmethod
    def delete_object(request: S3DeleteRequest) -> S3OperationResponse:
        s3 = S3Client().client
        s3.delete_object(Bucket=request.bucket, Key=request.object_key)
        return S3OperationResponse(
            success=True,
            bucket=request.bucket,
            object_key=request.object_key,
        )

    @staticmethod
    def share_object(request: S3ShareRequest) -> ShareS3Response:
        s3 = S3Client().client
        url = s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": request.bucket, "Key": request.object_key},
            ExpiresIn=request.expiration,
        )
        return ShareS3Response(
            success=True,
            bucket=request.bucket,
            object_key=request.object_key,
            url=url,
        )
