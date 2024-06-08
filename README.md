# liquid

An SDK for security tools for automation purposes.

# UML Diagram
```mermaid
classDiagram
Aqua <|-- Authentication
Aqua: dict auth_payload
Aqua *-- Client

Authentication : dict auth_options
Authentication: authentication()
Authentication: authentication_basic()

Client: str service
Client <-- CWP
Client <-- SCS
Client <-- CSPM
Client <-- Settings

CWP <-- ImageAssurancePolicy
CWP: GetImage(name)
CWP: GetImages()
CWP: GetVulnerabilities()
CWP: GetHostAssurancePolicy()
CWP: GetK8sAssurancePolicy()
CWP: GetContainerRuntimePolicy()
CWP: GetHostRuntimePolicy()

Settings <-- ApplicationScopes
Settings <-- Users
Settings <-- PermissionSets
Settings <-- Roles
Settings <-- SSORoleMappings
Settings <-- Labels

Users: str endpoint
Users: str login_id
Users: str name
Users: str email
Users: str password
Users: bool first_time
Users: bool is_super
Users: bool ui_access
Users: list actions
Users: list scopes
Users: str role
Users: list roles
Users: str user_type

Roles: str name
Roles: str description
Roles: str author
Roles: str updated
Roles: str permission
Roles: list scopes

PermissionSets: str name
PermissionSets: str description
PermissionSets: str author
PermissionSets: str updated
PermissionSets: bool ui_access
PermissionSets: bool is_super
PermissionSets: list actions

ImageAssurancePolicy: Get()
ImageAssurancePolicy: Create()
ImageAssurancePolicy: Update()

ApplicationScopes: Get()
ApplicationScopes: Create()
ApplicationScopes: Update()
```