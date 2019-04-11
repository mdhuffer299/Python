from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.models import Word2Vec
from pywebhdfs.webhdfs import PyWebHdfsClient
from requests_kerberos import HTTPKerberosAuth
import word_doc_parser as wdp


auth = HTTPKerberosAuth()
prdHdfs = PyWebHdfsClient(host = '',port = '', user_name = '', request_extra_opts={'auth': auth})

prdDir = 'directory/path/'
fileName = 'document.docx'

fileDoc = wdp.get_hdfs_word_doc(prdHdfs, prdDir, fileName)

fileParagraphs = wdp.get_docx_text(fileDoc)

def preprocess_word_doc(data):
    cleaned_data = data.replace("\n", " ")
    
    data_list = []
    
    # Loop through each sentence in the document
    for i in sent_tokenize(cleaned_data):
        temp_list = []
    
        # Tokenize each sentence into words
        for j in word_tokenize(i):
            temp_list.append(j.lower())
    
        # return each tokenized sentence into a list of lists
        data_list.append(temp_list)
    
    return(data_list)



def train_word_vec_model(data, model_type):
    if model_type.upper() == "CBOW":
        model_out = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5)
    elif model_type.upper() == "SKIP GRAM":
        model_out = gensim.models.Word2Vec(data, min_count = 1, size = 100, sg = 5)
    else:
        None
        
    return(model_out)
    
    
    
def avg_sentence_vector(words, model):
    feature_list = []
    
    for word in words:
        try:
            vector_word = model.wv[word]
            feature_list.append(vector_word)
        except:
            vector_word = [float(0)]
            feature_list.append(vector_word)
    
        #vector_weight = sum(feature_list)
    
    return(feature_list)
    

data = preprocess_word_doc(australiaParagraphs)

model_cbow = train_word_vec_model(data, "cbow")
model_sg = train_word_vec_model(data, "skip gram")

feature_vec = avg_sentence_vector(new_data, model_cbow)
