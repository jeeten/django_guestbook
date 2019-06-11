# django_guestbook
 
Login Request: curl -X POST http://127.0.0.1:8000/rest-auth/login/ -H "Content-Type: application/json"  -d '{"username": "admin","email": "","password":"admin@123"}'
Response:
{"key":"069c85669a7c5d5f0c345814a58ee4d3d27accf0"}(venv) dasarathi@dasarathi-Aspire-575

New Post: 
curl -X POST http://127.0.0.1:8000/guest/ -H  "Authorization:Token c21f4de550ae7c12e6ad9298090f00d3b0b157f6" -d "descriptin=hello world&dimage=hi there"

Logout : curl -X POST http://127.0.0.1:8000/rest-auth/logout/
