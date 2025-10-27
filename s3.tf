resource "aws_s3_bucket" "my_bucket" {
  bucket = "lab6-pranit1617" 
}

resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration { status = "Enabled" }
}
