# Homebuyer AI
**Intelligent, Parameter-Driven Real Estate Discovery**

[Live Demo](https://sabaloberoi9.github.io/homebuyerai/) | [Report an Issue](https://github.com/sabaloberoi9/homebuyerai/issues)

## The Problem
The modern housing market moves faster than ever, yet buyers are forced to rely on manual, time-consuming research. New homebuyers often spend hundreds of hours filtering through listings, only to miss out on the best deals due to information overload and the limitations of human research. Furthermore, as remote work decentralizes where people can live, traditional zip-code-based searching is no longer sufficient.

## The Solution
Homebuyer AI bridges the gap between complex market data and the everyday buyer. Instead of doom-scrolling listings, users input their foundational needs—income ranges, credit tiers, and lifestyle parameters—and the application searches the web to identify optimized housing opportunities. 

### Ethics & Compliance First
Real estate technology must be built with strict adherence to legal and ethical standards. This application has dedicated legal checks implemented to ensure strict compliance with the Fair Housing Act. The algorithms are designed to provide equitable, parameter-based results without discrimination.

---

## Project Description & Core Features
Homebuyer AI is an interactive, data-driven single-page web application that converts complex financial and personal profiling into tailored housing recommendations. The platform features an intuitive multi-stage interface that abstracts the complexity of traditional real estate search filters into guided logical steps.

### Strategic Profiling Flow
* **Welcome & Regulatory Acknowledgement:** Ensures users understand the platform parameters and legal guidelines prior to data submission.
* **Financial Assessment Engine:** Dynamically captures and evaluates financial parameters, profiling user backgrounds against target income ranges and credit tiers.
* **Lifestyle & Preference Matrix:** Collects qualitative metrics including property type preferences, target bedroom/bathroom configurations, and critical community priorities.
* **Automated Data Refinement:** Sanitizes, structures, and processes all parameters locally before routing data to the core computational layer to produce optimized matching results.

---

## Business & Monetization Proposal
To scale this tool sustainably, Homebuyer AI is structured around a freemium SaaS model designed to attract everyday buyers while offering deep value to serious investors.

* **Free Tier (The Navigator):** * Access to the core parameter-driven search engine.
  * Standardized results based on basic income, credit, and location needs.
  * Capped daily searches to manage server load.
* **Pro Tier (The Investor / Remote Worker):** * Unlock advanced geographical search for remote workers looking for the best cost-of-living optimizations nationwide.
  * Deeper financial predictive models (tax rate forecasting, HOA trend analysis).
  * Priority processing and automated email alerts for market drops.

---

## Technical Architecture & Execution

The application leverages a decoupled, event-driven Serverless Microservices Architecture designed to optimize presentation-layer performance while minimizing backend compute overhead and infrastructure costs. By strictly isolating static client delivery from dynamic backend script execution, the system achieves massive horizontal scaling capabilities with a structural baseline cost of absolute zero when idle.

### 1. Presentation Layer Architecture (React.js & GitHub Pages)

The client-facing application is engineered as a component-driven Single Page Application (SPA) leveraging React.js for state tracking and UI rendering. 

* **Deterministic State Machine Control:** Rather than relying on loosely coupled, scattered state hooks, user navigation through the multi-stage profiling wizard is strictly governed by a centralized deterministic state machine. This prevents runtime state corruption, ensures immutable data propagation down the component hierarchy, and isolates view re-renders to explicit parameter changes.
* **Payload Serialization and Minification:** Before transmitting user analytics to the backend compute layer, client-side serialization logic aggregates raw user variables. The engine sanitizes and compresses this data into a standardized, schema-validated JSON payload, drastically shrinking the HTTP request overhead.
* **Global CDN Edge Hosting:** The compiled static bundle is deployed directly onto GitHub Pages infrastructure. By bypassing traditional origin-server web hosting, static assets are cached and served globally via edge-delivery nodes, dropping network latency to sub-second metrics.

### 2. Serverless Compute Layer (Python & AWS Lambda)

The engine behind the platform consists of modular, highly specialized Python scripts (`main.py`, `local_scan.py`, `local_cyber_test.py`) that handle data orchestration, validation, and automated network auditing tasks.

* **Structural Justification: Why Lambda over Amazon EC2?**
  * Real estate search patterns are highly transactional and "bursty" by nature. Utilizing an Amazon EC2 instance would require continuous capital expenditure for 24/7 server uptime, regardless of actual CPU utilization. AWS Lambda operates on a strict pay-per-execution basis, meaning compute costs scale directly with traffic and drop to absolute zero when idle.
  * EC2 instances introduce significant operational complexity, including OS patching and load balancing. AWS Lambda abstracts the host operating system entirely, executing code in micro-containers that initialize instantly.
* **Structural Justification: Why Lambda over Amazon S3?**
  * While Amazon S3 is highly effective for object storage, it is fundamentally a passive storage mechanism lacking a runtime engine. AWS Lambda provides the dynamic runtime container required to parse data streams, enforce backend computational rules, and run multi-threaded scripts.

### 3. CI/CD Pipeline and Automated DevOps (GitHub Actions)

Code integration and deployment execution are fully managed via an automated continuous delivery engine configured inside the project root (`.github/workflows/static.yml`).

* **Workspace Cleanliness and Tree Optimization:** During initial builds, local virtual environments (`venv/`) and compiler distribution folders (`dist/`) generated massive binary logs, causing deployment jobs to fail due to memory limits.
* **Automated Isolation Matrix:** The deployment workflow solves this by initiating an isolated container runner on every push. The script strips out unneeded backend dependencies via aggressive target tracking and configures a `.nojekyll` bypass to prevent the static engine from breaking down during asset compilation.
* **Zero-Touch Production Syncing:** Once validation clears, the pipeline compresses the streamlined frontend footprint and publishes it to production, reducing deployment times to a flawless 5-second cloud sync.

### 4. Known Limitations & Future Roadmap
This is a V1 production release. As a solo-engineered project, the following limitations have been identified and are slated for the next development sprint:

* **Rate Limiting & Anti-Spam:** The application currently lacks a robust Web Application Firewall (WAF) or rate-limiting system. Malicious actors could potentially spam the AWS API endpoints. Future updates will include AWS API Gateway rate limiting and CAPTCHA integration to prevent DDoS vulnerabilities and link abuse.
* **Database Integration:** Transitioning user state from local storage to a secure, encrypted cloud database (Amazon DynamoDB) for cross-device session management and saved searches.
### 5. Technical Setup & Deployment Verification

**Local Development Environment Isolation**
```bash
# Clone the clean repository blueprint
git clone [https://github.com/sabaloberoi9/homebuyerai.git](https://github.com/sabaloberoi9/homebuyerai.git)
cd homebuyerai

# Instantiate an isolated local virtual environment
python3 -m venv venv
source venv/bin/activate

# Verify workspace configuration
python3 main.py
