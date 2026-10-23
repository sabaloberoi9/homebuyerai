# Homebuyer AI: Intelligent, Parameter-Driven Real Estate Discovery


## The Problem
The modern housing market moves faster than ever, yet buyers are forced to rely on manual, time-consuming research. New homebuyers often spend hundreds of hours filtering through listings, only to miss out on the best deals due to information overload and the limitations of human research. Furthermore, as remote work decentralizes where people can live, traditional zip-code-based searching is no longer sufficient.

## The Solution
Homebuyer AI bridges the gap between complex market data and the everyday buyer. Instead of endlessly scrolling listings, users input their foundational needs: income ranges, credit tiers, and lifestyle parameters. The application then synthesizes this data to identify optimized housing opportunities and strategic locations.

## Ethics and Compliance First
Real estate technology must be built with strict adherence to legal and ethical standards. This application utilizes dedicated prompt constraints to ensure compliance with the Fair Housing Act. The algorithms are designed to provide equitable, parameter-based results based strictly on objective metrics like commute times, affordability, and amenity density, avoiding any demographic discrimination.

## Project Description and Strategic Profiling Flow
Homebuyer AI is an interactive, data-driven single-page web application that converts complex financial and personal profiling into tailored housing recommendations. The platform features an intuitive multi-stage interface that abstracts the complexity of traditional real estate search filters into guided logical steps.

* Welcome and Regulatory Acknowledgement: Ensures users understand the platform parameters and legal guidelines prior to data submission.
* Financial Assessment Engine: Dynamically captures and evaluates financial parameters, profiling user backgrounds against target income ranges and credit tiers.
* Career and Lifestyle Matrix: Collects qualitative metrics including property type preferences, remote work footprints, and critical community priorities.
* Automated Data Refinement: Sanitizes, structures, and processes all parameters locally before routing data to the core AI computational layer.

## Business and Monetization Proposal
To scale this tool sustainably, Homebuyer AI is structured around a freemium SaaS model designed to attract everyday buyers while offering deep value to serious investors.

* Free Tier (The Navigator): Access to the core parameter-driven search engine.
  * Standardized results based on basic income, credit, and location needs.
  * Capped daily searches to manage server compute load.
* Pro Tier (The Investor and Remote Worker): Unlock advanced geographical search for users looking for cost-of-living optimizations nationwide.
  * Deeper financial predictive models and tax rate forecasting.
  * Priority processing and unlimited strategy generations.

## System Architecture

```
[ Client Web Application (Single Page) ]
                   │
                   ▼  HTTP POST (JSON Payload)
      [ AWS Lambda Function URL ]
                   │
    [ Docker Container on Amazon ECR ]
       - Python 3.12 runtime
       - Custom CORS preflight handling
       - Google GenAI SDK integration
                   │
                   ▼
      [ Google Gemini 2.5 Flash ]
       - Affordability heuristics
       - Career commuting and density analysis
       - Community and amenity matching
                   │
                   ▼
       [ Structured Strategy JSON ]
```

## Technical Execution and Engineering Decisions

The application leverages a decoupled Serverless Architecture designed to optimize presentation-layer performance while minimizing backend compute overhead.

### 1. Presentation Layer Architecture (React and Tailwind)
The client-facing application is engineered as a component-driven Single Page Application (SPA).
* Payload Serialization: Before transmitting user analytics to the backend compute layer, client-side logic aggregates raw user variables into a standardized, schema-validated JSON payload.

### 2. Serverless Compute Layer (Python, Docker, AWS Lambda)
The engine behind the platform consists of a containerized FastAPI application executing within AWS Lambda.
* Structural Justification: Why Containerized Lambda over Amazon EC2? Real estate search patterns are highly transactional. Utilizing an Amazon EC2 instance would require continuous capital expenditure for 24/7 server uptime, regardless of actual CPU utilization. AWS Lambda operates on a strict pay-per-execution basis, meaning compute costs scale directly with traffic and drop to absolute zero when idle.

### 3. CI/CD Pipeline and Automated DevOps (GitHub Actions)
Code integration and deployment execution are fully managed via an automated continuous delivery engine.
* Zero-Touch Production Syncing: A GitHub Actions workflow automates container compilation, tags the image, pushes it to Amazon Elastic Container Registry (ECR), and triggers a zero-downtime update of the Lambda function upon every merge to the main branch.

## Active Development and Engineering Roadmap
As an actively developed project, the following features are slated for upcoming development sprints:

| Phase | Milestone | Technical Scope | Status | 
| ----- | ----- | ----- | ----- | 
| Phase 1 | Frontend Authentication Gating | Implement state-driven UI gating with Clerk: guest landing page view versus authenticated 5-stage navigator. | In Progress | 
| Phase 2 | Backend Identity Verification | Decode and validate Clerk JWT claims within the Lambda container; enforce a 1-request-per-day rate limit for public users. | Queued | 
| Phase 3 | Strategy Persistence Layer | Provision an AWS DynamoDB table to persist user profiles and historical strategy runs. | Queued | 
| Phase 4 | Live MLS Property Ingestion | Connect external real estate data APIs (such as RentCast) to supply real-time property listings matching AI-recommended areas. | Queued | 

## Technical Setup and Deployment Verification

### Prerequisites
* Docker Desktop installed and running
* Python 3.11 or higher
* Node.js (for managing local frontend dependencies)

### Local Backend Execution
```bash
# Clone the repository
git clone https://github.com/sabaloberoi9/homebuyerai.git
cd homebuyerai

# Configure environment variables
echo "GEMINI_API_KEY=your_gemini_api_key" > .env

# Build and run the Docker container locally
docker build -t homebuyer-backend .
docker run -p 8000:8000 --env-file .env homebuyer-backend
```

### Frontend Client Execution
1. Navigate to the `frontend` directory (if applicable) or project root.
2. Launch `index.html` using a local web server (e.g., VS Code Live Server at `http://127.0.0.1:5500`).
3. Complete the multi-stage questionnaire to submit payloads to the inference endpoint.

## License
This project is licensed under the MIT License.
