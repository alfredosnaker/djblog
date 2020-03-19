#717be3bee99fc6db1b9fae41ac987ecc

import requests

url = "https://api2.online-convert.com/jobs"

payload = "{\"input\":[{\"type\":\"remote\",\"source\":\"https://static.online-convert.com/example-file/raster%20image/jpg/example_small.jpg\"}],\"conversion\":[{\"category\":\"image\",\"target\":\"png\"}]}"
headers = {
    'x-oc-api-key': "8d964d1e1977cbff13e3baf379c108b9",
    'content-type': "application/json",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

response.request

{"id":"78dbcf48-5059-4b2b-b13b-d11ba6cf767c","token":"268ef40b3c28fa6c1700c7e20416340d","type":"job","status":{"code":"downloading","info":"The file is currently downloading from the source URL."},"errors":[],"warnings":[],"process":true,"fail_on_input_error":true,"fail_on_conversion_error":true,"conversion":[{"id":"f0378eb7-b5da-4880-bdd6-87f9c6c1b2c6","target":"png","category":"image","options":{"download_password":null,"allow_multiple_outputs":false,"preset":null,"dpi":null,"width":null,"height":null,"crop_top":null,"crop_bottom":null,"crop_left":null,"crop_right":null,"crop_origin_x":null,"crop_origin_y":null,"crop_width":null,"crop_height":null,"color":"colored","enhance":null,"normalize":null,"sharpen":null,"antialias":null,"despeckle":null,"equalize":null,"deskew":null,"quality":null,"rotate":null,"alpha_channel":null,"resolution_unit":"inches"},"metadata":{},"output_target":[]}],"input":[{"id":"f8214127-a45d-4815-b8d6-33b9ae416c3f","type":"remote","status":"downloading","source":"https:\/\/static.online-convert.com\/example-file\/raster%20image\/jpg\/example_small.jpg","filename":"","size":0,"hash":"","checksum":"","content_type":"","created_at":"2020-03-07T18:54:09","modified_at":"2020-03-07T18:54:09","credentials":[],"parameters":[],"metadata":{}}],"output":[],"callback":"","notify_status":false,"server":"https:\/\/www53.online-convert.com\/dl\/web1","spent":0,"created_at":"2020-03-07T18:54:09","modified_at":"2020-03-07T18:54:09"}