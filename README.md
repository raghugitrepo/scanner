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
