/* ============================================
   Ultimate IAM Security Guide - JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
  initSidebar();
  initTabs();
  initAccordions();
  initCodeCopy();
  initSearch();
  initMobileMenu();
  initTableOfContents();
  highlightCurrentNav();
});

/* Sidebar Navigation */
function initSidebar() {
  const sectionHeaders = document.querySelectorAll('.nav-section-header');
  
  sectionHeaders.forEach(header => {
    header.addEventListener('click', function() {
      this.classList.toggle('collapsed');
    });
  });
  
  // Expand section containing current page
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const currentLink = document.querySelector(`.nav-item[href="${currentPath}"]`);
  
  if (currentLink) {
    currentLink.classList.add('active');
    const section = currentLink.closest('.nav-section');
    if (section) {
      const header = section.querySelector('.nav-section-header');
      if (header) {
        header.classList.remove('collapsed');
        header.classList.add('active');
      }
    }
  }
}

/* Highlight Current Navigation Item */
function highlightCurrentNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navItems = document.querySelectorAll('.nav-item');
  
  navItems.forEach(item => {
    if (item.getAttribute('href') === currentPath) {
      item.classList.add('active');
    }
  });
}

/* Tabs */
function initTabs() {
  const tabContainers = document.querySelectorAll('.tabs');
  
  tabContainers.forEach(container => {
    const buttons = container.querySelectorAll('.tab-btn');
    const contents = container.querySelectorAll('.tab-content');
    
    buttons.forEach((btn, index) => {
      btn.addEventListener('click', () => {
        // Remove active class from all
        buttons.forEach(b => b.classList.remove('active'));
        contents.forEach(c => c.classList.remove('active'));
        
        // Add active class to clicked
        btn.classList.add('active');
        contents[index].classList.add('active');
      });
    });
  });
}

/* Accordions */
function initAccordions() {
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  
  accordionHeaders.forEach(header => {
    header.addEventListener('click', function() {
      const item = this.parentElement;
      const wasOpen = item.classList.contains('open');
      
      // Optional: Close other items in same accordion
      // const accordion = item.parentElement;
      // accordion.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('open'));
      
      if (!wasOpen) {
        item.classList.add('open');
      } else {
        item.classList.remove('open');
      }
    });
  });
}

/* Code Copy */
function initCodeCopy() {
  const copyButtons = document.querySelectorAll('.code-copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', async function() {
      const codeBlock = this.closest('.code-block');
      const code = codeBlock.querySelector('code').textContent;
      
      try {
        await navigator.clipboard.writeText(code);
        this.classList.add('copied');
        this.innerHTML = '<span>✓</span> Copied!';
        
        setTimeout(() => {
          this.classList.remove('copied');
          this.innerHTML = '<span>📋</span> Copy';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
      }
    });
  });
}

/* Search Modal */
function initSearch() {
  const searchTrigger = document.querySelector('.search-trigger');
  const searchModal = document.querySelector('.search-modal');
  const searchInput = document.querySelector('.search-input');
  const searchResults = document.querySelector('.search-results');
  
  if (!searchTrigger || !searchModal) return;
  
  // Search data - pages with titles and keywords
  const searchData = [
    // Section 1: IAM Foundations
    { title: 'IAM Overview', path: '1-1-iam-overview.html', section: 'IAM Foundations', keywords: 'iam identity access management overview introduction fundamentals' },
    { title: 'Authentication vs Authorization', path: '1-2-authn-vs-authz.html', section: 'IAM Foundations', keywords: 'authentication authorization authn authz difference' },
    { title: 'Identity Lifecycle', path: '1-3-identity-lifecycle.html', section: 'IAM Foundations', keywords: 'lifecycle joiner mover leaver provisioning deprovisioning' },
    { title: 'Access Control Models', path: '1-4-access-control-models.html', section: 'IAM Foundations', keywords: 'rbac abac pbac dac mac access control models' },
    { title: 'Least Privilege & SoD', path: '1-5-least-privilege-sod.html', section: 'IAM Foundations', keywords: 'least privilege separation duties sod jit' },
    { title: 'Directory Services', path: '1-6-directory-services.html', section: 'IAM Foundations', keywords: 'ldap active directory ad ds gpo ou' },
    { title: 'Identity Governance', path: '1-7-identity-governance.html', section: 'IAM Foundations', keywords: 'iga governance access reviews certifications attestations' },
    { title: 'Privileged Access', path: '1-8-privileged-access.html', section: 'IAM Foundations', keywords: 'pam privileged access management vaulting session' },
    
    // Section 2: Authentication Protocols
    { title: 'Authentication Factors', path: '2-1-authentication-factors.html', section: 'Authentication Protocols', keywords: 'mfa multi factor authentication passwordless biometrics fido2' },
    { title: 'Kerberos', path: '2-2-kerberos.html', section: 'Authentication Protocols', keywords: 'kerberos kdc tgt tgs ticket golden silver' },
    { title: 'NTLM', path: '2-3-ntlm.html', section: 'Authentication Protocols', keywords: 'ntlm pass the hash pth deprecated' },
    { title: 'SAML', path: '2-4-saml.html', section: 'Authentication Protocols', keywords: 'saml assertion idp sp identity provider xml' },
    { title: 'OAuth 2.0', path: '2-5-oauth2.html', section: 'Authentication Protocols', keywords: 'oauth authorization code pkce client credentials tokens' },
    { title: 'OpenID Connect', path: '2-6-oidc.html', section: 'Authentication Protocols', keywords: 'oidc openid connect id token jwt claims userinfo' },
    { title: 'RADIUS & TACACS+', path: '2-7-radius-tacacs.html', section: 'Authentication Protocols', keywords: 'radius tacacs aaa network 802.1x nac' },
    { title: 'Certificates & PKI', path: '2-8-certificates-pki.html', section: 'Authentication Protocols', keywords: 'x509 certificate pki smart card ca' },
    { title: 'SSO Mechanisms', path: '2-9-sso-mechanisms.html', section: 'Authentication Protocols', keywords: 'sso single sign on desktop web mobile token' },
    { title: 'Authentication Attacks & Defense', path: '2-10-auth-attacks-defense.html', section: 'Authentication Protocols', keywords: 'credential stuffing phishing mfa bypass session hijacking' },
    
    // Section 3: Federation & SSO
    { title: 'Federation Fundamentals', path: '3-1-federation-fundamentals.html', section: 'Federation & SSO', keywords: 'federation trust relationship idp sp circle of trust' },
    { title: 'SAML Federation', path: '3-2-saml-federation.html', section: 'Federation & SSO', keywords: 'saml federation metadata attribute mapping assertions' },
    { title: 'OIDC Federation', path: '3-3-oidc-federation.html', section: 'Federation & SSO', keywords: 'oidc federation dynamic registration discovery jwks' },
    { title: 'WS-Federation & Legacy', path: '3-4-ws-federation-legacy.html', section: 'Federation & SSO', keywords: 'ws-fed ws-trust adfs claims legacy' },
    { title: 'B2B & B2C Federation', path: '3-5-b2b-b2c-federation.html', section: 'Federation & SSO', keywords: 'b2b b2c partner access guest social login ciam' },
    { title: 'Federation Troubleshooting', path: '3-6-federation-troubleshooting.html', section: 'Federation & SSO', keywords: 'troubleshooting saml tracer token debug clock skew' },
    
    // Section 4: Microsoft Entra ID
    { title: 'Entra ID Overview', path: '4-1-entra-overview.html', section: 'Microsoft Entra ID', keywords: 'azure ad entra id tenant licensing p1 p2' },
    { title: 'Entra ID Objects', path: '4-2-entra-objects.html', section: 'Microsoft Entra ID', keywords: 'users groups service principal managed identity app registration' },
    { title: 'Conditional Access', path: '4-3-conditional-access.html', section: 'Microsoft Entra ID', keywords: 'conditional access ca policy named locations device compliance' },
    { title: 'Entra PIM', path: '4-4-entra-pim.html', section: 'Microsoft Entra ID', keywords: 'pim privileged identity management eligible active jit' },
    { title: 'Entra Governance', path: '4-5-entra-governance.html', section: 'Microsoft Entra ID', keywords: 'access reviews entitlement management lifecycle workflows access packages' },
    { title: 'Entra Protection', path: '4-6-entra-protection.html', section: 'Microsoft Entra ID', keywords: 'identity protection risk policies risky users sign-ins' },
    { title: 'Hybrid Identity', path: '4-7-hybrid-identity.html', section: 'Microsoft Entra ID', keywords: 'azure ad connect cloud sync password hash pass-through adfs' },
    { title: 'Workload Identity', path: '4-8-entra-workload-id.html', section: 'Microsoft Entra ID', keywords: 'managed identity workload identity federation service principal' },
    
    // Section 5: Okta
    { title: 'Okta Overview', path: '5-1-okta-overview.html', section: 'Okta', keywords: 'okta universal directory org oie classic' },
    { title: 'Okta Authentication', path: '5-2-okta-authentication.html', section: 'Okta', keywords: 'okta sign-on policy authenticators adaptive mfa fastpass' },
    { title: 'Okta Authorization', path: '5-3-okta-authorization.html', section: 'Okta', keywords: 'okta authorization server scopes claims hooks tokens' },
    { title: 'Okta Lifecycle', path: '5-4-okta-lifecycle.html', section: 'Okta', keywords: 'okta lifecycle provisioning scim workflows hr' },
    { title: 'Okta Integration', path: '5-5-okta-integration.html', section: 'Okta', keywords: 'okta oin saml oidc integration api access' },
    { title: 'Okta Administration', path: '5-6-okta-admin.html', section: 'Okta', keywords: 'okta admin console delegated system log rate limits' },
    
    // Section 6: SailPoint & IGA
    { title: 'SailPoint Overview', path: '6-1-sailpoint-overview.html', section: 'SailPoint & IGA', keywords: 'sailpoint identitynow identityiq iga' },
    { title: 'IGA Fundamentals', path: '6-2-iga-fundamentals.html', section: 'SailPoint & IGA', keywords: 'iga identity governance access certifications compliance audit' },
    { title: 'Access Certifications', path: '6-3-access-certifications.html', section: 'SailPoint & IGA', keywords: 'certification campaigns manager owner micro remediation' },
    { title: 'Role Management', path: '6-4-role-management.html', section: 'SailPoint & IGA', keywords: 'role mining engineering lifecycle business it explosion' },
    { title: 'SoD Management', path: '6-5-sod-management.html', section: 'SailPoint & IGA', keywords: 'separation duties sod violations preventive detective toxic' },
    { title: 'Provisioning Workflows', path: '6-6-provisioning-workflows.html', section: 'SailPoint & IGA', keywords: 'access request workflow approval fulfillment connectors scim' },
    
    // Section 7: PAM
    { title: 'PAM Overview', path: '7-1-pam-overview.html', section: 'Privileged Access Management', keywords: 'pam privileged access management architecture accounts' },
    { title: 'Password Vaulting', path: '7-2-password-vaulting.html', section: 'Privileged Access Management', keywords: 'vault credential rotation check-out check-in emergency' },
    { title: 'Session Management', path: '7-3-session-management.html', section: 'Privileged Access Management', keywords: 'session recording keystroke logging proxy monitoring isolation' },
    { title: 'Just-in-Time Access', path: '7-4-jit-access.html', section: 'Privileged Access Management', keywords: 'jit just in time temporary elevation approval zero standing' },
    { title: 'Secrets Management', path: '7-5-secrets-management.html', section: 'Privileged Access Management', keywords: 'hashicorp vault azure key vault aws secrets manager rotation' },
    { title: 'PAM Vendors', path: '7-6-pam-vendors.html', section: 'Privileged Access Management', keywords: 'cyberark beyondtrust delinea comparison features' },
    
    // Section 8: Cloud IAM
    { title: 'AWS IAM', path: '8-1-aws-iam.html', section: 'Cloud IAM', keywords: 'aws iam policies roles users groups permission boundaries scp' },
    { title: 'AWS Identity Center', path: '8-2-aws-identity-center.html', section: 'Cloud IAM', keywords: 'aws sso identity center permission sets abac' },
    { title: 'Azure RBAC', path: '8-3-azure-rbac.html', section: 'Cloud IAM', keywords: 'azure rbac roles custom scope deny pim' },
    { title: 'GCP IAM', path: '8-4-gcp-iam.html', section: 'Cloud IAM', keywords: 'gcp iam resource hierarchy roles service accounts workload' },
    { title: 'Multi-Cloud Identity', path: '8-5-multi-cloud-identity.html', section: 'Cloud IAM', keywords: 'multi cloud identity federation ciem' },
    { title: 'Kubernetes IAM', path: '8-6-kubernetes-iam.html', section: 'Cloud IAM', keywords: 'kubernetes k8s rbac service accounts oidc pod identity' },
    { title: 'Infrastructure as Code', path: '8-7-infrastructure-as-code.html', section: 'Cloud IAM', keywords: 'terraform iac policy code cloudformation drift gitops' },
    { title: 'Cloud PAM', path: '8-8-cloud-pam.html', section: 'Cloud IAM', keywords: 'cloud pam jit ciem permission analytics' },
    
    // Section 9: IAM Architecture
    { title: 'Enterprise IAM Architecture', path: '9-1-enterprise-iam-arch.html', section: 'IAM Architecture', keywords: 'enterprise architecture reference components integration' },
    { title: 'Zero Trust IAM', path: '9-2-zero-trust-iam.html', section: 'IAM Architecture', keywords: 'zero trust never trust always verify continuous micro-segmentation' },
    { title: 'Hybrid Cloud IAM', path: '9-3-hybrid-cloud-iam.html', section: 'IAM Architecture', keywords: 'hybrid cloud on-prem identity bridge synchronization' },
    { title: 'CIAM Architecture', path: '9-4-ciam-architecture.html', section: 'IAM Architecture', keywords: 'ciam customer b2c progressive profiling social consent' },
    { title: 'API Security', path: '9-5-api-security.html', section: 'IAM Architecture', keywords: 'api gateway jwt oauth rate limiting api keys tokens' },
    { title: 'High Availability', path: '9-6-high-availability.html', section: 'IAM Architecture', keywords: 'ha dr disaster recovery geo redundancy failover backup' },
    
    // Section 10: IAM Migrations
    { title: 'Migration Planning', path: '10-1-migration-planning.html', section: 'IAM Migrations', keywords: 'migration planning assessment waves success rollback' },
    { title: 'IdP Migrations', path: '10-2-idp-migrations.html', section: 'IAM Migrations', keywords: 'okta entra adfs idp consolidation migration' },
    { title: 'Legacy Modernization', path: '10-3-legacy-modernization.html', section: 'IAM Migrations', keywords: 'ldap cloud on-prem legacy sso saml oidc' },
    { title: 'IGA & PAM Migrations', path: '10-4-iga-pam-migrations.html', section: 'IAM Migrations', keywords: 'iga pam platform migration data parallel' },
    { title: 'Application Migration', path: '10-5-app-migration.html', section: 'IAM Migrations', keywords: 'application migration protocol testing cutover' },
    { title: 'Coexistence & Cutover', path: '10-6-coexistence-cutover.html', section: 'IAM Migrations', keywords: 'coexistence phased big bang validation decommissioning' },
    
    // Section 11: Security & Attacks
    { title: 'Identity Threat Landscape', path: '11-1-identity-threat-landscape.html', section: 'Security & Attacks', keywords: 'identity threats attack chains mitre att&ck actors' },
    { title: 'Credential Attacks', path: '11-2-credential-attacks.html', section: 'Security & Attacks', keywords: 'phishing credential stuffing password spraying brute force rainbow' },
    { title: 'Token & Session Attacks', path: '11-3-token-session-attacks.html', section: 'Security & Attacks', keywords: 'token theft replay session hijacking cookie golden saml' },
    { title: 'Privilege Escalation', path: '11-4-privilege-escalation.html', section: 'Security & Attacks', keywords: 'privilege escalation vertical horizontal ad attack paths cloud' },
    { title: 'Detection & Response', path: '11-5-detection-response.html', section: 'Security & Attacks', keywords: 'detection response ueba impossible travel incident playbooks' },
    
    // Section 12: Reference
    { title: 'IAM Glossary', path: '12-1-iam-glossary.html', section: 'Reference & Interview Prep', keywords: 'glossary terminology definitions terms' },
    { title: 'Interview Questions', path: '12-2-interview-questions.html', section: 'Reference & Interview Prep', keywords: 'interview questions answers l1 l2 l3' },
    { title: 'Scenario Questions', path: '12-3-scenario-questions.html', section: 'Reference & Interview Prep', keywords: 'scenario questions real-world solutions' },
    { title: 'Protocol Flows', path: '12-4-protocol-flows.html', section: 'Reference & Interview Prep', keywords: 'protocol flows kerberos saml oauth oidc diagrams' },
    { title: 'Comparison Tables', path: '12-5-comparison-tables.html', section: 'Reference & Interview Prep', keywords: 'comparison tables protocols vendors cloud access models' },
    { title: 'CLI & API Reference', path: '12-6-cli-api-reference.html', section: 'Reference & Interview Prep', keywords: 'cli api azure aws powershell okta graph commands' }
  ];
  
  // Open search modal
  searchTrigger.addEventListener('click', openSearch);
  
  // Keyboard shortcut (Cmd/Ctrl + K)
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
    if (e.key === 'Escape') {
      closeSearch();
    }
  });
  
  // Close on overlay click
  searchModal.addEventListener('click', (e) => {
    if (e.target === searchModal) {
      closeSearch();
    }
  });
  
  // Search input
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      
      if (query.length < 2) {
        searchResults.innerHTML = '<div class="search-no-results">Type at least 2 characters to search...</div>';
        return;
      }
      
      const results = searchData.filter(item => 
        item.title.toLowerCase().includes(query) ||
        item.keywords.includes(query) ||
        item.section.toLowerCase().includes(query)
      );
      
      if (results.length === 0) {
        searchResults.innerHTML = '<div class="search-no-results">No results found</div>';
        return;
      }
      
      searchResults.innerHTML = results.map(item => `
        <a href="${item.path}" class="search-result-item">
          <div class="search-result-title">${item.title}</div>
          <div class="search-result-path">${item.section}</div>
        </a>
      `).join('');
    });
  }
  
  function openSearch() {
    searchModal.classList.add('active');
    if (searchInput) {
      searchInput.focus();
    }
  }
  
  function closeSearch() {
    searchModal.classList.remove('active');
    if (searchInput) {
      searchInput.value = '';
    }
    if (searchResults) {
      searchResults.innerHTML = '';
    }
  }
}

/* Mobile Menu */
function initMobileMenu() {
  const toggle = document.querySelector('.mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  
  if (!toggle || !sidebar) return;
  
  toggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    toggle.classList.toggle('active');
  });
  
  // Close sidebar when clicking outside on mobile
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && 
        sidebar.classList.contains('open') && 
        !sidebar.contains(e.target) && 
        !toggle.contains(e.target)) {
      sidebar.classList.remove('open');
      toggle.classList.remove('active');
    }
  });
  
  // Close sidebar on navigation
  const navLinks = sidebar.querySelectorAll('.nav-item');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        sidebar.classList.remove('open');
        toggle.classList.remove('active');
      }
    });
  });
}

/* Table of Contents - Auto-generate and scroll spy */
function initTableOfContents() {
  const toc = document.querySelector('.toc-list');
  const contentMain = document.querySelector('.content-main');
  
  if (!toc || !contentMain) return;
  
  // Get all headings
  const headings = contentMain.querySelectorAll('h2, h3');
  
  if (headings.length === 0) return;
  
  // Generate TOC
  headings.forEach((heading, index) => {
    // Add ID if not present
    if (!heading.id) {
      heading.id = `heading-${index}`;
    }
    
    const li = document.createElement('li');
    li.className = 'toc-item';
    
    const a = document.createElement('a');
    a.href = `#${heading.id}`;
    a.className = `toc-link depth-${heading.tagName.toLowerCase().slice(1)}`;
    a.textContent = heading.textContent;
    
    a.addEventListener('click', (e) => {
      e.preventDefault();
      heading.scrollIntoView({ behavior: 'smooth' });
      history.pushState(null, null, `#${heading.id}`);
    });
    
    li.appendChild(a);
    toc.appendChild(li);
  });
  
  // Scroll spy
  const tocLinks = toc.querySelectorAll('.toc-link');
  
  const observerOptions = {
    rootMargin: '-80px 0px -80% 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        tocLinks.forEach(link => link.classList.remove('active'));
        const activeLink = toc.querySelector(`a[href="#${entry.target.id}"]`);
        if (activeLink) {
          activeLink.classList.add('active');
        }
      }
    });
  }, observerOptions);
  
  headings.forEach(heading => observer.observe(heading));
}

/* Smooth scroll for anchor links */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

/* Syntax highlighting helper (basic) */
function highlightCode() {
  document.querySelectorAll('pre code').forEach(block => {
    // Add language class if not present
    if (!block.className) {
      block.className = 'language-text';
    }
  });
}

/* Utility: Debounce function */
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/* Handle responsive changes */
window.addEventListener('resize', debounce(() => {
  const sidebar = document.querySelector('.sidebar');
  const toggle = document.querySelector('.mobile-menu-toggle');
  
  if (window.innerWidth > 768 && sidebar) {
    sidebar.classList.remove('open');
    if (toggle) toggle.classList.remove('active');
  }
}, 250));
