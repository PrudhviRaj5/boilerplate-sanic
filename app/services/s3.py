import boto3
from b2b_app.config import (
    S3_AWS_REGION,
    S3_ACCESS_KEY_ID,
    S3_AWS_SECRET_ACCESS_KEY,
    S3_AWS_END_POINT,
    S3_B2B_APP_BUCKET,
)

class S3:
    def __init__(self, _id):
        self._id = _id
        self._s3_session = boto3.Session(
            aws_access_key_id=S3_ACCESS_KEY_ID,
            aws_secret_access_key=S3_AWS_SECRET_ACCESS_KEY,
        )
        self._s3_region_conn = {}
        self._s3_region_conn[S3_AWS_REGION] = self._s3_session.resource('s3', S3_AWS_REGION)
    
    def get_region_connection(self, region_name):
        if region_name in self._s3_region_conn:
            return self._s3_region_conn[region_name]
        else:
            new_conn = self._s3_session.resource('s3', region_name)
            self._s3_region_conn[region_name] = new_conn
            return new_conn
    
    # In a virtual-hosted–style URL
    # http://bucket.s3-aws-region.amazonaws.com
    # http://bucket.s3.s3-aws-region.amazonaws.com
    @staticmethod
    def get_details_from_virtual_style_url(url):
        url_split = url.split('/')
        end_point = url_split[2] #region and bucket
        file_key = urlsplit[3]
        end_point_split = end_point.split('.')[0]
        bucket = end_point_split[0]
        region = end_point_split[2]
        return {
            'end_point': end_point,
            'file_key': file_key,
            'bucket': bucket,
            'region': region,
        }
    
    # In a path–style URL
    # http://s3-aws-region.amazonaws.com/bucket
    @staticmethod
    def get_details_from_path_style_url(url):
        url_split = url.split('/')
        end_point = url_split[2] #region.
        bucket = url_split[3]
        file_key = urlsplit[4]
        region = end_point.split('.')[0]
        return {
            'end_point': end_point,
            'file_key': file_key,
            'bucket': bucket,
            'region': region,
        }

    def get_file_iterator(self, region, bucket, key):
        s3_obj = self.get_region_connection(region).Object(bucket_name=bucket, key=key)
        body = s3_obj.get()['Body']
        return body._raw_stream
        # for line in body._raw_stream:
        #     print('line', line)
    
    def get_url_for_upload(self, file, path, file_type):
        pass
