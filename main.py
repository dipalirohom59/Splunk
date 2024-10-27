# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import requests

# app = FastAPI()

# SPLUNK_URL = 'http://127.0.0.1:8089'
# SPLUNK_TOKEN = '7797501eccac236deb10831cd8bb5a2c09a7e0a6ec4e7bc6855aa000818c7d63'


# class SearchQuery(BaseModel):
#     query: str

# @app.post("/api/real-time-logs")
# async def get_real_time_logs(query: SearchQuery):
#     response = requests.post(
#         f'{SPLUNK_URL}/services/search/jobs',
#         headers={
#             'Authorization': f'Bearer {SPLUNK_TOKEN}',
#             'Content-Type': 'application/x-www-form-urlencoded'
#         },
#         data={'search': query.query}
#     )

#     if response.status_code == 200:
#         job_id = response.json().get('sid')
#         return await get_search_results(job_id)
#     else:
#         raise HTTPException(status_code=response.status_code, detail=response.text)

# async def get_search_results(job_id: str):
#     while True:
#         response = requests.get(
#             f'{SPLUNK_URL}/services/search/jobs/{job_id}/results?output_mode=json',
#             headers={'Authorization': f'Bearer {SPLUNK_TOKEN}'}
#         )
#         if response.status_code == 200:
#             results = response.json()
#             if results.get('results'):
#                 return results
#         else:
#             raise HTTPException(status_code=response.status_code, detail=response.text)
