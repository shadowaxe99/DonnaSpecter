```python
import os
from crm_sdk import CRM

# Initialize CRM SDK with API key
crm = CRM(os.getenv('CRM_API_KEY'))

def create_lead(name, email, phone):
    lead = {
        'name': name,
        'email': email,
        'phone': phone
    }
    response = crm.leads.create(lead)
    return response

def update_lead(lead_id, updates):
    response = crm.leads.update(lead_id, updates)
    return response

def delete_lead(lead_id):
    response = crm.leads.delete(lead_id)
    return response

def get_lead(lead_id):
    response = crm.leads.get(lead_id)
    return response

def list_leads():
    response = crm.leads.list()
    return response

def create_deal(name, value, lead_id):
    deal = {
        'name': name,
        'value': value,
        'lead_id': lead_id
    }
    response = crm.deals.create(deal)
    return response

def update_deal(deal_id, updates):
    response = crm.deals.update(deal_id, updates)
    return response

def delete_deal(deal_id):
    response = crm.deals.delete(deal_id)
    return response

def get_deal(deal_id):
    response = crm.deals.get(deal_id)
    return response

def list_deals():
    response = crm.deals.list()
    return response
```