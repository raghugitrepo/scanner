# scanner

This is a simple Python FastApi framework 

## Local development for macOS
### Environment setup
```bash

brew install pyenv
brew install pipenv
git clone https://github.com/raghugitrepo/scanner.git
cd scanner
pipenv install --dev
pipenv shell
```

### Installing Brakeman 
Prerequisite: Ruby installed 

Brakeman is best installed via RubyGems:
```
 gem install brakeman
 
 export PATH=$HOME/.gem/ruby/<version>/bin:$PATH   
 
 brakeman --version 
```
### Run the API
```bash

uvicorn src.api:app --reload

# Verify that it's running
curl localhost:8000

# Access the swagger UI
open browser and access  localhost:8000/docs
```

### Testing



```bash

cd {Project_path}
export PYTHONPATH="${PYTHONPATH}:${Project_path}"

# Run the unit tests
$ pytest tests/ut.py
# Run the end-to-end tests
$ pytest tests/e2e.py
```

### Building Dockerimage

** NOTE ** Port 80 is exposed in container. where as for local build app runs on 8000 port 

```bash
docker build -t scanner . 

docker run -d -p 80:80 scanner
```

### Run container from docker hub 
```bash
docker pull raghupokuri/scanner:latest

docker run -d -p 80:80 raghupokuri/scanner

```
### Access the api
```bash 
curl localhost:80/docs # swagger api 

### Below are api endpoints 
Method: POST
Endpoint: localhost/scan
Headers: 
application/json

Request Payload: 
{
    "scanner_name": "Brakeman",
    "language": "Ruby",
    "source_code_url": "https://github.com/manojbinjola/ruby-project"
}

Response status code: 200

Response body: 

{
    "report_id": 1663016631,
    "message": "success"
}

Method: Get
Endpoint: localhost/scan/reports/{report_id}
Headers: 
application/json
Response status code: 200
Response body: 

Json report
