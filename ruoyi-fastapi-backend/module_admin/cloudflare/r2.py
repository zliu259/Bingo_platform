import boto3
from botocore.config import Config

# 令牌值 【令牌名称root_token】
token = 'zkjIlc9Xnfvu4jdn_O_wpL3UDVJfmcxas7wRWbd7'
# 你的 Cloudflare R2 访问密钥和秘密密钥
# 访问密钥 ID
access_key = '89b0a532d7afa715eb5122fb2f2f6901'
# 机密访问密钥
secret_key = '3e7f1ff7fc1bf1739149125ee466a10d3aa7f60db71ad2a599c18c44863516cd'
# 存储桶的 URL
url = 'https://78939a17148c390144ef58e10a619393.r2.cloudflarestorage.com'

# 创建一个 S3 客户端，这里指定了 R2 的端点
config = Config(signature_version='s3v4')
s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=url,
    config=config
)
# 你要上传到存储桶的名字
bucket_name = 'bingo'
# 本地文件 文件名
file_path = r'C:\Users\liuzi\PycharmProjects\Bingo_platform\ruoyi-fastapi-backend\vf_admin\upload_path\upload\Screenshot 2024-12-16 at 23.25.24_20250107120156A360.png'
# 存储桶里的路径和文件名 此处可以重新命名上传后的文件名称，也可以添加文件夹
bucket_file_name = 'Screenshot 2024-12-16 at 23.25.24_20250107120156A360.png'
# 使用 S3 客户端上传文件
s3_client.upload_file(file_path, bucket_name, bucket_file_name)