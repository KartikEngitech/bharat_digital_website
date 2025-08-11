 // Mobile menu toggle
const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
const navLinks = document.querySelector(".nav-links");

mobileMenuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  mobileMenuBtn.innerHTML = navLinks.classList.contains("active")
    ? '<i class="fas fa-times"></i>'
    : '<i class="fas fa-bars"></i>';
});

// Close mobile menu when clicking on a link
document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    if (navLinks.classList.contains("active")) {
      navLinks.classList.remove("active");
      mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    }
  });
});

// Navbar scroll effect
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 20) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Highlight active link based on current page
document.addEventListener("DOMContentLoaded", function () {
  const currentLocation = location.href;
  const navLinks = document.querySelectorAll(".nav-links a");

  navLinks.forEach((link) => {
    if (link.href === currentLocation) {
      link.classList.add("active");
    }
  });
});

// Create particles
function createParticles() {
  const particlesContainer = document.getElementById("particles");
  const particleCount = 50; // Increased number of particles for better visibility

  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement("div");
    particle.classList.add("particle");

    // Random size between 1px and 3px
    const size = Math.random() * 2 + 1;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;

    // Random position
    particle.style.left = `${Math.random() * 100}vw`;
    particle.style.top = `${Math.random() * 100}vh`;

    // Random animation duration between 20s and 40s
    const duration = Math.random() * 20 + 20;
    particle.style.animationDuration = `${duration}s`;

    // Random delay
    particle.style.animationDelay = `${Math.random() * 5}s`;

    // Random opacity between 0.3 and 0.8
    const opacity = Math.random() * 0.5 + 0.3;
    particle.style.opacity = opacity;

    particlesContainer.appendChild(particle);
  }
}

// Initialize particles when page loads
window.addEventListener("load", createParticles);

// Modal functionality
const modalOverlay = document.getElementById('policyModal');
const modalTitle = document.getElementById('modalTitle');
const modalContent = document.getElementById('modalContent');
const closeModalBtn = document.querySelector('.modal-close-btn');

// Policy content
const policies = {
  privacy: {
    title: "Privacy Policy",
    content: `
      <h3>1. What We Collect</h3>
      <p>
        • Personal data (name, email, phone, company). </br>
        • Technical data (IP address, browser, device). </br>
        • Usage data (pages visited, time spent). </br>
      </p>
      
      <h3>2. How We Use It</h3>
      <p>  
        • To respond to inquiries and provide support. </br>
        • For billing, analytics, and marketing (with consent). </br>
        • To ensure security and comply with laws. </br>
      </p>
      
      <h3>3. Sharing & Security</h3>
      <p>  
        • We do not sell your data. </br>
        • We may share it with trusted service providers (e.g., payment processors, hosting). </br>
        • We use encryption, secure servers, and access control to protect your data. </br>

      </p>

      <h3>4. Your Rights </h3>
      <p>  
         Depending on your location, you may have the right to Opt out of marketing : </br>
         • Access, correct, or delete your data. </br>
         • Request data portability. 
      </p> 

      <h3>5. Cookies </h3>
      <p>  
        • We use cookies for basic functionality, analytics, and performance. </br>
        • You can manage them via browser settings. </br>
      </p> 

    `
  },
  terms: {
    title: "Terms of Service",
    content: `
      <h3>1. Services </h3>
      <p>We offer IT solutions and website design. Details of each project will be agreed upon separately. </p>
      
      <h3>2. Payments </h3>
      <p>Projects start after an agreed deposit. Payments are non-refundable once work begins unless otherwise stated.</p>
      
      <h3>3. Intellectual Property </h3>
      <p>All content and code we provide is either our property or licensed to you under specific terms. You may not reuse it without permission. </p>
      
      <h3>4. Client Responsibilities </h3>
      <p>You agree to provide timely feedback, assets, and approvals during project work.</p>

      <h3>5. Limitation of Liability</h3>
      <p>
        We are not liable for indirect losses or damages arising from delays, downtime, or third-party issues.</br>
        We reserve the right to stop services for any misuse or violation of our terms. 
      </p>

      <h3>6. Governing Law</h3>
      <p>These terms are governed by the laws of [India/Maharashtra].</p>
    `
  },
  cookie: {
    title: "Cookie Policy",
    content: `
      <h3>What Are Cookies</h3>
      <p>Cookies are small text files stored on your device when you visit our website.</p>
      
      <h3>How We Use Cookies</h3>
      <p>
        We use cookies to: </br>
          • Remember your preferences </br>
          • Analyze website traffic </br>
          • Improve user experience  
      </p>
      
      <h3>Managing Cookies</h3>
      <p>You can control or delete cookies through your browser settings. </br>
       However, this may affect website functionality.
       </p>
    `
  }
};

// Set up event listeners for policy links
document.querySelectorAll('.legal-links a').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    let policyType;
    
    if (link.textContent.toLowerCase().includes('privacy')) {
      policyType = 'privacy';
    } else if (link.textContent.toLowerCase().includes('terms')) {
      policyType = 'terms';
    } else if (link.textContent.toLowerCase().includes('cookie')) {
      policyType = 'cookie';
    } else {
      return; // Skip if it's not a policy link
    }
    
    modalTitle.textContent = policies[policyType].title;
    modalContent.innerHTML = policies[policyType].content;
    
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  });
});

// Close modal
closeModalBtn.addEventListener('click', () => {
  modalOverlay.classList.remove('active');
  document.body.style.overflow = 'auto';
});

// Close modal when clicking outside content
modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
});

// Close modal with Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
});