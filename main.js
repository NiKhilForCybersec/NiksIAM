/* ============================================
   Ultimate IAM Security Guide - JavaScript
   Dynamic Sidebar Navigation
   ============================================ */

// Navigation structure - defines all pages
const navigationData = [
  {
    section: "1. IAM Foundations",
    items: [
      { title: "IAM Overview", path: "1-1-iam-overview.html" },
      { title: "Authentication vs Authorization", path: "1-2-authn-vs-authz.html" },
      { title: "Identity Lifecycle", path: "1-3-identity-lifecycle.html" },
      { title: "Access Control Models", path: "1-4-access-control-models.html" },
      { title: "Least Privilege & SoD", path: "1-5-least-privilege-sod.html" },
      { title: "Directory Services", path: "1-6-directory-services.html" },
      { title: "Identity Governance", path: "1-7-identity-governance.html" },
      { title: "Privileged Access", path: "1-8-privileged-access.html" }
    ]
  },
  {
    section: "2. Authentication Protocols",
    items: [
      { title: "Authentication Factors", path: "2-1-authentication-factors.html" },
      { title: "Kerberos", path: "2-2-kerberos.html" },
      { title: "NTLM", path: "2-3-ntlm.html" },
      { title: "SAML", path: "2-4-saml.html" },
      { title: "OAuth 2.0", path: "2-5-oauth2.html" },
      { title: "OpenID Connect", path: "2-6-oidc.html" },
      { title: "RADIUS & TACACS+", path: "2-7-radius-tacacs.html" },
      { title: "Certificates & PKI", path: "2-8-certificates-pki.html" },
      { title: "SSO Mechanisms", path: "2-9-sso-mechanisms.html" },
      { title: "Auth Attacks & Defense", path: "2-10-auth-attacks-defense.html" }
    ]
  },
  {
    section: "3. Federation & SSO",
    items: [
      { title: "Federation Fundamentals", path: "3-1-federation-fundamentals.html" },
      { title: "SAML Federation", path: "3-2-saml-federation.html" },
      { title: "OIDC Federation", path: "3-3-oidc-federation.html" },
      { title: "WS-Federation & Legacy", path: "3-4-ws-federation-legacy.html" },
      { title: "B2B & B2C Federation", path: "3-5-b2b-b2c-federation.html" },
      { title: "Federation Troubleshooting", path: "3-6-federation-troubleshooting.html" }
    ]
  },
  {
    section: "4. Microsoft Entra ID",
    items: [
      { title: "Entra ID Overview", path: "4-1-entra-overview.html" },
      { title: "Entra ID Objects", path: "4-2-entra-objects.html" },
      { title: "Conditional Access", path: "4-3-conditional-access.html" },
      { title: "Entra PIM", path: "4-4-entra-pim.html" },
      { title: "Entra Governance", path: "4-5-entra-governance.html" },
      { title: "Entra Protection", path: "4-6-entra-protection.html" },
      { title: "Hybrid Identity", path: "4-7-hybrid-identity.html" },
      { title: "Workload Identity", path: "4-8-entra-workload-id.html" }
    ]
  },
  {
    section: "5. Okta",
    items: [
      { title: "Okta Overview", path: "5-1-okta-overview.html" },
      { title: "Okta Authentication", path: "5-2-okta-authentication.html" },
      { title: "Okta Authorization", path: "5-3-okta-authorization.html" },
      { title: "Okta Lifecycle", path: "5-4-okta-lifecycle.html" },
      { title: "Okta Integration", path: "5-5-okta-integration.html" },
      { title: "Okta Administration", path: "5-6-okta-admin.html" }
    ]
  },
  {
    section: "6. SailPoint & IGA",
    items: [
      { title: "SailPoint Overview", path: "6-1-sailpoint-overview.html" },
      { title: "IGA Fundamentals", path: "6-2-iga-fundamentals.html" },
      { title: "Access Certifications", path: "6-3-access-certifications.html" },
      { title: "Role Management", path: "6-4-role-management.html" },
      { title: "SoD Management", path: "6-5-sod-management.html" },
      { title: "Provisioning Workflows", path: "6-6-provisioning-workflows.html" }
    ]
  },
  {
    section: "7. Privileged Access (PAM)",
    items: [
      { title: "PAM Overview", path: "7-1-pam-overview.html" },
      { title: "Password Vaulting", path: "7-2-password-vaulting.html" },
      { title: "Session Management", path: "7-3-session-management.html" },
      { title: "Just-in-Time Access", path: "7-4-jit-access.html" },
      { title: "Secrets Management", path: "7-5-secrets-management.html" },
      { title: "PAM Vendors", path: "7-6-pam-vendors.html" }
    ]
  },
  {
    section: "8. Cloud IAM",
    items: [
      { title: "AWS IAM", path: "8-1-aws-iam.html" },
      { title: "AWS Identity Center", path: "8-2-aws-identity-center.html" },
      { title: "Azure RBAC", path: "8-3-azure-rbac.html" },
      { title: "GCP IAM", path: "8-4-gcp-iam.html" },
      { title: "Multi-Cloud Identity", path: "8-5-multi-cloud-identity.html" },
      { title: "Kubernetes IAM", path: "8-6-kubernetes-iam.html" },
      { title: "Infrastructure as Code", path: "8-7-infrastructure-as-code.html" },
      { title: "Cloud PAM", path: "8-8-cloud-pam.html" }
    ]
  },
  {
    section: "9. IAM Architecture",
    items: [
      { title: "Enterprise IAM Architecture", path: "9-1-enterprise-iam-arch.html" },
      { title: "Zero Trust IAM", path: "9-2-zero-trust-iam.html" },
      { title: "Hybrid Cloud IAM", path: "9-3-hybrid-cloud-iam.html" },
      { title: "CIAM Architecture", path: "9-4-ciam-architecture.html" },
      { title: "API Security", path: "9-5-api-security.html" },
      { title: "High Availability", path: "9-6-high-availability.html" }
    ]
  },
  {
    section: "10. IAM Migrations",
    items: [
      { title: "Migration Planning", path: "10-1-migration-planning.html" },
      { title: "IdP Migrations", path: "10-2-idp-migrations.html" },
      { title: "Legacy Modernization", path: "10-3-legacy-modernization.html" },
      { title: "IGA & PAM Migrations", path: "10-4-iga-pam-migrations.html" },
      { title: "Application Migration", path: "10-5-app-migration.html" },
      { title: "Coexistence & Cutover", path: "10-6-coexistence-cutover.html" }
    ]
  },
  {
    section: "11. Security & Attacks",
    items: [
      { title: "Identity Threat Landscape", path: "11-1-identity-threat-landscape.html" },
      { title: "Credential Attacks", path: "11-2-credential-attacks.html" },
      { title: "Token & Session Attacks", path: "11-3-token-session-attacks.html" },
      { title: "Privilege Escalation", path: "11-4-privilege-escalation.html" },
      { title: "Detection & Response", path: "11-5-detection-response.html" }
    ]
  },
  {
    section: "12. Reference & Interview",
    items: [
      { title: "IAM Glossary", path: "12-1-iam-glossary.html" },
      { title: "Interview Questions", path: "12-2-interview-questions.html" },
      { title: "Scenario Questions", path: "12-3-scenario-questions.html" },
      { title: "Protocol Flows", path: "12-4-protocol-flows.html" },
      { title: "Comparison Tables", path: "12-5-comparison-tables.html" },
      { title: "CLI & API Reference", path: "12-6-cli-api-reference.html" }
    ]
  }
];

document.addEventListener('DOMContentLoaded', function() {
  generateSidebar();
  initSidebar();
  initAccordions();
  initCodeCopy();
  initSearch();
  initMobileMenu();
  initTableOfContents();
});

/* Generate Sidebar Navigation Dynamically */
function generateSidebar() {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;
  
  // Check if navigation already exists (some pages have it built-in)
  const existingNav = sidebar.querySelector('.sidebar-nav');
  if (existingNav && existingNav.querySelector('.nav-section')) {
    // Navigation already exists, just highlight current page
    highlightCurrentPage();
    return;
  }
  
  // Get current page
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  
  // Create navigation container
  const navContainer = document.createElement('div');
  navContainer.className = 'sidebar-nav';
  
  // Generate sections
  navigationData.forEach((section, sectionIndex) => {
    const sectionDiv = document.createElement('div');
    sectionDiv.className = 'nav-section';
    
    // Check if current page is in this section
    const isCurrentSection = section.items.some(item => item.path === currentPath);
    
    // Section header
    const header = document.createElement('div');
    header.className = 'nav-section-header' + (isCurrentSection ? '' : ' collapsed');
    header.innerHTML = `<span>${section.section}</span><span class="nav-section-icon">▼</span>`;
    
    // Section items container
    const itemsDiv = document.createElement('div');
    itemsDiv.className = 'nav-section-items';
    
    // Generate items
    section.items.forEach(item => {
      const link = document.createElement('a');
      link.href = item.path;
      link.className = 'nav-item' + (item.path === currentPath ? ' active' : '');
      link.textContent = item.title;
      itemsDiv.appendChild(link);
    });
    
    sectionDiv.appendChild(header);
    sectionDiv.appendChild(itemsDiv);
    navContainer.appendChild(sectionDiv);
  });
  
  // Add search trigger before navigation
  const searchTrigger = document.createElement('div');
  searchTrigger.className = 'sidebar-search';
  searchTrigger.innerHTML = `
    <button class="search-trigger">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <span>Search</span>
      <kbd>⌘K</kbd>
    </button>
  `;
  
  sidebar.appendChild(searchTrigger);
  sidebar.appendChild(navContainer);
  
  // Add search modal to body if not exists
  if (!document.querySelector('.search-modal')) {
    const searchModal = document.createElement('div');
    searchModal.className = 'search-modal';
    searchModal.innerHTML = `
      <div class="search-container">
        <div class="search-input-wrapper">
          <svg class="search-input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" class="search-input" placeholder="Search documentation...">
          <kbd class="search-close">ESC</kbd>
        </div>
        <div class="search-results"></div>
      </div>
    `;
    document.body.appendChild(searchModal);
  }
}

/* Sidebar Navigation Collapse/Expand */
function initSidebar() {
  document.addEventListener('click', function(e) {
    if (e.target.closest('.nav-section-header')) {
      const header = e.target.closest('.nav-section-header');
      header.classList.toggle('collapsed');
    }
  });
}

/* Accordions */
function initAccordions() {
  document.addEventListener('click', function(e) {
    if (e.target.closest('.accordion-header')) {
      const header = e.target.closest('.accordion-header');
      const item = header.parentElement;
      item.classList.toggle('open');
    }
  });
}

/* Code Copy */
function initCodeCopy() {
  // Add copy buttons to code blocks that don't have them
  document.querySelectorAll('.code-block').forEach(block => {
    if (!block.querySelector('.code-copy-btn')) {
      const header = block.querySelector('.code-header');
      if (header) {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'code-copy-btn';
        copyBtn.innerHTML = '<span>📋</span> Copy';
        header.appendChild(copyBtn);
      }
    }
  });
  
  document.addEventListener('click', async function(e) {
    if (e.target.closest('.code-copy-btn')) {
      const btn = e.target.closest('.code-copy-btn');
      const codeBlock = btn.closest('.code-block');
      const code = codeBlock.querySelector('code').textContent;
      
      try {
        await navigator.clipboard.writeText(code);
        btn.classList.add('copied');
        btn.innerHTML = '<span>✓</span> Copied!';
        
        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = '<span>📋</span> Copy';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
      }
    }
  });
}

/* Search */
function initSearch() {
  // Build search index from navigation data
  const searchData = [];
  navigationData.forEach(section => {
    section.items.forEach(item => {
      searchData.push({
        title: item.title,
        path: item.path,
        section: section.section
      });
    });
  });
  
  // Add index page
  searchData.unshift({ title: 'Home', path: 'index.html', section: 'Main' });
  
  document.addEventListener('click', function(e) {
    const searchTrigger = e.target.closest('.search-trigger');
    const searchModal = document.querySelector('.search-modal');
    
    if (searchTrigger && searchModal) {
      searchModal.classList.add('active');
      const searchInput = searchModal.querySelector('.search-input');
      if (searchInput) searchInput.focus();
    }
    
    // Close when clicking outside
    if (searchModal && searchModal.classList.contains('active')) {
      if (!e.target.closest('.search-container') && !e.target.closest('.search-trigger')) {
        searchModal.classList.remove('active');
      }
    }
  });
  
  // Handle search input
  document.addEventListener('input', function(e) {
    if (e.target.classList.contains('search-input')) {
      const query = e.target.value.toLowerCase().trim();
      const searchResults = document.querySelector('.search-results');
      
      if (!searchResults) return;
      
      if (query.length < 2) {
        searchResults.innerHTML = '<div class="search-no-results">Type at least 2 characters...</div>';
        return;
      }
      
      const results = searchData.filter(item =>
        item.title.toLowerCase().includes(query) ||
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
    }
  });
  
  // Keyboard shortcuts
  document.addEventListener('keydown', function(e) {
    const searchModal = document.querySelector('.search-modal');
    
    // Cmd/Ctrl + K to open
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (searchModal) {
        searchModal.classList.add('active');
        const searchInput = searchModal.querySelector('.search-input');
        if (searchInput) searchInput.focus();
      }
    }
    
    // ESC to close
    if (e.key === 'Escape' && searchModal) {
      searchModal.classList.remove('active');
    }
  });
}

/* Mobile Menu */
function initMobileMenu() {
  const toggle = document.querySelector('.mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  
  if (toggle && sidebar) {
    toggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      toggle.classList.toggle('active');
    });
  }
  
  // Close on nav item click (mobile)
  document.addEventListener('click', function(e) {
    if (e.target.classList.contains('nav-item')) {
      const sidebar = document.querySelector('.sidebar');
      const toggle = document.querySelector('.mobile-menu-toggle');
      if (window.innerWidth <= 768 && sidebar) {
        sidebar.classList.remove('open');
        if (toggle) toggle.classList.remove('active');
      }
    }
  });
}

/* Table of Contents */
function initTableOfContents() {
  const toc = document.querySelector('.toc-list');
  const contentMain = document.querySelector('.content-main');
  
  if (!toc || !contentMain) return;
  
  const headings = contentMain.querySelectorAll('h2[id], h3[id]');
  
  if (headings.length === 0) return;
  
  headings.forEach((heading) => {
    const li = document.createElement('li');
    li.className = 'toc-item';
    
    const a = document.createElement('a');
    a.href = `#${heading.id}`;
    a.className = `toc-link depth-${heading.tagName.toLowerCase().charAt(1)}`;
    a.textContent = heading.textContent;
    
    a.addEventListener('click', (e) => {
      e.preventDefault();
      heading.scrollIntoView({ behavior: 'smooth' });
    });
    
    li.appendChild(a);
    toc.appendChild(li);
  });
  
  // Scroll spy
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        toc.querySelectorAll('.toc-link').forEach(link => link.classList.remove('active'));
        const activeLink = toc.querySelector(`a[href="#${entry.target.id}"]`);
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }, { rootMargin: '-80px 0px -80% 0px' });
  
  headings.forEach(heading => observer.observe(heading));
}

/* Highlight current page in existing navigation */
function highlightCurrentPage() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  
  // Remove existing active states
  document.querySelectorAll('.nav-item.active').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-section-header.active').forEach(el => el.classList.remove('active'));
  
  // Find and activate current page link
  const currentLink = document.querySelector(`.nav-item[href="${currentPath}"]`);
  if (currentLink) {
    currentLink.classList.add('active');
    
    // Expand parent section
    const section = currentLink.closest('.nav-section');
    if (section) {
      const header = section.querySelector('.nav-section-header');
      if (header) {
        header.classList.remove('collapsed');
        header.classList.add('active');
      }
    }
  }
  
  // Collapse other sections
  document.querySelectorAll('.nav-section').forEach(section => {
    const hasActive = section.querySelector('.nav-item.active');
    const header = section.querySelector('.nav-section-header');
    if (!hasActive && header && !header.classList.contains('collapsed')) {
      header.classList.add('collapsed');
    }
  });
}
