#!/usr/bin/env python3
"""
Comprehensive IAM Guide Page Generator
Generates all pages with real enterprise depth, scenarios, and technical details
"""

import os

# Common HTML template parts
def get_header(title, section_name, active_section_num):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="page-wrapper">
    <button class="mobile-menu-toggle" aria-label="Toggle navigation">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
'''

def get_nav_sidebar(active_page):
    """Generate navigation sidebar with proper active states"""
    sections = {
        1: ("IAM Foundations", [
            ("1-1-iam-overview.html", "IAM Overview"),
            ("1-2-authn-vs-authz.html", "Authentication vs Authorization"),
            ("1-3-identity-lifecycle.html", "Identity Lifecycle"),
            ("1-4-access-control-models.html", "Access Control Models"),
            ("1-5-least-privilege-sod.html", "Least Privilege & SoD"),
            ("1-6-directory-services.html", "Directory Services"),
            ("1-7-identity-governance.html", "Identity Governance"),
            ("1-8-privileged-access.html", "Privileged Access"),
        ]),
        2: ("Authentication Protocols", [
            ("2-1-authentication-factors.html", "Authentication Factors"),
            ("2-2-kerberos.html", "Kerberos"),
            ("2-3-ntlm.html", "NTLM"),
            ("2-4-saml.html", "SAML"),
            ("2-5-oauth2.html", "OAuth 2.0"),
            ("2-6-oidc.html", "OpenID Connect"),
            ("2-7-radius-tacacs.html", "RADIUS & TACACS+"),
            ("2-8-certificates-pki.html", "Certificates & PKI"),
            ("2-9-sso-mechanisms.html", "SSO Mechanisms"),
            ("2-10-auth-attacks-defense.html", "Auth Attacks & Defense"),
        ]),
        3: ("Federation & SSO", [
            ("3-1-federation-fundamentals.html", "Federation Fundamentals"),
            ("3-2-saml-federation.html", "SAML Federation"),
            ("3-3-oidc-federation.html", "OIDC Federation"),
            ("3-4-ws-federation-legacy.html", "WS-Federation & Legacy"),
            ("3-5-b2b-b2c-federation.html", "B2B & B2C Federation"),
            ("3-6-federation-troubleshooting.html", "Federation Troubleshooting"),
        ]),
        4: ("Microsoft Entra ID", [
            ("4-1-entra-overview.html", "Entra ID Overview"),
            ("4-2-entra-objects.html", "Entra ID Objects"),
            ("4-3-conditional-access.html", "Conditional Access"),
            ("4-4-entra-pim.html", "Entra PIM"),
            ("4-5-entra-governance.html", "Entra Governance"),
            ("4-6-entra-protection.html", "Entra Protection"),
            ("4-7-hybrid-identity.html", "Hybrid Identity"),
            ("4-8-entra-workload-id.html", "Workload Identity"),
        ]),
        5: ("Okta", [
            ("5-1-okta-overview.html", "Okta Overview"),
            ("5-2-okta-authentication.html", "Okta Authentication"),
            ("5-3-okta-authorization.html", "Okta Authorization"),
            ("5-4-okta-lifecycle.html", "Okta Lifecycle"),
            ("5-5-okta-integration.html", "Okta Integration"),
            ("5-6-okta-admin.html", "Okta Administration"),
        ]),
        6: ("SailPoint & IGA", [
            ("6-1-sailpoint-overview.html", "SailPoint Overview"),
            ("6-2-iga-fundamentals.html", "IGA Fundamentals"),
            ("6-3-access-certifications.html", "Access Certifications"),
            ("6-4-role-management.html", "Role Management"),
            ("6-5-sod-management.html", "SoD Management"),
            ("6-6-provisioning-workflows.html", "Provisioning Workflows"),
        ]),
        7: ("Privileged Access (PAM)", [
            ("7-1-pam-overview.html", "PAM Overview"),
            ("7-2-password-vaulting.html", "Password Vaulting"),
            ("7-3-session-management.html", "Session Management"),
            ("7-4-jit-access.html", "Just-in-Time Access"),
            ("7-5-secrets-management.html", "Secrets Management"),
            ("7-6-pam-vendors.html", "PAM Vendors"),
        ]),
        8: ("Cloud IAM", [
            ("8-1-aws-iam.html", "AWS IAM"),
            ("8-2-aws-identity-center.html", "AWS Identity Center"),
            ("8-3-azure-rbac.html", "Azure RBAC"),
            ("8-4-gcp-iam.html", "GCP IAM"),
            ("8-5-multi-cloud-identity.html", "Multi-Cloud Identity"),
            ("8-6-kubernetes-iam.html", "Kubernetes IAM"),
            ("8-7-infrastructure-as-code.html", "Infrastructure as Code"),
            ("8-8-cloud-pam.html", "Cloud PAM"),
        ]),
        9: ("IAM Architecture", [
            ("9-1-enterprise-iam-arch.html", "Enterprise IAM Architecture"),
            ("9-2-zero-trust-iam.html", "Zero Trust IAM"),
            ("9-3-hybrid-cloud-iam.html", "Hybrid Cloud IAM"),
            ("9-4-ciam-architecture.html", "CIAM Architecture"),
            ("9-5-api-security.html", "API Security"),
            ("9-6-high-availability.html", "High Availability"),
        ]),
        10: ("IAM Migrations", [
            ("10-1-migration-planning.html", "Migration Planning"),
            ("10-2-idp-migrations.html", "IdP Migrations"),
            ("10-3-legacy-modernization.html", "Legacy Modernization"),
            ("10-4-iga-pam-migrations.html", "IGA & PAM Migrations"),
            ("10-5-app-migration.html", "Application Migration"),
            ("10-6-coexistence-cutover.html", "Coexistence & Cutover"),
        ]),
        11: ("Security & Attacks", [
            ("11-1-identity-threat-landscape.html", "Identity Threat Landscape"),
            ("11-2-credential-attacks.html", "Credential Attacks"),
            ("11-3-token-session-attacks.html", "Token & Session Attacks"),
            ("11-4-privilege-escalation.html", "Privilege Escalation"),
            ("11-5-detection-response.html", "Detection & Response"),
        ]),
        12: ("Reference & Interview", [
            ("12-1-iam-glossary.html", "IAM Glossary"),
            ("12-2-interview-questions.html", "Interview Questions"),
            ("12-3-scenario-questions.html", "Scenario Questions"),
            ("12-4-protocol-flows.html", "Protocol Flows"),
            ("12-5-comparison-tables.html", "Comparison Tables"),
            ("12-6-cli-api-reference.html", "CLI & API Reference"),
        ]),
    }
    
    # Find active section
    active_section = None
    for sec_num, (sec_name, pages) in sections.items():
        for page_file, _ in pages:
            if page_file == active_page:
                active_section = sec_num
                break
    
    nav_html = '''    <nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
      <div class="sidebar-nav">
'''
    
    for sec_num, (sec_name, pages) in sections.items():
        is_active_section = (sec_num == active_section)
        collapsed = "" if is_active_section else " collapsed"
        active_class = " active" if is_active_section else ""
        
        nav_html += f'''        <div class="nav-section">
          <div class="nav-section-header{collapsed}{active_class}"><span>{sec_num}. {sec_name}</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
'''
        for page_file, page_title in pages:
            page_active = " active" if page_file == active_page else ""
            nav_html += f'            <a href="{page_file}" class="nav-item{page_active}">{page_title}</a>\n'
        
        nav_html += '''          </div>
        </div>
'''
    
    nav_html += '''      </div>
    </nav>
'''
    return nav_html

def get_footer():
    return '''
  <script src="main.js"></script>
</body>
</html>'''

def get_page_nav(prev_page, prev_title, next_page, next_title):
    nav = '          <nav class="page-nav">\n'
    if prev_page:
        nav += f'''            <a href="{prev_page}" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">{prev_title}</span>
            </a>
'''
    if next_page:
        nav += f'''            <a href="{next_page}" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">{next_title}</span>
            </a>
'''
    nav += '          </nav>\n'
    return nav

# ============================================================================
# PAGE CONTENT DEFINITIONS - Each page with comprehensive enterprise content
# ============================================================================

PAGE_CONTENT = {}

# 1-1 IAM Overview - Already comprehensive, will be handled separately
# 1-2 Authentication vs Authorization
PAGE_CONTENT["1-2-authn-vs-authz.html"] = {
    "title": "Authentication vs Authorization",
    "badge": "L1 Fundamentals",
    "section": "IAM Foundations",
    "prev": ("1-1-iam-overview.html", "IAM Overview"),
    "next": ("1-3-identity-lifecycle.html", "Identity Lifecycle"),
    "content": '''
          <div class="overview-box">
            <h3>🎯 What This Page Covers</h3>
            <p>
              The fundamental distinction every IAM professional must understand: proving WHO you are 
              (authentication) versus what you're ALLOWED to do (authorization). This page covers 
              real-world examples, common mistakes, and how these concepts apply in enterprise environments.
            </p>
          </div>

          <h2 id="core-concepts">The Core Concepts</h2>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    AUTHENTICATION vs AUTHORIZATION                                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                          AUTHENTICATION (AuthN)                                  │   │
│   │                          "Who are you?"                                          │   │
│   │                                                                                  │   │
│   │   USER ──────► [ Username + Password ] ──────► IDENTITY VERIFIED ✓              │   │
│   │                [ + MFA Code         ]                                            │   │
│   │                                                                                  │   │
│   │   Examples:                                                                      │   │
│   │   • Entering badge code at office door                                          │   │
│   │   • Logging into Windows with username/password                                 │   │
│   │   • Scanning fingerprint on phone                                               │   │
│   │   • Entering MFA code from authenticator app                                    │   │
│   │                                                                                  │   │
│   │   Result: System knows WHO you are (identity established)                       │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                          │                                              │
│                                          ▼                                              │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                          AUTHORIZATION (AuthZ)                                   │   │
│   │                          "What can you do?"                                      │   │
│   │                                                                                  │   │
│   │   VERIFIED USER ──────► [ Check Permissions ] ──────► ACCESS GRANTED/DENIED     │   │
│   │                         [ Check Roles       ]                                    │   │
│   │                         [ Check Policies    ]                                    │   │
│   │                                                                                  │   │
│   │   Examples:                                                                      │   │
│   │   • Can this user access the Finance SharePoint?                                │   │
│   │   • Can this admin delete production databases?                                 │   │
│   │   • Can this contractor view salary data?                                       │   │
│   │   • Can this service account write to this S3 bucket?                          │   │
│   │                                                                                  │   │
│   │   Result: System knows WHAT you can do (permissions checked)                    │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
│   KEY INSIGHT: Authentication ALWAYS happens before Authorization                        │
│                You can't check permissions for someone you haven't identified           │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="real-world-analogy">Real-World Analogy: The Airport</h2>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Step</th>
                  <th>Airport Example</th>
                  <th>IT Equivalent</th>
                  <th>AuthN or AuthZ?</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>Show passport at check-in</td>
                  <td>Enter username/password</td>
                  <td><span class="badge badge-l1">AuthN</span></td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Agent verifies you're on the flight manifest</td>
                  <td>System verifies credentials against directory</td>
                  <td><span class="badge badge-l1">AuthN</span></td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>You get a boarding pass for seat 24A (Economy)</td>
                  <td>You get a token with your roles/groups</td>
                  <td><span class="badge badge-l2">AuthZ</span></td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>TSA checks your boarding pass against your ID</td>
                  <td>Application validates your token</td>
                  <td><span class="badge badge-l1">AuthN</span> + <span class="badge badge-l2">AuthZ</span></td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Can't enter First Class lounge (not authorized)</td>
                  <td>Can't access Admin panel (not in Admin group)</td>
                  <td><span class="badge badge-l2">AuthZ</span></td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Can board plane but only sit in Economy</td>
                  <td>Can login but only see standard user features</td>
                  <td><span class="badge badge-l2">AuthZ</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="enterprise-example">Enterprise Example: Day in the Life</h2>

          <h3>Scenario: Sarah from Engineering accesses company resources</h3>

          <div class="steps">
            <div class="step">
              <div class="step-number">1</div>
              <div class="step-content">
                <h4>8:30 AM - Login to Laptop</h4>
                <p><strong>Authentication:</strong> Sarah enters domain credentials (username + password)</p>
                <p><strong>Authorization:</strong> Group Policy applies based on her OU and group memberships</p>
                <div class="code-block">
                  <pre><code># What AD checks (AuthN)
User: CORP\\schen
Password: ********
Result: Credentials valid, Kerberos TGT issued

# What GPO applies (AuthZ)
User in OU: Engineering
Groups: Domain Users, Engineering-Staff, VPN-Users
Applied GPOs: Default Domain Policy, Engineering-Workstations</code></pre>
                </div>
              </div>
            </div>
            <div class="step">
              <div class="step-number">2</div>
              <div class="step-content">
                <h4>8:35 AM - Access Email (Outlook/M365)</h4>
                <p><strong>Authentication:</strong> Seamless SSO via Kerberos (no password prompt)</p>
                <p><strong>Authorization:</strong> M365 checks license assignment and mailbox permissions</p>
                <div class="code-block">
                  <pre><code># AuthN: Seamless SSO
Kerberos ticket for AZUREADSSOACC$ presented
Token issued by Entra ID

# AuthZ: License and permissions check
User has E3 license? YES
User mailbox exists? YES
User can send external email? YES (not in restricted group)</code></pre>
                </div>
              </div>
            </div>
            <div class="step">
              <div class="step-number">3</div>
              <div class="step-content">
                <h4>9:00 AM - Access GitHub Enterprise</h4>
                <p><strong>Authentication:</strong> SSO via Okta (SAML assertion)</p>
                <p><strong>Authorization:</strong> GitHub checks team memberships, repo permissions</p>
                <div class="code-block">
                  <pre><code># AuthN: SAML SSO
1. Sarah clicks GitHub in Okta portal
2. Okta issues SAML assertion (proves identity)
3. GitHub trusts Okta's assertion

# AuthZ: GitHub permission check
GitHub Team: engineering-frontend
Repo access: frontend-app (write), backend-api (read), infra (none)
Can create repos? NO (not in repo-creators team)
Can approve PRs? YES (in code-reviewers team)</code></pre>
                </div>
              </div>
            </div>
            <div class="step">
              <div class="step-number">4</div>
              <div class="step-content">
                <h4>10:00 AM - Try to Access HR SharePoint</h4>
                <p><strong>Authentication:</strong> Already authenticated (SSO token valid)</p>
                <p><strong>Authorization:</strong> DENIED - not in HR-Staff group</p>
                <div class="code-block">
                  <pre><code># AuthN: Already complete
Token valid until: 4:30 PM
MFA satisfied: YES (earlier today)

# AuthZ: Permission check FAILED
SharePoint Site: HR Confidential
Required group: HR-Staff OR HR-Managers
Sarah's groups: Engineering-Staff, VPN-Users
Result: ACCESS DENIED (403 Forbidden)</code></pre>
                </div>
              </div>
            </div>
          </div>

          <h2 id="technologies">Authentication vs Authorization Technologies</h2>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Authentication Technologies</th>
                  <th>Authorization Technologies</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Protocols</strong></td>
                  <td>Kerberos, NTLM, SAML (partially), OIDC, OAuth 2.0 (partially), RADIUS</td>
                  <td>OAuth 2.0 scopes, XACML, OPA (Open Policy Agent), Cedar</td>
                </tr>
                <tr>
                  <td><strong>What They Carry</strong></td>
                  <td>Credentials, tokens proving identity, certificates</td>
                  <td>Permissions, roles, scopes, claims, policies</td>
                </tr>
                <tr>
                  <td><strong>Microsoft Stack</strong></td>
                  <td>Entra ID authentication, Windows Hello, FIDO2 keys</td>
                  <td>RBAC, Conditional Access, PIM, App Roles</td>
                </tr>
                <tr>
                  <td><strong>AWS Stack</strong></td>
                  <td>IAM user/role authentication, SSO, Cognito</td>
                  <td>IAM Policies, SCPs, Permission Boundaries, Resource Policies</td>
                </tr>
                <tr>
                  <td><strong>Token Types</strong></td>
                  <td>ID Token (OIDC), Kerberos TGT</td>
                  <td>Access Token, Kerberos Service Ticket</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="common-mistakes">Common Mistakes and Misconceptions</h2>

          <div class="accordion">
            <div class="accordion-item">
              <button class="accordion-header">
                <span>❌ Mistake: "If they can login, they should have access"</span>
                <span class="accordion-icon">▼</span>
              </button>
              <div class="accordion-content">
                <div class="accordion-body">
                  <p><strong>The Problem:</strong> Confusing authentication success with authorization</p>
                  <p><strong>Example:</strong> A contractor successfully logs in with valid credentials, but that doesn't mean they should access employee salary data.</p>
                  <p><strong>Correct Approach:</strong> Authentication proves identity; authorization is a separate decision based on roles, groups, and policies.</p>
                </div>
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header">
                <span>❌ Mistake: "OAuth is for authentication"</span>
                <span class="accordion-icon">▼</span>
              </button>
              <div class="accordion-content">
                <div class="accordion-body">
                  <p><strong>The Problem:</strong> OAuth 2.0 is an authorization framework, not authentication</p>
                  <p><strong>Clarification:</strong></p>
                  <ul>
                    <li><strong>OAuth 2.0:</strong> Authorization - grants access tokens with scopes/permissions</li>
                    <li><strong>OpenID Connect (OIDC):</strong> Authentication layer ON TOP of OAuth 2.0</li>
                  </ul>
                  <p><strong>Correct Usage:</strong> Use OIDC for login (get ID token proving identity), OAuth for API access (get access token with permissions)</p>
                </div>
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header">
                <span>❌ Mistake: "MFA is authorization"</span>
                <span class="accordion-icon">▼</span>
              </button>
              <div class="accordion-content">
                <div class="accordion-body">
                  <p><strong>The Problem:</strong> MFA is additional authentication, not authorization</p>
                  <p><strong>What MFA Does:</strong> Provides stronger proof of identity (something you know + something you have)</p>
                  <p><strong>What MFA Doesn't Do:</strong> Determine what resources you can access</p>
                  <p><strong>However:</strong> Authorization policies can REQUIRE MFA for certain resources (e.g., Conditional Access requiring MFA for admin portals)</p>
                </div>
              </div>
            </div>
          </div>

          <h2 id="combined-flow">How They Work Together: Real Protocol Flow</h2>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    OIDC + OAuth 2.0 FLOW (Combined AuthN + AuthZ)                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   USER                    APP                     AUTHORIZATION           RESOURCE       │
│   (Browser)               (Client)                SERVER (IdP)            SERVER (API)   │
│      │                       │                          │                      │         │
│      │  1. Click "Login"     │                          │                      │         │
│      │──────────────────────►│                          │                      │         │
│      │                       │                          │                      │         │
│      │  2. Redirect to IdP (Authorization Request)      │                      │         │
│      │◄──────────────────────│                          │                      │         │
│      │                       │                          │                      │         │
│      │  3. Login page (Username + Password + MFA)       │                      │         │
│      │─────────────────────────────────────────────────►│                      │         │
│      │                                                  │                      │         │
│      │            ┌─────────────────────────────────────┤                      │         │
│      │            │  AUTHENTICATION HAPPENS HERE        │                      │         │
│      │            │  • Verify credentials               │                      │         │
│      │            │  • Check MFA                        │                      │         │
│      │            │  • Verify user exists               │                      │         │
│      │            └─────────────────────────────────────┤                      │         │
│      │                                                  │                      │         │
│      │  4. Redirect back with Authorization Code        │                      │         │
│      │◄─────────────────────────────────────────────────│                      │         │
│      │                       │                          │                      │         │
│      │  5. Forward code      │                          │                      │         │
│      │──────────────────────►│                          │                      │         │
│      │                       │                          │                      │         │
│      │                       │  6. Exchange code for tokens                    │         │
│      │                       │─────────────────────────►│                      │         │
│      │                       │                          │                      │         │
│      │                       │            ┌─────────────┤                      │         │
│      │                       │            │  TOKENS:    │                      │         │
│      │                       │            │  • ID Token (AuthN) - WHO         │         │
│      │                       │            │  • Access Token (AuthZ) - WHAT    │         │
│      │                       │            └─────────────┤                      │         │
│      │                       │                          │                      │         │
│      │                       │  7. ID Token + Access Token                     │         │
│      │                       │◄─────────────────────────│                      │         │
│      │                       │                          │                      │         │
│      │                       │  8. API Request with Access Token               │         │
│      │                       │───────────────────────────────────────────────►│         │
│      │                       │                                                 │         │
│      │                       │            ┌────────────────────────────────────┤         │
│      │                       │            │  AUTHORIZATION HAPPENS HERE        │         │
│      │                       │            │  • Validate token signature        │         │
│      │                       │            │  • Check scopes/permissions        │         │
│      │                       │            │  • Check roles/claims             │         │
│      │                       │            │  • Evaluate access policies        │         │
│      │                       │            └────────────────────────────────────┤         │
│      │                       │                                                 │         │
│      │                       │  9. API Response (if authorized)                │         │
│      │                       │◄───────────────────────────────────────────────│         │
│      │                       │                                                 │         │
│      │  10. Display data     │                          │                      │         │
│      │◄──────────────────────│                          │                      │         │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="tokens-explained">ID Token vs Access Token</h2>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Aspect</th>
                  <th>ID Token (Authentication)</th>
                  <th>Access Token (Authorization)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Purpose</strong></td>
                  <td>Prove user's identity to the client app</td>
                  <td>Grant access to resources/APIs</td>
                </tr>
                <tr>
                  <td><strong>Audience</strong></td>
                  <td>The client application</td>
                  <td>The resource server (API)</td>
                </tr>
                <tr>
                  <td><strong>Contains</strong></td>
                  <td>User info: sub, name, email, auth_time</td>
                  <td>Permissions: scopes, roles, resource access</td>
                </tr>
                <tr>
                  <td><strong>Format</strong></td>
                  <td>Always JWT (per OIDC spec)</td>
                  <td>JWT or opaque (implementation varies)</td>
                </tr>
                <tr>
                  <td><strong>Lifetime</strong></td>
                  <td>Short (minutes to hour)</td>
                  <td>Short to medium (minutes to hours)</td>
                </tr>
                <tr>
                  <td><strong>Should API validate?</strong></td>
                  <td>NO - ID token is not for APIs</td>
                  <td>YES - API validates access token</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">Example: ID Token vs Access Token (JWT)</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code>// ID TOKEN - Proves WHO the user is
{
  "iss": "https://login.microsoftonline.com/tenant-id",
  "sub": "user-unique-id",
  "aud": "client-app-id",          // For the CLIENT app
  "name": "Sarah Chen",
  "email": "schen@company.com",
  "preferred_username": "schen@company.com",
  "iat": 1699900000,
  "exp": 1699903600,
  "auth_time": 1699900000,          // When user authenticated
  "amr": ["pwd", "mfa"]             // Authentication methods used
}

// ACCESS TOKEN - Grants WHAT user can do
{
  "iss": "https://login.microsoftonline.com/tenant-id",
  "sub": "user-unique-id",
  "aud": "api://my-api",           // For the RESOURCE server
  "roles": ["User.Read", "Files.ReadWrite"],
  "scp": "openid profile email",    // Scopes granted
  "groups": ["engineering-staff", "vpn-users"],
  "iat": 1699900000,
  "exp": 1699903600
}</code></pre>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>

          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Common Interview Questions</div>
              
              <p><strong>"Explain the difference between authentication and authorization"</strong></p>
              <ul>
                <li>Authentication = Verifying identity (WHO are you?)</li>
                <li>Authorization = Checking permissions (WHAT can you do?)</li>
                <li>AuthN always happens before AuthZ</li>
                <li>Use the airport analogy: passport check (AuthN) vs boarding pass (AuthZ)</li>
              </ul>

              <p><strong>"Is OAuth authentication or authorization?"</strong></p>
              <ul>
                <li>OAuth 2.0 is an AUTHORIZATION framework</li>
                <li>OIDC (built on OAuth) provides AUTHENTICATION</li>
                <li>Know the difference: ID token (identity) vs Access token (permissions)</li>
              </ul>

              <p><strong>"Give an example where a user is authenticated but not authorized"</strong></p>
              <ul>
                <li>User logs in successfully but can't access a specific SharePoint site</li>
                <li>Admin authenticates to AWS but IAM policy denies access to production account</li>
                <li>Contractor SSOs to Okta but application isn't assigned to them</li>
              </ul>
            </div>
          </div>
'''
}

# 1-4 Access Control Models
PAGE_CONTENT["1-4-access-control-models.html"] = {
    "title": "Access Control Models",
    "badge": "L1 Fundamentals",
    "section": "IAM Foundations",
    "prev": ("1-3-identity-lifecycle.html", "Identity Lifecycle"),
    "next": ("1-5-least-privilege-sod.html", "Least Privilege & SoD"),
    "content": '''
          <div class="overview-box">
            <h3>🎯 What This Page Covers</h3>
            <p>
              Understanding access control models is fundamental to designing and implementing IAM systems. 
              This page covers DAC, MAC, RBAC, ABAC, and ReBAC with real-world enterprise examples, 
              showing when to use each model and how they're implemented in actual systems.
            </p>
          </div>

          <h2 id="overview">Access Control Models Overview</h2>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         ACCESS CONTROL MODELS COMPARISON                                 │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │  DAC (Discretionary)        │  MAC (Mandatory)           │  RBAC (Role-Based)   │   │
│   │  Owner controls access      │  System enforces labels    │  Roles grant access  │   │
│   │                             │                            │                      │   │
│   │  📁 "I'll share this file   │  🔒 "TOP SECRET can only  │  👤 "Managers can    │   │
│   │      with my team"          │      access TOP SECRET"    │      approve POs"    │   │
│   │                             │                            │                      │   │
│   │  Examples:                  │  Examples:                 │  Examples:           │   │
│   │  • Windows NTFS             │  • Military systems        │  • AD Groups         │   │
│   │  • SharePoint sharing       │  • SELinux                 │  • Azure RBAC        │   │
│   │  • Google Drive             │  • Classified networks     │  • Okta app assign   │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │  ABAC (Attribute-Based)                    │  ReBAC (Relationship-Based)        │   │
│   │  Policies evaluate attributes              │  Access based on relationships     │   │
│   │                                            │                                    │   │
│   │  📋 "IF user.department = 'Finance'        │  🔗 "User can edit doc if they    │   │
│   │      AND resource.sensitivity = 'Low'      │      are owner OR in a group      │   │
│   │      AND time.hour BETWEEN 9-17            │      that has edit permission"    │   │
│   │      THEN allow"                           │                                    │   │
│   │                                            │                                    │   │
│   │  Examples:                                 │  Examples:                         │   │
│   │  • AWS IAM Policies                        │  • Google Zanzibar                 │   │
│   │  • Azure Conditional Access                │  • Auth0 FGA                       │   │
│   │  • XACML implementations                   │  • SpiceDB, Ory Keto               │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="dac">DAC: Discretionary Access Control</h2>

          <p>
            In DAC, the resource <strong>owner</strong> decides who gets access. This is the most common 
            model in everyday computing - when you share a file or folder, you're using DAC.
          </p>

          <h3>How DAC Works</h3>
          <ul>
            <li>Resource has an owner (usually the creator)</li>
            <li>Owner can grant/revoke access to others</li>
            <li>Owner can delegate ownership</li>
            <li>Access decisions are at owner's discretion</li>
          </ul>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">DAC Example: Windows NTFS Permissions</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code># View file permissions
icacls "D:\\Projects\\budget.xlsx"

# Output:
# D:\\Projects\\budget.xlsx
#   CORP\\schen:(F)              # Full Control (Owner)
#   CORP\\Finance-Team:(R)       # Read only
#   CORP\\jsmith:(M)             # Modify

# Owner grants access to another user
icacls "D:\\Projects\\budget.xlsx" /grant "CORP\\mwilson:(R)"

# PowerShell: Get owner
Get-Acl "D:\\Projects\\budget.xlsx" | Select-Object Owner
# Owner: CORP\\schen</code></pre>
          </div>

          <div class="callout warning">
            <div class="callout-content">
              <div class="callout-title">⚠️ DAC Security Limitations</div>
              <ul>
                <li><strong>Trojan Horse Problem:</strong> Malware running as user has all user's permissions</li>
                <li><strong>Accidental Oversharing:</strong> Users may share sensitive data inappropriately</li>
                <li><strong>No Central Control:</strong> Hard to enforce organization-wide policies</li>
                <li><strong>Audit Challenges:</strong> Difficult to track who shared what with whom</li>
              </ul>
            </div>
          </div>

          <h2 id="mac">MAC: Mandatory Access Control</h2>

          <p>
            In MAC, a <strong>central authority</strong> defines access rules that users cannot override. 
            The system enforces classification labels regardless of user preferences.
          </p>

          <h3>Classification Labels</h3>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Government/Military</th>
                  <th>Corporate Equivalent</th>
                  <th>Who Can Access</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>TOP SECRET</td>
                  <td>Highly Restricted</td>
                  <td>Only users with TOP SECRET clearance</td>
                </tr>
                <tr>
                  <td>SECRET</td>
                  <td>Confidential</td>
                  <td>SECRET or TOP SECRET clearance</td>
                </tr>
                <tr>
                  <td>CONFIDENTIAL</td>
                  <td>Internal</td>
                  <td>CONFIDENTIAL and above</td>
                </tr>
                <tr>
                  <td>UNCLASSIFIED</td>
                  <td>Public</td>
                  <td>Anyone</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">MAC Example: SELinux on Linux</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code># Check SELinux context of a file
ls -Z /var/www/html/index.html
# -rw-r--r--. root root unconfined_u:object_r:httpd_sys_content_t:s0 index.html

# Context breakdown:
# unconfined_u  = SELinux user
# object_r      = Role
# httpd_sys_content_t = Type (only httpd can read)
# s0            = Sensitivity level

# Even if file has chmod 777, SELinux can still block access
# if the process doesn't have the right context</code></pre>
          </div>

          <h2 id="rbac">RBAC: Role-Based Access Control</h2>

          <p>
            RBAC is the <strong>most widely used model in enterprise IAM</strong>. Users are assigned to 
            roles, and roles have permissions. This simplifies administration dramatically.
          </p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              RBAC MODEL                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   USERS                    ROLES                      PERMISSIONS                        │
│                                                                                          │
│   ┌─────────┐             ┌─────────────────┐        ┌─────────────────────────────┐   │
│   │  Sarah  │─────┐       │   Engineer      │───────►│ Read code repos             │   │
│   └─────────┘     │       │                 │───────►│ Write to dev environment    │   │
│                   ├──────►│                 │───────►│ View CI/CD pipelines        │   │
│   ┌─────────┐     │       └─────────────────┘        └─────────────────────────────┘   │
│   │  Mike   │─────┘                                                                     │
│   └─────────┘                                                                           │
│                           ┌─────────────────┐        ┌─────────────────────────────┐   │
│   ┌─────────┐             │   Manager       │───────►│ Approve access requests     │   │
│   │  John   │────────────►│                 │───────►│ View team reports           │   │
│   └─────────┘             │                 │───────►│ All Engineer permissions    │   │
│                           └─────────────────┘        └─────────────────────────────┘   │
│                                                                                          │
│   ┌─────────┐             ┌─────────────────┐        ┌─────────────────────────────┐   │
│   │  Admin  │────────────►│   SysAdmin      │───────►│ Full system access          │   │
│   └─────────┘             │                 │───────►│ User management             │   │
│                           │                 │───────►│ Audit log access            │   │
│                           └─────────────────┘        └─────────────────────────────┘   │
│                                                                                          │
│   KEY BENEFITS:                                                                          │
│   • Add new employee → Assign role → Instant correct permissions                        │
│   • Change policy → Update role → All role members affected                             │
│   • Audit → List role members → Know who has what                                       │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h3>RBAC in Practice: Active Directory Groups</h3>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">RBAC Implementation with AD Groups</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code># Role hierarchy using AD groups
# 
# APP-Salesforce-Users (Role)
#   └── Members: All employees who need Salesforce
#
# APP-Salesforce-Admins (Role)  
#   └── Members: Salesforce administrators
#
# RBAC assignment via group membership:
Add-ADGroupMember -Identity "APP-Salesforce-Users" -Members schen

# Nested groups for role hierarchy:
# "Sales-Department" is member of "APP-Salesforce-Users"
# Everyone in Sales automatically gets Salesforce access

# Azure RBAC example
New-AzRoleAssignment `
  -SignInName "schen@company.com" `
  -RoleDefinitionName "Contributor" `
  -ResourceGroupName "prod-resources"</code></pre>
          </div>

          <h2 id="abac">ABAC: Attribute-Based Access Control</h2>

          <p>
            ABAC makes access decisions based on <strong>attributes</strong> of the user, resource, action, 
            and environment. It's more flexible than RBAC but more complex to manage.
          </p>

          <h3>ABAC Components</h3>
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Attribute Category</th>
                  <th>Examples</th>
                  <th>Usage</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Subject (User)</strong></td>
                  <td>department, title, clearance, location, device</td>
                  <td>Who is requesting access?</td>
                </tr>
                <tr>
                  <td><strong>Resource</strong></td>
                  <td>classification, owner, type, sensitivity</td>
                  <td>What is being accessed?</td>
                </tr>
                <tr>
                  <td><strong>Action</strong></td>
                  <td>read, write, delete, approve, execute</td>
                  <td>What operation?</td>
                </tr>
                <tr>
                  <td><strong>Environment</strong></td>
                  <td>time, location, threat_level, network</td>
                  <td>Context of the request</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">ABAC Example: AWS IAM Policy</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code>{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::company-data/*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalTag/Department": "Finance"    // User attribute
        },
        "StringEquals": {
          "s3:ExistingObjectTag/Classification": "Internal"  // Resource attribute
        },
        "IpAddress": {
          "aws:SourceIp": "10.0.0.0/8"               // Environment attribute
        },
        "DateGreaterThan": {
          "aws:CurrentTime": "2024-01-01T09:00:00Z"  // Time-based
        },
        "DateLessThan": {
          "aws:CurrentTime": "2024-12-31T17:00:00Z"
        }
      }
    }
  ]
}</code></pre>
          </div>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">ABAC Example: Azure Conditional Access</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code># Conditional Access Policy (ABAC in action)
# 
# Name: "Require MFA for Finance accessing sensitive apps from untrusted locations"
#
# Conditions (Attributes):
#   Users: Members of "Finance-Department" group           (Subject)
#   Cloud apps: SharePoint, Dynamics 365                   (Resource)
#   Locations: All locations EXCEPT "Corporate Network"    (Environment)
#   Device platforms: Any                                  (Environment)
#   
# Access Controls:
#   Grant: Require MFA
#   Session: Sign-in frequency = 1 hour
#
# Result: Finance users accessing sensitive apps from outside office
#         must complete MFA every hour</code></pre>
          </div>

          <h2 id="comparison">When to Use Each Model</h2>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Model</th>
                  <th>Best For</th>
                  <th>Avoid When</th>
                  <th>Real-World Example</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>DAC</strong></td>
                  <td>File sharing, collaboration</td>
                  <td>Strict compliance requirements</td>
                  <td>SharePoint, Google Drive</td>
                </tr>
                <tr>
                  <td><strong>MAC</strong></td>
                  <td>Military, healthcare, classified data</td>
                  <td>Need flexible sharing</td>
                  <td>Government systems, HIPAA data</td>
                </tr>
                <tr>
                  <td><strong>RBAC</strong></td>
                  <td>Enterprise applications, clear job functions</td>
                  <td>Highly dynamic access needs</td>
                  <td>Active Directory groups, Azure RBAC</td>
                </tr>
                <tr>
                  <td><strong>ABAC</strong></td>
                  <td>Complex policies, dynamic conditions</td>
                  <td>Simple environments (overkill)</td>
                  <td>AWS IAM, Conditional Access</td>
                </tr>
                <tr>
                  <td><strong>ReBAC</strong></td>
                  <td>Document systems, social features</td>
                  <td>Simple permission structures</td>
                  <td>Google Docs sharing, GitHub</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="hybrid-approach">Enterprise Reality: Hybrid Approaches</h2>

          <p>
            Most enterprises use a <strong>combination</strong> of access control models. Here's how they 
            typically layer together:
          </p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE ACCESS CONTROL LAYERS                                      │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   Layer 1: RBAC via Active Directory Groups                                             │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │  User → Department Group → Application Access Groups → Application              │   │
│   │  schen → Engineering-Staff → APP-GitHub-Users → GitHub Enterprise               │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                         │                                               │
│                                         ▼                                               │
│   Layer 2: ABAC via Conditional Access                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │  Even with group membership, additional conditions apply:                        │   │
│   │  • Trusted device required                                                       │   │
│   │  • MFA if outside corporate network                                              │   │
│   │  • Block if user risk is High                                                    │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                         │                                               │
│                                         ▼                                               │
│   Layer 3: DAC within Application                                                       │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │  Once in GitHub, repository-level permissions (owner-controlled):               │   │
│   │  • Repo owners control who can push to main                                     │   │
│   │  • Team leads can add/remove team members                                       │   │
│   │  • Individual files can have CODEOWNERS                                         │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>

          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Common Interview Questions</div>
              
              <p><strong>"Explain the difference between RBAC and ABAC"</strong></p>
              <ul>
                <li>RBAC: Access based on assigned roles (static)</li>
                <li>ABAC: Access based on evaluated attributes (dynamic)</li>
                <li>RBAC is simpler to manage; ABAC is more flexible</li>
                <li>Most enterprises use both (RBAC for base access, ABAC for conditions)</li>
              </ul>

              <p><strong>"What access control model would you recommend for [scenario]?"</strong></p>
              <ul>
                <li>Healthcare with PHI → MAC (mandatory classification) + RBAC</li>
                <li>SaaS application with teams → RBAC + DAC for team resources</li>
                <li>Zero Trust environment → ABAC with continuous evaluation</li>
                <li>Document collaboration → ReBAC or DAC</li>
              </ul>

              <p><strong>"How does Conditional Access relate to these models?"</strong></p>
              <ul>
                <li>Conditional Access is ABAC applied at the authentication/authorization layer</li>
                <li>Evaluates attributes: user, device, location, risk, app</li>
                <li>Works alongside RBAC (groups still determine base access)</li>
              </ul>
            </div>
          </div>
'''
}

# Continue with more pages...
# Due to length, I'll create a function to generate remaining pages

def generate_page(page_file, page_data):
    """Generate a complete HTML page"""
    
    # Find section number from filename
    section_num = int(page_file.split('-')[0])
    
    html = get_header(page_data["title"], page_data["section"], section_num)
    html += get_nav_sidebar(page_file)
    
    # Main content
    html += f'''
    <main class="main-content">
      <header class="content-header">
        <div class="breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">›</span>
          <a href="#">{page_data["section"]}</a>
          <span class="breadcrumb-separator">›</span>
          <span>{page_data["title"]}</span>
        </div>
      </header>

      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge {get_badge_class(page_data["badge"])}">{page_data["badge"]}</div>
          <h1>{page_data["title"]}</h1>
          
{page_data["content"]}

{get_page_nav(page_data["prev"][0] if page_data["prev"] else None, 
              page_data["prev"][1] if page_data["prev"] else None,
              page_data["next"][0] if page_data["next"] else None,
              page_data["next"][1] if page_data["next"] else None)}
        </article>

        <aside class="toc">
          <div class="toc-header">On This Page</div>
          <ul class="toc-list">
            <!-- TOC generated by JavaScript -->
          </ul>
        </aside>
      </div>
    </main>
  </div>
'''
    html += get_footer()
    return html

def get_badge_class(badge_text):
    if "L1" in badge_text:
        return "badge-l1"
    elif "L2" in badge_text:
        return "badge-l2"
    elif "L3" in badge_text:
        return "badge-l3"
    return "badge-l1"

# Main execution
if __name__ == "__main__":
    output_dir = "/home/claude/iam-guide"
    
    # Generate pages that have content defined
    for page_file, page_data in PAGE_CONTENT.items():
        filepath = os.path.join(output_dir, page_file)
        html = generate_page(page_file, page_data)
        with open(filepath, 'w') as f:
            f.write(html)
        print(f"Generated: {page_file}")
    
    print(f"\nGenerated {len(PAGE_CONTENT)} comprehensive pages")
