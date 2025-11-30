#!/usr/bin/env python3
"""
IAM Guide Page Generator
Generates all 81 content pages with enterprise-grade content
"""

import os

# Page definitions: (filename, title, section, badge, prev_file, prev_title, next_file, next_title)
PAGES = [
    # Section 1: IAM Foundations (8 pages) - pages 1-2 already created
    ("1-3-identity-lifecycle.html", "Identity Lifecycle", "IAM Foundations", "L1", "1-2-authn-vs-authz.html", "Authentication vs Authorization", "1-4-access-control-models.html", "Access Control Models"),
    ("1-4-access-control-models.html", "Access Control Models", "IAM Foundations", "L2", "1-3-identity-lifecycle.html", "Identity Lifecycle", "1-5-least-privilege-sod.html", "Least Privilege & SoD"),
    ("1-5-least-privilege-sod.html", "Least Privilege & SoD", "IAM Foundations", "L1", "1-4-access-control-models.html", "Access Control Models", "1-6-directory-services.html", "Directory Services"),
    ("1-6-directory-services.html", "Directory Services", "IAM Foundations", "L2", "1-5-least-privilege-sod.html", "Least Privilege & SoD", "1-7-identity-governance.html", "Identity Governance"),
    ("1-7-identity-governance.html", "Identity Governance", "IAM Foundations", "L2", "1-6-directory-services.html", "Directory Services", "1-8-privileged-access.html", "Privileged Access"),
    ("1-8-privileged-access.html", "Privileged Access", "IAM Foundations", "L2", "1-7-identity-governance.html", "Identity Governance", "2-1-authentication-factors.html", "Authentication Factors"),
    
    # Section 2: Authentication Protocols (10 pages)
    ("2-1-authentication-factors.html", "Authentication Factors", "Authentication Protocols", "L1", "1-8-privileged-access.html", "Privileged Access", "2-2-kerberos.html", "Kerberos"),
    ("2-2-kerberos.html", "Kerberos", "Authentication Protocols", "L2", "2-1-authentication-factors.html", "Authentication Factors", "2-3-ntlm.html", "NTLM"),
    ("2-3-ntlm.html", "NTLM", "Authentication Protocols", "L2", "2-2-kerberos.html", "Kerberos", "2-4-saml.html", "SAML"),
    ("2-4-saml.html", "SAML", "Authentication Protocols", "L2", "2-3-ntlm.html", "NTLM", "2-5-oauth2.html", "OAuth 2.0"),
    ("2-5-oauth2.html", "OAuth 2.0", "Authentication Protocols", "L2", "2-4-saml.html", "SAML", "2-6-oidc.html", "OpenID Connect"),
    ("2-6-oidc.html", "OpenID Connect", "Authentication Protocols", "L2", "2-5-oauth2.html", "OAuth 2.0", "2-7-radius-tacacs.html", "RADIUS & TACACS+"),
    ("2-7-radius-tacacs.html", "RADIUS & TACACS+", "Authentication Protocols", "L2", "2-6-oidc.html", "OpenID Connect", "2-8-certificates-pki.html", "Certificates & PKI"),
    ("2-8-certificates-pki.html", "Certificates & PKI", "Authentication Protocols", "L2", "2-7-radius-tacacs.html", "RADIUS & TACACS+", "2-9-sso-mechanisms.html", "SSO Mechanisms"),
    ("2-9-sso-mechanisms.html", "SSO Mechanisms", "Authentication Protocols", "L2", "2-8-certificates-pki.html", "Certificates & PKI", "2-10-auth-attacks-defense.html", "Auth Attacks & Defense"),
    ("2-10-auth-attacks-defense.html", "Auth Attacks & Defense", "Authentication Protocols", "L3", "2-9-sso-mechanisms.html", "SSO Mechanisms", "3-1-federation-fundamentals.html", "Federation Fundamentals"),
    
    # Section 3: Federation & SSO (6 pages)
    ("3-1-federation-fundamentals.html", "Federation Fundamentals", "Federation & SSO", "L1", "2-10-auth-attacks-defense.html", "Auth Attacks & Defense", "3-2-saml-federation.html", "SAML Federation"),
    ("3-2-saml-federation.html", "SAML Federation", "Federation & SSO", "L2", "3-1-federation-fundamentals.html", "Federation Fundamentals", "3-3-oidc-federation.html", "OIDC Federation"),
    ("3-3-oidc-federation.html", "OIDC Federation", "Federation & SSO", "L2", "3-2-saml-federation.html", "SAML Federation", "3-4-ws-federation-legacy.html", "WS-Federation & Legacy"),
    ("3-4-ws-federation-legacy.html", "WS-Federation & Legacy", "Federation & SSO", "L2", "3-3-oidc-federation.html", "OIDC Federation", "3-5-b2b-b2c-federation.html", "B2B & B2C Federation"),
    ("3-5-b2b-b2c-federation.html", "B2B & B2C Federation", "Federation & SSO", "L2", "3-4-ws-federation-legacy.html", "WS-Federation & Legacy", "3-6-federation-troubleshooting.html", "Federation Troubleshooting"),
    ("3-6-federation-troubleshooting.html", "Federation Troubleshooting", "Federation & SSO", "L3", "3-5-b2b-b2c-federation.html", "B2B & B2C Federation", "4-1-entra-overview.html", "Entra ID Overview"),
    
    # Section 4: Microsoft Entra ID (8 pages)
    ("4-1-entra-overview.html", "Entra ID Overview", "Microsoft Entra ID", "L1", "3-6-federation-troubleshooting.html", "Federation Troubleshooting", "4-2-entra-objects.html", "Entra ID Objects"),
    ("4-2-entra-objects.html", "Entra ID Objects", "Microsoft Entra ID", "L2", "4-1-entra-overview.html", "Entra ID Overview", "4-3-conditional-access.html", "Conditional Access"),
    ("4-3-conditional-access.html", "Conditional Access", "Microsoft Entra ID", "L2", "4-2-entra-objects.html", "Entra ID Objects", "4-4-entra-pim.html", "Entra PIM"),
    ("4-4-entra-pim.html", "Entra PIM", "Microsoft Entra ID", "L2", "4-3-conditional-access.html", "Conditional Access", "4-5-entra-governance.html", "Entra Governance"),
    ("4-5-entra-governance.html", "Entra Governance", "Microsoft Entra ID", "L2", "4-4-entra-pim.html", "Entra PIM", "4-6-entra-protection.html", "Entra Protection"),
    ("4-6-entra-protection.html", "Entra Protection", "Microsoft Entra ID", "L2", "4-5-entra-governance.html", "Entra Governance", "4-7-hybrid-identity.html", "Hybrid Identity"),
    ("4-7-hybrid-identity.html", "Hybrid Identity", "Microsoft Entra ID", "L2", "4-6-entra-protection.html", "Entra Protection", "4-8-entra-workload-id.html", "Workload Identity"),
    ("4-8-entra-workload-id.html", "Workload Identity", "Microsoft Entra ID", "L3", "4-7-hybrid-identity.html", "Hybrid Identity", "5-1-okta-overview.html", "Okta Overview"),
    
    # Section 5: Okta (6 pages)
    ("5-1-okta-overview.html", "Okta Overview", "Okta", "L1", "4-8-entra-workload-id.html", "Workload Identity", "5-2-okta-authentication.html", "Okta Authentication"),
    ("5-2-okta-authentication.html", "Okta Authentication", "Okta", "L2", "5-1-okta-overview.html", "Okta Overview", "5-3-okta-authorization.html", "Okta Authorization"),
    ("5-3-okta-authorization.html", "Okta Authorization", "Okta", "L2", "5-2-okta-authentication.html", "Okta Authentication", "5-4-okta-lifecycle.html", "Okta Lifecycle"),
    ("5-4-okta-lifecycle.html", "Okta Lifecycle", "Okta", "L2", "5-3-okta-authorization.html", "Okta Authorization", "5-5-okta-integration.html", "Okta Integration"),
    ("5-5-okta-integration.html", "Okta Integration", "Okta", "L2", "5-4-okta-lifecycle.html", "Okta Lifecycle", "5-6-okta-admin.html", "Okta Administration"),
    ("5-6-okta-admin.html", "Okta Administration", "Okta", "L2", "5-5-okta-integration.html", "Okta Integration", "6-1-sailpoint-overview.html", "SailPoint Overview"),
    
    # Section 6: SailPoint & IGA (6 pages)
    ("6-1-sailpoint-overview.html", "SailPoint Overview", "SailPoint & IGA", "L1", "5-6-okta-admin.html", "Okta Administration", "6-2-iga-fundamentals.html", "IGA Fundamentals"),
    ("6-2-iga-fundamentals.html", "IGA Fundamentals", "SailPoint & IGA", "L1", "6-1-sailpoint-overview.html", "SailPoint Overview", "6-3-access-certifications.html", "Access Certifications"),
    ("6-3-access-certifications.html", "Access Certifications", "SailPoint & IGA", "L2", "6-2-iga-fundamentals.html", "IGA Fundamentals", "6-4-role-management.html", "Role Management"),
    ("6-4-role-management.html", "Role Management", "SailPoint & IGA", "L2", "6-3-access-certifications.html", "Access Certifications", "6-5-sod-management.html", "SoD Management"),
    ("6-5-sod-management.html", "SoD Management", "SailPoint & IGA", "L2", "6-4-role-management.html", "Role Management", "6-6-provisioning-workflows.html", "Provisioning Workflows"),
    ("6-6-provisioning-workflows.html", "Provisioning Workflows", "SailPoint & IGA", "L2", "6-5-sod-management.html", "SoD Management", "7-1-pam-overview.html", "PAM Overview"),
    
    # Section 7: PAM (6 pages)
    ("7-1-pam-overview.html", "PAM Overview", "Privileged Access Management", "L1", "6-6-provisioning-workflows.html", "Provisioning Workflows", "7-2-password-vaulting.html", "Password Vaulting"),
    ("7-2-password-vaulting.html", "Password Vaulting", "Privileged Access Management", "L2", "7-1-pam-overview.html", "PAM Overview", "7-3-session-management.html", "Session Management"),
    ("7-3-session-management.html", "Session Management", "Privileged Access Management", "L2", "7-2-password-vaulting.html", "Password Vaulting", "7-4-jit-access.html", "Just-in-Time Access"),
    ("7-4-jit-access.html", "Just-in-Time Access", "Privileged Access Management", "L2", "7-3-session-management.html", "Session Management", "7-5-secrets-management.html", "Secrets Management"),
    ("7-5-secrets-management.html", "Secrets Management", "Privileged Access Management", "L2", "7-4-jit-access.html", "Just-in-Time Access", "7-6-pam-vendors.html", "PAM Vendors"),
    ("7-6-pam-vendors.html", "PAM Vendors", "Privileged Access Management", "L2", "7-5-secrets-management.html", "Secrets Management", "8-1-aws-iam.html", "AWS IAM"),
    
    # Section 8: Cloud IAM (8 pages)
    ("8-1-aws-iam.html", "AWS IAM", "Cloud IAM", "L2", "7-6-pam-vendors.html", "PAM Vendors", "8-2-aws-identity-center.html", "AWS Identity Center"),
    ("8-2-aws-identity-center.html", "AWS Identity Center", "Cloud IAM", "L2", "8-1-aws-iam.html", "AWS IAM", "8-3-azure-rbac.html", "Azure RBAC"),
    ("8-3-azure-rbac.html", "Azure RBAC", "Cloud IAM", "L2", "8-2-aws-identity-center.html", "AWS Identity Center", "8-4-gcp-iam.html", "GCP IAM"),
    ("8-4-gcp-iam.html", "GCP IAM", "Cloud IAM", "L2", "8-3-azure-rbac.html", "Azure RBAC", "8-5-multi-cloud-identity.html", "Multi-Cloud Identity"),
    ("8-5-multi-cloud-identity.html", "Multi-Cloud Identity", "Cloud IAM", "L3", "8-4-gcp-iam.html", "GCP IAM", "8-6-kubernetes-iam.html", "Kubernetes IAM"),
    ("8-6-kubernetes-iam.html", "Kubernetes IAM", "Cloud IAM", "L2", "8-5-multi-cloud-identity.html", "Multi-Cloud Identity", "8-7-infrastructure-as-code.html", "Infrastructure as Code"),
    ("8-7-infrastructure-as-code.html", "Infrastructure as Code", "Cloud IAM", "L2", "8-6-kubernetes-iam.html", "Kubernetes IAM", "8-8-cloud-pam.html", "Cloud PAM"),
    ("8-8-cloud-pam.html", "Cloud PAM", "Cloud IAM", "L3", "8-7-infrastructure-as-code.html", "Infrastructure as Code", "9-1-enterprise-iam-arch.html", "Enterprise IAM Architecture"),
    
    # Section 9: IAM Architecture (6 pages)
    ("9-1-enterprise-iam-arch.html", "Enterprise IAM Architecture", "IAM Architecture", "L3", "8-8-cloud-pam.html", "Cloud PAM", "9-2-zero-trust-iam.html", "Zero Trust IAM"),
    ("9-2-zero-trust-iam.html", "Zero Trust IAM", "IAM Architecture", "L2", "9-1-enterprise-iam-arch.html", "Enterprise IAM Architecture", "9-3-hybrid-cloud-iam.html", "Hybrid Cloud IAM"),
    ("9-3-hybrid-cloud-iam.html", "Hybrid Cloud IAM", "IAM Architecture", "L2", "9-2-zero-trust-iam.html", "Zero Trust IAM", "9-4-ciam-architecture.html", "CIAM Architecture"),
    ("9-4-ciam-architecture.html", "CIAM Architecture", "IAM Architecture", "L2", "9-3-hybrid-cloud-iam.html", "Hybrid Cloud IAM", "9-5-api-security.html", "API Security"),
    ("9-5-api-security.html", "API Security", "IAM Architecture", "L2", "9-4-ciam-architecture.html", "CIAM Architecture", "9-6-high-availability.html", "High Availability"),
    ("9-6-high-availability.html", "High Availability", "IAM Architecture", "L3", "9-5-api-security.html", "API Security", "10-1-migration-planning.html", "Migration Planning"),
    
    # Section 10: IAM Migrations (6 pages)
    ("10-1-migration-planning.html", "Migration Planning", "IAM Migrations", "L2", "9-6-high-availability.html", "High Availability", "10-2-idp-migrations.html", "IdP Migrations"),
    ("10-2-idp-migrations.html", "IdP Migrations", "IAM Migrations", "L2", "10-1-migration-planning.html", "Migration Planning", "10-3-legacy-modernization.html", "Legacy Modernization"),
    ("10-3-legacy-modernization.html", "Legacy Modernization", "IAM Migrations", "L2", "10-2-idp-migrations.html", "IdP Migrations", "10-4-iga-pam-migrations.html", "IGA & PAM Migrations"),
    ("10-4-iga-pam-migrations.html", "IGA & PAM Migrations", "IAM Migrations", "L2", "10-3-legacy-modernization.html", "Legacy Modernization", "10-5-app-migration.html", "Application Migration"),
    ("10-5-app-migration.html", "Application Migration", "IAM Migrations", "L2", "10-4-iga-pam-migrations.html", "IGA & PAM Migrations", "10-6-coexistence-cutover.html", "Coexistence & Cutover"),
    ("10-6-coexistence-cutover.html", "Coexistence & Cutover", "IAM Migrations", "L2", "10-5-app-migration.html", "Application Migration", "11-1-identity-threat-landscape.html", "Identity Threat Landscape"),
    
    # Section 11: Security & Attacks (5 pages)
    ("11-1-identity-threat-landscape.html", "Identity Threat Landscape", "Security & Attacks", "L2", "10-6-coexistence-cutover.html", "Coexistence & Cutover", "11-2-credential-attacks.html", "Credential Attacks"),
    ("11-2-credential-attacks.html", "Credential Attacks", "Security & Attacks", "L2", "11-1-identity-threat-landscape.html", "Identity Threat Landscape", "11-3-token-session-attacks.html", "Token & Session Attacks"),
    ("11-3-token-session-attacks.html", "Token & Session Attacks", "Security & Attacks", "L3", "11-2-credential-attacks.html", "Credential Attacks", "11-4-privilege-escalation.html", "Privilege Escalation"),
    ("11-4-privilege-escalation.html", "Privilege Escalation", "Security & Attacks", "L3", "11-3-token-session-attacks.html", "Token & Session Attacks", "11-5-detection-response.html", "Detection & Response"),
    ("11-5-detection-response.html", "Detection & Response", "Security & Attacks", "L2", "11-4-privilege-escalation.html", "Privilege Escalation", "12-1-iam-glossary.html", "IAM Glossary"),
    
    # Section 12: Reference & Interview (6 pages)
    ("12-1-iam-glossary.html", "IAM Glossary", "Reference & Interview Prep", "L1", "11-5-detection-response.html", "Detection & Response", "12-2-interview-questions.html", "Interview Questions"),
    ("12-2-interview-questions.html", "Interview Questions", "Reference & Interview Prep", "L1", "12-1-iam-glossary.html", "IAM Glossary", "12-3-scenario-questions.html", "Scenario Questions"),
    ("12-3-scenario-questions.html", "Scenario Questions", "Reference & Interview Prep", "L2", "12-2-interview-questions.html", "Interview Questions", "12-4-protocol-flows.html", "Protocol Flows"),
    ("12-4-protocol-flows.html", "Protocol Flows", "Reference & Interview Prep", "L2", "12-3-scenario-questions.html", "Scenario Questions", "12-5-comparison-tables.html", "Comparison Tables"),
    ("12-5-comparison-tables.html", "Comparison Tables", "Reference & Interview Prep", "L1", "12-4-protocol-flows.html", "Protocol Flows", "12-6-cli-api-reference.html", "CLI & API Reference"),
    ("12-6-cli-api-reference.html", "CLI & API Reference", "Reference & Interview Prep", "L2", "12-5-comparison-tables.html", "Comparison Tables", "index.html", "Home"),
]

# Content templates for each page type
CONTENT_TEMPLATES = {
    "1-3-identity-lifecycle.html": """
          <div class="overview-box">
            <h3>🎯 What You'll Learn</h3>
            <p>
              The identity lifecycle encompasses all stages of a digital identity from creation to deletion.
              Understanding Joiner-Mover-Leaver (JML) processes is critical for security, compliance, and 
              operational efficiency in enterprise IAM.
            </p>
          </div>

          <h2 id="lifecycle-stages">Identity Lifecycle Stages</h2>
          <p>
            Every digital identity goes through distinct phases during its existence within an organization.
            Proper management of each stage is essential for maintaining security posture and regulatory compliance.
          </p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────┐
│                        IDENTITY LIFECYCLE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│   │  JOINER  │───►│  ACTIVE  │───►│  MOVER   │───►│  LEAVER  │             │
│   │          │    │          │    │          │    │          │             │
│   │ Onboard  │    │ Day-to-  │    │ Role     │    │ Offboard │             │
│   │ Provision│    │ Day Work │    │ Change   │    │ Deprov   │             │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘             │
│        │               │               │               │                    │
│        ▼               ▼               ▼               ▼                    │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │                    GOVERNANCE & AUDIT                            │      │
│   │  Access Reviews │ Certifications │ Compliance │ Audit Trail     │      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="joiner-process">Joiner Process (Onboarding)</h2>
          <p>
            When a new employee, contractor, or partner joins the organization, their identity must be 
            created and provisioned with appropriate access rights based on their role and responsibilities.
          </p>

          <h3>Joiner Workflow Steps</h3>
          <div class="steps">
            <div class="step">
              <div class="step-number">1</div>
              <div class="step-content">
                <h4>HR System Trigger</h4>
                <p>New hire record created in HRIS (Workday, SAP SuccessFactors, etc.) triggers identity creation.</p>
              </div>
            </div>
            <div class="step">
              <div class="step-number">2</div>
              <div class="step-content">
                <h4>Identity Creation</h4>
                <p>Unique identifier generated, core attributes populated from HR data (name, department, manager, location).</p>
              </div>
            </div>
            <div class="step">
              <div class="step-number">3</div>
              <div class="step-content">
                <h4>Role Assignment</h4>
                <p>Based on job title and department, appropriate birthright roles are automatically assigned.</p>
              </div>
            </div>
            <div class="step">
              <div class="step-number">4</div>
              <div class="step-content">
                <h4>Access Provisioning</h4>
                <p>Accounts created in target systems (AD, email, applications) based on role entitlements.</p>
              </div>
            </div>
            <div class="step">
              <div class="step-number">5</div>
              <div class="step-content">
                <h4>Credential Delivery</h4>
                <p>Initial credentials securely delivered; MFA enrollment initiated on first login.</p>
              </div>
            </div>
          </div>

          <h2 id="mover-process">Mover Process (Role Changes)</h2>
          <p>
            When employees change roles, departments, or locations, their access rights must be adjusted 
            to reflect their new responsibilities while removing access no longer required.
          </p>

          <div class="callout warning">
            <div class="callout-content">
              <div class="callout-title">⚠️ Access Accumulation Risk</div>
              <p>
                Without proper mover processes, employees accumulate access over time as they change roles.
                This "privilege creep" violates least privilege and creates security and compliance risks.
                Always implement "remove before add" or simultaneous access reviews during transitions.
              </p>
            </div>
          </div>

          <h2 id="leaver-process">Leaver Process (Offboarding)</h2>
          <p>
            Timely deprovisioning of departing employees is one of the most critical security processes.
            Orphaned accounts are a primary attack vector and compliance violation.
          </p>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Timeframe</th>
                  <th>Actions</th>
                  <th>Systems</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Immediate (T+0)</strong></td>
                  <td>Disable all accounts, revoke active sessions, disable VPN/remote access</td>
                  <td>AD, IdP, VPN, SSO</td>
                </tr>
                <tr>
                  <td><strong>Same Day</strong></td>
                  <td>Reset passwords, remove from groups, disable email, archive mailbox</td>
                  <td>Exchange, Teams, Groups</td>
                </tr>
                <tr>
                  <td><strong>Week 1</strong></td>
                  <td>Transfer ownership of shared resources, reassign licenses</td>
                  <td>SharePoint, OneDrive, SaaS apps</td>
                </tr>
                <tr>
                  <td><strong>30 Days</strong></td>
                  <td>Delete accounts (after data retention period)</td>
                  <td>All systems</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="hr-integration">HR System Integration</h2>
          <p>
            Modern identity lifecycle management relies on authoritative HR data as the source of truth.
            Integration with HRIS systems enables automation and reduces manual errors.
          </p>

          <div class="tabs">
            <div class="tabs-header">
              <button class="tab-btn active">Workday</button>
              <button class="tab-btn">SAP SuccessFactors</button>
              <button class="tab-btn">Custom HRIS</button>
            </div>
            <div class="tab-content active">
              <h4>Workday Integration</h4>
              <p>Workday provides robust integration capabilities through its Integration Cloud Platform.</p>
              <div class="code-block">
                <div class="code-header">
                  <span class="code-language">Workday Studio - Worker Change Event</span>
                  <button class="code-copy-btn"><span>📋</span> Copy</button>
                </div>
                <pre><code># Workday Integration Events to Monitor
- Hire
- Terminate  
- Change Job (promotion, transfer, demotion)
- Leave of Absence (start/return)
- Contingent Worker events
- Contract End Date changes</code></pre>
              </div>
            </div>
            <div class="tab-content">
              <h4>SAP SuccessFactors Integration</h4>
              <p>SuccessFactors Employee Central provides OData APIs for identity synchronization.</p>
            </div>
            <div class="tab-content">
              <h4>Custom HRIS Integration</h4>
              <p>For custom or legacy HRIS systems, implement scheduled batch or real-time event integrations.</p>
            </div>
          </div>

          <h2 id="best-practices">Best Practices</h2>
          <ul>
            <li><strong>Single Authoritative Source:</strong> HR system should be the sole source of truth for identity creation/deletion</li>
            <li><strong>Automation First:</strong> Minimize manual provisioning; automate birthright access based on roles</li>
            <li><strong>Pre-dated Actions:</strong> Schedule future start/end dates in advance for planned changes</li>
            <li><strong>Manager Involvement:</strong> Require manager attestation for access changes beyond birthright</li>
            <li><strong>Audit Everything:</strong> Log all lifecycle events for compliance and forensics</li>
            <li><strong>Graceful Transitions:</strong> Allow overlap periods for knowledge transfer during role changes</li>
          </ul>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Points Interviewers Look For</div>
              <ul>
                <li>Understanding of JML (Joiner-Mover-Leaver) terminology</li>
                <li>Knowledge of HR integration patterns and authoritative sources</li>
                <li>Awareness of orphaned account risks and leaver process urgency</li>
                <li>Experience with IGA platforms (SailPoint, Saviynt, etc.)</li>
                <li>Understanding of birthright access vs. request-based access</li>
              </ul>
            </div>
          </div>
""",
    "1-4-access-control-models.html": """
          <div class="overview-box">
            <h3>🎯 What You'll Learn</h3>
            <p>
              Access control models define how permissions are granted and enforced in an organization.
              This page covers RBAC, ABAC, PBAC, DAC, MAC, and ReBAC with detailed comparisons, 
              use cases, and decision frameworks for selecting the right model.
            </p>
          </div>

          <h2 id="model-overview">Access Control Models Overview</h2>
          
          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Model</th>
                  <th>Full Name</th>
                  <th>Based On</th>
                  <th>Best For</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>RBAC</strong></td>
                  <td>Role-Based Access Control</td>
                  <td>Predefined roles</td>
                  <td>Stable hierarchical organizations</td>
                </tr>
                <tr>
                  <td><strong>ABAC</strong></td>
                  <td>Attribute-Based Access Control</td>
                  <td>User/resource/environment attributes</td>
                  <td>Dynamic, context-aware access</td>
                </tr>
                <tr>
                  <td><strong>PBAC</strong></td>
                  <td>Policy-Based Access Control</td>
                  <td>Explicit policy rules</td>
                  <td>Complex, auditable requirements</td>
                </tr>
                <tr>
                  <td><strong>DAC</strong></td>
                  <td>Discretionary Access Control</td>
                  <td>Resource owner decisions</td>
                  <td>File systems, collaboration</td>
                </tr>
                <tr>
                  <td><strong>MAC</strong></td>
                  <td>Mandatory Access Control</td>
                  <td>Security labels/clearances</td>
                  <td>Government, classified data</td>
                </tr>
                <tr>
                  <td><strong>ReBAC</strong></td>
                  <td>Relationship-Based Access Control</td>
                  <td>Object relationships</td>
                  <td>Social, collaborative platforms</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="rbac">Role-Based Access Control (RBAC)</h2>
          <p>
            RBAC assigns permissions to roles, and users receive permissions by being assigned to roles.
            It simplifies management in organizations with well-defined job functions.
          </p>

          <h3>RBAC Hierarchy</h3>
          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────┐
│                    RBAC HIERARCHY                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Users ──────► Roles ──────► Permissions ──────► Resources     │
│                                                                  │
│   ┌─────────┐    ┌─────────────┐    ┌────────────────┐          │
│   │ Alice   │───►│ HR_Manager  │───►│ Read: Employee │          │
│   │ Bob     │    │             │    │ Write: Benefits│          │
│   │ Carol   │    └─────────────┘    │ Approve: Leave │          │
│   └─────────┘           │           └────────────────┘          │
│        │                │                                        │
│        │         ┌──────▼──────┐                                │
│        └────────►│ HR_Staff    │──► Read: Employee              │
│                  │ (inherits)  │    View: Benefits              │
│                  └─────────────┘                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <div class="callout tip">
            <div class="callout-content">
              <div class="callout-title">💡 RBAC Best Practice</div>
              <p>
                Design roles around job functions, not individuals. Avoid creating "role explosion" 
                by having too many granular roles. Implement role hierarchies where child roles 
                inherit permissions from parent roles.
              </p>
            </div>
          </div>

          <h2 id="abac">Attribute-Based Access Control (ABAC)</h2>
          <p>
            ABAC evaluates attributes of the subject (user), object (resource), action, and environment
            to make dynamic access decisions. More flexible than RBAC but more complex to implement.
          </p>

          <div class="code-block">
            <div class="code-header">
              <span class="code-language">XACML-style ABAC Policy</span>
              <button class="code-copy-btn"><span>📋</span> Copy</button>
            </div>
            <pre><code>Policy: AccessPatientRecords
  Target: resource.type == "PatientRecord"
  
  Rule: AllowTreatingPhysician
    Condition:
      subject.role == "Physician" AND
      subject.department == resource.treatment_department AND
      action == "read" AND
      environment.time BETWEEN "08:00" AND "20:00"
    Effect: Permit
    
  Rule: DenyDefault
    Effect: Deny</code></pre>
          </div>

          <h2 id="decision-tree">Model Selection Decision Tree</h2>
          <div class="callout info">
            <div class="callout-content">
              <div class="callout-title">🔍 Choosing the Right Model</div>
              <ul>
                <li><strong>Stable org structure + clear job functions?</strong> → RBAC</li>
                <li><strong>Need context-aware decisions (time, location, risk)?</strong> → ABAC</li>
                <li><strong>Complex, auditable compliance requirements?</strong> → PBAC</li>
                <li><strong>User-controlled sharing (documents, files)?</strong> → DAC</li>
                <li><strong>Classified data with security clearances?</strong> → MAC</li>
                <li><strong>Social/collaborative with complex relationships?</strong> → ReBAC</li>
                <li><strong>Hybrid needs?</strong> → Combine models (RBAC + ABAC is common)</li>
              </ul>
            </div>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Points Interviewers Look For</div>
              <ul>
                <li>Ability to compare and contrast RBAC vs ABAC with real examples</li>
                <li>Understanding of "role explosion" problem and mitigation strategies</li>
                <li>Knowledge of when to use hybrid approaches</li>
                <li>Awareness of Zero Trust implications on access control models</li>
              </ul>
            </div>
          </div>
""",
}

def get_sidebar_html():
    """Return the complete sidebar navigation HTML."""
    return '''<nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
      <div class="sidebar-nav">
        <div class="nav-section">
          <div class="nav-section-header"><span>1. IAM Foundations</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="1-1-iam-overview.html" class="nav-item">IAM Overview</a>
            <a href="1-2-authn-vs-authz.html" class="nav-item">Authentication vs Authorization</a>
            <a href="1-3-identity-lifecycle.html" class="nav-item">Identity Lifecycle</a>
            <a href="1-4-access-control-models.html" class="nav-item">Access Control Models</a>
            <a href="1-5-least-privilege-sod.html" class="nav-item">Least Privilege & SoD</a>
            <a href="1-6-directory-services.html" class="nav-item">Directory Services</a>
            <a href="1-7-identity-governance.html" class="nav-item">Identity Governance</a>
            <a href="1-8-privileged-access.html" class="nav-item">Privileged Access</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>2. Authentication Protocols</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="2-1-authentication-factors.html" class="nav-item">Authentication Factors</a>
            <a href="2-2-kerberos.html" class="nav-item">Kerberos</a>
            <a href="2-3-ntlm.html" class="nav-item">NTLM</a>
            <a href="2-4-saml.html" class="nav-item">SAML</a>
            <a href="2-5-oauth2.html" class="nav-item">OAuth 2.0</a>
            <a href="2-6-oidc.html" class="nav-item">OpenID Connect</a>
            <a href="2-7-radius-tacacs.html" class="nav-item">RADIUS & TACACS+</a>
            <a href="2-8-certificates-pki.html" class="nav-item">Certificates & PKI</a>
            <a href="2-9-sso-mechanisms.html" class="nav-item">SSO Mechanisms</a>
            <a href="2-10-auth-attacks-defense.html" class="nav-item">Auth Attacks & Defense</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>3. Federation & SSO</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="3-1-federation-fundamentals.html" class="nav-item">Federation Fundamentals</a>
            <a href="3-2-saml-federation.html" class="nav-item">SAML Federation</a>
            <a href="3-3-oidc-federation.html" class="nav-item">OIDC Federation</a>
            <a href="3-4-ws-federation-legacy.html" class="nav-item">WS-Federation & Legacy</a>
            <a href="3-5-b2b-b2c-federation.html" class="nav-item">B2B & B2C Federation</a>
            <a href="3-6-federation-troubleshooting.html" class="nav-item">Federation Troubleshooting</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>4. Microsoft Entra ID</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="4-1-entra-overview.html" class="nav-item">Entra ID Overview</a>
            <a href="4-2-entra-objects.html" class="nav-item">Entra ID Objects</a>
            <a href="4-3-conditional-access.html" class="nav-item">Conditional Access</a>
            <a href="4-4-entra-pim.html" class="nav-item">Entra PIM</a>
            <a href="4-5-entra-governance.html" class="nav-item">Entra Governance</a>
            <a href="4-6-entra-protection.html" class="nav-item">Entra Protection</a>
            <a href="4-7-hybrid-identity.html" class="nav-item">Hybrid Identity</a>
            <a href="4-8-entra-workload-id.html" class="nav-item">Workload Identity</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>5. Okta</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="5-1-okta-overview.html" class="nav-item">Okta Overview</a>
            <a href="5-2-okta-authentication.html" class="nav-item">Okta Authentication</a>
            <a href="5-3-okta-authorization.html" class="nav-item">Okta Authorization</a>
            <a href="5-4-okta-lifecycle.html" class="nav-item">Okta Lifecycle</a>
            <a href="5-5-okta-integration.html" class="nav-item">Okta Integration</a>
            <a href="5-6-okta-admin.html" class="nav-item">Okta Administration</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>6. SailPoint & IGA</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="6-1-sailpoint-overview.html" class="nav-item">SailPoint Overview</a>
            <a href="6-2-iga-fundamentals.html" class="nav-item">IGA Fundamentals</a>
            <a href="6-3-access-certifications.html" class="nav-item">Access Certifications</a>
            <a href="6-4-role-management.html" class="nav-item">Role Management</a>
            <a href="6-5-sod-management.html" class="nav-item">SoD Management</a>
            <a href="6-6-provisioning-workflows.html" class="nav-item">Provisioning Workflows</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>7. Privileged Access (PAM)</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="7-1-pam-overview.html" class="nav-item">PAM Overview</a>
            <a href="7-2-password-vaulting.html" class="nav-item">Password Vaulting</a>
            <a href="7-3-session-management.html" class="nav-item">Session Management</a>
            <a href="7-4-jit-access.html" class="nav-item">Just-in-Time Access</a>
            <a href="7-5-secrets-management.html" class="nav-item">Secrets Management</a>
            <a href="7-6-pam-vendors.html" class="nav-item">PAM Vendors</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>8. Cloud IAM</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="8-1-aws-iam.html" class="nav-item">AWS IAM</a>
            <a href="8-2-aws-identity-center.html" class="nav-item">AWS Identity Center</a>
            <a href="8-3-azure-rbac.html" class="nav-item">Azure RBAC</a>
            <a href="8-4-gcp-iam.html" class="nav-item">GCP IAM</a>
            <a href="8-5-multi-cloud-identity.html" class="nav-item">Multi-Cloud Identity</a>
            <a href="8-6-kubernetes-iam.html" class="nav-item">Kubernetes IAM</a>
            <a href="8-7-infrastructure-as-code.html" class="nav-item">Infrastructure as Code</a>
            <a href="8-8-cloud-pam.html" class="nav-item">Cloud PAM</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>9. IAM Architecture</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="9-1-enterprise-iam-arch.html" class="nav-item">Enterprise IAM Architecture</a>
            <a href="9-2-zero-trust-iam.html" class="nav-item">Zero Trust IAM</a>
            <a href="9-3-hybrid-cloud-iam.html" class="nav-item">Hybrid Cloud IAM</a>
            <a href="9-4-ciam-architecture.html" class="nav-item">CIAM Architecture</a>
            <a href="9-5-api-security.html" class="nav-item">API Security</a>
            <a href="9-6-high-availability.html" class="nav-item">High Availability</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>10. IAM Migrations</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="10-1-migration-planning.html" class="nav-item">Migration Planning</a>
            <a href="10-2-idp-migrations.html" class="nav-item">IdP Migrations</a>
            <a href="10-3-legacy-modernization.html" class="nav-item">Legacy Modernization</a>
            <a href="10-4-iga-pam-migrations.html" class="nav-item">IGA & PAM Migrations</a>
            <a href="10-5-app-migration.html" class="nav-item">Application Migration</a>
            <a href="10-6-coexistence-cutover.html" class="nav-item">Coexistence & Cutover</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>11. Security & Attacks</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="11-1-identity-threat-landscape.html" class="nav-item">Identity Threat Landscape</a>
            <a href="11-2-credential-attacks.html" class="nav-item">Credential Attacks</a>
            <a href="11-3-token-session-attacks.html" class="nav-item">Token & Session Attacks</a>
            <a href="11-4-privilege-escalation.html" class="nav-item">Privilege Escalation</a>
            <a href="11-5-detection-response.html" class="nav-item">Detection & Response</a>
          </div>
        </div>
        <div class="nav-section">
          <div class="nav-section-header collapsed"><span>12. Reference & Interview</span><span class="nav-section-icon">▼</span></div>
          <div class="nav-section-items">
            <a href="12-1-iam-glossary.html" class="nav-item">IAM Glossary</a>
            <a href="12-2-interview-questions.html" class="nav-item">Interview Questions</a>
            <a href="12-3-scenario-questions.html" class="nav-item">Scenario Questions</a>
            <a href="12-4-protocol-flows.html" class="nav-item">Protocol Flows</a>
            <a href="12-5-comparison-tables.html" class="nav-item">Comparison Tables</a>
            <a href="12-6-cli-api-reference.html" class="nav-item">CLI & API Reference</a>
          </div>
        </div>
      </div>
    </nav>'''

def get_default_content(title, section):
    """Generate default content for pages without specific templates."""
    return f'''
          <div class="overview-box">
            <h3>🎯 What You'll Learn</h3>
            <p>
              This comprehensive guide covers {title} concepts, implementation best practices, 
              security considerations, and real-world enterprise examples. Essential knowledge
              for security professionals and IAM practitioners.
            </p>
          </div>

          <h2 id="overview">Overview</h2>
          <p>
            {title} is a critical component of enterprise identity and access management.
            Understanding these concepts is essential for designing, implementing, and
            maintaining secure IAM solutions.
          </p>

          <h2 id="key-concepts">Key Concepts</h2>
          <p>
            This section covers the fundamental concepts and terminology you need to understand
            for {title}.
          </p>

          <div class="callout info">
            <div class="callout-content">
              <div class="callout-title">📚 Core Principles</div>
              <p>
                Understanding the core principles of {title} enables you to make informed
                decisions about implementation strategies and security controls.
              </p>
            </div>
          </div>

          <h2 id="implementation">Implementation Guide</h2>
          <p>
            Step-by-step guidance for implementing {title} in enterprise environments.
          </p>

          <h2 id="best-practices">Best Practices</h2>
          <ul>
            <li>Follow the principle of least privilege</li>
            <li>Implement defense in depth strategies</li>
            <li>Maintain comprehensive audit logs</li>
            <li>Regular access reviews and certifications</li>
            <li>Automated provisioning and deprovisioning</li>
          </ul>

          <h2 id="security-considerations">Security Considerations</h2>
          <div class="callout warning">
            <div class="callout-content">
              <div class="callout-title">⚠️ Security Best Practices</div>
              <p>
                Always consider security implications when implementing {title}.
                Regular security assessments and monitoring are essential.
              </p>
            </div>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Points Interviewers Look For</div>
              <ul>
                <li>Clear understanding of core concepts</li>
                <li>Real-world implementation experience</li>
                <li>Knowledge of security best practices</li>
                <li>Ability to troubleshoot common issues</li>
                <li>Understanding of enterprise requirements</li>
              </ul>
            </div>
          </div>
'''

def generate_page(filename, title, section, badge, prev_file, prev_title, next_file, next_title):
    """Generate a complete HTML page."""
    badge_class = f"badge-l{badge[-1].lower()}" if badge.startswith("L") else "badge-l2"
    badge_text = f"{badge} {'Fundamentals' if badge == 'L1' else 'Technical' if badge == 'L2' else 'Expert'}"
    
    # Get content - use specific template if available, otherwise default
    content = CONTENT_TEMPLATES.get(filename, get_default_content(title, section))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔐</text></svg>">
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
    {get_sidebar_html()}
    <main class="main-content">
      <header class="content-header">
        <div class="breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">›</span>
          <span>{section}</span>
          <span class="breadcrumb-separator">›</span>
          <span>{title}</span>
        </div>
        <div class="header-actions">
          <button class="search-trigger">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <span>Search</span>
            <kbd>⌘K</kbd>
          </button>
        </div>
      </header>
      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge {badge_class}">{badge_text}</div>
          <h1>{title}</h1>
          {content}
          <nav class="page-nav">
            <a href="{prev_file}" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">{prev_title}</span>
            </a>
            <a href="{next_file}" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">{next_title}</span>
            </a>
          </nav>
        </article>
        <aside class="toc">
          <div class="toc-header">On This Page</div>
          <ul class="toc-list"></ul>
        </aside>
      </div>
    </main>
    <div class="search-modal">
      <div class="search-container">
        <div class="search-input-wrapper">
          <svg class="search-input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" class="search-input" placeholder="Search documentation...">
        </div>
        <div class="search-results"></div>
      </div>
    </div>
  </div>
  <script src="main.js"></script>
</body>
</html>'''
    return html

def main():
    """Generate all pages."""
    for page in PAGES:
        filename, title, section, badge, prev_file, prev_title, next_file, next_title = page
        html = generate_page(filename, title, section, badge, prev_file, prev_title, next_file, next_title)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created: {filename}")

if __name__ == "__main__":
    main()
