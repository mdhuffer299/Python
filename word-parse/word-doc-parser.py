from pywebhdfs.webhdfs import PyWebHdfsClient
from requests_kerberos import HTTPKerberosAuth
import io
import zipfile
from xml.etree.cElementTree import XML

auth = HTTPKerberosAuth()

prdHdfs = PyWebHdfsClient(host = 'HDFS Host',port = '50070', user_name = 'User Name', request_extra_opts={'auth': auth})

prdDir = '/fileDir/'
prdFileName = 'fileName'

def get_hdfs_word_doc(hdfsClientVar, directory, fileName):
    file = hdfsClientVar.read_file(directory + fileName)
    byteFile = io.BytesIO(file)
    
    return(byteFile)

def get_docx_text(fileName):
    zipFile = zipfile.ZipFile(fileName)

    WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    PARA = WORD_NAMESPACE + 'p'
    TEXT = WORD_NAMESPACE + 't'
    
    name = 'word/document.xml'
    document = zipFile.read(name, pwd = None)
    documentTree = XML(document)

    paragraphs = []
    for paragraph in documentTree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    return('\n\n'.join(paragraphs))

hdfsPcoeFile = get_hdfs_word_doc(devHdfs, projectDir, projectFileName)

pcoeParagraphs = get_docx_text(hdfsPcoeFile)
