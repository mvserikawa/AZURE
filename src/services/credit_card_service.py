from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import from Config

def analyze_credit_card(card_url):
    
    credential = AzureKeyCredential(Config.KEY)
        
    document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        
    card-info = document_Client.begin_analyze_documento_from_url("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = card_info.result()
        
    for document in result.documents:
        fields = document.get('fields', {})
        
        return {
            "card_name":fields.get('CardHolderName', {}.get('content'))
            "card_number":fields.get('CardNumber', {}.get('content'))
            "expiry_date":fields.get('ExpirationDate', {}.get('content'))
            "bank_name":fields.get('IssuingBank', {}.get('content'))
        }    

