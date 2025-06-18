# Caso-3-Diseno-de-Software

Members: Pablo Mesén, Alonso Durán Muñoz, Ana Hernández Muñoz, Jesus Valverde



# INDEX
- [DESCRIPTION](#DESCRIPTION)
- [STRATEGY AND PLANNING](#STRATEGY-AND-PLANNING)
- [DEFINITION OF REQUIREMENTS](#DEFINITION-OF-REQUIREMENTS)
- [SYSTEM ANALYSIS](#SYSTEM-ANALYSIS)
- [LEGAL AND REGULATORY FRAMEWORK](#LEGAL-AND-REGULATORY-FRAMEWORK)
- [STACK](#STACK)
- [FRONTEND](#FRONTEND)
	-[AUTHENTICATION PLATFORM](#Authentication-platform)
	-[POC MFA](#POC-MFA)
- [BACKEND](#BACKEND)
	- [API ENDPOINTS](#API-Endpoints)
   	- [IMPORTANT CLASSES & COMPONENTS](#Important-Classes-&-Components)
   	- [ERROR HANDLING](#Error-Handling)
   	- [SECURITY LAYER DESIGN](#Security-Layer-Design)
   	- [AUDIT & LOGGING](#Audit-&-Logging)
   	- [THIRDPARTY SERVICES](#THIRDPARTY-SERVICES)
   	- [KEY WORKFLOWs](#Key-Workflows)
   	- [DATA LAYER DESIGN](#Data-Layer-Design)


# DESCRIPTION
For years, Costa Rica has faced a significant structural limitation: the absence of a centralized data system that facilitates access, analysis, and utilization of information by various actors. Currently, there is no national ecosystem that allows individuals, public institutions, state branches, social organizations, and the private sector to share, reuse, and market information in a structured manner. This fragmentation has hindered evidence-based decision-making, slowed institutional processes, and limited the development of innovative solutions that could emerge from the strategic use of data.

In response to this challenge, the creation of a national ecosystem of interoperable, secure, and regulated data is proposed, in which both public and private entities can contribute and utilize valuable information. This system would allow data to be classified according to its nature: open or restricted access, free or subject to a fee-based model. Robust security and privacy standards would be established to ensure the protection of sensitive information and regulatory compliance. The goal is to enable an environment in which reliable data can be used to generate new applications, technological products, and services based on data science and artificial intelligence.

With the implementation of this ecosystem, Costa Rica could take a leap toward an economy and government driven by real data. Institutions would optimize their processes, the private sector would find new opportunities for innovation and collaboration, and citizens would have access to useful and transparent information. Furthermore, the coexistence of public and private data, managed under clear and secure frameworks, would open up a dynamic space for technological development and the country's sustainable digital transformation.

# STRATEGY AND PLANNING
## Roadmap
![Agile Product Roadmap](https://github.com/user-attachments/assets/290593af-6321-4e67-8d2a-53b4e363d946)

## Milestones
- M1: Validated architecture

- M2: Core technical infrastructure deployed (data lake, backend, encryption)

- M3: Secure user registration system with advanced validation and IP control

- M4: First datasets published with granular control, metadata, and pricing

- M5: AI-powered, non-downloadable data exploration dashboards operational

- M6: Ecosystem validated through security audits and regulatory compliance

- M7: 10+ integrated institutions, 100+ active datasets, first monetization revenue

## Technical Team

| **Role**                  | **Quantity** | **Responsibilities**                                                       |
|---------------------------|--------------|-----------------------------------------------------------------------------|
| Cloud Solutions Architect | 1            | Designs cloud infrastructure, security, scalability                        |
| DevOps Engineers          | 2            | Deployment automation, CI/CD, versioning                                   |
| Backend Developers        | 3            | API development, encryption, access control, authentication                |
| Frontend Developers       | 2            | User portals (registration, dashboards, admin interface)                   |
| Security Specialists      | 2            | Key management, MFA, audits, legal compliance                              |
| AI & ETDL Specialists     | 2            | Document validation, data flow automation, AI dashboards                   |
| Data Engineers            | 2            | Modeling, metadata, data quality                                           |
| Product Manager           | 1            | Agile delivery coordination, documentation                                 |
| UI/UX Designer            | 1            | Portal and backoffice interface design                                     |
| Legal & Compliance Advisor| 1            | Legal analysis, data protection, IP/data ownership                         |
## UX Journeys
![UX Journey 1](https://github.com/user-attachments/assets/51a549f9-286c-4e5f-b118-af91c3e0b110)
![UX Journey 2](https://github.com/user-attachments/assets/09dd118f-dcd9-4822-b251-ae6915d54a82)
![UX Journey 3](https://github.com/user-attachments/assets/b1a67421-d2fb-4313-828a-e91145229388)
##  Risks Assesment 
| ID  | Risk Description                                                              | Likelihood | Impact   | Risk Level | Control/Mitigation Measures                                                    | Owner                |
|-----|----------------------------------------------------------------------------------|------------|----------|------------|----------------------------------------------------------------------------------|----------------------|
| R1  | Failure in biometric identity validation due to poor image/document quality     | Medium     | High     | **High**   | Implement quality filters, retry mechanism, and fallback to manual validation   | DevOps / Identity    |
| R2  | Unauthorized access due to improper IP restriction configuration                | Low        | High     | **Medium** | Enforce IP whitelist checks, automate validation tests on deploy                | Security Team        |
| R3  | Data breach of confidential datasets marked as “restricted”                     | Low        | Critical | **High**   | Encrypt at rest with AWS KMS, enable row-level access policies in Snowflake     | Security / Infra     |
| R4  | Misuse of uploaded datasets due to incorrect permissioning                      | Medium     | High     | **High**   | Create permission configuration wizard with preview and rollback                | Data Engineering     |
| R5  | System downtime during batch ingestion or data validation                       | Medium     | Medium   | **Medium** | Queue-based ingestion (SQS), retry logic, alerting via EventBridge              | Platform Ops         |
| R6  | Reputational damage due to publication of inaccurate or unverified data         | Medium     | High     | **High**   | Enforce ML validation and mandatory manual QA for public datasets               | Data Governance      |
| R7  | Frustration due to poor UX in uploading or dashboarding tools                   | High       | Medium   | **Medium** | Add progress indicators, previews, guided steps and clear errors                | UX / Frontend Team   |
| R8  | Breach of user personal data from onboarding                                    | Low        | Critical | **High**   | Encrypted transmission, audit logs, token masking, PII redaction                | Infra / Security     |
| R9  | Regulatory non-compliance                                                       | Low        | Critical | **High**   | Regular audits, privacy policy updates, DPIA documentation                      | Legal / Compliance   |
| R10 | Excessive cost due to inefficient cloud resource usage                          | Medium     | Medium   | **Medium** | Cost monitoring dashboards, job timeouts, quotas                                | Cloud FinOps         |

#### Likelihood
- **Low**: Rare or unlikely to occur  
- **Medium**: Could occur occasionally under certain conditions  
- **High**: Expected to occur frequently  

#### Impact
- **Medium**: Moderate disruption, user complaints, minor SLA breach  
- **High**: Major disruption, sensitive data exposure, trust loss  
- **Critical**: Legal implications, national-level breach, irreversible damage
## Code, CI/CD, and Cloud Deployment Practices
The team must use Git as the version control system, with repositories hosted on GitHub.
The following branching model must be implemented based on Git Flow:
### 1.1 Git Flow Branching Strategy

| Branch        | Purpose                                 | Merges into           | Created from         |
|---------------|------------------------------------------|------------------------|-----------------------|
| `main`        | Stable code in production                | –                      | `release/*`, `hotfix/*` |
| `develop`     | Development and integration branch       | `release/*`            | `feature/*`           |
| `feature/*`   | New features or enhancements             | `develop`              | `develop`             |
| `release/*`   | Prepares code for production release     | `main` and `develop`   | `develop`             |
| `hotfix/*`    | Urgent fixes applied to production       | `main` and `develop`   | `main`      

### 1.2 Commit Message Convention

All commit messages must follow a standardized structure for clarity and traceability:

<type>(component): short description in present tense

# Examples:
feat(api): add validation to donation endpoint
fix(auth): resolve login timeout issue
chore(ci): update deployment script for staging

The development team must use the following commit types for consistency and clarity in version control:

| Type      | Description                           |
|-----------|---------------------------------------|
| `feat`    | New feature                           |
| `fix`     | Bug fix                               |
| `docs`    | Documentation changes                 |
| `style`   | Formatting only (no code logic change)|
| `refactor`| Code restructuring (no behavior change)|
| `test`    | Adding or updating tests              |
| `chore`   | Maintenance tasks, tooling, CI/CD     |

## 2. Coding Standards

All code must follow predefined standards to ensure readability, consistency, and quality.

### 2.1 Frontend (React)

- Use Prettier for automatic formatting
- Use React Testing Library for testing
- Components: PascalCase
- Variables/Functions: camelCase
- Avoid inline styles; use TailwindCSS or component-scoped styles

### 2.2 Backend (Python)

- Use Black for formatting
- Linting: Pylint 
- Testing: pytest
- Validate APIs using OpenAPI specifications

### 2.3 Database

### 2.3 Database (Snowflake and Amazon S3)

- Snowflake models and tables must include data quality tests such as uniqueness, not_null constraints, and referential integrity validations, implemented via Snowflake tasks.
- Use clear naming conventions and prefixes for Snowflake objects:
  - `stg_` for staging tables (raw data imported from sources)
  - `dim_` for dimension tables (reference data)
  - `fct_` for fact tables (transactional or measurable data)
- All Snowflake object names (tables, schemas, views, columns) must use snake_case naming conventions.
- Data stored in Amazon S3 must follow a clear folder and file naming structure aligned with project requirements, including environment and date partitions (`s3://bucket-name/project/env/date=YYYY-MM-DD/`).
- When ingesting data from S3 into Snowflake, ensure data formats are consistent, with schemas enforced via Snowflake external tables or COPY commands with file format definitions.

## 3. Pull Requests and Code Review

Every change must be reviewed through a pull request (PR):

- All PRs must be based on a feature, hotfix, or release branch
- At least one approval is required before merging
- All checks must pass (CI, linting, tests)
- PR descriptions must explain what was changed and why
- Screenshots or test output must be included for UI or API changes
- Large PRs must be split into smaller, manageable commits

## 4. Continuous Integration (CI)

GitHub Actions must be configured for CI on every pull request to `develop` or `main`.

### CI Pipeline Steps

- Checkout repository
- Install dependencies
- Run linters
- Execute unit and integration tests

## 5. Continuous Deployment (CD)

Automatic deployments must be configured for both staging and production environments using GitHub Actions.

| Environment | Branch  | Trigger                | Requires Approval |
|-------------|---------|------------------------|-------------------|
| staging     | develop | Push to develop        | No                |
| production  | main    | Merge or manual trigger| Yes               |

Deployment must include steps for:

- Environment variable injection
- Health checks post-deployment
- Rollback mechanism in case of failure

## KPIs and Metrics

| Category            | Metric                  | Data Source                          | Calculation Method                          | Visualization       |
|---------------------|-------------------------|--------------------------------------|---------------------------------------------|---------------------|
| **System Availability** | ≥99.9%                 | CloudWatch logs                     | Uptime / Total time (Monthly)               | Gauge               |
| **Query Latency**    | <200ms (P95)           | Snowflake query logs                | 95th percentile query time (Monthly)        | Line chart          |
| **Error Rate**       | <0.1%                  | CloudWatch error logs               | Failed requests / Total requests (Monthly)  | Bar chart           |
| **Data Ingestion**   | <2 minutes             | S3/Snowpipe logs                    | Processing duration (Monthly)               | Scatter plot        |
| **Security Compliance** | 100%                | Okta, WAF, KMS logs                 | Audit pass rate (Semi-annual)               | Table               |
| **Active Datasets**  | ≥100                   | Snowflake metadata                  | Table count (Quarterly)                     | Counter             |
| **User Satisfaction**| ≥4.5 (out of 5)        | User surveys                        | Survey average (Quarterly)                  | Gauge               |
| **Recovery Time**    | <2 hours               | Incident reports                    | Test duration (Semi-annual)                 | -                   |

**Dashboard Features:**
- **Platform:** Amazon QuickSight
- **Visualizations:** Mixed types (gauges, line charts, bar charts, scatter plots, tables, counters)
- **Filters:** Time range, service components
- **Alerts:** SNS notifications for threshold breaches
- **Security:** RBAC/RLS implementation
- **Compliance:** No data exports allowed, full auditability
- **Refresh Rate:** Real-time for operational metrics, periodic for others

## Deployment and Operations Strategy

The deployment strategy for Data Pura Vida utilizes Blue-Green Deployment to ensure zero-downtime updates, meeting the 99.9% SLA and supporting scalability for millions of records and thousands of concurrent users. New versions are deployed to a "Green" environment, mirroring the production "Blue" environment, using AWS Fargate for the monolithic Node.js/Express backend and React Native frontend. GitHub Actions and Terraform automate CI/CD, provisioning infrastructure like Snowflake, AWS S3, and VPC endpoints. Comprehensive tests (unit, integration, security via OWASP ZAP, and load) validate performance (<200ms query latency, <0.1% errors) in Green. AWS WAF restricts access to Costa Rica-based IPs, and a Node.js service with AWS KMS manages tripartite keys (one part with Data Pura Vida, two with custodians). Traffic shifts to Green via AWS Application Load Balancer after validation, with Blue retained for 24 hours for rollback, ensuring <2-hour recovery. This approach supports future microservices migration and complies with Law 8968, GDPR, and ISO 27001.

## Monitoring and Operations

Observability: AWS CloudWatch captures structured logs from all system layers, complemented by Snowflake query history for data access audits, ensuring traceability per Law 8968 and GDPR. CloudWatch Metrics track latency, errors, traffic, and per-user/entity dataset usage. AWS SNS sends alerts for downtime, errors, or security incidents (e.g., unauthorized IP access). Amazon QuickSight dashboards provide real-time insights into system health, dataset usage, and backoffice operations like user management and audits.

High Availability: Snowflake’s multi-cluster architecture and Fargate auto-scaling handle usage spikes and 10TB/year data growth. AWS Application Load Balancer with WAF distributes traffic. Daily full backups and 4-hour incremental backups in S3 with versioning, plus Snowflake snapshots, ensure data integrity. Automated disaster recovery playbooks using Terraform and S3/Snowflake restore the system in <2 hours, tested quarterly. Snowflake Snowpark drives AI for data normalization and dashboards, with AWS SageMaker as a fallback, and CloudWatch optimizes costs for Snowflake and Fargate usage.

# DEFINITION OF REQUIREMENTS
## Functional Requirements

### User Management and Registration

- Allow registration of natural persons, legal entities, institutions, chambers, groups, and companies, and adapt the system (forms) based on the user type.

- Digital identity, biometrics, liveness detection, and MFA (Multi-Factor Authentication).

- Assign tripartite security keys to organizations for access delegation/revocation.

- Capture IBAN and/or credit card data during registration.

- Email notification system.

- Generate symmetric and asymmetric keys with a tripartite system.

### Data Management

- Support for Excel, CSV, JSON APIs, SQL and NoSQL databases.

- Define data as public/private, free/paid, temporary/permanent.

- Access control by institution, individual, or specific group (granular control).

- Allow selection of specific fields to encrypt.

- Specify columns that relate datasets to each other.

- Extraction, transformation, cleaning, context detection, modeling, and loading (ETDL).

- Avoid duplication and optimize existing relationships.

- Configuration of differential fields and update frequency.

### Commercialization and Payments

- Free data up to a certain size, with charges for additional space.

- Platform fee/commission on paid data based on size and duration.

- Multiple payment methods: credit cards, debit cards, and national mechanisms.

- Automatic permission assignment upon payment confirmation.

- Consumption control, real-time monitoring of paid data usage.

### Visualization and Analysis

- Custom dashboards, built manually or through AI prompts.

- Multiple visualizations: tables, graphs, counts, trends, and predictions.

- Share dashboards among users or allow internal public visibility.

- The system must implement data delivery mechanisms that minimize the possibility of indirect extraction of information, especially for unauthorized uses such as AI model training. When necessary to deliver visual representations of data, formats like SVG or PDF may be considered, as long as they prevent automated reconstruction or reverse engineering of the underlying data.

- Log all transactions and data usage in a user-accessible history for consultation and internal audit.

### Backoffice

- User management: maintenance of identities, memberships, and roles.

- Configuration of rules, formats, validations, and structures by entity type.

- Administration of API connectivity, databases, and external callbacks.

- Key management: revocation and regeneration of security keys.

- Full audit trail: details by user, action, date, and effect.

- Usage reports, access logs, consumption data, metrics, data quality, and anomalies.

- Operational monitoring: service status, tasks, transfers, and processes.

## Non-Funtional Requirements

### Performance

- The dashboard query engine must deliver results in under 200 milliseconds for 95% of requests under normal load.
  
- The platform shall support at least 200 concurrent users with no noticeable performance degradation. All of this the fifth year of operation.
  
- Data ingestion pipelines must process files up to 1GB in size within 2 minutes, including ETDL stages.

### Scalability

- The infrastructure must support automatic horizontal scaling in response to usage spikes.

- The data lake architecture must accommodate growth of up to 10TB per year without manual intervention.

- The system must allow onboarding of new data providers without modifying core services.

### Reliability

- The system must not exceed 43.2 minutes of downtime per month, aligning with a 99.9% SLA.

- All transactions must be ACID-compliant, and service errors must trigger automated retries with rollback capabilities.

- Full backups of all datasets and user metadata must be taken daily, with incremental backups every 4 hours.

- In the event of a critical failure, full system recovery must be achieved within 2 hours, using predefined playbooks and automated infrastructure recovery.

### Availability

- The system must maintain 99.9% availability, with high availability configurations and load balancers.

- The system infrastructure (including core services, APIs, and Snowflake-based data operations) must demonstrate a minimum mean time between failures of 30 days, ensuring fault tolerance at both the compute and storage layers.

- In the event of any service interruption or system failure, the system must be recoverable and operational within a maximum mean time to repair of 2 hours, supported by automated diagnostics and recovery scripts.

- Scheduled maintenance activities must:
	- Be limited to predefined windows.
	- Be communicated to stakeholders at least 72 hours in advance.
	- Include health verification steps and after the execution to ensure service continuity.

- The system must include Snowflake’s automatic multi-cluster architecture to ensure high availability and fault isolation for queries and pipelines and real time monitoring and alerting to trigger failover workflows.

### Security 

- All data in transit and at rest must be enceypted using AES-256. All APIs must enforce TLS 1.3 for secure communications.

- PENDIENTE HABLAR SOBRE auth y verification

### Usability

- Screen reader support, keyboard navigation, and contrast options must be available to ensure compliance with inclusive design principles.

- Some of the inclusive design principles to follow are: 
	- Give control: Allow users to personalize their experience (font size, colors, contrast)
	- Offer choices: Offer multiple choices to interact (voice, clicks, keyboard)
	- Provide equivalent experiences: Ensure the same experience to all users in despite of their capabilities

- Use of UX principles for a better user interaction with the UI.
	- Consistency: Use familiar patterns, layouts, and terminology throughout the interface so users can predict interactions and learn quickly.
	- Feedback: Provide immediate, clear responses to user actions (e.g., button clicks, form submissions, errors) so users understand what is happening.
	- Simplicity: Eliminate unnecessary steps, clutter, or features. Focus on helping users complete tasks with minimal effort and cognitive load.
	- Visibility of System Status: Keep users informed about what’s going on with timely and appropriate status indicators (e.g., loading spinners, progress bars, confirmation messages).

### Maintainability

- All system components must emit structured logs to a centralized logging system. Metrics must be exposed via Prometheus, with real time dashboards in Amazon Quicksight.

- Source code must be managed using Github with GitFlow branching. All deployments are automated via CI/CD pipelines with infrastructure defined via Terraform.

- All code must adhere to industry recognized standards and best practices:
	- Follow the SOLID principles for maintainable software.
	- Maintain at least 90% unit test coverage across all business logic and services.
	- All pull requests must be peer-reviewed, and merged only after passing all automated tests.
	- Commit messages must follow the Conventional Commits specification for traceability.

### Interoperability

- All data exchange and system interaction must comply with open standards to ensure broad interoperability across institutional and technological boundaries.

- The system must support seamless integration with:
	- External public data systems (government registries, public entities databases)
	- Private sector API’s
	- Both SQL and NoSQL connectors for ingesting structured and semi-structured data.

- API’s must be:
	- RESTful, stateless, and resource-oriented.
	- Secured with rate limiting, IP whitelisting, token-based auth, and MFA.
	- Equipped with detailed versioned documentation (e.g., Swagger UI).
	- Designed to expose only the minimum viable data based on roles and permissions (RBAC/RLS).

### Compliance

- The system must fully comply with Law 8968 – Protection of the Person Regarding the Processing of Personal Data (Costa Rica), including provisions for:
	- Informed consent and purpose limitation.
	- Data subject rights such as access, rectification, and deletion.
	- Registration of personal data databases with PRODHAB (Agencia de Protección de Datos de los Habitantes).

- All personal and sensitive data handling must adhere to the General Data Protection Regulation (GDPR).

- The platform must implement and maintain an Information Security Management System (ISMS) aligned with ISO/IEC 27001.

- OECD Recommendation on Data Governance for the Public Sector. Data Pura Vida must reflect principles of:
	- Openness and reusability of public data.
	- Trust, transparency, and accountability in data use.
	- Clear roles and responsibilities for data stewardship.

- Related to security industry standards to follow:
	- Use of TLS 1.3 for encrypted communications.
	- End-to-end encryption of sensitive data using AES-256.
	- Implementation of Role-Based Access Control (RBAC) and Row-Level Security (RLS).

### Extensibility

- The platform must allow modular addition of new AI models, data connectors, and dashboard templates without affecting existing operations. APIs and services must be designed to support future migration to microservices.

### Documentation

- End-user guides must be provided Spanish, accessible directly within the portal.

- System administration manuals, backup and recovery guides, and access control procedures must be maintained in a secure internal wiki.

- Full API documentation (Swagger), architecture diagrams, CI/CD guidelines, and code style references must be available in the repository.

- Documentation must be version-controlled alongside the codebase and updated with each release as part of the definition of done in Scrum tasks.

# SYSTEM ANALYSIS
## DETAILED DECOMPOSITION BY COMPONENTS DIAGRAM
![image](https://github.com/user-attachments/assets/4d110e56-2af7-4c70-84a4-d333e6deef8b)

![image](https://github.com/user-attachments/assets/f457b93b-36ca-47d0-949e-e59e92d764bc)

![image](https://github.com/user-attachments/assets/5e1f18f2-1958-49a5-8eaf-d5fd45738a1d)

![image](https://github.com/user-attachments/assets/59cfe50f-b0c6-4582-a39f-92ece42860ad)

![image](https://github.com/user-attachments/assets/8f7f0329-ee79-4e83-b003-d654225768eb)

![image](https://github.com/user-attachments/assets/aac2c9a3-ca7a-4b80-afff-23feff63fa7a)

# LEGAL AND REGULATORY FRAMEWORK

## Regulatory Compliance and Privacy Policies
For years, Costa Rica has faced a significant structural limitation: the absence of a centralized data system that facilitates access, analysis, and utilization of information by diverse actors. Currently, there is no national ecosystem that allows individuals, public institutions, state branches, social organizations, and the private sector to share, reuse, and market information in a structured manner. This fragmentation has hindered evidence-based decision-making, slowed institutional processes, and limited the development of innovative solutions that could emerge from the strategic use of data.
One of the main obstacles to overcoming this gap is not only technical but also political and institutional. Many state organizations do not feel comfortable sharing information with other government entities or private actors, whether due to mistrust, institutional jealousy, concerns about misuse, or a lack of regulatory clarity. This reluctance creates data silos that prevent the construction of an integrated view of the country and limits the potential for cross-sector solutions. Faced with this challenge, DataPuraVida proposes a flexible and controlled approach to overcome this political problem. Participating organizations would not be required to share all their data; instead, they would be allowed to choose which data to share, under what conditions, and with whom. This creates a transparent and regulated data market, where institutional autonomy is respected, but collaboration is encouraged through clear rules, incentives, and trust. By offering control, privacy, and traceability mechanisms, the system reduces political resistance and lays the groundwork for true data governance at the country level.

## User-centric data governance and regulatory compliance
Link to view Law 8968: http://www.pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=70975
The system must be developed in compliance with the principles established in Law 8968. This includes:
- Informed consent: All collection and processing of personal data must have the free, specific, and documented authorization of the data subject, with the possibility of easy revocation.
- Clear purpose: Each use of data must be justified, informed, and limited to its original purpose.
- Data subject rights: Interfaces will be enabled so users can securely review, correct, or request deletion of their data.
- Quality and updating: The system will incorporate automatic validations and periodic reviews to keep the data accurate and relevant.
- Protection of sensitive data: If information such as health or religious information is handled, enhanced security measures will be applied and explicit consent will be required.
- Data processing responsibility: Each database must have a clearly identified and trained person responsible for ensuring legal and technical compliance.
- Robust security: Encryption, access control, and monitoring protocols will be implemented to prevent security breaches.

## Integration of international standards
Link to view GDPR (Spanish): https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679
In addition to national legislation, DataPuraVida aligns with the European Union's General Data Protection Regulation (GDPR), which establishes advanced standards for the ethical handling of information. Among its key contributions to the system:

- Privacy by design and by default: The system will only collect the minimum data necessary, ensuring anonymization, access segmentation, and minimization through its architecture.
- Data Impact Assessments (DPIA): A formal risk analysis will be conducted when the system processes personal data on a large scale or sensitive data.
- Data Protection Officer (DPO): It is recommended to designate a person responsible for regulatory compliance, technical advice, and contact with users.
- Portability: Users will be able to obtain and transfer their data in standard formats, fostering their autonomy.
- Incident Management: Mechanisms will be implemented to detect and report security breaches within 72 hours, meeting transparency and immediate action requirements.
- Accountability: The system will document all actions involving personal data, conducting audits and maintaining traceability to demonstrate compliance. Fines of up to €20 million or 4% of global annual turnover, whichever is greater. According to the following article: https://time.com/5290043/nazi-history-eu-data-privacy-gdpr/?.com

## Security and interoperability as pillars
The implementation of ISO/IEC 27001 will ensure a rigorous approach to information security. The following will be established:
- Clearly defined roles and permissions.
- Cryptographic controls and strong authentication.
- Regular audits to verify data integrity, confidentiality, and availability.
- Continuous improvement plans for security management.

The OECD Guidelines on Data Governance provide a holistic view. For DataPuraVida, this means:
- Data quality and interoperability: Establishing standards for metadata, formats, and version control.
- Clear and accountable governance: Defining inclusive governance structures that promote the participation of public, private, and social sectors.
- Data lineage documentation: Enabling the tracing of data origin, use, and transformations.
- Transparency and public trust: Ensuring that all system processes are visible and auditable.

DataPuraVida is not simply a technological infrastructure, but a platform for the political, institutional, and social transformation of the country. By enabling voluntary yet secure management of data exchange and complying with the most demanding national and international standards, the system can break decades of fragmentation and become the catalyst for an economy based on knowledge, innovation, and trust. Data governance is no longer an option, but a necessity for the sustainable, transparent, and equitable development of Costa Rica.


# STACK

- Amazon Web Service as the designated Cloud Service

- Snowflake for data analytics and data processing, also for for MFA, IP whitelist and token validation (session validation)

Frontend:

    React Native 18.2.x – Provides high performance and scalability for web and mobile interactions.

Backend:

    Python: Handles all incoming REST requests. Connects to the PostgreSQL database. Implements general business logic (authentication, user management, file uploads, task creation) implementing external services such as AWS services.

    Flask: Web framework for Node.js, used to handle REST, manage middleware, routing, and request/response lifecycle.

    REST: For structured, not state-dependant operation and service-oriented operations. Authentication and registration, use of AWS services, etc... 

Database:

    Snowflake --> Definir más 

AI & Machine Learning:

    Snowflake can be integrated with LLM's, in relation with the choosen model of the LLM a training for ETDL flow management is required. This AI will be used as well for documents revision.
    Reference Link: https://www.youtube.com/watch?app=desktop&v=9FejjGVZrPg&t=0s

    **AI Processing with SageMaker**
    	1. **S3-Native Processing**: SageMaker can directly read from and write to S3 without data movement
	2. **Scalable Infrastructure**: Automatically provisions ML instances (from ml.t3.medium to ml.p3.16xlarge)
	3. **Cost Efficiency**: Spot instances for training, serverless inference for sporadic workloads
	4. **Integration**: Native Step Functions integration for orchestration

Cloud & Hosting:   
 
    Amazon Web Services: Ensures good communication and compatbility with Snowflake and multiple useful services. 

DevOps & CI/CD:

    GitHub Actions: Automates integration and deployment workflows.

Quality Assurance:

# FRONTEND
## Authentication platform
To ensure secure access across Snowflake, AWS, and Amazon S3, the development and operations team must implement Multi-Factor Authentication (MFA) and support biometric authentication where possible.
### Technologies Involved
- Frontend: React + Okta SDK (OIDC + biometrics via WebAuthn)
- Backend: Python Flask + Okta JWT Verification

### Workflow  
React frontend is integrated with Okta’s Auth JS SDK, which simplifies OpenID Connect (OIDC) login flows.
When the user clicks “Log In,” your app:

When the user clicks login:
1. Redirects the user to Okta’s hosted login page.
2. Specifies scopes like `openid`, `profile`, and `email`.
3. Adds a redirect_uri to bring them back after login.

In the Okta's page:
1. The user enters their credentials
2. MFA is enforced based on the user's policy (SMS, Google, Okta Verify)
3. Biometric Login (WebAuthn) prompts the user to use FaceID, or TouchID.

The user gets redirected by Okta back to the platform with an authorization code after succesfully login in. This redirection URL isn’t random, it contains a temporary, one-time-use authorization code in the query string. Example:
`https://yourapp.com/login/callback?code=AUTH_CODE&state=xyz`
- `code=AUTH_CODE`: This is the temporary authorization code.
- `state=xyz`: A value used to verify that the response is tied to the initial login request (protects against CSRF attacks).

At this point there no tokens yet, just a temporary code. So the next step is to exchange that code for real tokens. Using the Okta SDK, your app sends a secure request directly to Okta’s token endpoint. This request contains:
- The authorization code you just received
- A client identifier (so Okta knows which app is asking)
- The redirect URI (to match it against the one registered)
- A proof of identity, such as a client secret or PKCE challenge

Okta validates everything and responds with:

- Access Token (JWT): This is the most important token for the backend. It's a signed JSON Web Token (JWT) that proves the user is authenticated. It includes what the user is allowed to do, expiry, and user ID. The platform uses this to call your Flask backend API in a secure way.
- ID Token (JWT): This token contains user identity details, like their name, email, and roles. Used by the frontend to display profile info or make UI decisions. Not sent to the backend.

These tokens are stored securely in the frontend, in memory or browser session (not local storage). Okta SDK can manage session renewal automatically. Once the platform has successfully received the Access Token (JWT) from Okta, it now uses this token to make authenticated API requests to the backend (Python Flask). Each API request includes the access token in the Authorization header of the HTTP request like this:
`Authorization: Bearer <access_token>`
This access token contains embedded information, including:
- The user’s unique ID (sub)
- The user's email address
- The groups or roles the user belongs to
- Token issuance time (iat) and expiration time (exp)
- The audience (aud), who the token is meant for (API)
- The issuer (iss), Okta domain

For the backend to verify the token, it follows the next steps:
- Step 1: Fetch Okta's Public Signing Keys (JWKS): Okta signs all access tokens using a private key. It publishes the corresponding public keys at a secure endpoint. The backend uses these public keys to validate that the token signature is authentic and unmodified. This ensures no one could have faked or altered the token.
- Step 2: Decode and Validate the Token, the backend checks:
	-Signature: Is it valid and signed by a known Okta key?
	- Expiration (exp): Has the token expired?
	- Audience (aud): Was this token meant for this backend?
	- Issuer (iss): Was this token really issued by your Okta tenant?
If any check fails, the request is rejected.
Once the token is verified, your Flask backend can authorize the request based on the token contents. The groups claim inside the token may say for example:
`["admin", "donor"]`
The backend can map these to your platform’s internal permissions. This mapping controls which endpoints each user can reach and what actions they can perform. Now that the backend knows who the user is and what they’re allowed to do, it can allow or deny access to the specific route, return secure, personalized data and continue processing the business logic.

![Agile Product Roadmap](https://github.com/user-attachments/assets/0a7dd9a8-ae89-4567-83ee-db3428ee22ad)

### POC MFA



# BACKEND

Complete Diagram: https://lucid.app/lucidchart/6b3cff80-ec40-4584-99eb-46dad1afd5ec/edit?invitationId=inv_c137e4e0-9a2d-446c-8f9d-16471948de2a&page=HWEp-vi-RSFO#

![image](https://github.com/user-attachments/assets/38344fe9-cb99-4504-b84c-cded9db1f45f)

Data Pura Vida is a secure data platform for Costa Rican institutions, providing dataset management, AI-powered analytics, and governed data sharing with enterprise-grade security controls.

### Core Capabilities
- **Secure Dataset Management**: Upload, encrypt, and manage sensitive datasets
- **AI-Powered Analytics**: Natural language queries and automated insights
- **Governed Data Sharing**: Multi-party approval workflows with custodian controls
- **Geographic Compliance**: Costa Rica-specific access controls and data residency
  
### API Design and Architecture

The chosen approach for the API architecture is a Monolithic architecture. Meaning, the entire application (UI, business logic, data access, integrations) is built, deployed and managed as a single, cohesive unit. Components within the monolith typically communicate directly through method calls or internal APIs.
The monolith will run on AWS Fargate; this moves closer to serverless for the container execution, as AWS manages the underlying EC2 instances for Fargate. However, the system takes advantage of AWS services for specific functionalities like authentication, storage, ETL, monitoring and security; this enables modern scalability, resilience, security, and observability, common features in cloud-native and decoupled architectures.
The API will follow the principles of Representational State Transfer (REST). Rest APIs use standard HTTP methods (like GET, POST, PUT, DELETE) to communicate with the servers, enabling clients to access and maniúlate data. Taking in consideration that “Data Pura Vida” is mainly a data consultation service the approach is ideal. For example:

- CRUD operations
- File uploads 
- Authentication and user management

##### Logical division for workload distribution

The monolithic architecture chosen for this project contains layers designed to be responsible for different tasks, ensuring good separation of concerns and maintainability. The general responsabilities of each layer are describe in the following table. Ahead of the table each layer will be explained in detail.


| **Layer**                  | **Responsibilities** |
|---------------------------|-----------------------|
| **Handler Layer**          | - Handles HTTP requests and responses, orchestrates endpoints.<br>- Entry point for all API requests.<br>- Parses HTTP input, delegates to services, and formats responses.<br><br>**Key Responsibilities:**<br>- HTTP request parsing and validation<br>- Authentication context extraction<br>- Service layer coordination<br>- Response formatting<br>- Error handling |
| **Middleware Layer**       | - Applies cross-cutting concerns to the request/response pipeline.<br>- Middleware executes in a chain before/after handlers for shared functionality.<br><br>**Key Components:**<br>- `SecurityContextMiddleware`: Builds security context<br>- `GeoRestrictionMiddleware`: Enforces Costa Rica IP restrictions<br>- `AuthenticationMiddleware`: Validates JWTs and sessions<br>- `UsageLimitMiddleware`: Enforces subscription and query limits<br>- `AuditMiddleware`: Logs all operations for compliance |
| **Service Layer**          | - Contains core business logic and application rules.<br>- Coordinates validations and database/external system interactions.<br>- Acts as intermediary between Handler and Repository layers.<br><br>**Key Responsibilities:**<br>- Business rule enforcement<br>- Multi-repository coordination<br>- External service integration<br>- Transaction management<br>- Domain-specific validations |
| **Security Layer**         | - Manages authentication and authorization.<br>- Controls access to system features, data, logs, and user management.<br>- Handles token logic (e.g., JWT). |
| **Repository Layer**       | - Encapsulates all database access.<br>- Provides clean interfaces for CRUD operations.<br><br>**Key Components:**<br>- `SFRepository`: Snowflake operations<br>- `S3Repository`: Dataset and artifact storage<br>- `AWSVaultRepository`: Secret and identity management |
| **AI Data Transformation Layer** | - Hosts AI-driven logic for data processing.<br>- Detects patterns in data and metadata.<br>- Makes autonomous or human-assisted decisions to modify or enrich data.<br>- Integrates with AI/ML agents. |

### Serverless Architecture

The project’s serverless structure is based on two main principles: leveraging fully managed cloud services and decoupling infrastructure management from application logic. By using services like AWS Fargate for containerized API execution and a combination of tools such as S3, Glue, Cognito, Step Functions, and Snowflake, the system avoids the need to provision or maintain servers.

This serverless architecture simplifies the need for hardware demands and cloud machine types, as it eliminates the need to manage servers, scaling, or provisioning infrastructure manually—delegating those responsibilities to fully managed cloud services that automatically handle compute, memory, and scaling behind the scenes.

#### Overview of the architecture

This project implements a Serverless Architecture to enable a highly scalable, resilient, and low-maintenance data platform. The system is composed of three primary components:

- Flask-based API hosted on AWS Fargate

- AWS Managed Services (Cognito, S3, Glue, Step Functions, QuickSight, KMS, etc.)

- Snowflake as the centralized data platform

All of this grounded in the following **principles**.

- No infrastucture management

- Event-driven processing

-  Auto-scalling and pay-per-use

#### Architecture Components and Design

##### 1. Flask API with AWS Fargate (Containerized Serverless)

- AWS Fargate enables serverless containers by abstracting EC2 management.
- The Flask API is packaged into a Docker container and deployed with Fargate using ECS, providing:
	- Scalable RESTful endpoints
	- Stateless compute execution
	- Integration with other AWS services

##### 2. AWS Serverless Services

The project uses a suite of AWS services that collectively handle authentication, storage, orchestration, analytics, and encryption—all without managing servers.


| **Service**            | **Purpose**                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| **Amazon Cognito**     | Serverless user authentication and authorization                   |
| **Amazon S3**          | Serverless object storage for files, data inputs, and outputs      |
| **AWS Glue**           | Serverless ETL for processing and transforming data into Snowflake |
| **AWS Step Functions** | Serverless orchestration of ETL and data pipelines                 |
| **Amazon QuickSight**  | Serverless BI for dashboards and data visualization                |
| **AWS KMS**            | Key management for encryption of sensitive data                    |

##### 3. Snowflake – Serverless Data Platform
Snowflake complements the architecture by providing: 

- Serverless SQL query execution
- Automatic scaling of compute warehouses
- Zero-managment data sharing (ability to share live, ready-to-query data across accounts and organizations without needing to manage infrastructure, data movement, or replication manually.)
- Integration with AWS via Snowpipe, external stages, and S3

## API Endpoints

### Authentication & Sessions
```
POST   /auth/login              # User authentication
POST   /auth/logout             # Session termination
POST   /auth/refresh            # Token refresh
GET    /auth/session/validate   # Session validation
```

**Example Login Request**:
```json
{
  "email": "analyst@itcr.ac.cr",
  "password": "vivalaliga",
  "organization_id": "itcr_pollito"
}
```

**Example Login Response**:
```json
{
  "access_token": "sdgklhaeouirhgpaorgergh...",
  "refresh_token": "erthertwhwertgerg...",
  "expires_in": 3600,
  "user": {
    "id": "alonso",
    "email": "alduran@estudiantec.cr",
    "organizations": ["itcr_pollito"],
    "permissions": ["dataset.read", "query.execute"]
  }
}
```

### Dataset Management
```
POST   /datasets/upload/init            		# Initialize dataset upload
POST   /datasets/upload/{session}/chunk 		# Upload data chunk
POST   /datasets/upload/{session}/finalize 		# Complete upload
GET    /datasets                        		# List available datasets
GET    /datasets/{id}                   		# Get dataset details
DELETE /datasets/{id}                   		# Delete dataset
GET    /datasets/{id}/preview           		# Get data sample
GET    /datasets/{id}/schema            		# Get dataset schema
```

**Example Dataset Upload Initialization**:
```json
{
  "name": "Costa Rica Padron Electoral",
  "description": "blah blah blah",
  "classification": "SENSITIVE",
  "file_size": 420,
  "file_hash": "...",
  "schema": {
    "columns": [
      {"name": "province", "type": "string", "nullable": false},
      {"name": "population", "type": "integer", "nullable": false}
    ]
  }
}
```

### Query Execution
```
POST   /queries/execute         # Execute SQL query
GET    /queries/{id}/status     # Check query status
GET    /queries/{id}/results    # Get query results
DELETE /queries/{id}            # Cancel running query
GET    /queries/history         # Get user's query history
```

**Example Query Execution**:
```json
{
  "sql": "SELECT province, AVG(population) FROM padron_2025 GROUP BY province",
  "dataset_ids": ["dataset_vivalaliga"],
  "output_format": "json",
  "limit": 1000
}
```

### AI-Powered Analytics
```
POST   /ai/chat                 # Natural language query
POST   /ai/schema/analyze       # AI schema analysis
POST   /ai/insights/generate    # Generate data insights
GET    /ai/suggestions          # Get query suggestions
```

### Data Sharing & Permissions
```
POST   /sharing/datasets/{id}/share     # Share dataset access
POST   /sharing/datasets/{id}/revoke    # Revoke dataset access
GET    /sharing/datasets/{id}/access    # Get access list
POST   /sharing/approve/{request_id}    # Custodian approval
```

### Monetization
```
GET    /pricing/datasets/{id}           # Get dataset pricing
POST   /purchase/datasets/{id}          # Purchase dataset access
GET    /billing/usage                   # Get usage metrics
GET    /subscriptions                   # Get user subscriptions
```
## Important Classes & Components

### Core Services

#### **DatasetService**
Central orchestrator for dataset lifecycle management.
- **Key Methods**: `initializeUpload()`, `finalizeUpload()`, `getDatasetMetadata()`
- **Dependencies**: StorageService, ValidationService, MetadataService
- **Responsibilities**: Dataset CRUD, metadata management, lifecycle coordination

#### **AccessControlService**
Manages permissions and access policies.
- **Key Methods**: `validateAccess()`, `grantPermission()`, `revokeAccess()`
- **Dependencies**: SecurityManager, SFRepository
- **Responsibilities**: RBAC enforcement, row-level security, policy evaluation

#### **AIChatService**
Handles natural language query processing.
- **Key Methods**: `translateQuery()`, `executeNLQuery()`, `generateInsights()`
- **Dependencies**: QueryExecutionService, AccessControlService
- **Responsibilities**: NL-to-SQL translation, query optimization, result interpretation

### Security Components

#### **SecurityManager**
Central security coordinator for all operations.
- **Key Methods**: `createSecurityContext()`, `validateOperation()`
- **Dependencies**: TripartiteKeyManager, CustodianManager, GeoAccessValidator
- **Responsibilities**: Security orchestration, context management, operation validation

#### **TripartiteKeyManager**
Manages three-party key splitting and reconstruction.
- **Key Methods**: `generateEntityKeys()`, `reconstructKeyForOperation()`
- **Dependencies**: AWSVaultRepository
- **Responsibilities**: Shamir's Secret Sharing, key lifecycle, secure reconstruction

### Repository Abstractions

#### **SFRepository**
Snowflake data warehouse operations.
- **Key Methods**: `executeQuery()`, `createTemporaryTable()`, `bulkLoadFromStage()`
- **Responsibilities**: SQL execution, warehouse management, performance optimization

#### **S3Repository**
Object storage for datasets and artifacts.
- **Key Methods**: `putObject()`, `initiateMultipartUpload()`, `generatePresignedUrl()`
- **Responsibilities**: File storage, multipart uploads, presigned URL generation

### Custom Middleware

#### **SecurityContextMiddleware**
Creates security context for every request.
- **Execution Order**: First (sets foundation for all other middleware)
- **Responsibilities**: Context creation, user validation, permission extraction

#### **GeoRestrictionMiddleware**
Enforces geographic access controls.
- **Execution Order**: After SecurityContext
- **Responsibilities**: IP validation, institutional whitelist checking, access logging

## Error Handling

### Standard Error Response Format
Example: read a dataset
```
{
  "error": {
    "code": "INSUFFICIENT_PERMISSIONS",
    "message": "User lacks required permissions for this dataset",
    "details": {
      "required_permissions": ["dataset.read"],
      "user_permissions": ["query.execute"]
    },
    "trace_id": "trace_abc123"
  }
}
```

### Common Error Codes
- `AUTHENTICATION_FAILED`: Invalid or expired credentials
- `INSUFFICIENT_PERMISSIONS`: User lacks required permissions
- `GEOGRAPHIC_RESTRICTION`: Access denied due to location
- `USAGE_LIMIT_EXCEEDED`: Subscription limits reached
- `CUSTODIAN_APPROVAL_REQUIRED`: Operation requires custodian approval
- `DATASET_NOT_FOUND`: Requested dataset doesn't exist
- `QUERY_TIMEOUT`: Query execution exceeded time limit

## Security Layer Design

The Security Layer acts as a centralized security orchestrator that enforces authentication, authorization, encryption, and access control across all system components. It integrates seamlessly with the existing Handler, Service, and Repository layers.

### Security Components
1. `SecurityManager`
This is the central orchestrator that coordinates all security operations across the system.
- Acts as a facade that unifies all security components
- Creates and manages security contexts for requests
- Coordinates between authentication, authorization, key management, and geographic validation
- Provides a single interface for handlers to perform security operations, by being injected into `BaseHandler`

2. `SecurityContext`
Container object that carries security information throughout the request lifecycle.

- Immutable object created once per request, attached to request objects in SecurityContextMiddleware through securityManager, passed to all service methods that need security validation, and used by repositories for row-level security and access control
- Contains user identity, permissions, IP address, and organization memberships
- Provides security information for authorization decisions

3. `TripartiteKeyManager`
Manages the three-party key system where keys are split between Data Pura Vida and two custodians.

- Uses Shamir's Secret Sharing  (https://www.geeksforgeeks.org/shamirs-secret-sharing-algorithm-cryptography/) to split keys into 3 parts.
- Generates both symmetric (AES-256) and asymmetric (RSA-4096) keys
- Stores one share with Data Pura Vida, distributes two to custodians
- Reconstructs keys temporarily in secure memory for operations
- Immediately purges reconstructed keys after use

This is used when a new user (org, company, person) registers with `OrganizationSecurityService `, `DataCipherService ` uses it for creating a specific encryption , used by custodians to access or upload data `DataSetHandler` and for key rotation of 90 days. 

4. `CustodianManager`

Manages custodian assignments, approval workflows, and multi-party authorization during entity registration, dataset sharing and key operations.

- Assigns primary and secondary custodians to entities
- Sends approval requests via notifications through email
- Tracks approval status and validates signatures
- Enforces multi-party approval requirements for sensitive operations
`DatSetSharingHandler` uses it for dataset sharing approvals, `OrganizarionSecurityService` for access delegation, and `AccessControlService` for permission changes.

5. `GeoAccessValidator`
Enforces geographic restrictions, ensuring access only from Costa Rica or whitelisted institutional IPs by `GeoRestrictionMiddleware` for every request and `SecurityManager` for request validation.

- Maintains IP ranges for Costa Rica
- Manages institutional IP whitelist with custodian approval
- Validates client IP against allowed ranges on every request
- Supports dynamic IP registration for institutions

6. `UsageLimitEnforcer`
Monitors and enforces usage limits, automatically suspending access when limits are exceeded with `UsageLimitMiddleware` for every request and `QueryExecutionHandler` before query execution.
- Tracks real-time usage per user/dataset
- Compares against subscription plan limits
- Temporarily disables access when limits exceeded
- Provides upgrade options and renewal paths

### Related Services
1. `OrganizationSecurityService`
Manages multi-organization accounts and security delegation within organizations through organization management handlers during user access delegation workflows. 
- Allows single users to manage multiple organizations
- Enforces custodian approval for access delegation
- Manages organization-specific security keys
- Controls user access assignment and revocation

2. `DataProtectionService`
Protects sensitive data from unauthorized access, including platform engineers, in `DatasetHandler` during dataset finalization (after upload)  for datasets that are marked as sensitive through policy configuration.
- Encrypts sensitive dataset columns with entity-specific keys
- Creates secure access zones in Snowflake
- Removes direct data access for platform engineers
- Implements controlled data views that prevent bulk downloads

### Related Middleware
1. `SecurityContextMiddleware`
Creates and attaches security context to every incoming request, triggered before any other security validations because it sets up a security foundation for the entire request.
- Extracts authentication information from request headers
- Validates session and retrieves user information
- Creates `SecurityContext` object with user permissions and metadata
- Attaches context to request for use by subsequent layers

2. `GeoRestrictionMiddleware`
Right after `SecurityContextMiddleware` validates geographic access restrictions on every request.
- Extracts client IP from request
- Validates IP against Costa Rica ranges and institutional whitelist
- Blocks requests from unauthorized geographic locations
- Logs geographic access attempts for audit

3. `UsageLimitMiddleware`
Validates usage limits before allowing requests to proceed, applied to requests involving dataset queries or access.
- Checks current user usage against subscription limits
- Prevents operations that would exceed limits
- Provides upgrade options when limits reached
- Tracks usage patterns for billing

### Related Repositories
1. `VaultRepository`
- Manages **custodian** information storage and retrieval through `CustodianManager` using existing vault infrastructure. Stores custodian configurations in AWS Vault, Manages approval requests and responses, Tracks custodian assignment history, Provides custodian lookup functionality. 
- TripartiteKey: This repo manages tripartite key storage using existing vault infrastructure.


## Audit & Logging

![TPDDJyCm38Rl-HKM9pWW3jnsG8Zn8Q4960NjxALcYvOs8t4OyEjnqdIqVDngv_5h-qrw7XWznyOgDcm9fjR5Ue6irp1pgm3iO1wDtbHcjMQuH4Qujcwd56fs7fu3URKL1QFD5bk6Wny21u01felqEUPcs2nh4OkjPkFQp7MvCLUTmaNK6s8uVCGTt5RtTqSPhaub7hCtDie67dUMV](https://github.com/user-attachments/assets/665464ff-5705-460f-8ba4-3dea8995535a)

### Achitectura Principles
The system implements comprehensive audit logging with AWS CloudWatch, structured logging, and long-term archival. All logs follow a standardized JSON structure for consistency, correlation, and automated processing. The architecture supports real-time monitoring, compliance reporting, and business intelligenc

### Core Design Patterns

- Observer Pattern: Components emit events that are automatically captured by the audit system
- Strategy Pattern: Different log categories use specialized processing strategies
- Pipeline Pattern: Logs flow through structured transformation stages
- Correlation Pattern: All events include trace IDs for end-to-end request tracking

### Logging Categories

#### Standard Log Format

```
{
  "timestamp": "2025-06-10T14:30:15.123Z",
  "event_type": "DATASET_ACCESS",
  "trace_id": "trace_abc123",
  "severity": "INFO",
  "user": {
    "id": "user_alonso",
    "email": "alduran@itcr.ac.cr",
    "organization": "tec",
    "roles": ["data_analyst"]
  },
  "operation": {
    "type": "DATASET_QUERY",
    "dataset_id": "dataset_1",
    "classification": "SENSITIVE",
    "query_hash": "gsergherhqergqwerge",
    "approval_required": false
  },
  "security_context": {
    "ip_address": "200.9.156.45",
    "country": "CR",
    "device_fingerprint": "fp_xyz789",
    "session_id": "sess_abc456",
    "user_agent": "Mozilla/5.0..."
  },
  "result": {
    "status": "SUCCESS",
    "rows_accessed": 1500,
    "processing_time_ms": 2847
  }
}
```

#### 1. Security Audit Logs
Comprehensive security event tracking for compliance and threat detection.

**CloudWatch Group**: `/datapuravida/security/audit`  
**Retention**: 7 years
**Encryption**: AWS KMS

**Events Logged**:
- Authentication and authorization events
- Data access and permission changes
- Custodian approval workflows
- Geographic access control violations
- Encryption key operations

#### 2. Application Performance Logs
Application behavior monitoring and performance optimization

**CloudWatch Group**: `/datapuravida/application`  
**Retention**: 1 year  
**Encryption**: AWS KMS

**Events Logged**:
- Request/response lifecycle
- Service method execution
- Error conditions and stack traces
- Performance metrics and SLA monitoring

### 3. Query Execution Logs
Data query performance and billing tracking

**CloudWatch Group**: `/datapuravida/queries`  
**Retention**: 3 years  
**Encryption**: AWS KMS

### 4. Snowflake Integration Logs
Complete database activity monitoring via native Snowflake logging

**CloudWatch Group**: `/datapuravida/snowflake`  
**Data Source**: Snowflake Information Schema + Query History  
**Processing**: AWS Lambda with 5-minute intervals

## Implementation Architecture
### Audit Service Design

The centralized `AuditService` provides a consistent interface for all audit logging operations across the application stack.

### End-to-End Logging Flow
#### 1. Log Generation
Logs are generated at multiple points in the application architecture:

**Handler Layer**: All handlers extend `BaseHandler` which provides automatic audit logging through the middleware chain.

**Middleware Layer**: Specialized middleware components generate contextual logs
- `LoggingMiddleware`: Captures request metadata and trace id's
- `AuthenticationMiddleware`: Logs authentication events
- `SecurityMiddleware`: Records security violations
- `ComplianceMiddleware`: Tracks regulatory compliance events

**ServiceLayer**: Besiness logic services emit operation-specific logs
- `AuditService`: Centralizes all audit event generation
- `DatasetService`: Logs dataset lifecycle events
- `QueryExecutionService`: Captures query performance metrics
- `PaymentService`: Records monetization events

All application components write structured logs to designated CloudWatch Log Groups. The AuditService provides a unified interface for consistent log formatting and routing.

```
# Interfaz del servicio de auditoría
class AuditService(ABC):

    @abstractmethod
    async def log_security_event(self, event: SecurityEvent) -> None:
        pass

    @abstractmethod
    async def log_data_access(self, event: DataAccessEvent) -> None:
        pass

    @abstractmethod
    async def log_query_execution(self, event: QueryEvent) -> None:
        pass

    @abstractmethod
    async def log_system_event(self, event: SystemEvent) -> None:
        pass

    @abstractmethod
    async def log_custodian_approval(self, event: ApprovalEvent) -> None:
        pass
```
#### 2. Data Processing Pipeline
The system implements a complete ETL pipeline for log processing

![PP4zRiCm34PtdOB8qYbJzoAERCS8ZFuvG6T6PcGrikJA59AUgqVenUe86PncuGVYFO2Kk1eP0yVUYl5et801Ux364NyF13vmvsUWfGD6opiwSsQDTZqv1ZKL2a8yG4u7uumolpzkKi7vreyYa69qsX8ifFMn_K1M7THUZml04RAvK6E_Rn6Ayp1DXZ8wnSQxvAtdNlC8xtY2RVFo3](https://github.com/user-attachments/assets/c2874817-a75e-47ca-8e1f-7049ee35d133)

CloudWatch log groups trigger Lambda functions on log arrival, lambda exports raw JSON logs to S3 buckets organized by date and log category, and raw logs stored in S3 with path structure: `s3://logs-bucket/year/month/day/hour/`

### Event Correlation

All log entries include a `trace_id` that enables end-to-end request tracking across distributed components.

### Data Processing Infrastructure
**Lambda Functions**
- `log-export-function`: Exports CloudWatch logs to S3 (triggered every 5 minutes)
- `snowflake-integration`: Pulls Snowflake query history (runs every 5 minutes)
- `log-enrichment`: Adds geolocation and user context to logs

### Glue Components
- `audit-logs-crawler`: Daily schema discovery for all log categories
- `security-logs-etl`: Processes security audit logs for compliance reporting
- `performance-logs-etl`: Transforms performance data for dashboard analytics
- `query-logs-etl`: Processes query execution data for billing and optimization

### S3 Storage Structure

```
audit-logs-bucket/
├── raw-json/
│   ├── security/year/month/day/hour/
│   ├── application/year/month/day/hour/
│   └── queries/year/month/day/hour/
└── processed-parquet/
    ├── security/year/month/day/
    ├── application/year/month/day/
    └── queries/year/month/day/
```


## THIRDPARTY SERVICES

### AWS services used to complement the design

#### **Security Services**

Critical AWS Services (Must Have):

(Explicar AWS SDK)

Core Security:

- AWS Cognito - User authentication & MFA
- AWS Secrets Manager - Tripartite key storage
- AWS CloudHSM - Hardware key generation
- AWS KMS - Dataset encryption
- AWS IAM: Fine-grained access control, role-based permissions, and service-to-service authentication for all security components, service authentication, role management
	- Creates entity-specific roles for users and organizations
	- Manages dataset access policies with fine-grained permissions
	- Handles role assumption for secure operations
	- Sets up service roles for Lambda, Fargate, and Snowflake
 	-  Creates organization groups and admin policies
	- Delegates access within organizations with custodian approval
	- Manages multi-organization permissions for single users
	- Creates custodian-specific roles with limited permissions
	- Enforces approval-only access (custodians can approve but not access data)
	- Manages custodian role assumption for approval workflows
 	- `SecurityManager`: Enhanced with IAM role validation, `AccessControlService`: Creates IAM policies for dataset access, `DatasetHandler`: Uses role assumption for operations, `CustodianManager`: Validates IAM permissions for approvals

Network Security:

- AWS WAF - Costa Rica IP filtering
- AWS VPC - Network isolation
- AWS Certificate Manager - SSL/TLS

Monitoring & Compliance:

- AWS CloudTrail - Complete audit logging
- AWS CloudWatch - Real-time monitoring
- AWS Config - Compliance validation


#### AWS Secrets

#### AWS KMS

#### AWS CloudWatch

#### AWS Vault 
 
#### AWS Fargate
 
#### AWS QuickSight

#### AWS EventBridge

#### AWS StepFunctions

#### AWS Lambda

#### AWS Glue

#### AWS S3

#### AWS Cognito

### Snowflake Integration

#### Cortex

## Key Workflows
### 1. Dataset Upload
![image](https://github.com/user-attachments/assets/d5839f90-2cfd-4438-82fb-278102f37f5d)

#### **Phase 1: Upload Initialization**

```
POST /datasets/upload/init
```

1. **Handler Layer** receives request and validates user permissions
2. **Service Layer** (`DatasetService`) performs:
   - Security context validation via `SecurityManager`
   - Geographic restriction check via `GeoAccessValidator`
   - Session initialization with unique session ID
3. **Security Layer** generates encryption keys:
   - `TripartiteKeyManager` creates three key shares
   - One share stored with Data Pura Vida
   - Two shares distributed to designated custodians
4. **Storage Layer** (`S3Repository`) creates:
   - S3 upload session with multipart configuration
   - Presigned URLs for each chunk (valid for 1 hour)

#### **Phase 2: Chunk Upload**

```
PUT [presigned_url]
```

1. **Client** splits file into chunks
2. **Direct Upload** to S3 using presigned URLs
3. **Parallel Processing** enabled for multiple chunks
4. **Automatic Retry** for failed chunks via `RetryHandler`
5. **Checksum Validation** ensures data integrity


#### **Phase 3: Upload Finalization**

```
POST /datasets/upload/{session}/finalize
```

**Request Body Example:**
```json
{
  "chunk_references": [
    {"chunk_id": 1, "checksum": "md5:def456..."},
    {"chunk_id": 2, "checksum": "md5:ghi789..."}
  ]
}
```

1. **Validation Phase**
   - Handler layer validates all chunks are present
   - Service layer verifies checksums match
   - Ensures no missing or duplicate chunks

2. **Encryption Phase**
   - Security layer reconstructs tripartite keys
   - `DataCipherService` encrypts sensitive columns
   - Keys immediately purged from memory

3. **ETL Trigger Phase**
   - Service layer initiates AWS Step Function
   - Passes chunk references and metadata
   - Triggers AWS Glue job for processing

4. **Storage Migration**
   - Repository layer moves data from staging to final S3 location
   - Updates metadata in tracking system
   - Prepares for Snowflake ingestion

### Technical Components

#### DatasetService
Central orchestrator for dataset lifecycle
- **Key Methods**:
  - `initializeUpload()`: Creates upload session and security context
  - `processChunk()`: Validates and tracks chunk uploads
  - `finalizeUpload()`: Coordinates encryption and ETL trigger
- **Dependencies**: StorageService, ValidationService, SecurityManager

#### UploadManager
Handles chunked upload logic
- **Responsibilities**:
  - Chunk validation and ordering
  - Retry logic for failed uploads
  - Progress tracking and reporting

#### SecurityManager
Enforces security policies during upload
- **Operations**:
  - Creates security context for upload session
  - Validates geographic and permission requirements
  - Coordinates key generation and encryption

#### S3Repository
  - `initiateMultipartUpload()`: Creates S3 multipart session
  - `generatePresignedUrl()`: Creates secure upload URLs
  - `completeMultipartUpload()`: Finalizes S3 upload

#### SFRepository (Snowflake)
  - `createExternalStage()`: Links S3 data to Snowflake
  - `copyIntoTable()`: Bulk loads data from S3
  - `validateDataQuality()`: Runs quality checks

### Security Measures

#### 1. Authentication & Authorization
- JWT validation via AWS Cognito
- Role-based access control (RBAC)
- Organization-level permissions

#### 2. Encryption
- **At Rest**: AES-256-GCM in S3 and Snowflake
- **In Transit**: TLS 1.3 for all communications
- **Key Management**: AWS KMS with tripartite system

#### 3. Access Control
- IP whitelisting (Costa Rica only + approved institutions)
- Row-level security (RLS) in Snowflake
- Audit logging of all operations

#### 4. Data Protection
- Sensitive field encryption before storage
- Automated PII detection and masking
- Secure key reconstruction only during operations

### Data Transformation and AI Processing

![alt text](image.png)

#### **ETL Pipeline (AWS Glue)**
1. **Data Reading**
   - Glue reads chunks from S3 staging area
   - Detects file format (CSV, JSON, Parquet)
   - Applies schema inference

2. **Initial Processing**
   - **Merge**: Combines all chunks into unified dataset
   - **Basic Clean**: Removes obvious duplicates, handles nulls
   - **Format**: Converts to Parquet for efficient processing
   - **Output**: Stores cleaned data in S3 for AI processing

3. **Handoff to AI**
   - Glue job completes and triggers Step Function
   - Passes S3 location of processed data
   - Includes metadata about dataset characteristics

![image](https://github.com/user-attachments/assets/751408d1-674d-457b-b176-c10d02f73df6)

#### **AI Processing with SageMaker**

**AI Processing Flow:**

![image](https://github.com/user-attachments/assets/102f5e7b-8904-43d8-8c21-770ed9119730)

#### AI Components

**AI Agent Selection: AWS SageMaker with Snowflake Schema Integration**
- **Native S3 Integration**: Can directly process data from S3 without moving it
- **Scalability**: Handles datasets from MB to TB scale
- **Step Functions Integration**: Seamlessly fits into your existing orchestration
- **Cost-Effective**: Pay only for processing time, auto-scales down when idle
- **Model Flexibility**: Supports both custom models and pre-built algorithms

However SageMaker must communicate bi-directionally with Snowflake to propose schema changes.

![image](https://github.com/user-attachments/assets/744e1d01-967f-48da-b7d5-6b7c4b5c790a)

#### SageMaker and Snowflake Integration

```python
# Location: AI Processing Layer - Between Glue ETL and Snowflake Load
class SageMakerDataProcessor:
    """AI agent for pattern detection and schema evolution"""
    
    def __init__(self):
        self.sagemaker_client = boto3.client('sagemaker')
        self.snowflake_connector = SnowflakeConnection()
        self.schema_analyzer = SchemaEvolutionAnalyzer()
        
    def process_dataset(self, glue_output_path: str, dataset_metadata: dict):
        """Main entry point with schema awareness"""
        
        # Step 1: Get current Snowflake schema
        current_schema = self.get_snowflake_schema(dataset_metadata['target_table'])
        
        # Step 2: Analyze data AND existing schema together
        analysis_job = self.create_schema_aware_processing_job(
            data_path=glue_output_path,
            current_schema=current_schema,
            dataset_metadata=dataset_metadata
        )
        
        # Step 3: Get AI recommendations
        recommendations = self.wait_and_get_results(analysis_job)
        
        # Step 4: Process recommendations
        if recommendations['schema_changes_needed']:
            schema_evolution_plan = self.plan_schema_evolution(
                current_schema=current_schema,
                recommendations=recommendations,
                data_path=glue_output_path
            )
            
            # Step 5: Apply using Compensating Transaction Pattern
            self.apply_schema_evolution(schema_evolution_plan)
        
        # Step 6: Transform data to match new/existing schema
        transformed_path = self.transform_data_for_schema(
            glue_output_path,
            recommendations['data_transformations']
        )
        
        return transformed_path
    
    def get_snowflake_schema(self, table_name: str) -> dict:
        """Retrieves current schema from Snowflake"""
        query = f"""
        SELECT 
            column_name,
            data_type,
            is_nullable,
            column_default,
            comment
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position
        """
        
        current_schema = self.snowflake_connector.execute(query)
        
        # Also get relationships and constraints
        constraints = self.get_table_constraints(table_name)
        indexes = self.get_table_indexes(table_name)
        
        return {
            'columns': current_schema,
            'constraints': constraints,
            'indexes': indexes,
            'row_count': self.get_row_count(table_name)
        }
```

#### Schema Evolution Analyzer (Runs in SageMaker)

```python
class SchemaEvolutionAnalyzer:
    """Analyzes data patterns and proposes schema changes"""
    
    def analyze(self, data_sample: pd.DataFrame, current_schema: dict) -> dict:
        recommendations = {
            'schema_changes_needed': False,
            'changes': [],
            'data_transformations': []
        }
        
        # 1. Detect new columns in data not in schema
        new_columns = self.detect_new_columns(data_sample, current_schema)
        if new_columns:
            recommendations['schema_changes_needed'] = True
            recommendations['changes'].extend([
                {
                    'type': 'ADD_COLUMN',
                    'ddl': f"ALTER TABLE {{table}} ADD COLUMN {col['name']} {col['type']}",
                    'column': col
                } for col in new_columns
            ])
        
        # 2. Detect data type mismatches
        type_changes = self.detect_type_changes(data_sample, current_schema)
        for change in type_changes:
            recommendations['schema_changes_needed'] = True
            recommendations['changes'].append({
                'type': 'MODIFY_COLUMN',
                'ddl': f"ALTER TABLE {{table}} MODIFY COLUMN {change['column']} {change['new_type']}",
                'risk_level': 'HIGH' if change['requires_conversion'] else 'LOW'
            })
        
        # 3. Detect relationship opportunities
        relationships = self.detect_relationships(data_sample, current_schema)
        for rel in relationships:
            recommendations['changes'].append({
                'type': 'ADD_CONSTRAINT',
                'ddl': f"ALTER TABLE {{table}} ADD FOREIGN KEY ({rel['column']}) REFERENCES {rel['ref_table']}({rel['ref_column']})",
                'confidence': rel['confidence']
            })
        
        # 4. Detect optimization opportunities
        optimizations = self.detect_optimizations(data_sample, current_schema)
        recommendations['changes'].extend(optimizations)
        
        return recommendations
```

#### Compensating Transaction for Schema Evolution

```python
class SchemaEvolutionPipeline(DataModelTransformationPipeline):
    """Safely applies schema changes with rollback capability"""
    
    def __init__(self, snowflake_conn):
        super().__init__()
        self.sf = snowflake_conn
        self.staging_schema = 'STAGING_SCHEMA_CHANGES'
        
    def apply_schema_evolution(self, evolution_plan: dict):
        """Apply schema changes with full rollback capability"""
        
        # Step 1: Create staging schema with proposed changes
        staging_table = f"{self.staging_schema}.{evolution_plan['table']}_proposed"
        
        try:
            # Create copy of production table in staging
            self.sf.execute(f"""
                CREATE TABLE {staging_table} 
                CLONE {evolution_plan['table']}
            """)
            
            # Apply each proposed change to staging
            for change in evolution_plan['changes']:
                if change['type'] == 'ADD_COLUMN':
                    self.apply_add_column(staging_table, change)
                elif change['type'] == 'MODIFY_COLUMN':
                    self.apply_modify_column(staging_table, change)
                elif change['type'] == 'ADD_CONSTRAINT':
                    self.apply_add_constraint(staging_table, change)
            
            # Test data load into new schema
            test_success = self.test_data_load(
                staging_table, 
                evolution_plan['sample_data_path']
            )
            
            if test_success:
                # Validate data quality in new schema
                quality_check = self.validate_data_quality(staging_table)
                
                if quality_check['passed']:
                    # Apply to production
                    self.promote_to_production(staging_table, evolution_plan['table'])
                else:
                    # Rollback and alert
                    raise DataQualityException(quality_check['issues'])
            else:
                raise SchemaIncompatibilityException()
                
        except Exception as e:
            # Compensate: Clean up staging and alert human
            self.compensate(staging_table)
            self.alert_data_architect({
                'error': str(e),
                'plan': evolution_plan,
                'recommendation': 'Manual schema evolution required'
            })
            
            # Fallback: Transform data to fit existing schema
            return self.transform_to_existing_schema(evolution_plan)
        
        finally:
            # Always clean up staging
            self.cleanup_staging(staging_table)
```

#### Integration with Snowflake via Lambda

```python
# Lambda function that bridges SageMaker and Snowflake
def coordinate_schema_evolution(event, context):
    """Orchestrates schema evolution between SageMaker and Snowflake"""
    
    # Get SageMaker recommendations
    recommendations = event['sagemaker_output']
    
    if recommendations['schema_changes_needed']:
        # Connect to Snowflake
        conn = get_snowflake_connection()
        
        # Prepare evolution plan
        evolution_plan = {
            'table': event['target_table'],
            'changes': recommendations['changes'],
            'sample_data_path': event['data_path'],
            'approval_required': any(
                c['risk_level'] == 'HIGH' 
                for c in recommendations['changes']
            )
        }
        
        # High-risk changes need custodian approval
        if evolution_plan['approval_required']:
            approval_request_id = request_custodian_approval(evolution_plan)
            return {
                'status': 'PENDING_APPROVAL',
                'request_id': approval_request_id
            }
        
        # Apply schema evolution
        pipeline = SchemaEvolutionPipeline(conn)
        result = pipeline.apply_schema_evolution(evolution_plan)
        
        return {
            'status': 'SCHEMA_UPDATED',
            'changes_applied': result['applied_changes']
        }
    
    return {
        'status': 'NO_SCHEMA_CHANGES',
        'data_ready_for_load': True
    }
```

#### Pattern Detection Container

```python
# /opt/ml/code/pattern_detector.py - Runs inside SageMaker container
class PatternDetector:
    """Detects data patterns using trained ML models"""
    
    def __init__(self):
        self.models = {
            'duplicate_detector': self.load_model('duplicate_detection.pkl'),
            'relationship_finder': self.load_model('relationship_detection.pkl'),
            'anomaly_detector': self.load_model('anomaly_detection.pkl')
        }
        
    def detect_patterns(self, data_path: str) -> List[Pattern]:
        # Read sample of data (SageMaker provides high-memory instances)
        df = self.read_data_sample(data_path, sample_size='500MB')
        
        patterns = []
        
        # Detect duplicate columns
        duplicates = self.detect_duplicates(df)
        if duplicates:
            patterns.append(Pattern(
                type='DUPLICATE_COLUMNS',
                confidence=duplicates['confidence'],
                metadata={'columns': duplicates['column_pairs']}
            ))
        
        # Find relationships between datasets
        relationships = self.find_relationships(df)
        patterns.extend(relationships)
        
        # Detect anomalies and quality issues
        anomalies = self.detect_anomalies(df)
        patterns.extend(anomalies)
        
        return patterns
```

#### Integration with Step Functions

```json
{
  "Comment": "Dataset processing workflow with AI",
  "StartAt": "GlueETL",
  "States": {
    "GlueETL": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "initial-etl-job"
      },
      "Next": "InvokeSageMaker"
    },
    "InvokeSageMaker": {
      "Type": "Task", 
      "Resource": "arn:aws:states:::sagemaker:createProcessingJob.sync",
      "Parameters": {
        "ProcessingJobName.$": "$.dataset_id",
        "ProcessingInputs": [{
          "InputName": "input",
          "S3Input": {
            "S3Uri.$": "$.glue_output_path"
          }
        }]
      },
      "Next": "ApplyTransformations"
    },
    "ApplyTransformations": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:apply-transformations",
      "Next": "LoadToSnowflake"
    }
  }
}
```

#### Stimulus Processing Components
- **StimulusSelector**: Identifies relevant data patterns using SageMaker
- **MLModel**: Deployed as SageMaker endpoints for real-time inference
- **Transformation Agents**:
  - UnionAgent: Merges related columns detected by ML
  - SplitAgent: Separates nested data structures
  - AppendAgent: Handles incremental updates

### Design Patterns

![image](https://github.com/user-attachments/assets/b827b2b2-3a83-466f-bc37-be2e547b9079)

#### 1. Claim Check Pattern

**Purpose**: Handles large file uploads (500MB - 10GB+) by separating the actual data payload from the control flow, preventing memory overload and network timeouts.

**When It's Used**:
- Triggered immediately when `POST /datasets/upload/init` is called
- Active throughout the entire chunk upload phase
- Remains in use until `POST /datasets/upload/{session}/finalize` completes

**Where It's Implemented**:

```python
# Location: Service Layer - UploadManager & ChunkUploader
class ClaimCheckToken:
    """Token that travels through the system while data stays in S3"""
    def __init__(self):
        self.id = generate_uuid()
        self.chunk_metadata_list = []  # Only references, not data
        self.created_at = datetime.now()
        self.dataset_metadata = {}      # Size, format, schema info

class ChunkUploader:
    def upload(self, chunk: Chunk, token: ClaimCheckToken):
        # 1. Heavy data goes directly to S3
        s3_key = self.s3_repository.put_object(chunk.data)
        
        # 2. Only lightweight reference stored in token
        metadata = ChunkMetadata(
            checksum=chunk.checksum,
            sequence_id=chunk.sequence_id,
            s3_key=s3_key,              # Reference to S3 location
            size=chunk.size
        )
        token.chunk_metadata_list.append(metadata)
        
        # 3. Token passes through services, not the data
        return token  # Lightweight object
```

**How It Works**:
1. **Initial Request**: Client provides file metadata, not the file itself
2. **Token Creation**: System creates a ClaimCheckToken with unique ID
3. **Chunk Upload**: Each chunk uploaded directly to S3 via presigned URLs
4. **Reference Storage**: Only S3 keys and metadata stored in the token
5. **Processing**: ETL jobs retrieve data from S3 using references in token
6. **Memory Efficiency**: Services pass around 1KB tokens instead of GB of data

**Integration Points**:
- `DatasetHandler` → Creates initial token
- `S3Repository` → Stores actual data chunks
- `MetadataStore` → Persists token information
- `AWS Step Functions` → Passes token through ETL pipeline
- `AWS Glue` → Retrieves data using token references

#### 2. Compensating Transaction Pattern

**Purpose**: Ensures data transformations and model changes follow an "all or nothing" principle, with automatic rollback on failure and human escalation for complex issues.

**When It's Used**:
- Activated during the ETL phase after all chunks are uploaded
- Specifically when AI suggests structural changes to the data model
- Before data is committed to production Snowflake tables
- During any multi-step transformation that could partially fail

**Where It's Implemented**:

```python
# Location: AI Data Transformation Layer - After AWS Glue processes raw data
class DataModelTransformationPipeline:
    """Manages reversible transformations with compensation logic"""
    
    def __init__(self):
        self.steps = []
        self.compensation_log = DurableLog()  # AWS DynamoDB
        self.lock_manager = LockManager()      # Distributed locks
        
    def execute(self):
        # Phase 1: Acquire locks on affected datasets
        resources = self.identify_resources()
        for resource in resources:
            if not self.lock_manager.acquire(resource):
                raise ConcurrentModificationError()
        
        # Phase 2: Execute transformation steps
        completed_steps = []
        try:
            for step in self.steps:
                # Log state before execution
                self.compensation_log.write_entry(step.get_state())
                
                # Execute with timeout
                step.execute(timeout=300)  # 5 minutes max
                completed_steps.append(step)
                
        except Exception as e:
            # Phase 3: Compensate in reverse order
            self.compensate(completed_steps)
            
            # Phase 4: Human escalation
            self.alert_data_architect(e, self.compensation_log)
            raise
            
    def compensate(self, completed_steps):
        """Rollback completed steps in reverse order"""
        for step in reversed(completed_steps):
            compensator = step.get_compensator()
            compensator.compensate()

# Example transformation steps:
class ModelTransformationStep:
    """Base class for reversible transformations"""
    
    def execute(self):
        # Save current state
        self.original_schema = self.sf_repository.get_schema()
        # Apply transformation
        self.sf_repository.alter_table(self.new_schema)
        
    def get_compensator(self):
        return SchemaRollback(self.original_schema)
```

**How It Works**:
1. **Planning Phase**: AI analyzes data and suggests transformations
2. **Validation Phase**: Each transformation creates a compensation strategy
3. **Execution Phase**: Steps executed with state logging
4. **Success Path**: All steps complete → Commit to production
5. **Failure Path**: Any step fails → Automatic rollback → Human intervention

**Integration Points**:
- `AWS Glue Jobs` → Triggers pipeline after data validation
- `Snowflake` → Applies schema changes in staging environment
- `AWS Step Functions` → Orchestrates the pipeline
- `DynamoDB` → Stores durable compensation log
- `SNS` → Alerts data architects on failure

#### 3. Learning-Based Pattern

**Purpose**: Enables AI to automatically detect data patterns, classify content types, and apply intelligent transformations without explicit programming.

**When It's Used**:
- During ETL processing after chunks are merged
- When system encounters new data formats or structures
- For detecting relationships between datasets
- During data quality improvement and normalization

**Where It's Implemented**:

```python
# Location: AI Layer - Integrated with AWS Glue and SageMaker
class LearningBasedDataProcessor:
    """AI-driven pattern detection and transformation system"""
    
    def __init__(self):
        self.stimulus_selector = StimulusSelector()
        self.ml_models = {
            'supervised': SupervisedLearning(),    # For known patterns
            'unsupervised': UnsupervisedLearning() # For discovery
        }
        self.executor = TransformationExecutor()
        
    def process_dataset(self, dataset_id: str, raw_data_path: str):
        # Phase 1: Create stimuli from raw data
        stimuli = self.create_stimuli(dataset_id, raw_data_path)
        
        # Phase 2: Pattern detection
        patterns = self.detect_patterns(stimuli)
        
        # Phase 3: Agent selection and execution
        transformations = self.execute_transformations(stimuli, patterns)
        
        return transformations
    
    def create_stimuli(self, dataset_id: str, path: str):
        """Convert raw data into analyzable stimuli"""
        data_sample = self.s3_repository.read_sample(path, size='10MB')
        metadata = self.metadata_service.get(dataset_id)
        
        stimuli = []
        for column in data_sample.columns:
            stimulus = Stimulus(
                id=generate_uuid(),
                type=self.infer_type(column),
                metadata={
                    'column_name': column.name,
                    'data_types': column.detected_types,
                    'null_ratio': column.null_percentage,
                    'cardinality': column.unique_count
                },
                value=column.sample_values
            )
            stimuli.append(stimulus)
        return stimuli
    
    def detect_patterns(self, stimuli: List[Stimulus]):
        """AI detects patterns using both supervised and unsupervised learning"""
        patterns = []
        
        # Supervised: Match against known patterns
        known_patterns = self.ml_models['supervised'].classify(stimuli)
        patterns.extend(known_patterns)
        
        # Unsupervised: Discover new patterns
        discovered = self.ml_models['unsupervised'].find_clusters(stimuli)
        patterns.extend(discovered)
        
        return patterns
    
    def execute_transformations(self, stimuli, patterns):
        """Select and apply appropriate transformation agents"""
        results = []
        
        for pattern in patterns:
            # Select appropriate agent based on pattern type
            if pattern.type == 'DUPLICATE_COLUMNS':
                agent = UnionAgent()  # Merges similar columns
            elif pattern.type == 'NESTED_JSON':
                agent = SplitAgent()  # Flattens nested structures
            elif pattern.type == 'INCREMENTAL_DATA':
                agent = AppendAgent() # Handles delta updates
            else:
                agent = DefaultAgent()
                
            # Apply transformation
            result = agent.action(stimuli, pattern)
            results.append(result)
            
        return results

# Example Agent Implementation:
class UnionAgent(Agent):
    """Merges columns with similar data patterns"""
    
    def action(self, stimuli: List[Stimulus], pattern: Pattern) -> Output:
        # Identify columns to merge
        merge_candidates = pattern.metadata['similar_columns']
        
        # Create transformation plan
        transformation = {
            'operation': 'UNION_COLUMNS',
            'source_columns': merge_candidates,
            'target_column': self.generate_column_name(merge_candidates),
            'transformation_rules': self.create_merge_rules(stimuli)
        }
        
        # Execute via Snowflake
        sql = self.generate_merge_sql(transformation)
        self.sf_repository.execute(sql)
        
        return Output(
            status='SUCCESS',
            transformation=transformation,
            affected_rows=self.get_affected_rows()
        )
```

**How It Works**:
1. **Data Ingestion**: Raw data arrives in S3
2. **Stimuli Creation**: System samples data and creates analytical objects
3. **Pattern Detection**: AI models analyze stimuli for patterns
4. **Agent Selection**: System chooses appropriate transformation agents
5. **Transformation**: Agents apply changes in Snowflake staging
6. **Validation**: Results checked before production deployment

**Integration Points**:
- `AWS Glue` → Triggers AI processing after initial ETL
- `AWS SageMaker` → Provides ML capabilities for pattern detection and transformation
- `S3` → Source data location and intermediate storage
- `Step Functions` → Orchestrates the learning pipeline
- `Lambda` → Applies final transformations before Snowflake load

#### Monitoring

All upload operations are monitored via:
- AWS CloudWatch metrics
- Custom dashboards in Amazon QuickSight
- Real-time alerts for failures or slowdowns
- Usage tracking for billing and quotas

![alt text](image.png)

![image](https://github.com/user-attachments/assets/d5839f90-2cfd-4438-82fb-278102f37f5d)


![image](https://github.com/user-attachments/assets/102f5e7b-8904-43d8-8c21-770ed9119730)

![image](https://github.com/user-attachments/assets/751408d1-674d-457b-b176-c10d02f73df6)



### 2. Secure Data Sharing with Custodian Approval

#### Overview

This workflow facilitates the secure sharing of datasets within the Data Pura Vida platform, requiring approval from two custodians to ensure compliance with regulatory standards and organizational policies. The process leverages a tripartite key system, Role-Based Access Control (RBAC), Row-Level Security (RLS), and geographic restrictions, with all actions logged for auditability. The diagram illustrates the sequence of events from the requester's initial request to the final granting of access, including key reconstruction and purging.

#### Workflow Description

The workflow begins with a requester initiating a dataset access request, which the System validates. Approval requests are sent to two custodians (Custodian1 and Custodian2), who must both approve the request. Upon approval, the System reconstructs the access keys using the tripartite system, updates Snowflake with row-level permissions, and grants access to the requester. Post-access, the keys are purged from memory to maintain security. The process is orchestrated by the `SecurityManager`, `CustodianManager`, and `AccessControlService`, with integration into Snowflake and AWS services.

#### Steps

- Request Dataset Access
  - Actor: Requester
  - Action: The requester sends a request to access a dataset via `POST /sharing/datasets/{id}/share`.
  - System Interaction: The request is received by the System, initiating the workflow.
  - AWS Involvement:
    - Cognito: Validates the requester’s JWT token for authentication.
    - WAF: Filters the request to ensure it originates from Costa Rica or whitelisted IPs.
  - Location: Handler Layer(AWS Fargate)
  - Security: The `SecurityContextMiddleware` validates the requester’s identity, and `GeoRestrictionMiddleware` checks the IP against Costa Rica or whitelisted institutional IPs.
  - Design Patterns: Observer Pattern (request triggers validation event).
  - Principles: Single Responsibility (handler focuses on request routing), Least Privilege (Cognito restricts access to authenticated users).
- Validate Request
  - Actor: System
  - Action: The System validates the request, checking the requester’s permissions (`dataset.share`) and dataset eligibility using `AccessControlService`.
  - AWS Involvement:
    - IAM: Checks RBAC policies to ensure the requester has `dataset.share` permission.
    - Secrets Manager: Retrieves custodian metadata and dataset classification rules.
  - Location: Service Layer (AWS Fargate)
  - Process: The `SecurityManager` ensures compliance with RBAC and dataset classification.
  - Security: Validation logs are recorded in `/datapuravida/security/audit` via `AuditService`.
  - Design Patterns: Strategy Pattern (different validation strategies for different datasets).
  - Principles: Open/Closed (new datasets can be added without modifying existing code), Accountability (logs ensure traceability).
- Send Approval Request
  - Actor: System
  - Action: The System sends approval requests to Custodian1 and Custodian2 via AWS SNS (encrypted notifications).
  - AWS Involvement:
    - SNS: Sends notifications to custodians with a unique `request_id`.
    - Secrets Manager: Retrieves custodian details (email, roles) from `VaultRepository`.
    - KMS: Encrypts notification content.
  - Location: Service Layer (AWS Fargate) and AWS SNS
  - Components Involved:
    - CustodianManager: Assigns custodians based on dataset ownership and retrieves their details from `VaultRepository` (AWS Secrets Manager).
    - Notification Service: Delivers requests with a unique `request_id`.
  - Security: Notifications are encrypted, and custodian identities are validated with AWS IAM roles.
  - Design Patterns: Publish-Subscribe Pattern (SNS notifies custodians).
  - Principles: Data Minimization (only necessary data shared), Transparency (notifications logged).
- Approve Request
  - Actors: Custodian1 and Custodian2
  - Action: Each custodian reviews and approves the request via `POST /sharing/approve/{request_id}`, submitting their key share.
  - AWS Involvement:
    - Cognito: Validates custodian identities.
    - Secrets Manager: Retrieves custodian key shares from `VaultRepository`.
    - IAM: Validates custodian permissions for approval.
  - Location: Handler Layer (AWS Fargate) and AWS Services.
  - Components Involved:
    - CustodianApprovalHandler: Processes approval requests.
    - TripartiteKeyManager: Validates custodian signatures and prepares for key reconstruction.
  - Security: Both approvals are required within a time window. Unauthorized attempts trigger alerts via AWS CloudWatch.
  - Design Patterns: Chain of Responsibility (approval process requires both custodians).
  - Principles:  Fail-Safe (time-bound approval), Defense in Depth (multi-layer authentication).
- Reconstruct Access Keys
  - Actor: System
  - Action: The System reconstructs the dataset’s access keys using the tripartite shares via `TripartiteKeyManager`.
  - AWS Involvement:
    - KMS: Decrypts the key shares.
    - Secrets Manager: Retrieves the tripartite key shares from `VaultRepository`.
  - Location: Service Layer (AWS Fargate).
  - Process: Shamir’s Secret Sharing is applied to reconstruct the AES-256 key in secure memory.
  - Security: The key is temporary, used only for permission updates, and immediately purged post-operation (highlighted in the diagram).
  - Design Patterns: Command Pattern (key reconstruction as a secure command).
  - Principles: Ephemeral State (keys exist only during operation), Security by Design.
- Grant Row-Level Permissions
  - Actor: System
  - Action: The System updates Snowflake with row-level permissions for the requester using `AccessControlService`.
  - AWS Involvement:
    - Snowflake: Applies Row-Level Security (RLS) policies based on the reconstructed keys.
    - IAM: Ensures the System has permissions to modify Snowflake datasets.
    - KMS: Ensures encrypted data access.
  - Location: Service Layer (AWS Fargate) and Snowflake.
  - Components Involved:
    - SFRepository: Applies RLS policies in Snowflake.
    - DataProtectionService: Ensures sensitive columns remain encrypted and bulk downloads are prevented.
  - Process: Permissions are granted based on the sharing scope.
  - Security: Access is restricted to authorized IPs via `GeoAccessValidator` and logged in `/datapuravida/queries`.
  - Design Patterns: Adapter Pattern (IAM adapts Snowflake permissions).
  - Principles: Granularity (fine-grained access control), Least Privilege.
- Access Granted
  - Actor: Requester
  - Action: The System notifies the requester of access approval, enabling dataset access.
  - AWS Involvement:
    - SNS: Sends notification to the requester.
    - S3Repository: Generates presigned URLs for S3 artifacts if applicable.
  - Location: Handler Layer (AWS Fargate) and AWS S3.
  - Components Involved: `S3Repository` generates presigned URLs if S3 artifacts are involved.
  - Security: Access is logged, and results are delivered in non-downloadable formats.
  - Design Patterns: Facade Pattern (simplified access interface).
  - Principles: Usability (accessible format), Accountability (logging).
- Keys Purged from Memory
  - Actor: System
  - Action: After access is granted, the reconstructed keys are purged from memory to prevent unauthorized use.
  - AWS Involvement:
    - CloudWatch: Logs the purge operation.
    - KMS: Ensures no residual keys remain in memory.
  - Location: Service Layer (AWS Fargate).
  - Security: This step ensures compliance with security best practices, with the purge logged in `/datapuravida/security/audit`.
  - Design Patterns: Cleanup Pattern (post-operation resource release).
  - Principles: Zero Trust (no residual access), Auditability.

#### Key Components

1. SecurityManager: Orchestrates validation, key reconstruction, and permission updates.
2. TripartiteKeyManager: Manages key splitting and reconstruction using Shamir’s Secret Sharing.
3. CustodianManager: Assigns custodians and handles approval workflows.
4. AccessControlService: Enforces RBAC and RLS for access control.
5. AuditService: Logs all steps (validation, approvals, access) for compliance.
6. GeoAccessValidator: Ensures geographic compliance.
7. AWS Services: Cognito (authentication), KMS (encryption), SNS (notifications), CloudWatch (logging), Secrets Manager (key storage), Snowflake (data management).

#### Security and Compliance

1. Encryption: Data in transit uses TLS 1.3, and at rest uses AES-256 via AWS KMS. Access keys are reconstructed and purged per operation.
2. Auditability: All actions are logged with trace_id in CloudWatch, with a 7-year retention for security logs, meeting Law 8968 and GDPR requirements.
3. Regulatory Compliance: Ensures informed consent, data subject rights, and purpose limitation. Custodian approvals provide accountability.
4. Geographic Restriction: Enforced via AWS WAF and GeoAccessValidator, limiting access to Costa Rica or approved IPs.

Image Reference:
![image](https://github.com/user-attachments/assets/da4b0a49-1cdc-4904-bb44-a6315e683853)

### 3. AI-Powered Query Translation

#### Overview

This AI-driven workflow enables users to submit natural language (NL) queries that are securely translated into SQL statements, executed on Snowflake, and returned in a compliant, non-downloadable format. It leverages **Snowflake Cortex**, integrated with security, audit, and access control mechanisms to ensure data safety, performance (sub-200ms latency for 95% of queries), and policy enforcement.

#### Workflow Description

The system translates natural language queries into SQL, validates both the query and user permissions, executes the SQL on Snowflake, formats the result, and delivers a secure response. Invalid queries and unauthorized access are intercepted early, as shown in the flow diagram.

#### Step-by-Step Breakdown  

- Natural Language Query Submission
  - Endpoint: POST /ai/chat
  - User Action: A user submits an NL query (e.g., _“Show me the average population by province in the 2025 electoral dataset”_).
  - Component: AIQueryHandler receives the request.

- AI Service Invocation
  - Component: AIChatService receives the NL query.
  - Middlewares:
    - AuthenticationMiddleware: Validates JWT via AWS Cognito.
    - SecurityContextMiddleware: Captures user identity, roles, and IP.
    - GeoRestrictionMiddleware: Allows only Costa Rica or whitelisted IPs.
    - UsageLimitMiddleware: Enforces plan-based usage quotas.

- Query Validation
  - Purpose: Ensures the NL query can be safely and meaningfully processed.
  - Outcome:  
    - Valid Query: Proceeds to permission checks.  
    - Invalid Query: Returns an error (e.g., malformed, ambiguous).

- Permission Check
  - Component: AccessControlService
  - Validation: Ensures query.execute permission and dataset-level access.
  - Outcome:  
    - Sufficient Permissions: Proceeds to SQL generation.  
    - Insufficient Permissions: Returns “Access Denied”.
- SQL Generation
  - Component: AIChatService + MLModel
  - Process:
    - Parses intent (e.g., aggregate, filter).
    - Maps tokens to dataset schema (GET /datasets/{id}/schema).
    - Generates sanitized SQL using LLM models like **Snowflake Cortex**.
- Query Execution
  - Component: SFRepository, QueryExecutionService
  - Execution: Runs in a Snowflake virtual warehouse with auto-scaling.
  - Tracking:
    - GET /queries/{id}/status
    - GET /queries/{id}/results
  - Security:
    - Row-Level Security (RLS)
    - Encrypted in transit (TLS 1.3)
- Result Formatting
  - Component: AIChatService + DataProcessor
  - Output: Returned in user-specified format (e.g., JSON, table)
  - Optional Visualization: Integration with Amazon QuickSight
  - Security: DataProtectionService enforces:
    - Non-downloadable formats
    - Sensitive field masking
    - Output conversions (e.g., SVG, PDF)
- Response to User
  - Delivery: Results returned via API or embedded dashboards.
  - Sharing: Internal dashboards require custodian approval (POST /sharing/dashboards)
  - Audit: Execution and access events logged by AuditService (/datapuravida/queries)

#### Key Components

1. AIChatService: Translates NL to SQL, validates and optimizes queries
2. MLModel: Learns NL→SQL mappings using supervised learning
3. SFRepository: Executes SQL and manages result lifecycle
4. AccessControlService: Enforces RBAC and RLS access policies
5. DataProtectionService: Secures output formats, blocks unauthorized exports
6. SecurityManager: Coordinates auth, geo-restrictions, and classification compliance
7. AuditService: Logs all query activity and result access for regulatory audit
8. AWS Services: Cognito (auth), QuickSight (viz), KMS (encryption), WAF

#### Security and Compliance

- Encryption: TLS 1.3 (transit), AES-256 (at rest via AWS KMS)
- Audit Logging: Logs retained for 3 years; includes query, SQL, metadata
- Compliance:
  - Law 8968 (Costa Rica): Subject rights, limited processing
  - GDPR: Minimization, transparency
- Geo Restrictions: Requests must originate from approved IPs (CR-only)
- Performance SLA: 95% of queries return in <200ms (CloudWatch monitored)

![image](https://github.com/user-attachments/assets/9440c17d-f9d8-438f-87ea-667b7f0cac30)

## Data Layer Design

This document defines the architecture, configuration, and access patterns for the Data Layer of the system. It provides implementation-level guidance for developers and architects working on the core data flows, including the stage (raw) and production (refined) environments. The system is deployed in AWS Fargate, with integrations to several AWS-native services and Snowflake as the primary data engine.

### Data Architecture & Storage

#### a) Data Topology

1. **Cloud Service Technology:**

  - The data layer is composed of two primary environments: a Staging environment hosted in Amazon S3, and a Production environment hosted in Snowflake. The system uses AWS Glue and Step Functions for data orchestration and transformation.

  - Data ingestion from external sources is staged in S3, then ETL jobs transform and load this data into Snowflake for production use.

2. **Object-Oriented Design Patterns:**

  PENDIENTE

3. **Class Layers for Data Access:**

- **Repository Layer:** Classes with S3 for staging and Snowflake for production. Repositories are accesed by the main repositorie class and implemented using cloud-specific SDKs (Boto3, Snowflake Connector). Classes involved are `SFRepository`, `S3Repository` and `MainRepository`.

- **Service Layer:** Handles transformation logic, orchestration triggers, and data preparation.

4. **Configuration Policies/Rules:**

- Clear separation between staging and production environments

- Versioned S3 buckets with lifecycle policies

- Snowflake environment with separate schemas for staged, and curated data

- Automated ETL pipelines via AWS Glue

- Data transformation process to production data with AI

- Handle congested data access with Snowflake multi-cluster architecture with data blocks.

5. **Expected Benefits:**

Decoupling of ingestion and processing layers

Scalable architecture with clean separation of environments

Simplified rollback and audit through versioning and schema separation

6. Data Topology Classification:

- The data topology follows a **Distributed and Replicated Model**:

  - **Distributed:** Data is ingested from diverse sources and processed in parallel through AWS Step Functions and Glue jobs. The architecture scales horizontally across services.

  - **Replicated:** Staging data in S3 is versioned and often replicated across availability zones for durability, while Snowflake supports replication and Time Travel for high availability and fault tolerance.

#### b) Big Data Repository - Data Lake

1. **Cloud Service Technology:**

- Amazon S3 functions as the raw data lake, optimized for scale and throughput

- Snowflake acts as the enterprise data warehouse/data mart for curated and production data

- AWS Glue provides cataloging and ETL capabilities

2. **Cloud Design Patterns:**

- **Claim-check pattern:** Used to upload chunks of big payloads given by the client to S3. More information about the pattern in the following link: https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check

- **Compensating transaction patterm** Use to validate the steps the data transformation AI suggested. More information about the pattern un the following link: https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction

3. **Class Layers for Data Access:**

- Ingestion Handlers: Manage data arrival in S3 and trigger pipelines

- Glue Jobs / Services: Transform raw data into structured formats

- Snowflake Writers: Insert transformed data into appropriate schemas

4. **Configuration Policies/Rules:**

- Defined S3 folder hierarchy: /raw/, /staged/, /processed/

- Glue Data Catalogs and Crawlers auto-register schemas

- Snowflake Time Travel and Fail-safe features enabled

- Row-level access policies for sensitive datasets

5. **Expected Benefits:**

- Unified and centralized repository for all enterprise data

- Automated metadata management via Glue Catalog

- Flexible query engine through Snowflake for analytics and reporting

#### c) Database Engine

1. **Cloud Service Technology:**

- Snowflake as the primary production engine (relational, columnar storage, SQL-based analytics)

- Amazon S3 with Parquet/ORC formats for semi-structured or unstructured data

2. **Configuration Policies/Rules:**

- Snowflake auto-scaling policies configured

- Query tagging and warehouse monitoring enabled

- Schema versioning policies in place

3. **Expected Benefits:**

- High-performance analytics with Snowflake’s MPP engine

- Cost-effective storage and flexible data formats in S3

- Pluggable design to support new data engines

#### d) Tenancy and Data Security

1. **Cloud Service Technology:**

- AWS Cognito for user identity and federated access

- AWS KMS for key management and encryption of S3 buckets

- AWS Secrets Manager for storing Snowflake credentials

- Snowflake RBAC and Network Policies

2. **Object-Oriented Design Patterns:**

  SECURITY LAYER

3. **Class Layers for Data Access:**

  SECURITY LAYER

4. **Configuration Policies/Rules:**

- S3 encryption at rest and in transit

- Snowflake role-based access and row-level security

- Fine-grained IAM roles per microservice and Lambda function

- Access audits and alerts integrated with CloudWatch

5. **Expected Benefits:**

- Centralized and enforceable access control

- Granular permission model for multi-tenant architecture

- Encryption and auditability as standard features. Audit system with help of AWS Cloudwatch 

- Prevent any data engineer, DevOps personnel, or technical staff with privileges from accessing data in plain text or without proper authorization.

- Allow multiple levels of access with logical control, based on user, entity, or data type.

#### e) Recovery and Fault Tolerance

1. **Cloud Service Technology:**

- S3 Versioning & Replication for backup and disaster recovery

- Snowflake Time Travel and Fail-safe features

- CloudWatch Alarms, Step Functions Retries, and DLQs (Dead Letter Queues)

3. **Class Layers for Data Access:**

  AUDIT SYSTEM

4. **Configuration Policies/Rules:**

S3 Lifecycle Rules with Glacier for archival

Snowflake recovery window configured per schema

Circuit breakers for long-running queries

5. **Expected Benefits:**

- High availability and resilience across data layers

- Minimal data loss with versioned and replicated backups

- Cost-efficient long-term archival and legal compliance

### Object-Oriented Design - Programming

#### a) Transactionality

#### b) Use of ORM

#### c) Connection Pooling

#### d) Use of Cache

#### e) Drivers

#### f) Data Design

```
Qué hacer:
Diseñar arquitectura de almacenamiento masivo
BatchLoad
Implementar IA para normalización de datos
Crear sistema de detección de duplicados
Diseñar gestión de cargas delta
Implementar cifrado en reposo y en tránsito
Crear sistema de trazabilidad de datos
Anotaciones del profesor:
Batch o stream
Evitar repetir datos con LLM? 
Con contexto, se puede dar contexto para crear el modelo dinámico de datos. (Ver patrones de diseno de agentes para AI [Ejercicio 9])
Alteracion de diseno de tablas inteligentemente.
ETL = Extract-Transform-Design-Load
Unificación de datos
Merge de datos
Actualización parcial y deltas
Temas a investigar:
Identidad Digital
DID: Decentralized Identificaction
Diseno de procesos
Diseno de servicios
Tipos de registro: 
Diferente documentación
Diferente proceso de registro
Validaciones diferente: 
Validacion por AI 
Validacion de formatos de datos
Scanners de documentos (Naciona, extrangeros, 3rd party services)
Diseno de DB: Cada cloud tiene al menos una maquina de workflows
```

### Datalake

```
Ideas para el Data Lake, aqui hay un enlace para tener una definición concreta: https://www.geeksforgeeks.org/what-is-data-lake/

A continuación hay varios de los puntos del apartado que investigue y trate de buscar soluciones:

- La API debe desarrollarse en la misma tecnología cloud utilizada para los portales web del sistema.

Se puede utilizar lambda functions, cloud functions, azure functions.
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

- Toda interacción con la API debe estar protegida por mecanismos de acceso como whitelist de IPs, validación de tokens y MFA.

Esto lo puede manejar snowflake https://docs.snowflake.com/en/user-guide/security-mfa

- Las operaciones API deben cubrir: autenticación, validación de identidad, gestión de usuarios, operaciones sobre datasets, llaves de acceso, métricas, y procesos administrativos

AWS VPC endpoints sirven para whitelisting, etc
AWS secrets para validacion y segmentacion de info, credenciales, tokens

- La lógica de negocio debe garantizar trazabilidad, cumplimiento legal, y control de cada transacción realizada dentro del sistema

Snowflake tiene historial por usuario, por rol, warehouse, etc. Son los query history de snowflake
Para la parte legal, hay que asegurar que todo el historial se guarda, que hay un warehouse especifico, desde un IP especifico....

- Se deben incluir endpoints para gestionar accesos temporales, revocación de permisos, y control granular por rol y contexto.

Snowflake con aws, con middleware.
https://aws.amazon.com/financial-services/partner-solutions/snowflake/

- Aunque se llame “datalake”, puede ser cualquier infraestructura moderna que permita almacenamiento, consulta y gestión masiva de datos

AWS s3 para guardar los datos raw y luego en snowflake con los stages que jala los datos y los guarda. AWS Glue guarda todo raw y luego se pasa a snowflake ya que snowflake no puede almacenar datos raw, pasa por un proceso de ETL a snowflake, estructurado o semiestrucurado. Almacenamiento dentro de GLUE y gestion en snowflake

- Debe soportar millones de registros, miles de usuarios concurrentes, y un crecimiento dinámico de la información.

Snowflake, warehouse mas grande = crecimiento vertical, mas clusters = crecimiento horizontal.

- Usar inteligencia artificial para normalizar los modelos de datos, rediseñarlos según uso y relacionarlos automáticamente con datasets existentes

Snowflake for AI. https://www.snowflake.com/en/product/ai/

- Detectar y evitar duplicidad de datos durante cargas y transferencias

bronce layer (Data raw), silver layer (Para los devs, ing de datos para manipular), gold layer (para el end user). Duplicidad en el silver layer tener un master antes de echar los datos al master del silver layer se verifica si ese dato ya existe y asi no se duplica. AI es una alternativa, pero tambien estan los orquestadores como Apache Airflow (recomendado porque es agnostica que sirve con snowflake), AWS tambien tiene.

- Controlar y gestionar cargas delta, identificando diferencias entre cargas anteriores y actuales

Snowflake y tablas incrementales. Si se actualiza/manipula datos como manter la informacion intacta y no duplicada. Load data that hasn't been loaded yet. Snapshots anteriores, cargas las que van entrando. No es el orquestador. Snapshot de snowflake: https://docs.snowflake.com/en/sql-reference/sql/create-snapshot
dbt cargas delta: https://docs.getdbt.com/docs/build/incremental-models

- Ser eficiente en operaciones de merge de datos, sin perder integridad ni contexto

De nuevo, Bronce, silver y gold layer. Es conservar informacion relevante del goldlayer basicamente. Nulos, ceros, casos atipicos, incongruentes. Esto se maneja con reglas de negocios definidas entre nosotros y las instituciones, pero basicamente definidas anteriormente.

- Llevar trazabilidad continua de datos usados, no usados, descartados y archivados

Trazabilidad de las capas. De la gold toma tablas de la silver y asi, por medio de nodos se puede ver cuales son usados, no usados, descartados y archivados. Gobernanza las las personas deben documentar bien que es lo que hacen. Es como un arbol con nodos e hijos.
DBT gestor de datos, sirve para esto con gobernanza

- Tener monitoreo en tiempo real de estado, salud, tráfico, errores, cuellos de botella y uso por entidad o usuario

Entidad o usuario con snowflake sirve salud, tráfico, errores, cuellos de botella con orquestadores (airflow)

- Permitir múltiples niveles de acceso con control lógico, por usuario, entidad, o tipo de dato

Snowflake

- Implementar RBAC (control de acceso basado en roles) y RLS (restricción a nivel de fila) para segmentación fina

Snowflake https://docs.snowflake.com/en/user-guide/security-access-control-overview

- Toda la data sensible debe estar cifrada en reposo y en tránsito, y sus accesos siempre deben dejar registro auditable

Cualquier cosa que se haga en snowflake se registra y permite encriptacion

- Restringir IP whitelist importante,

hacer el acceso a datos por warehouses para accceder a datos en particular solo en esas tablas y ya.
Limitacion o restricciones a nivel de rol. 

- Por ultimo cifrado, encriptado, hashes, etc.
  https://docs.snowflake.com/en/sql-reference/functions/encrypt 



Buenas noches compañeros y 
@vsurak
.  A continuación voy a hacer una breve explicación de la investigación/análisis que he realizado en relación al diseño solución del caso 3 y algunas sugerencias hechas anteriormente por el profesor. A manera de aclaración la investigación tiene vinculo principalmente con la parte de "Pura Vida DataLake".
Primeramente, proporcionar dos videos que me parecieron de mucha utilidad para entender mejor Snowflake y como integrarlo a nuestro diseño:
1 - Getting Started - Architecture & Key Concepts: https://youtu.be/GtVwChmxdpw?si=4B9XBEY1BkyU4yK4
2- Getting Started: Introduction To Snowflake Virtual Warehouses: https://youtu.be/TeD5zshkdjY?si=9Vz-Y4WBu6H82gci
El segundo video se adentra en uno de los conceptos principales de SF, y el cual se describe en el primer video como una parte fundamental de su arquitectura. Ahora se presentarán algunas ideas para un par de puntos del diseño.

- Debe soportar millones de registros, miles de usuarios concurrentes, y un crecimiento dinámico de la información
Como se mencionó en observaciones pasadas SF solamente ofrece algoritmos y un diseño efectivo, por esto hay diferentes servicios de AWS que podrían servir. Se contempla AWS Lake Formation para construir, asegurar y administrar un data lake centralizado sobre Amazon S3 (Simple Storage Service), el cuál es sumamente escalable y no necesita predefinir limites de espacio.
Lo anterior se basa en separar responsabilidades para que el almacenamiento principal esté en cloud y SF se pueda centrar en otras cosas como análisis y procesamiento de datos a gran escala.
- El sistema estará basado inicialmente en servicios monolíticos con posibilidad de migrar a una arquitectura de microservicios en el futuro
Se tienen dos propuestas para este aspecto:
	1- Utilizar patrones como el "Modular Monolith", donde cada dominio (autenticación, compartición, 	visualización) se desarrolla como un módulo autónomo dentro del mismo despliegue.
	2- Implementar una arquitectura por capas separando handlers, servicios y repositorios.
- Se debe implementar versionamiento en los endpoints de la API y mantener compatibilidad hacia atrás en la medida posible
Hay diferentes prácticas como opciones en esté aspecto. Tanto el versionamiento en URL ó el versionamiento en headers son buenas prácticas pero se ven relacionadas a como se trabajará el backend, se debe de discutir más esto último con el equipo de trabajo.
Una referencia de versionamiento en URL (Norma en API´s REST): https://medium.com/@espinozajge/versionamiento-de-apis-rest-mejores-prácticas-y-consideraciones-4b5021dd0a11
Por último por el momento, para el tema del pricing de Snowflake se ha investigado también. Snowflake utiliza un modelo de pago por consumo, lo que significa que solamente se paga por lo que se usa. Entre las consideraciones de costos están los siguientes:
Almacenamiento de datos -> Se cobra por terabyte (TB) al mes, dependiendo de la región y proveedor de nube.
Fuerza de computación -> Se paga por uso mediante créditos Snowflake. Las unidades principales de cómputo son los "virtual warehouses", agrupados por tamaño.
Funciones Serverless
Servicios en la nubes -> Snowflake coordina autenticación, seguridad y compilación de consultas.
Es importante mencionar que hay diferentes ediciones que corresponden a diferentes perfiles de clientes, los créditos en cada edición cambian en su precio por ejemplo.
Toda la información viene de la guía oficial de SF sobre su pricing, a continuación el link:
https://www.snowflake.com/wp-content/uploads/2023/12/The-Simple-Guide-to-Snowflake-Pricing.pdf
```

## QUALITY AND TESTING

### Test Strategy

The testing strategy for Data Pura Vida ensures system reliability, performance, security, and compliance with functional and non-functional requirements. It encompasses unit tests, integration tests, end-to-end (E2E) tests, security tests, and load/performance tests, covering all components (frontend, backend, data layer, and AI services). The strategy aligns with the system’s 99.9% SLA, <200ms query latency.

#### Unit Tests

**Objective**: Validate individual components in isolation to ensure correct functionality of business logic, security mechanisms, and data operations.

- Scope:
  - Frontend: React components, hooks, and utilities (e.g., authentication flows, dashboard rendering).
  - Backend: Flask services (e.g., DatasetService, AccessControlService, AIChatService), middleware (e.g., SecurityContextMiddleware, GeoRestrictionMiddleware), and repository methods (e.g., SFRepository, S3Repository).
  - AI Layer: MLModel for NL-to-SQL translation, StimulusSelector for data classification, and transformation agents (UnionAgent, SplitAgent).
  - Security: TripartiteKeyManager key splitting/reconstruction, CustodianManager approval workflows.
  - Data Layer: Snowflake query execution, S3 file handling, and ETL transformations.

- Tools:
  - Frontend: React Testing Library, Jest.
  - Backend: pytest, unittest (Python).
  - AI: Custom test harnesses for ML model validation using pytest.
  - Data: Snowflake’s TEST functions for data quality checks (e.g., uniqueness, not_null constraints).

- Standards:
  - Minimum 90% code coverage for business logic and services (enforced via CI/CD).
  - Mock external dependencies (e.g., AWS SDK, Snowflake Connector) using moto and unittest.mock.
  - Test cases must cover edge cases (e.g., invalid inputs, expired tokens, unauthorized access).

#### Integration Testing

**Objective**: Validate interactions between system components, including APIs, services, middleware, and external services (AWS, Snowflake).

- Scope:
  - API endpoints: Test `/auth/login`, `/datasets/upload`, `/queries/execute`, `/ai/chat`, and `/sharing/datasets/{id}/share`.
  - Middleware: Ensure `SecurityContextMiddleware`, `GeoRestrictionMiddleware`, and `UsageLimitMiddleware` correctly process requests.
  - Data Layer: Validate S3-to-Snowflake ETL pipelines via AWS Glue and Snowpipe.
  - Security: Test RBAC/RLS enforcement and tripartite key workflows.
  - AI: Verify NL query translation, execution, and result formatting.

- Tools:
  - Postman/Newman for API testing.
  - pytest with Snowflake Connector for data layer tests.
  - AWS SDK (Boto3) for testing S3, KMS, and Cognito integrations.
  - Snowflake Query History for validating query execution outcomes.

- Standards:
  - Tests must simulate real-world scenarios.
  - Use temporary Snowflake warehouses and S3 staging buckets for isolated test environments.
  - Validate error handling.

#### End-to-End (E2E) Testing

**Objective**: Validate complete user journeys, ensuring all components work together as expected, from frontend interactions to backend processing and data retrieval.

- Scope:
  - User registration and authentication with MFA and biometrics.
  - Dataset upload, encryption, and sharing with custodian approval.
  - AI-powered query submission and dashboard visualization.
  - Backoffice operations (e.g., user management, audit log review).
  - Monetization workflows (e.g., dataset purchase, usage tracking).

- Tools:
  - Cypress for frontend E2E testing (React Native UI).
  - Selenium for backoffice interface testing.
  - Custom scripts for simulating multi-user workflows.
  - AWS Step Functions for orchestrating E2E test scenarios.

- Standards:
  - Tests must cover all UX journeys (see provided diagrams).
  - Simulate production-like environments using AWS Fargate and Snowflake staging warehouses.
  - Validate compliance with accessibility standards (e.g., screen reader support, keyboard navigation).

#### Security Testing

**Objective**: Identify vulnerabilities, ensure data protection, and validate compliance with security policies.

- Scope:
  - Penetration testing for API endpoints, focusing on authentication, authorization, and data access.
  - Static code analysis for security vulnerabilities (e.g., OWASP Top 10).
  - Dynamic analysis of AI models to detect biases or data leakage.
  - Security audits of AWS services (IAM roles, KMS keys, S3 bucket policies).

- Tools:
  - OWASP ZAP for dynamic security testing.
  - Bandit for static code analysis (Python).
  - Custom scripts for testing tripartite key workflows and custodian approvals.
  - AWS Inspector for infrastructure security assessments.

- Standards:
  - All security tests must be automated and integrated into the CI/CD pipeline.
  - Vulnerabilities must be categorized (e.g., critical, high, medium, low) and remediated based on risk.
  - Regular security audits every 6 months or after major changes.

#### Load and Performance Testing

**Objective**: Validate system performance under expected load, ensuring SLA compliance and identifying bottlenecks.

- Scope:
  - API performance under concurrent user load (e.g., 1000+ users).
  - Snowflake query execution performance (e.g., sub-200ms latency for 95% of queries).
  - Data ingestion and transformation throughput (e.g., S3 to Snowflake ETL jobs).

- Tools:
  - Apache JMeter for API load testing.
  - Locust for simulating user traffic and measuring response times.
  - Snowflake Query Profiling for analyzing query performance.
  - AWS CloudWatch for monitoring resource utilization (CPU, memory, I/O).

- Standards:
  - Load tests must simulate peak usage scenarios (e.g., end-of-month reporting).
  - Performance metrics must be collected and analyzed for trends.
  - Bottlenecks must be identified and addressed (e.g., scaling Snowflake warehouses, optimizing queries).

#### Implementation Guidelines

- CI/CD Integration: All tests are integrated into GitHub Actions pipelines, running on every pull request to develop and main.
- Test Environments: Use separate AWS accounts and Snowflake warehouses for staging and testing to avoid production data contamination.
- Test Data: Use synthetic datasets mimicking real-world scenarios with PII redacted.
- Monitoring: Test results are logged in CloudWatch, with failures triggering SNS alerts.
- Compliance: Security tests align with Law 8968 and GDPR, ensuring auditability and data protection.

## DEVOPS AND DEPLOYMENT

### Gestión de Código

The DevOps and deployment strategy for Data Pura Vida leverages modern cloud-native practices to ensure reliable, scalable, and secure deployments. It builds on the existing Git Flow branching model, CI/CD pipelines, and Blue-Green deployment strategy, integrating AWS services, Snowflake, and robust monitoring.

### Code Management

- Version Control:
  - Repository: Hosted on GitHub, using Git as the version control system.
  - Branching Strategy: Follows Git Flow (see provided table: `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`).
  - Commit Standards: Adhere to Conventional Commits for traceability and automated changelog generation.

- Code Quality:
  - Linting:
    - Frontend: ESLint with Airbnb rules for React.
    - Backend: Pylint and Black for Python/Flask.
  - Formatting: Prettier (frontend), Black (backend) enforced via pre-commit hooks.
  - Code Reviews: Mandatory pull request reviews with at least one approval, enforced via GitHub branch protection rules.
  - Documentation: API specs, architecture diagrams, and guides versioned in the repository.

### CI/CD Pipeline

#### Continuous Integration

- Tool: GitHub Actions.
- Triggers: Runs on every push to feature/*, develop, and main branches.
- Pipeline Steps:
  - Checkout code and cache dependencies.
  - Install dependencies (npm for frontend, pip for backend).
  - Run linters (ESLint, Pylint).
  - Execute unit and integration tests (Jest, pytest).
  - Perform security scans (OWASP ZAP).
  - Build Docker images for Flask API and React Native frontend.
- Standards:
  - All checks must pass before PR approval.
  - Code coverage reports uploaded to GitHub PRs.
  - Security scan results reviewed by security specialists.

#### Continuous Deployment

- Tool: GitHub Actions with Terraform for infrastructure as code (IaC).
- Environments:
  - Staging: Deploys to develop branch automatically, no approval required.
  - Production: Deploys to main branch with manual approval from the Product Manager.
- Deployment Strategy: Blue-Green deployment using AWS Fargate and Application Load Balancer (ALB).
  - Blue Environment: Current production (stable).
  - Green Environment: New version, validated via health checks and tests.
  - Traffic shifts to Green via ALB after validation; Blue retained for 24 hours for rollback.
- Steps:
  - Provision infrastructure (Fargate, S3, Snowflake, VPC) using Terraform.
  - Deploy Flask API and React Native frontend as Docker containers on Fargate.
  - Run post-deployment health checks (API endpoints, Snowflake connectivity).
  - Validate performance metrics (<200ms query latency, <0.1% error rate).
  - Rollback to Blue environment if checks fail.
- Standards:
  - Environment variables injected securely via AWS Secrets Manager.
  - Deployments logged in CloudWatch with SNS alerts for failures.
  - Rollback mechanism automated via Terraform scripts.

### Infrastructure as Code

- Tool: Terraform.
- Scope:
  - AWS Resources: Fargate, S3, KMS, Cognito, WAF, CloudWatch, QuickSight, Step Functions, Glue, Lambda.
  - Snowflake: Warehouses, schemas, roles, and network policies.
- Standards:
  - Modular Terraform modules for each service.
  - Versioned in GitHub, with separate state files for staging and production.
  - Infrastructure changes require PR review and approval.
- Benefits:
  - Reproducible environments.
  - Automated recovery playbooks for disaster scenarios (<2-hour recovery time).

### Monitoring and Operations

- Tools:
  - AWS CloudWatch: Captures logs, metrics, and alerts for Fargate, S3, and Lambda.
  - Snowflake Query History: Tracks query performance and data access.
  - Amazon QuickSight: Real-time dashboards for system health, dataset usage, and billing.
  - AWS CloudTrail: Audits all API calls and configuration changes.
- Metrics (see KPIs in Strategy and Planning):
  - System Availability: ≥99.9%.
  - Query Latency: <200ms (P95).
  - Error Rate: <0.1%.
  - Data Ingestion: <2 minutes for 1GB files.
-Alerts:
  - SNS notifications for downtime, errors, or security incidents.
  - Threshold-based alerts for usage limits and performance degradation.
- High Availability:
  - Fargate auto-scaling for API traffic spikes.
  - Snowflake multi-cluster architecture for query load balancing.
  - S3 versioning and Snowflake Time Travel for data recovery.

### Disaster Recovery

- Backup Strategy:
  - S3: Daily full backups, 4-hour incremental backups with versioning.
  - Snowflake: Daily snapshots with Time Travel (7-day retention).
  - Metadata: Stored in AWS Secrets Manager and backed up daily.
- Recovery Playbooks:
  - Automated via Terraform and AWS Step Functions.
  - Recovery time: <2 hours for critical failures.
  - Tested quarterly to validate 99.9% SLA.
- Failover:
  - Multi-AZ deployment for S3 and Fargate.
  - Snowflake replication across regions for fault tolerance.

## EVALUATION AND IMPROVEMENT

### Architecture Compliance Matrix

| Requirement | Compliance Status | Evidence | Notes |
|-------------|-------------------|----------|-------|
| 99.9% System Availability | Compliant | Blue-Green deployment, Fargate auto-scaling, Snowflake multi-cluster | Quarterly DR tests validate SLA |
| <200ms Query Latency | Compliant | Snowflake Query Profiling, CloudWatch metrics | Validated in performance tests |
| Support 200 Concurrent Users (Year 5) | Compliant | Fargate auto-scaling, Snowflake MPP architecture | Load tests simulate peak usage |
| AES-256 Encryption | Compliant | AWS KMS for data at rest, TLS 1.3 for transit | Security audits confirm compliance |
| GDPR Compliance | Compliant | Data minimization, user consent, right to erasure | DPO assigned for oversight |
| ISO 27001 Compliance | Compliant | Security policies, access controls, audit logs | Regular audits scheduled |
| AI-Powered Data Normalization | Compliant | Snowflake Cortex, MLModel for ETDL | Validated in integration tests |
| Tripartite Key System | Compliant | Shamir’s Secret Sharing, custodian approvals | Security tests confirm robustness |
| Geographic Restriction | Compliant | GeoRestrictionMiddleware, AWS WAF | Penetration tests validate enforcement |

### Analysis of Advantages/Disadvantages

#### Design Strengths

- Scalability:
  - AWS Fargate and Snowflake auto-scaling support millions of records and thousands of concurrent users.
  - S3 and Snowflake handle 10TB/year data growth without manual intervention.
- Security:
  - AES-256 encryption, TLS 1.3, and tripartite key system ensure data protection.
  - RBAC, RLS, and geographic restrictions align with GDPR.
- Compliance:
  - Comprehensive audit logging ensures traceability.
  - Privacy by design and data subject rights support regulatory requirements.
- Flexibility:
  - Monolithic architecture with modular design supports future migration to microservices.
  - AI-driven ETDL and NL query processing enhance usability and innovation.
- Reliability:
  - Blue-Green deployment ensures zero-downtime updates.
  - Automated backups and recovery playbooks achieve <2-hour recovery time.

#### Known Limitations

- Monolithic Architecture:
  - While modular, the monolith may face scaling bottlenecks compared to microservices for very high loads beyond year 5.
  - Tight coupling of components increases complexity for large-scale changes.
- Cost Management:
  - Snowflake’s pay-per-use model and Fargate scaling may lead to high costs if not optimized.
  - Lack of real-time cost monitoring dashboards (planned for future iterations).
- AI Dependency:
  - NL-to-SQL translation accuracy depends on Snowflake Cortex training quality.
  - Limited fallback mechanisms if AI fails to interpret complex queries.
- Geographic Restriction Overhead:
  - IP whitelisting via AWS WAF may complicate access for legitimate users outside Costa Rica like remote workers.
- Onboarding Complexity:
  - Tripartite key system and custodian approvals may slow down dataset sharing for new users.

#### Proposals for Future Improvements  

- Cost Optimization:
  - Implement AWS Cost Explorer dashboards and Snowflake resource monitors to track usage and optimize spending.
  - Introduce query cost estimation before execution to prevent expensive operations.
- AI Enhancements:
  - Integrate AWS SageMaker for custom ML models as a fallback for Cortex failures.
  - Develop a feedback loop for users to refine NL-to-SQL translations.
- Simplified Onboarding:
  - Streamline custodian approval workflows with automated reminders and pre-approved IP ranges.
  - Provide guided UI wizards for dataset sharing and permission configuration.
- Global Access with Compliance:
  - Explore secure VPN solutions or proxy services for non-Costa Rica users while maintaining geographic compliance.
  - Implement dynamic IP registration for trusted institutions.

#### Evolution Roadmap

| Phase | Timeline | Objectives |
|-------|----------|------------|
| Short-Term (0-6 months) | Q3-Q4 2025 | Implement cost monitoring dashboards, optimize Snowflake query performance |
| Mid-Term (6-18 months) | Q1 2026 - Q2 2027 | Transition to microservices for high-traffic services |
| Long-Term (18+ months) | Q3 2027 + | Integrate advanced AI models (SageMaker), support global access with VPN |
