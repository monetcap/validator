# Validator

bring up the validator service
`docker-compose up -d`

copy any samples you wish to process into the `./samples` directory
`cp sample.xlsx ./samples`

export your api token
`export API_TOKEN=secretapitoken`

run the analysis of the samples against the stage
`docker-compose exec validator validator --api-token $API_TOKEN --workbook ./samples/sample.xlsx`

check the output directory for the results of your process
`ls -al output`


### Be aware of:
- Downloading Google Sheets as `.xlsx` to process with Validator. You must open
the file within excel and `Ctrl-S`, because for some reason when Validator
extracts the phone numbers from the rows, it appends a `.0` to the string.
  - `ex./ '505-213-3402.0'`. `Ctrl-S` remediates this.
