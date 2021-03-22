# Selenium Test Demo with Selenium Grid

This repository demonstrates how to configure selenium with `remote` webdriver in order to run selenium tests in remote browsers such as in selenium grid.

## Selenium Grid

Start and stop selenium grid:

    docker-compose up
    docker-compose down

Navigate to Selenium grid console:

    http://localhost:4444

## Build and run selenium tests

As we run the tests inside a docker container, we cannot simply address the selenium hub with `localhost:4444`, as the docker container by default is running in its own network where `localhost` does not refer to the loopback address network of the host machine. 
There might be a more practical way, but for now I decided to let the selenium test container join the selenium hub network where it can address the selenium hub with its DNS name within its network.

    docker build -t selenium-test .

    docker run --rm --network selenium-grid selenium-test