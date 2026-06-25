from langchain_community.document_loaders import PyPDFLoader

def document_loader(path):
        loader = PyPDFLoader(path)
        return loader.load()
    
if __name__=="__main__":
    documents = document_loader("comprehensive-clinical-nephrology.pdf")


