// IAM Ultimate Guide - Main JavaScript
// =====================================

document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile menu toggle - toggles sidebar on mobile
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const sidebar = document.querySelector('.sidebar');
    
    // Create overlay for mobile sidebar
    let overlay = document.querySelector('.sidebar-overlay');
    if (!overlay && sidebar) {
        overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);
    }
    
    function closeSidebar() {
        if (sidebar) sidebar.classList.remove('open');
        if (overlay) overlay.classList.remove('active');
        if (mobileMenuBtn) mobileMenuBtn.textContent = '☰';
    }
    
    function openSidebar() {
        if (sidebar) sidebar.classList.add('open');
        if (overlay) overlay.classList.add('active');
        if (mobileMenuBtn) mobileMenuBtn.textContent = '✕';
    }
    
    if (mobileMenuBtn && sidebar) {
        mobileMenuBtn.addEventListener('click', () => {
            if (sidebar.classList.contains('open')) {
                closeSidebar();
            } else {
                openSidebar();
            }
        });
        
        // Close sidebar when clicking overlay
        if (overlay) {
            overlay.addEventListener('click', closeSidebar);
        }
        
        // Close sidebar when clicking a nav link on mobile
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    closeSidebar();
                }
            });
        });
        
        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && sidebar.classList.contains('open')) {
                closeSidebar();
            }
        });
        
        // Close sidebar on window resize if switching to desktop
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) {
                closeSidebar();
            }
        });
    }

    // Architecture tab switching (for enterprise-architecture.html)
    document.querySelectorAll('.arch-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.arch-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.arch-content').forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            const targetId = tab.dataset.tab;
            const targetContent = document.getElementById(targetId);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });

    // Use case tab switching - scoped to parent container
    document.querySelectorAll('.usecase-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            // Get the parent tabs container to scope the switching
            const tabsContainer = tab.parentElement;
            
            // Find siblings within the same tab group
            tabsContainer.querySelectorAll('.usecase-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            // Find the content sections that follow this tab group
            let sibling = tabsContainer.nextElementSibling;
            while (sibling && sibling.classList.contains('usecase-content')) {
                sibling.classList.remove('active');
                if (sibling.id === tab.dataset.usecase) {
                    sibling.classList.add('active');
                }
                sibling = sibling.nextElementSibling;
            }
        });
    });

    // Component click handler for architecture diagram
    document.querySelectorAll('.arch-component.clickable').forEach(comp => {
        comp.addEventListener('click', (e) => {
            e.stopPropagation();
            const componentId = comp.dataset.component;
            if (typeof showComponentDetails === 'function') {
                showComponentDetails(componentId);
            }
        });
    });

    // Modal close on background click
    const modal = document.getElementById('componentModal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target.id === 'componentModal') {
                if (typeof closeModal === 'function') {
                    closeModal();
                } else {
                    modal.classList.remove('active');
                }
            }
        });
    }

    // Modal close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const modal = document.getElementById('componentModal');
            if (modal && modal.classList.contains('active')) {
                if (typeof closeModal === 'function') {
                    closeModal();
                } else {
                    modal.classList.remove('active');
                }
            }
        }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#') {
                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Code block copy functionality
    document.querySelectorAll('pre code').forEach(codeBlock => {
        const wrapper = codeBlock.parentElement;
        if (!wrapper.querySelector('.copy-btn')) {
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.textContent = 'Copy';
            copyBtn.style.cssText = 'position: absolute; top: 0.5rem; right: 0.5rem; padding: 0.25rem 0.5rem; font-size: 0.7rem; background: var(--accent); color: #000; border: none; border-radius: 4px; cursor: pointer;';
            
            wrapper.style.position = 'relative';
            wrapper.appendChild(copyBtn);
            
            copyBtn.addEventListener('click', () => {
                navigator.clipboard.writeText(codeBlock.textContent).then(() => {
                    copyBtn.textContent = 'Copied!';
                    setTimeout(() => {
                        copyBtn.textContent = 'Copy';
                    }, 2000);
                });
            });
        }
    });

    console.log('IAM Ultimate Guide - JavaScript loaded successfully');
});

// Global functions for modal (can be called from inline onclick handlers)
function closeModal() {
    const modal = document.getElementById('componentModal');
    if (modal) {
        modal.classList.remove('active');
    }
}