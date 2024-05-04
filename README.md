Purpose of this repo:
create a boilerplate for a scalable but still compact Flask app.

You can run the app in a few ways:
Docker, pipenv

security
snyk, dependabot
run bandit https://github.com/PyCQA/bandit
run semgrep
add security headers, especially if you don't use cloudflare

and for the love of God, use a linter: pylint

Why factory pattern is here?
To run tests and the app using different environmental variables