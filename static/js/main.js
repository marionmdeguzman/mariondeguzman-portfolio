// ─── THEME TOGGLE ─────────────────────────────────────────────────────────────
function toggleTheme() {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  const next = isLight ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next === 'dark' ? '' : 'light');
  localStorage.setItem('theme', next);
  syncThemeIcon();
}

function syncThemeIcon() {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  const moon = document.querySelector('.icon-moon');
  const sun  = document.querySelector('.icon-sun');
  if (!moon || !sun) return;
  moon.style.display = isLight ? 'none'  : 'block';
  sun.style.display  = isLight ? 'block' : 'none';
}

// Sync icon on load
document.addEventListener('DOMContentLoaded', syncThemeIcon);

// ─── NAV ACTIVE STATE (same-page anchor spy) ─────────────────────────────────
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');

function updateActive() {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 120) current = s.id;
  });
  navLinks.forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#' + current);
  });
}

if (navLinks.length > 0) {
  window.addEventListener('scroll', updateActive, { passive: true });
}

// ─── HAMBURGER ────────────────────────────────────────────────────────────────
function toggleNav() {
  document.getElementById('navLinks').classList.toggle('open');
}

// Close on link click (mobile)
document.querySelectorAll('.nav-links a').forEach(a => {
  a.addEventListener('click', () => {
    document.getElementById('navLinks').classList.remove('open');
  });
});

// ─── SCROLL REVEAL ────────────────────────────────────────────────────────────
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
