# Cogram coding challenge

### High level notes
There was no time to research the weather provider, so I used python-weather as one of the first results in quick search. 
I picked the lib with sdk, to avoid maintaining contract with the provider.

I have used a small boilerplate I made a while ago, which is perfect for use-cases like this.
(Boilerplates over the internet are bloated with unnecessary stuff, so I made my own). 

I'm using ports-adapters architecture, that is a bit of overkill for project as simple as this, and I'm unable to prove its value with given scope.
However, I picked this architecture because:
1. In this case it does provide some flexibility (i.e. easier mocking of adapters if I'd like to extend project)
2. I'm used to this approach, so I picked approach favorable by "the team" (me)


### Tests
As the project is basically an integration without any business logic I decided to skip units as it would be an overkill. 
I focused on integration tests, which are more valuable in this case. Integration tests cost more, so I tried to be diligent and not test any possible edge case.

## Development setup

Requirements:

-   Docker (and docker-compose)

Requirements (dev):

-   Python 3.12+
-   Poetry

Project is using Makefile to simplify the process. Every shell command starts with `make` prefix and should be run from main project directory.

Installation:

-   `make init` 
- replace params in `.env` with your own values
-   `make build`
-   to set up Python env for IDE to work properly, run `poetry install` from main directory

Running project:

-  `make it_run` 

Running tests:

-   `make test`

## API Documentation

Running project exposes Swagger interface at http://localhost:8008/docs





