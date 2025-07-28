# Development Plan for llm
## Architecture
1. Load raw data from [Kengxxiao/ArknightsGameData_YoStar](https://github.com/Kengxxiao/ArknightsGameData_YoStar).
2. Convert and save the data into mongodb.
3. Expose those resource as resource.
4. Make and expose tools for more specific use-case.
5. make and expose prompts for examples.

### Data Management
#### Prod Environment
Use pre-fetched repository clone if there is no recent commit of the github repo.  
If there is, pull from repo.

#### Dev Environment
Use pre-fetched repository clone as data source

### Stacks
- python
- fastmcp
- mongodb
- gitpython