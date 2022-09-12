# scanner

This is a simple fast api framework 

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
# Run the unit tests
$ pytest tests/ut.py
# Run the end-to-end tests
$ pytest tests/e2e.py
```

### Building Dockerimage

** NOTE **


I have m1 mac so the platform the image built is  --platform=linux/arm64/v8 (This is tested as working)

If you have amd64 arch change  --platform=linux/amd64 in Dockerfile. (This is not tested since I dont have machine)

```bash
docker build -t scanner . 

docker run -d -p 80:80 scanner
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
