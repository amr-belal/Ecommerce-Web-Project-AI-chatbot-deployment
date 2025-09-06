# import yake 
from math import ulp
from controllers.ObjectUserDataCont import ObjectUserData 
# from pydantic import BaseModel
import yake
import spacy
# from keybert import KeyBERT
# from rake_nltk import Rake


class KeywordExtractor :
    def __init__(self , extractor_name = "yake"):
        self.extractor_name = extractor_name
        
        
    def yake_keywords(self , text :str):
        # text  = user_data.message
        kw_extractor = yake.KeywordExtractor(lang = "en" , n = 2 ,top = 5)
        return [kw for kw, score in kw_extractor.extract_keywords(text)]
        
    # def spacy_extractor(self ,text , top_n ):
    #     doc = nlp(text)
    #     chunks = [chunk.text for chunk in doc.noun_chunks]
    #     return chunks[:top_n]
        
        
        
class Factory_Extractor :
    @staticmethod
    def create (extractor_name :str):
        if  extractor_name == "yake":
            return KeywordExtractor(extractor_name)
        else:
            raise ValueError(f"Invalid model type: {extractor_name}")