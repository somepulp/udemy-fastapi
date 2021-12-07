# Notes

Starting server:
`uvicorn <script_name>:<app_name> --reload`
Note:
`--reload` is to reload the server when any code changes. This should not be active in production since the code shouldn't be changing often!

- sample curl request is in the docs after you click 'try it out': curl -X 'GET' 'http://127.0.0.1:8000/' -H 'accept: application/json'

- order matters! put exact paths before paths which ingest path parameter, so there's no confusion. FastAPI finds the first applicable route. 
