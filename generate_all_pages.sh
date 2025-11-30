#!/bin/bash
# Generate all comprehensive IAM guide pages

OUTPUT_DIR="/home/claude/iam-guide"

# Function to create a page
create_page() {
    local filename="$1"
    local title="$2"
    local badge="$3"
    local section="$4"
    local prev_file="$5"
    local prev_title="$6"
    local next_file="$7"
    local next_title="$8"
    local content="$9"
    
    cat > "$OUTPUT_DIR/$filename" << PAGEEOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$title - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="page-wrapper">
    <nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
    </nav>
    <main class="main-content">
      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge $badge">$(echo $badge | sed 's/badge-//' | tr '[:lower:]' '[:upper:]' | sed 's/L1/L1 Fundamentals/;s/L2/L2 Technical/;s/L3/L3 Advanced/')</div>
          <h1>$title</h1>
$content
          <nav class="page-nav">
            <a href="$prev_file" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">$prev_title</span>
            </a>
            <a href="$next_file" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">$next_title</span>
            </a>
          </nav>
        </article>
      </div>
    </main>
  </div>
  <script src="main.js"></script>
</body>
</html>
PAGEEOF
    echo "Created: $filename"
}

echo "Generating comprehensive IAM guide pages..."

# ============================================================================
# SECTION 1: IAM FOUNDATIONS
# ============================================================================

# 1-4 Access Control Models
cat > "$OUTPUT_DIR/1-4-access-control-models.html" << 'PAGEEOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Access Control Models - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="page-wrapper">
    <nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
    </nav>
    <main class="main-content">
      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge badge-l1">L1 Fundamentals</div>
          <h1>Access Control Models: DAC, MAC, RBAC, ABAC</h1>
          
          <div class="overview-box">
            <h3>🎯 What This Page Covers</h3>
            <p>Understanding access control models is essential for IAM architecture. This covers DAC, MAC, RBAC, and ABAC with real enterprise implementations.</p>
          </div>

          <h2 id="overview">Access Control Models Overview</h2>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         ACCESS CONTROL MODELS                                            │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│  DAC (Discretionary)     │  MAC (Mandatory)         │  RBAC (Role-Based)                │
│  Owner controls access   │  System enforces labels  │  Roles grant permissions          │
│  Ex: SharePoint sharing  │  Ex: Military/SELinux    │  Ex: AD Groups, Azure RBAC        │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│  ABAC (Attribute-Based)                │  ReBAC (Relationship-Based)                    │
│  Policies evaluate attributes          │  Access based on relationships                 │
│  Ex: AWS IAM, Conditional Access       │  Ex: Google Docs, GitHub                       │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="dac">DAC: Discretionary Access Control</h2>
          <p>Resource <strong>owner</strong> decides who gets access. Most common in everyday computing.</p>
          
          <div class="code-block">
            <div class="code-header"><span class="code-language">DAC Example: Windows NTFS</span></div>
            <pre><code># View permissions
icacls "D:\Projects\budget.xlsx"
# CORP\schen:(F)         - Full Control (Owner)
# CORP\Finance-Team:(R)  - Read only

# Owner grants access
icacls "D:\Projects\budget.xlsx" /grant "CORP\mwilson:(R)"</code></pre>
          </div>

          <h2 id="rbac">RBAC: Role-Based Access Control</h2>
          <p><strong>Most widely used in enterprise.</strong> Users → Roles → Permissions.</p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              RBAC MODEL                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│   USERS              ROLES                    PERMISSIONS                               │
│   Sarah ─────┐       ┌─────────────┐         ┌──────────────────────┐                  │
│   Mike  ─────┼──────►│  Engineer   │────────►│ Read code repos      │                  │
│              │       └─────────────┘         │ Write dev env        │                  │
│   John ──────┼──────►┌─────────────┐         └──────────────────────┘                  │
│              │       │  Manager    │────────►┌──────────────────────┐                  │
│              └──────►└─────────────┘         │ Approve requests     │                  │
│                                              │ + All Engineer perms │                  │
│                                              └──────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <div class="code-block">
            <div class="code-header"><span class="code-language">RBAC with AD Groups</span></div>
            <pre><code># Assign role via group membership
Add-ADGroupMember -Identity "APP-Salesforce-Users" -Members schen

# Azure RBAC assignment
New-AzRoleAssignment `
  -SignInName "schen@company.com" `
  -RoleDefinitionName "Contributor" `
  -ResourceGroupName "prod-resources"</code></pre>
          </div>

          <h2 id="abac">ABAC: Attribute-Based Access Control</h2>
          <p>Access based on <strong>attributes</strong> of user, resource, action, and environment.</p>

          <div class="table-wrapper">
            <table>
              <thead><tr><th>Attribute Type</th><th>Examples</th></tr></thead>
              <tbody>
                <tr><td><strong>Subject</strong></td><td>department, title, clearance, location</td></tr>
                <tr><td><strong>Resource</strong></td><td>classification, owner, sensitivity</td></tr>
                <tr><td><strong>Action</strong></td><td>read, write, delete, approve</td></tr>
                <tr><td><strong>Environment</strong></td><td>time, IP address, device compliance</td></tr>
              </tbody>
            </table>
          </div>

          <div class="code-block">
            <div class="code-header"><span class="code-language">ABAC: AWS IAM Policy</span></div>
            <pre><code>{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::company-data/*",
  "Condition": {
    "StringEquals": {
      "aws:PrincipalTag/Department": "Finance"
    },
    "IpAddress": {
      "aws:SourceIp": "10.0.0.0/8"
    }
  }
}</code></pre>
          </div>

          <h2 id="comparison">When to Use Each Model</h2>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Model</th><th>Best For</th><th>Real Example</th></tr></thead>
              <tbody>
                <tr><td><strong>DAC</strong></td><td>File sharing, collaboration</td><td>SharePoint, Google Drive</td></tr>
                <tr><td><strong>MAC</strong></td><td>Military, classified data</td><td>Government systems, SELinux</td></tr>
                <tr><td><strong>RBAC</strong></td><td>Enterprise apps, clear roles</td><td>AD Groups, Azure RBAC</td></tr>
                <tr><td><strong>ABAC</strong></td><td>Complex, dynamic policies</td><td>AWS IAM, Conditional Access</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Interview Points</div>
              <ul>
                <li><strong>RBAC vs ABAC:</strong> RBAC is simpler (static roles), ABAC is flexible (dynamic attributes)</li>
                <li><strong>Most enterprises use hybrid:</strong> RBAC for base + ABAC for conditions</li>
                <li><strong>Conditional Access = ABAC</strong> applied at authentication layer</li>
                <li><strong>Know real examples:</strong> AD Groups (RBAC), AWS IAM Policies (ABAC)</li>
              </ul>
            </div>
          </div>

          <nav class="page-nav">
            <a href="1-3-identity-lifecycle.html" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">Identity Lifecycle</span>
            </a>
            <a href="1-5-least-privilege-sod.html" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">Least Privilege & SoD</span>
            </a>
          </nav>
        </article>
      </div>
    </main>
  </div>
  <script src="main.js"></script>
</body>
</html>
PAGEEOF
echo "Created: 1-4-access-control-models.html"

# 1-5 Least Privilege & SoD
cat > "$OUTPUT_DIR/1-5-least-privilege-sod.html" << 'PAGEEOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Least Privilege & SoD - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="page-wrapper">
    <nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
    </nav>
    <main class="main-content">
      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge badge-l1">L1 Fundamentals</div>
          <h1>Least Privilege & Separation of Duties</h1>
          
          <div class="overview-box">
            <h3>🎯 What This Page Covers</h3>
            <p>Two fundamental security principles that prevent insider threats and reduce blast radius of compromises. Essential for compliance (SOX, PCI-DSS, HIPAA).</p>
          </div>

          <h2 id="least-privilege">Principle of Least Privilege (PoLP)</h2>
          <p>Users should have <strong>only the minimum permissions</strong> needed to perform their job functions, and only for the time they need them.</p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                     LEAST PRIVILEGE IN PRACTICE                                          │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   ❌ BAD: Permanent Admin Access                                                         │
│   ┌────────────────────────────────────────────────────────────────────────────┐        │
│   │  User "jsmith" has Global Admin 24/7/365                                   │        │
│   │  Risk: Credential theft = complete compromise                              │        │
│   └────────────────────────────────────────────────────────────────────────────┘        │
│                                                                                          │
│   ✅ GOOD: Just-in-Time (JIT) Access                                                     │
│   ┌────────────────────────────────────────────────────────────────────────────┐        │
│   │  User "jsmith" has standard access normally                                │        │
│   │  Requests Global Admin via PIM → Approved → 2 hours only                   │        │
│   │  Risk: Limited window for credential theft                                 │        │
│   └────────────────────────────────────────────────────────────────────────────┘        │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h3>Implementing Least Privilege</h3>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Area</th><th>Implementation</th><th>Tools</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>Admin Access</strong></td>
                  <td>JIT elevation, time-limited roles</td>
                  <td>Entra PIM, CyberArk, AWS IAM Roles</td>
                </tr>
                <tr>
                  <td><strong>Application Access</strong></td>
                  <td>Role-based, request-based for sensitive</td>
                  <td>SailPoint, Okta, ServiceNow</td>
                </tr>
                <tr>
                  <td><strong>Data Access</strong></td>
                  <td>Need-to-know, classification-based</td>
                  <td>Purview, DLP, file permissions</td>
                </tr>
                <tr>
                  <td><strong>Network Access</strong></td>
                  <td>Microsegmentation, ZTNA</td>
                  <td>Zscaler, Palo Alto, Tailscale</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="code-block">
            <div class="code-header"><span class="code-language">Entra PIM: JIT Admin Access</span></div>
            <pre><code># User requests elevation via PIM
# 1. Open PIM in Azure Portal
# 2. Click "Activate" on eligible role
# 3. Provide justification
# 4. Role active for configured duration (e.g., 2 hours)

# PowerShell: Check eligible roles
Get-AzureADMSPrivilegedRoleAssignment -ProviderId "aadRoles" `
  -ResourceId $tenantId -Filter "subjectId eq '$userId'"

# Audit: Who activated what
Get-AzureADAuditDirectoryLogs -Filter "activityDisplayName eq 'Add member to role completed (PIM activation)'"</code></pre>
          </div>

          <h2 id="sod">Separation of Duties (SoD)</h2>
          <p>No single person should have enough access to commit fraud or cause significant harm without detection. Split critical functions across multiple people.</p>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                     SEPARATION OF DUTIES EXAMPLES                                        │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   FINANCE: Payment Processing                                                           │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐            │
│   │   CREATE VENDOR     │  │   APPROVE PAYMENT   │  │   RELEASE PAYMENT   │            │
│   │   (Accounts Payable)│  │   (AP Manager)      │  │   (Treasury)        │            │
│   │                     │  │                     │  │                     │            │
│   │   Person A          │  │   Person B          │  │   Person C          │            │
│   └─────────────────────┘  └─────────────────────┘  └─────────────────────┘            │
│                                                                                          │
│   IT: Code Deployment                                                                    │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐            │
│   │   WRITE CODE        │  │   REVIEW/APPROVE    │  │   DEPLOY TO PROD    │            │
│   │   (Developer)       │  │   (Tech Lead)       │  │   (DevOps/SRE)      │            │
│   └─────────────────────┘  └─────────────────────┘  └─────────────────────┘            │
│                                                                                          │
│   CONFLICT: Same person should NOT have both "Create Vendor" AND "Approve Payment"      │
│             This would allow creation of fake vendors and self-approval of payments     │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h3>Common SoD Violations (Toxic Combinations)</h3>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Function 1</th><th>Function 2</th><th>Risk</th></tr></thead>
              <tbody>
                <tr>
                  <td>Create Vendor</td>
                  <td>Approve Payment</td>
                  <td>Create fake vendor, pay self</td>
                </tr>
                <tr>
                  <td>Create User</td>
                  <td>Assign Permissions</td>
                  <td>Create backdoor account with admin</td>
                </tr>
                <tr>
                  <td>Write Code</td>
                  <td>Deploy to Production</td>
                  <td>Deploy malicious code without review</td>
                </tr>
                <tr>
                  <td>Process Refund</td>
                  <td>Approve Refund</td>
                  <td>Self-approve fraudulent refunds</td>
                </tr>
                <tr>
                  <td>Modify Audit Logs</td>
                  <td>System Admin</td>
                  <td>Cover tracks after malicious activity</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Implementing SoD Controls</h3>
          <div class="code-block">
            <div class="code-header"><span class="code-language">SailPoint: SoD Policy Definition</span></div>
            <pre><code># SoD Policy: "Vendor Management Conflict"
{
  "name": "AP-Vendor-Payment-Conflict",
  "description": "Users cannot both create vendors and approve payments",
  "leftCriteria": {
    "entitlements": ["SAP:Create_Vendor", "Oracle:AP_VENDOR_ENTRY"]
  },
  "rightCriteria": {
    "entitlements": ["SAP:Approve_Payment", "Oracle:AP_PAYMENT_APPROVAL"]
  },
  "conflictAction": "BLOCK",  // or "ALLOW_WITH_MITIGATION"
  "mitigatingControl": "Quarterly review by Internal Audit"
}</code></pre>
          </div>

          <h2 id="compliance">Compliance Requirements</h2>
          <div class="table-wrapper">
            <table>
              <thead><tr><th>Framework</th><th>Least Privilege Requirement</th><th>SoD Requirement</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>SOX</strong></td>
                  <td>Access limited to job function</td>
                  <td>Required for financial systems</td>
                </tr>
                <tr>
                  <td><strong>PCI-DSS</strong></td>
                  <td>Req 7: Restrict access to need-to-know</td>
                  <td>Req 6.4.2: Separate dev/test/prod</td>
                </tr>
                <tr>
                  <td><strong>HIPAA</strong></td>
                  <td>Minimum necessary standard</td>
                  <td>Workforce clearance procedures</td>
                </tr>
                <tr>
                  <td><strong>ISO 27001</strong></td>
                  <td>A.9.2.3: Management of privileged access</td>
                  <td>A.6.1.2: Segregation of duties</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Interview Points</div>
              <ul>
                <li><strong>Least Privilege:</strong> Minimum access needed, for minimum time (JIT)</li>
                <li><strong>SoD:</strong> Split critical functions to prevent fraud without collusion</li>
                <li><strong>Know toxic combinations:</strong> Create vendor + approve payment, write code + deploy</li>
                <li><strong>Tools:</strong> Entra PIM (JIT), SailPoint (SoD policies), access certifications</li>
                <li><strong>Compliance:</strong> SOX requires SoD for financial systems</li>
              </ul>
            </div>
          </div>

          <nav class="page-nav">
            <a href="1-4-access-control-models.html" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">Access Control Models</span>
            </a>
            <a href="1-6-directory-services.html" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">Directory Services</span>
            </a>
          </nav>
        </article>
      </div>
    </main>
  </div>
  <script src="main.js"></script>
</body>
</html>
PAGEEOF
echo "Created: 1-5-least-privilege-sod.html"

echo "Section 1 foundations complete. Generating Section 4 (Entra ID)..."

# 4-3 Conditional Access
cat > "$OUTPUT_DIR/4-3-conditional-access.html" << 'PAGEEOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Conditional Access - Ultimate IAM Security Guide</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="page-wrapper">
    <nav class="sidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-logo">
          <div class="sidebar-logo-icon">🔐</div>
          <div class="sidebar-logo-text">IAM <span>Guide</span></div>
        </a>
      </div>
    </nav>
    <main class="main-content">
      <div class="content-wrapper">
        <article class="content-main">
          <div class="badge badge-l2">L2 Technical</div>
          <h1>Conditional Access: Zero Trust Policy Engine</h1>
          
          <div class="overview-box">
            <h3>🎯 What This Page Covers</h3>
            <p>Conditional Access is Microsoft's Zero Trust policy engine. Every sign-in is evaluated against policies that consider user, device, location, app, and risk. This is critical for enterprise security.</p>
          </div>

          <h2 id="how-it-works">How Conditional Access Works</h2>

          <div class="flow-diagram">
            <pre>
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    CONDITIONAL ACCESS EVALUATION FLOW                                    │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│   USER SIGNS IN                                                                          │
│        │                                                                                 │
│        ▼                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                     SIGNAL COLLECTION (Conditions)                               │   │
│   │  • User: Who? Groups? Roles? Risk level?                                        │   │
│   │  • Device: Compliant? Hybrid joined? Platform?                                  │   │
│   │  • Location: Named location? Country? IP range?                                 │   │
│   │  • Application: Which app? Client app type?                                     │   │
│   │  • Risk: Sign-in risk? User risk?                                               │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│        │                                                                                 │
│        ▼                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                     POLICY EVALUATION                                            │   │
│   │                                                                                  │   │
│   │  FOR EACH applicable policy:                                                    │   │
│   │    IF all conditions match THEN apply access controls                           │   │
│   │                                                                                  │   │
│   │  Multiple policies can apply - most restrictive wins                            │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│        │                                                                                 │
│        ▼                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                     ACCESS DECISION                                              │   │
│   │                                                                                  │   │
│   │  ✅ GRANT: Allow access (possibly with controls like MFA)                       │   │
│   │  ❌ BLOCK: Deny access completely                                                │   │
│   │  ⚠️ GRANT with CONTROLS: Require MFA, compliant device, app protection, etc.   │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
            </pre>
          </div>

          <h2 id="common-policies">Common CA Policies (Enterprise Baseline)</h2>

          <div class="table-wrapper">
            <table>
              <thead><tr><th>Policy Name</th><th>Conditions</th><th>Controls</th><th>Purpose</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>Require MFA for All Users</strong></td>
                  <td>All users, all cloud apps</td>
                  <td>Require MFA</td>
                  <td>Baseline protection</td>
                </tr>
                <tr>
                  <td><strong>Block Legacy Auth</strong></td>
                  <td>All users, legacy auth clients</td>
                  <td>Block</td>
                  <td>Prevent IMAP/POP/SMTP attacks</td>
                </tr>
                <tr>
                  <td><strong>Require Compliant Device</strong></td>
                  <td>All users, Office 365 apps</td>
                  <td>Require compliant device</td>
                  <td>Ensure managed devices</td>
                </tr>
                <tr>
                  <td><strong>Block High Risk Sign-ins</strong></td>
                  <td>All users, sign-in risk: High</td>
                  <td>Block</td>
                  <td>Stop compromised accounts</td>
                </tr>
                <tr>
                  <td><strong>Require MFA for Admins</strong></td>
                  <td>Directory roles (GA, etc.)</td>
                  <td>Require MFA + compliant device</td>
                  <td>Protect privileged access</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="policy-example">Policy Deep Dive: Require MFA Outside Network</h2>

          <div class="code-block">
            <div class="code-header"><span class="code-language">CA Policy Configuration</span></div>
            <pre><code>Policy Name: "Require MFA for External Access"

ASSIGNMENTS:
  Users and Groups:
    Include: All users
    Exclude: Break-glass accounts, Service accounts
  
  Cloud Apps:
    Include: All cloud apps
    Exclude: None
  
  Conditions:
    Locations:
      Include: All locations
      Exclude: "Corporate Network" (named location: 10.0.0.0/8, office IPs)
    
    Device Platforms: All platforms
    Client Apps: Browser, Mobile apps and desktop clients

ACCESS CONTROLS:
  Grant:
    ☑ Require multi-factor authentication
    
  Session:
    Sign-in frequency: 12 hours

RESULT: 
  - On corporate network → No MFA prompt
  - From home/coffee shop → MFA required every 12 hours</code></pre>
          </div>

          <h2 id="named-locations">Named Locations Setup</h2>
          <div class="code-block">
            <div class="code-header"><span class="code-language">PowerShell: Create Named Locations</span></div>
            <pre><code># Connect to Microsoft Graph
Connect-MgGraph -Scopes "Policy.ReadWrite.ConditionalAccess"

# Create IP-based named location
$params = @{
    "@odata.type" = "#microsoft.graph.ipNamedLocation"
    displayName = "Corporate Network"
    isTrusted = $true
    ipRanges = @(
        @{ "@odata.type" = "#microsoft.graph.iPv4CidrRange"; cidrAddress = "10.0.0.0/8" }
        @{ "@odata.type" = "#microsoft.graph.iPv4CidrRange"; cidrAddress = "192.168.1.0/24" }
        @{ "@odata.type" = "#microsoft.graph.iPv4CidrRange"; cidrAddress = "203.0.113.50/32" }  # Office IP
    )
}
New-MgIdentityConditionalAccessNamedLocation -BodyParameter $params

# Create country-based named location
$countryParams = @{
    "@odata.type" = "#microsoft.graph.countryNamedLocation"
    displayName = "Blocked Countries"
    countriesAndRegions = @("KP", "IR", "RU", "CN")  # North Korea, Iran, Russia, China
    includeUnknownCountriesAndRegions = $false
}
New-MgIdentityConditionalAccessNamedLocation -BodyParameter $countryParams</code></pre>
          </div>

          <h2 id="troubleshooting">Troubleshooting CA Issues</h2>

          <div class="accordion">
            <div class="accordion-item">
              <button class="accordion-header">
                <span>🔴 User blocked but shouldn't be</span>
                <span class="accordion-icon">▼</span>
              </button>
              <div class="accordion-content">
                <div class="accordion-body">
                  <p><strong>Step 1:</strong> Check sign-in logs</p>
                  <div class="code-block">
                    <pre><code>Entra ID → Sign-in logs → Filter by user → Click failed sign-in
Look at: 
  - "Conditional Access" tab → Shows which policy blocked
  - "Basic info" tab → Shows IP, device, location detected
  - "Device info" tab → Shows compliance status</code></pre>
                  </div>
                  <p><strong>Step 2:</strong> Use What If tool</p>
                  <div class="code-block">
                    <pre><code>Entra ID → Conditional Access → What If
Select:
  - User: affected user
  - Cloud app: app they're accessing
  - IP address: their current IP
  - Device platform: their device
Click "What If" → See which policies would apply</code></pre>
                  </div>
                </div>
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header">
                <span>🟡 User gets MFA prompt repeatedly</span>
                <span class="accordion-icon">▼</span>
              </button>
              <div class="accordion-content">
                <div class="accordion-body">
                  <p><strong>Common causes:</strong></p>
                  <ul>
                    <li>Sign-in frequency set too low</li>
                    <li>Persistent browser session disabled</li>
                    <li>Multiple CA policies conflicting</li>
                    <li>Token lifetime too short</li>
                  </ul>
                  <p><strong>Fix:</strong> Adjust session controls, use "persistent browser session" for trusted devices</p>
                </div>
              </div>
            </div>
          </div>

          <h2 id="interview-tips">Interview Tips</h2>
          <div class="callout interview">
            <div class="callout-content">
              <div class="callout-title">💡 Key Interview Points</div>
              <ul>
                <li><strong>CA = Zero Trust policy engine</strong> - evaluates every sign-in</li>
                <li><strong>Signals:</strong> User, device, location, app, risk</li>
                <li><strong>Controls:</strong> Block, require MFA, require compliant device, limit session</li>
                <li><strong>Know baseline policies:</strong> MFA for all, block legacy auth, require compliance</li>
                <li><strong>Troubleshooting:</strong> Sign-in logs + What If tool</li>
                <li><strong>Break-glass accounts:</strong> Always exclude from blocking policies</li>
              </ul>
            </div>
          </div>

          <nav class="page-nav">
            <a href="4-2-entra-objects.html" class="page-nav-link prev">
              <span class="page-nav-label">← Previous</span>
              <span class="page-nav-title">Entra ID Objects</span>
            </a>
            <a href="4-4-entra-pim.html" class="page-nav-link next">
              <span class="page-nav-label">Next →</span>
              <span class="page-nav-title">Entra PIM</span>
            </a>
          </nav>
        </article>
      </div>
    </main>
  </div>
  <script src="main.js"></script>
</body>
</html>
PAGEEOF
echo "Created: 4-3-conditional-access.html"

echo "Generating more pages..."
