# Contributing to Sentinel Orchestra

## Code of Conduct
We abide by the Contributor Covenant 2.1

## Project Structure

├── src
│   ├── sensors
│   ├── agents
│   ├── protocols
│   └── infrastructure
├── docs
│   ├── rfc
│   └── design
├── benchmarks
├── tests
│   ├── unit
│   └── integration
└── examples


## Development Workflow
1. `make setup` - Install dependencies
2. `make test` - Run test suite
3. `make lint` - Type checking + formatting

## Architecture Proposals
All major architecture decisions require RFC approval. Submit to:
- docs/rfc/proposals/

## Reporting Security Issues
Send confidential reports to: security@sentinelorchestra.com

## License
All contributions must be Apache 2.0 licensed