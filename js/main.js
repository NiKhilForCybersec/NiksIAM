/* =========================================
   IAM Ultimate Guide - Main JavaScript
   ========================================= */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive components
    initMobileMenu();
    initCodeCopyButtons();
    initAccordions();
    initTabs();
    initSidebarActiveState();
    initSmoothScroll();
    initAnimations();
});

/* Mobile Menu Toggle */
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuBtn && sidebar) {
        menuBtn.addEventListener('click', function() {
            sidebar.classList.toggle('open');
            this.innerHTML = sidebar.classList.contains('open') ? '✕' : '☰';
        });
        
        // Close sidebar when clicking outside
        document.addEventListener('click', function(e) {
            if (!sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
                sidebar.classList.remove('open');
                menuBtn.innerHTML = '☰';
            }
        });
    }
}

/* Code Copy Buttons */
function initCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('.code-block');
    
    codeBlocks.forEach(block => {
        const copyBtn = block.querySelector('.code-copy-btn');
        const code = block.querySelector('code');
        
        if (copyBtn && code) {
            copyBtn.addEventListener('click', async function() {
                try {
                    await navigator.clipboard.writeText(code.textContent);
                    
                    // Visual feedback
                    const originalText = this.innerHTML;
                    this.innerHTML = '✓ Copied!';
                    this.classList.add('copied');
                    
                    setTimeout(() => {
                        this.innerHTML = originalText;
                        this.classList.remove('copied');
                    }, 2000);
                } catch (err) {
                    console.error('Failed to copy:', err);
                    this.innerHTML = '✗ Failed';
                    setTimeout(() => {
                        this.innerHTML = '⧉ Copy';
                    }, 2000);
                }
            });
        }
    });
}

/* Accordion Functionality */
function initAccordions() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const item = this.parentElement;
            const content = item.querySelector('.accordion-content');
            const icon = this.querySelector('.accordion-icon');
            
            // Check if we should allow multiple open
            const accordion = item.parentElement;
            const allowMultiple = accordion.hasAttribute('data-allow-multiple');
            
            if (!allowMultiple) {
                // Close other items
                accordion.querySelectorAll('.accordion-item.active').forEach(activeItem => {
                    if (activeItem !== item) {
                        activeItem.classList.remove('active');
                    }
                });
            }
            
            // Toggle current item
            item.classList.toggle('active');
        });
    });
}

/* Tabs Functionality */
function initTabs() {
    const tabContainers = document.querySelectorAll('.tabs');
    
    tabContainers.forEach(container => {
        const headers = container.querySelectorAll('.tab-header');
        const contents = container.querySelectorAll('.tab-content');
        
        headers.forEach((header, index) => {
            header.addEventListener('click', function() {
                // Remove active state from all
                headers.forEach(h => h.classList.remove('active'));
                contents.forEach(c => c.classList.remove('active'));
                
                // Add active state to clicked tab
                this.classList.add('active');
                if (contents[index]) {
                    contents[index].classList.add('active');
                }
            });
        });
    });
}

/* Sidebar Active State */
function initSidebarActiveState() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const sidebarLinks = document.querySelectorAll('.sidebar-nav a');
    
    sidebarLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage) {
            link.classList.add('active');
            
            // Expand parent section if collapsed
            const section = link.closest('.sidebar-section');
            if (section) {
                section.classList.add('expanded');
            }
        }
    });
}

/* Smooth Scroll for Anchor Links */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update URL without jumping
                history.pushState(null, null, targetId);
            }
        });
    });
}

/* Scroll-triggered Animations */
function initAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        animatedElements.forEach(el => observer.observe(el));
    } else {
        // Fallback for older browsers
        animatedElements.forEach(el => el.classList.add('animate-fade-in'));
    }
}

/* Table of Contents Generator */
function generateTOC(containerSelector) {
    const container = document.querySelector(containerSelector);
    const content = document.querySelector('.main-content');
    
    if (!container || !content) return;
    
    const headings = content.querySelectorAll('h2, h3');
    const tocList = document.createElement('ul');
    tocList.className = 'toc-list';
    
    headings.forEach((heading, index) => {
        // Create ID if not exists
        if (!heading.id) {
            heading.id = `section-${index}`;
        }
        
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${heading.id}`;
        a.textContent = heading.textContent.replace(/^\/\/\s*/, '');
        
        if (heading.tagName === 'H3') {
            a.classList.add('toc-level-2');
        }
        
        li.appendChild(a);
        tocList.appendChild(li);
    });
    
    container.appendChild(tocList);
}

/* Search Functionality */
function initSearch() {
    const searchInput = document.querySelector('.search-input');
    const searchResults = document.querySelector('.search-results');
    
    if (!searchInput) return;
    
    // This would typically connect to a search index
    searchInput.addEventListener('input', debounce(function(e) {
        const query = e.target.value.toLowerCase().trim();
        
        if (query.length < 2) {
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
            return;
        }
        
        // Placeholder - in production, this would search actual content
        searchResults.innerHTML = '<div class="search-result-item">Search functionality requires backend implementation</div>';
        searchResults.style.display = 'block';
    }, 300));
}

/* Utility: Debounce */
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

/* Print Page */
function printPage() {
    window.print();
}

/* Toggle Dark/Light Mode (placeholder for future enhancement) */
function toggleTheme() {
    document.body.classList.toggle('light-mode');
    localStorage.setItem('theme', document.body.classList.contains('light-mode') ? 'light' : 'dark');
}

/* Load Theme Preference */
function loadThemePreference() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
    }
}

/* Highlight Active TOC Item on Scroll */
function initScrollSpy() {
    const sections = document.querySelectorAll('h2[id], h3[id]');
    const tocLinks = document.querySelectorAll('.toc-list a');
    
    if (!sections.length || !tocLinks.length) return;
    
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -80% 0px',
        threshold: 0
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocLinks.forEach(link => link.classList.remove('active'));
                const activeLink = document.querySelector(`.toc-list a[href="#${entry.target.id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }, observerOptions);
    
    sections.forEach(section => observer.observe(section));
}

/* Export functions for external use */
window.IAMGuide = {
    generateTOC,
    initSearch,
    printPage,
    toggleTheme
};
