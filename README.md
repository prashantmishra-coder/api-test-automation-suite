# API Test Automation Suite

Request/response and status-code validation suite for a public REST API,
built with **Postman** (collection + assertions) and **Python (requests
+ pytest)**, runnable locally or via **Newman** in a CI pipeline.

## Why this project

Manually re-running Postman collections before every release doesn't
scale. This suite automates that validation two ways: a Postman
collection for per-request checks (status code, response shape,
response time), and a Python/pytest suite for chained, multi-step
validation (create → verify → update → delete) that's easier to express
in code than in Postman's per-request test scripts.

## Tech Stack
- Postman (collection + JavaScript test assertions)
- Newman (CLI runner for CI integration)
- Python 3.10+, requests, pytest, pytest-html
- GitHub Actions (CI pipeline)

## Project Structure
