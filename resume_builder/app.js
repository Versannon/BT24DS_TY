/**
 * DS Resume Studio - Dual Template Application Logic
 * Option 1: Classic Formal ATS
 * Option 2: Modern Graphic Arch (Screenshot Replicated Design)
 */

const sampleDSData = {
  personal: {
    fullName: "Alex Sharma",
    title: "3rd Year B.Tech Data Science Student",
    email: "alex.sharma.ds@gmail.com",
    phone: "+91 98765 43210",
    location: "Bengaluru, India",
    linkedin: "linkedin.com/in/alex-sharma-ds",
    github: "github.com/alex-sharma-ds",
    website: "alexsharma.dev",
    summary: "Motivated 3rd Year B.Tech Data Science student with a solid foundation in Machine Learning, Statistical Analysis, and Exploratory Data Analysis. Proficient in Python, SQL, and Scikit-Learn with hands-on experience building end-to-end predictive models and interactive data dashboards.",
    avatarUrl: ""
  },
  education: [
    {
      id: "edu_1",
      degree: "B.Tech in CSE (Data Science)",
      institution: "National Institute of Technology",
      dates: "2022 - 2026",
      score: "CGPA: 8.6 / 10.0"
    }
  ],
  skillBars: [
    { id: "sk_1", name: "Python & Pandas", percent: 90 },
    { id: "sk_2", name: "SQL (MySQL/PostgreSQL)", percent: 85 },
    { id: "sk_3", name: "Scikit-Learn & ML", percent: 80 },
    { id: "sk_4", name: "PowerBI & Tableau", percent: 75 },
    { id: "sk_5", name: "Git & GitHub", percent: 85 },
    { id: "sk_6", name: "Applied Statistics", percent: 70 }
  ],
  languages: "Python, SQL, R, C++, English, Hindi",
  hobbies: "Kaggle Competitions, LeetCode, Chess, Traveling",
  projects: [
    {
      id: "proj_1",
      title: "Telecom Customer Churn Classifier",
      tech: "Python / Scikit-Learn / Streamlit",
      dates: "2024 - Present",
      bullets: [
        "Analyzed 7,000+ customer records to identify churn drivers with Pandas, uncovering a 35% churn correlation with contract tenure.",
        "Trained XGBoost classifier with 89% AUC-ROC accuracy and deployed live Streamlit web app for real-time risk scoring."
      ]
    },
    {
      id: "proj_2",
      title: "Review Sentiment Classifier (NLP)",
      tech: "Python / NLTK / Flask",
      dates: "2023 - 2024",
      bullets: [
        "Preprocessed 15,000+ review texts using tokenization, lemmatization, and TF-IDF vectorization.",
        "Engineered sentiment classification pipeline yielding 91% accuracy and deployed REST API using Flask."
      ]
    }
  ],
  extras: [
    { id: "ext_1", text: "Global Rank Top 15% in Kaggle ML Competition ('House Prices')." },
    { id: "ext_2", text: "NPTEL Certified in 'Python for Data Science' (Silver Medal)." },
    { id: "ext_3", text: "Solved 150+ Data Structures & Algorithms problems on LeetCode." }
  ]
};

// Global App State
let state = JSON.parse(localStorage.getItem('ds_dual_resume_state')) || JSON.parse(JSON.stringify(sampleDSData));
let currentTemplate = localStorage.getItem('ds_resume_template') || 'tpl-formal';

function saveState() {
  localStorage.setItem('ds_dual_resume_state', JSON.stringify(state));
  localStorage.setItem('ds_resume_template', currentTemplate);
  renderSheet();
}

// Template Switching Handler
document.querySelectorAll('.tpl-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    document.querySelectorAll('.tpl-btn').forEach(b => b.classList.remove('active'));
    const target = e.currentTarget;
    target.classList.add('active');
    currentTemplate = target.getAttribute('data-template');
    saveState();
  });
});

// Tab Switching
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

    const b = e.currentTarget;
    b.classList.add('active');
    document.getElementById(b.getAttribute('data-tab')).classList.add('active');
  });
});

// Avatar Image Handling
document.getElementById('input-avatar-file').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (event) => {
      state.personal.avatarUrl = event.target.result;
      updateAvatarPreview();
      saveState();
    };
    reader.readAsDataURL(file);
  }
});

document.getElementById('btn-remove-photo').addEventListener('click', () => {
  state.personal.avatarUrl = '';
  document.getElementById('input-avatar-file').value = '';
  updateAvatarPreview();
  saveState();
});

function updateAvatarPreview() {
  const img = document.getElementById('avatar-img');
  const monogram = document.getElementById('avatar-monogram');
  const p = state.personal;

  if (p.avatarUrl) {
    img.src = p.avatarUrl;
    img.style.display = 'block';
    monogram.style.display = 'none';
  } else {
    img.style.display = 'none';
    monogram.style.display = 'inline';
    const initials = (p.fullName || 'Alex Sharma').split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
    monogram.innerText = initials || 'AS';
  }
}

// Static Form Inputs
function initStaticInputs() {
  const pMap = {
    'input-fullname': 'fullName', 'input-title': 'title', 'input-email': 'email',
    'input-phone': 'phone', 'input-location': 'location', 'input-linkedin': 'linkedin',
    'input-github': 'github', 'input-website': 'website', 'input-summary': 'summary'
  };

  Object.entries(pMap).forEach(([id, key]) => {
    const el = document.getElementById(id);
    if (el) {
      el.value = state.personal[key] || '';
      el.addEventListener('input', (e) => {
        state.personal[key] = e.target.value;
        if (key === 'fullName') updateAvatarPreview();
        saveState();
      });
    }
  });

  const langInput = document.getElementById('input-spoken-languages');
  if (langInput) {
    langInput.value = state.languages || '';
    langInput.addEventListener('input', (e) => { state.languages = e.target.value; saveState(); });
  }

  const hobInput = document.getElementById('input-hobbies');
  if (hobInput) {
    hobInput.value = state.hobbies || '';
    hobInput.addEventListener('input', (e) => { state.hobbies = e.target.value; saveState(); });
  }

  document.querySelectorAll('.tpl-btn').forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-template') === currentTemplate);
  });

  updateAvatarPreview();
}

// Dynamic List Editors
function renderSkillBarsEditor() {
  const container = document.getElementById('skill-bars-list');
  container.innerHTML = '';
  state.skillBars.forEach((sk, idx) => {
    const card = document.createElement('div');
    card.className = 'dynamic-item-card';
    card.innerHTML = `
      <div class="card-header">
        <h3>Skill #${idx + 1}</h3>
        <button class="btn btn-danger btn-delete-sk">Delete</button>
      </div>
      <div class="form-grid">
        <div class="form-group"><label>Skill Name</label><input type="text" class="sk-name" value="${sk.name}"></div>
        <div class="form-group"><label>Proficiency (%)</label><input type="number" min="10" max="100" class="sk-percent" value="${sk.percent}"></div>
      </div>
    `;
    card.querySelector('.sk-name').addEventListener('input', (e) => { sk.name = e.target.value; saveState(); });
    card.querySelector('.sk-percent').addEventListener('input', (e) => { sk.percent = e.target.value; saveState(); });
    card.querySelector('.btn-delete-sk').addEventListener('click', () => {
      state.skillBars = state.skillBars.filter(item => item.id !== sk.id);
      renderSkillBarsEditor();
      saveState();
    });
    container.appendChild(card);
  });
}

document.getElementById('btn-add-skill-bar').addEventListener('click', () => {
  state.skillBars.push({ id: 'sk_' + Date.now(), name: '', percent: 80 });
  renderSkillBarsEditor();
  saveState();
});

function renderEducationEditor() {
  const container = document.getElementById('education-list');
  container.innerHTML = '';
  state.education.forEach((edu, idx) => {
    const card = document.createElement('div');
    card.className = 'dynamic-item-card';
    card.innerHTML = `
      <div class="card-header">
        <h3>Education #${idx + 1}</h3>
        <button class="btn btn-danger btn-delete-edu">Delete</button>
      </div>
      <div class="form-grid">
        <div class="form-group full-width"><label>Degree</label><input type="text" class="edu-degree" value="${edu.degree}"></div>
        <div class="form-group full-width"><label>University / School</label><input type="text" class="edu-institution" value="${edu.institution}"></div>
        <div class="form-group"><label>Dates</label><input type="text" class="edu-dates" value="${edu.dates}"></div>
        <div class="form-group"><label>CGPA / Score</label><input type="text" class="edu-score" value="${edu.score}"></div>
      </div>
    `;
    card.querySelector('.edu-degree').addEventListener('input', (e) => { edu.degree = e.target.value; saveState(); });
    card.querySelector('.edu-institution').addEventListener('input', (e) => { edu.institution = e.target.value; saveState(); });
    card.querySelector('.edu-dates').addEventListener('input', (e) => { edu.dates = e.target.value; saveState(); });
    card.querySelector('.edu-score').addEventListener('input', (e) => { edu.score = e.target.value; saveState(); });
    card.querySelector('.btn-delete-edu').addEventListener('click', () => {
      state.education = state.education.filter(item => item.id !== edu.id);
      renderEducationEditor();
      saveState();
    });
    container.appendChild(card);
  });
}

document.getElementById('btn-add-education').addEventListener('click', () => {
  state.education.push({ id: 'edu_' + Date.now(), degree: '', institution: '', dates: '', score: '' });
  renderEducationEditor();
  saveState();
});

function renderProjectsEditor() {
  const container = document.getElementById('projects-list');
  container.innerHTML = '';
  state.projects.forEach((proj, idx) => {
    const card = document.createElement('div');
    card.className = 'dynamic-item-card';
    card.innerHTML = `
      <div class="card-header">
        <h3>Project / Role #${idx + 1}</h3>
        <button class="btn btn-danger btn-delete-proj">Delete</button>
      </div>
      <div class="form-grid">
        <div class="form-group full-width"><label>Title</label><input type="text" class="proj-title" value="${proj.title}"></div>
        <div class="form-group"><label>Tech Stack / Subtitle</label><input type="text" class="proj-tech" value="${proj.tech}"></div>
        <div class="form-group"><label>Dates</label><input type="text" class="proj-dates" value="${proj.dates}"></div>
        <div class="form-group full-width"><label>Bullets (1 per line)</label><textarea class="proj-bullets" rows="3">${proj.bullets ? proj.bullets.join('\n') : ''}</textarea></div>
      </div>
    `;
    card.querySelector('.proj-title').addEventListener('input', (e) => { proj.title = e.target.value; saveState(); });
    card.querySelector('.proj-tech').addEventListener('input', (e) => { proj.tech = e.target.value; saveState(); });
    card.querySelector('.proj-dates').addEventListener('input', (e) => { proj.dates = e.target.value; saveState(); });
    card.querySelector('.proj-bullets').addEventListener('input', (e) => {
      proj.bullets = e.target.value.split('\n').filter(l => l.trim() !== '');
      saveState();
    });
    card.querySelector('.btn-delete-proj').addEventListener('click', () => {
      state.projects = state.projects.filter(item => item.id !== proj.id);
      renderProjectsEditor();
      saveState();
    });
    container.appendChild(card);
  });
}

document.getElementById('btn-add-project').addEventListener('click', () => {
  state.projects.push({ id: 'proj_' + Date.now(), title: '', tech: '', dates: '', bullets: [''] });
  renderProjectsEditor();
  saveState();
});

function renderExtrasEditor() {
  const container = document.getElementById('extras-list');
  container.innerHTML = '';
  state.extras.forEach((ext, idx) => {
    const card = document.createElement('div');
    card.className = 'dynamic-item-card';
    card.innerHTML = `
      <div class="card-header">
        <h3>Certification #${idx + 1}</h3>
        <button class="btn btn-danger btn-delete-ext">Delete</button>
      </div>
      <div class="form-group full-width"><input type="text" class="ext-text" value="${ext.text}"></div>
    `;
    card.querySelector('.ext-text').addEventListener('input', (e) => { ext.text = e.target.value; saveState(); });
    card.querySelector('.btn-delete-ext').addEventListener('click', () => {
      state.extras = state.extras.filter(item => item.id !== ext.id);
      renderExtrasEditor();
      saveState();
    });
    container.appendChild(card);
  });
}

document.getElementById('btn-add-extra').addEventListener('click', () => {
  state.extras.push({ id: 'ext_' + Date.now(), text: '' });
  renderExtrasEditor();
  saveState();
});

// MAIN RESUME RENDERER FOR BOTH TEMPLATES
function renderSheet() {
  const sheet = document.getElementById('resume-sheet');
  sheet.className = `resume-sheet ${currentTemplate}`;

  const p = state.personal;

  if (currentTemplate === 'tpl-formal') {
    // OPTION 1: CLASSIC FORMAL ATS
    const contactLine = [p.email, p.phone, p.location, p.linkedin, p.github, p.website].filter(Boolean).join(' • ');

    const eduHTML = state.education.map(e => e.degree ? `
      <div style="margin-bottom: 8px;">
        <div class="formal-row"><span class="formal-item-title">${e.degree}</span><span class="formal-item-date">${e.dates}</span></div>
        <div class="formal-row"><span class="formal-item-sub">${e.institution}</span><span class="formal-item-date">${e.score}</span></div>
      </div>
    ` : '').join('');

    const skillText = state.skillBars.map(s => s.name).join(', ') + (state.languages ? `, ${state.languages}` : '');

    const projectsHTML = state.projects.map(pr => pr.title ? `
      <div style="margin-bottom: 12px;">
        <div class="formal-row"><span class="formal-item-title">${pr.title}</span><span class="formal-item-date">${pr.dates}</span></div>
        ${pr.tech ? `<div style="font-size: 8.8pt; font-weight:600; color:#4b5563;">Tech: ${pr.tech}</div>` : ''}
        ${pr.bullets ? `<ul class="formal-bullets">${pr.bullets.map(b => `<li>${b}</li>`).join('')}</ul>` : ''}
      </div>
    ` : '').join('');

    const certsHTML = `<ul class="formal-bullets">${state.extras.map(e => e.text ? `<li>${e.text}</li>` : '').join('')}</ul>`;

    sheet.innerHTML = `
      <header class="formal-header">
        <h1 class="formal-name">${p.fullName || 'ALEX SHARMA'}</h1>
        <p class="formal-title">${p.title || '3rd Year B.Tech Data Science Student'}</p>
        <div class="formal-contact">${contactLine}</div>
      </header>

      ${p.summary ? `
        <h2 class="formal-sec-title">PROFESSIONAL SUMMARY</h2>
        <div class="formal-sec-line"></div>
        <p style="text-align:justify;">${p.summary}</p>
      ` : ''}

      <h2 class="formal-sec-title">EDUCATION</h2>
      <div class="formal-sec-line"></div>
      ${eduHTML}

      <h2 class="formal-sec-title">TECHNICAL SKILLS</h2>
      <div class="formal-sec-line"></div>
      <p><strong>Core Skills:</strong> ${skillText}</p>

      <h2 class="formal-sec-title">PROJECTS & EXPERIENCE</h2>
      <div class="formal-sec-line"></div>
      ${projectsHTML}

      <h2 class="formal-sec-title">CERTIFICATIONS & ACHIEVEMENTS</h2>
      <div class="formal-sec-line"></div>
      ${certsHTML}
    `;

  } else {
    // OPTION 2: MODERN GRAPHIC ARCH (REPLICATING SCREENSHOT DESIGN)
    let avatarHTML = '';
    if (p.avatarUrl) {
      avatarHTML = `<div class="arch-avatar-frame"><img src="${p.avatarUrl}" alt="Photo"></div>`;
    } else {
      const initials = (p.fullName || 'Alex Sharma').split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
      avatarHTML = `<div class="arch-avatar-frame"><span class="arch-monogram">${initials}</span></div>`;
    }

    // Contact List
    const contactItems = [];
    if (p.phone) contactItems.push(`<div class="arch-contact-item">📞 ${p.phone}</div>`);
    if (p.email) contactItems.push(`<div class="arch-contact-item">✉️ ${p.email}</div>`);
    if (p.website) contactItems.push(`<div class="arch-contact-item">🌐 ${p.website}</div>`);
    if (p.location) contactItems.push(`<div class="arch-contact-item">📍 ${p.location}</div>`);
    if (p.linkedin) contactItems.push(`<div class="arch-contact-item">💼 ${p.linkedin}</div>`);

    // Education in bottom dark arch card
    const eduArchHTML = state.education.map(e => e.degree ? `
      <div class="arch-edu-item">
        <div class="arch-edu-school">${e.institution || 'University'}</div>
        <div class="arch-edu-deg">${e.degree}</div>
        <div class="arch-edu-date">${e.dates} | ${e.score}</div>
      </div>
    ` : '').join('');

    // Certs in bottom dark arch card
    const certsArchHTML = state.extras.map(e => e.text ? `
      <div style="font-size: 7.5pt; color: #d4d4d4; margin-bottom: 4px;">• ${e.text}</div>
    ` : '').join('');

    // Projects in Right Column
    const jobsHTML = state.projects.map(pr => pr.title ? `
      <div class="arch-job-item">
        <div class="job-header">
          <span class="job-title">${pr.title}</span>
          <span class="job-date">${pr.dates}</span>
        </div>
        ${pr.tech ? `<div class="job-sub">${pr.tech}</div>` : ''}
        ${pr.bullets ? `<ul class="job-bullets">${pr.bullets.map(b => `<li>${b}</li>`).join('')}</ul>` : ''}
      </div>
    ` : '').join('');

    // Skill Bars (2 Columns)
    const skillBars2Col = state.skillBars.map(s => `
      <div class="skill-bar-item">
        <div class="sk-bar-head">${s.name}</div>
        <div class="sk-bar-track"><div class="sk-bar-fill" style="width:${s.percent}%;"></div></div>
      </div>
    `).join('');

    // Languages Tags
    const langTags = (state.languages || 'English, Python, SQL').split(',').map(l => `<span class="tag-badge">${l.trim()}</span>`).join('');
    const hobTags = (state.hobbies || 'Kaggle, LeetCode, Chess').split(',').map(h => `<span class="tag-badge">${h.trim()}</span>`).join('');

    sheet.innerHTML = `
      <!-- LEFT SIDEBAR -->
      <div class="arch-sidebar">
        <div class="arch-top-card">
          <h1 class="arch-name">${p.fullName || 'ALEX SHARMA'}</h1>
          <p class="arch-title">${p.title || '3RD YEAR B.TECH DATA SCIENCE'}</p>
          ${avatarHTML}
        </div>

        <div class="arch-contact-sec">
          <div class="arch-sec-head"><span class="icon-badge">👤</span> CONTACT ME</div>
          ${contactItems.join('')}
        </div>

        <div class="arch-bottom-card">
          <div class="arch-sec-head"><span class="icon-badge">🎓</span> EDUCATION</div>
          ${eduArchHTML}

          <div class="arch-sec-head" style="margin-top: 16px;"><span class="icon-badge">🏆</span> HONORS</div>
          ${certsArchHTML}
        </div>
      </div>

      <!-- RIGHT MAIN COLUMN -->
      <div class="arch-main-col">
        ${p.summary ? `
          <div class="main-sec">
            <div class="main-sec-head"><span class="icon-badge">👤</span> ABOUT ME</div>
            <p class="arch-p">${p.summary}</p>
          </div>
        ` : ''}

        <div class="main-sec">
          <div class="main-sec-head"><span class="icon-badge">💼</span> KEY PROJECTS</div>
          ${jobsHTML}
        </div>

        <div class="main-sec">
          <div class="main-sec-head"><span class="icon-badge">⚙️</span> SKILLS</div>
          <div class="skills-2col">${skillBars2Col}</div>
        </div>

        <div class="bottom-2col">
          <div>
            <div class="main-sec-head"><span class="icon-badge">🌐</span> LANGUAGES</div>
            <div class="tag-list">${langTags}</div>
          </div>
          <div>
            <div class="main-sec-head"><span class="icon-badge">🧩</span> HOBBIES</div>
            <div class="tag-list">${hobTags}</div>
          </div>
        </div>
      </div>
    `;
  }
}

// Global Actions
document.getElementById('btn-load-sample').addEventListener('click', () => {
  if (confirm("Load sample Data Science resume data?")) {
    state = JSON.parse(JSON.stringify(sampleDSData));
    initStaticInputs();
    renderSkillBarsEditor();
    renderEducationEditor();
    renderProjectsEditor();
    renderExtrasEditor();
    saveState();
  }
});

document.getElementById('btn-clear').addEventListener('click', () => {
  if (confirm("Clear all resume fields?")) {
    state = {
      personal: { fullName: '', title: '', email: '', phone: '', location: '', linkedin: '', github: '', website: '', summary: '', avatarUrl: '' },
      education: [], skillBars: [], languages: '', hobbies: '', projects: [], extras: []
    };
    initStaticInputs();
    renderSkillBarsEditor();
    renderEducationEditor();
    renderProjectsEditor();
    renderExtrasEditor();
    saveState();
  }
});

document.getElementById('btn-export-pdf').addEventListener('click', () => window.print());

// Boot
initStaticInputs();
renderSkillBarsEditor();
renderEducationEditor();
renderProjectsEditor();
renderExtrasEditor();
renderSheet();
