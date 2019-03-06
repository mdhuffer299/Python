from pywebhdfs.webhdfs import PyWebHdfsClient
from requests_kerberos import HTTPKerberosAuth

# Create Client connection to Kerberos Hadoop Cluster
auth = HTTPKerberosAuth()
devHdfs = PyWebHdfsClient(host = 'devHost',port = 'portNumber', user_name = 'userName', request_extra_opts={'auth': auth})
prdHdfs = PyWebHdfsClient(host = 'prodHost',port = 'portNumber', user_name = 'userName', request_extra_opts={'auth': auth})

userDir = '/user/path'
userFileName = 'DemoFile1'
print(devHdfs.read_file(userDir + userFileName))


prdDir = '/projects/'
prdFileName = 'fileName.txt'
print(prdHdfs.read_file(prdDir + prdFileName))
