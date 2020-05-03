## NCTU+ refactor API server

### built with **Flask**
- config of flask and database 
    -  `cp app/configmodule_sample.py app/configmodule.py`
        - replace the upper case string in configmodule_sample.py
- config of nctu oauth
    - `cp app/auth/config_sample.py app/auth/config.py`
        - fill the empty strings
- `export FLASK_APP=run.py`
- `flask run`

### Ref
- [API doc](https://hackmd.io/@5UsPoUEPTv2sD6aUW99oRA/SyyjcMif4/%2Fs%2FrkSEZBFNZ?type=book)
