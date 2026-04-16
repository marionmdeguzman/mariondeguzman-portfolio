from flask import Flask, render_template, abort

app = Flask(__name__)

# ─── PROFILE DATA ─────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Marion De Guzman",
    "title_tags": ["SaaS", "Observability", "Senior Support Engineering"],
    "badge": "Available for Opportunities",
    "summary": (
        "Senior engineering professional with 8+ years in Cloud, Software Applications "
        "& Observability. Seasoned in Senior Support / Team Lead, SME Tech Lead, and "
        "Observability Support Engineering roles."
    ),
    "email": "deguzmancaptain@gmail.com",
    "phone": "+63 9363392851",
    "location": "Manila, Philippines",
    "github": None,  # Add your GitHub URL here when ready
}

ABOUT_CARDS = [
    {
        "icon_key": "user",
        "title": "Who I Am",
        "body": (
            "I am a Senior Engineering Professional specialising in Cloud Infrastructure, "
            "Observability, and SaaS technical operations. With 8+ years of experience, "
            "I have a strong track record spanning telco platforms, cloud-native environments, "
            "and international enterprise support."
        ),
    },
    {
        "icon_key": "activity",
        "title": "What I Do",
        "body": (
            "I serve as a technical consultant and customer success engineer at Coralogix, "
            "owning end-to-end resolution of complex customer issues across AWS, Kubernetes, "
            "Terraform, and Observability stacks — ensuring satisfaction and reliability at "
            "enterprise scale."
        ),
    },
    {
        "icon_key": "users",
        "title": "Leadership",
        "body": (
            "I have led L2/L3 Technical Operations teams, managed vendor relationships, and "
            "driven operational excellence in tier-1 telecom and SaaS platforms — consistently "
            "delivering 24x7 KPI compliance and stakeholder satisfaction."
        ),
    },
    {
        "icon_key": "star",
        "title": "Passion & Drive",
        "body": (
            "Beyond the terminal, I am passionate about sharing knowledge — from university "
            "lecturing to community presentations on Cisco and Linux. My goal is to continue "
            "pushing the boundaries of cloud-native observability and engineering excellence "
            "in the APAC region."
        ),
    },
]

HIGHLIGHTS = [
    {
        "icon": "🏆",
        "title": "Licensed Electronics Engineer",
        "body": (
            "Passed the Philippine Electronics Engineer Licensure Examination, establishing "
            "a strong formal foundation in engineering practice and professional standards."
        ),
        "tag": "Professional License",
        "tag_class": "tag-gold",
    },
    {
        "icon": "🎤",
        "title": "Cisco & Linux Presenter — Adamson University",
        "body": (
            "Invited as a technical speaker at Adamson University to present on Cisco "
            "networking fundamentals and Linux system administration, bridging industry "
            "practice with academic learning."
        ),
        "tag": "Speaker",
        "tag_class": "tag-blue",
    },
    {
        "icon": "🎓",
        "title": "Part-Time Professor — Adamson University ECE",
        "body": (
            "Served as a part-time college professor for the Electronics Engineering "
            "department from February to April 2020, delivering lectures in Electronic "
            "Devices & Circuit Theory and Electronics Circuits & Design Laboratory."
        ),
        "tag": "Educator · Feb–Apr 2020",
        "tag_class": "tag-blue",
    },
    {
        "icon": "🌏",
        "title": "First Filipino Senior Support Engineer at Coralogix",
        "body": (
            "Made history as the first Filipino to hold a Senior Support Engineering "
            "position at Coralogix — an international Observability SaaS platform — "
            "representing excellence for Filipino engineers in the global cloud industry."
        ),
        "tag": "Pioneering Achievement",
        "tag_class": "tag-green",
    },
    {
        "icon": "☸️",
        "title": "Certified Kubernetes Administrator (CKA)",
        "body": (
            "Successfully attained the Certified Kubernetes Administrator (CKA) credential, "
            "validating hands-on expertise in deploying, configuring, and managing Kubernetes "
            "clusters at production scale."
        ),
        "tag": "Certification · 2026",
        "tag_class": "tag-gold",
    },
    {
        "icon": "⭐",
        "title": "2025 Outstanding Support Engineer — Coralogix APAC",
        "body": (
            "Received the 2025 Year-End Commendation as Outstanding Support Engineer for "
            "the APAC region at Coralogix, recognising exceptional customer satisfaction, "
            "technical depth, and regional leadership."
        ),
        "tag": "Award · 2025",
        "tag_class": "tag-gold",
    },
]

EXPERIENCE = [
    {
        "role": "Observability SaaS — Senior Support Engineer",
        "company": "Coralogix",
        "period": "Apr 2024 – Present",
        "bullets": [
            "Customer Success & Operations Engineering with strong Cloud DevOps and Observability expertise.",
            "Single point of contact / Technical Consultant for all product and technology-related issues.",
            "End-to-end ownership of customer support cases from opening to closure, ensuring satisfaction.",
            "Resolved complex issues across AWS (ECS, EKS, EC2, CloudWatch, S3, Firehose, Lambda), "
            "Kubernetes, Terraform, APIs & SDKs, telemetry integrations (FluentD, Filebeat, OpenTelemetry), "
            "and Observability stacks (ELK, Prometheus, Lucene, PromQL).",
        ],
        "tags": ["AWS EKS", "Kubernetes", "Terraform", "OpenTelemetry", "Prometheus", "ELK", "PromQL", "APIs / SDKs"],
    },
    {
        "role": "Application Operations Manager",
        "company": "Globe Telecom Inc.",
        "period": "Jun 2023 – Mar 2024",
        "bullets": [
            "SME for a tier-1 platform covering Telco 3GPP Standards, System Architecture, AWS, "
            "Grafana/Prometheus/AlertManager, and APIs in Telco systems.",
            "Planned, implemented, controlled, reviewed, and audited production applications to meet "
            "business requirements 24x7.",
            "Managed L2 and L3 Vendor Technical Operations teams.",
            "Drove business stakeholder management and support across operational domains.",
        ],
        "tags": ["3GPP", "Grafana", "AlertManager", "AWS", "Team Leadership", "Telco"],
    },
    {
        "role": "Team Lead & SME",
        "company": "SMS Global Technologies, Inc.",
        "period": "Jun 2021 – Jun 2023",
        "bullets": [
            "L2 Technical Subject Matter Expert for a tier-1 application system.",
            "Managed L2 Technical Ops Team and L3 Vendor Operations Support.",
            "Interfaced with client counterparts as Technical L2 Support Lead.",
        ],
        "tags": ["SME", "L2/L3 Ops", "Vendor Management"],
    },
    {
        "role": "Senior Technical Support Engineer",
        "company": "SMS Global Technologies Inc.",
        "period": "Jan 2021 – May 2021",
        "bullets": [
            "Maintained tier-1 Telco Platform at 99% service availability and performance.",
            "Incident management: system troubleshooting, restoration, root cause analysis, and final resolution deployment.",
            "Authored shell scripts for task automation; gathered data for KPI forecasting and preventive maintenance.",
            "Created monthly operational reports covering system KPIs, ticket management, highlights, and lowlights.",
            "Coached and trained subordinate engineers.",
        ],
        "tags": ["Incident Management", "Shell Scripting", "KPI Reporting"],
    },
    {
        "role": "Electronics Engineering Professor (Part-Time)",
        "company": "Adamson University",
        "period": "Feb 2020 – May 2020",
        "bullets": [
            "Delivered lectures in Electronic Devices and Circuit Theory.",
            "Facilitated Electronic Circuits and Design Laboratory sessions for ECE students.",
        ],
        "tags": ["Lecturing", "ECE", "Circuit Theory"],
    },
    {
        "role": "Technical Support Engineer",
        "company": "SMS Global Technologies Inc.",
        "period": "Jan 2018 – Dec 2020",
        "bullets": [
            "Sustained 99% service availability on a tier-1 Telco Platform through operational application support.",
            "Handled incident management, root cause analysis, and resolution deployment.",
            "Developed shell scripts for task automation and KPI data gathering.",
            "Produced monthly operational reports covering KPIs, ticket management, and platform highlights.",
        ],
        "tags": ["Telco", "Linux", "Shell Scripting", "RCA"],
    },
    {
        "role": "Technical Support Engineer Intern",
        "company": "SMS Global Technologies Inc.",
        "period": "Nov 2016 – Jan 2017",
        "bullets": [
            "Collected, generated, and analysed KPI monitoring reports for a load-balancing Telco platform.",
            "Championed scheduled KPI testing for a 4G LTE Network Element across Manila business districts.",
        ],
        "tags": ["KPI Monitoring", "4G LTE", "Load Balancing"],
    },
]

SKILLS = [
    {"name": "Linux Sysadmin",    "color": "#f97316"},
    {"name": "Shell Scripting",   "color": "#84cc16"},
    {"name": "Python / Web Dev",  "color": "#3b82f6"},
    {"name": "AWS Services",      "color": "#f59e0b"},
    {"name": "Kubernetes",        "color": "#326ce5"},
    {"name": "Terraform",         "color": "#7c3aed"},
    {"name": "APIs & SDKs",       "color": "#06b6d4"},
    {"name": "OpenTelemetry",     "color": "#10b981"},
    {"name": "ELK Stack",         "color": "#ef4444"},
    {"name": "Prometheus",        "color": "#e27343"},
    {"name": "PromQL / Lucene",   "color": "#60a5fa"},
    {"name": "Grafana",           "color": "#f43f5e"},
    {"name": "FluentD / Filebeat","color": "#fbbf24"},
    {"name": "3GPP / Telco",      "color": "#a78bfa"},
    {"name": "Team Leadership",   "color": "#34d399"},
    {"name": "Customer Success",  "color": "#38bdf8"},
]

EDUCATION = [
    {
        "degree": "B.S. Electronics Engineering",
        "school": "Adamson University",
        "years": "2011 – 2017",
    }
]

CERTIFICATIONS = [
    {"name": "Cisco Certified Network Associate (CCNA)", "year": "2019", "icon": "🌐", "bg": "rgba(16,185,129,0.1)"},
    {"name": "Red Hat Certified System Administrator (RHCSA)", "year": "2022", "icon": "🐧", "bg": "rgba(239,68,68,0.1)"},
    {"name": "AWS Solutions Architect Associate", "year": "2023", "icon": "☁️", "bg": "rgba(245,158,11,0.1)"},
    {"name": "Certified Kubernetes Administrator (CKA)", "year": "2026", "icon": "☸️", "bg": "rgba(59,130,246,0.1)"},
]

# ─── BLOG POSTS ───────────────────────────────────────────────────────────────
# Add entries here to publish posts. Future: swap this list for a DB query.
# Each post needs: slug (url-safe), title, date (YYYY-MM-DD), summary, body (HTML or markdown).
BLOG_POSTS = [
    # {
    #     "slug": "my-first-post",
    #     "title": "My First Post",
    #     "date": "2026-03-16",
    #     "summary": "A short description shown on the blog index.",
    #     "body": "<p>Full post content here. Can be raw HTML or rendered markdown.</p>",
    # },
]

# ─── SERVICES ─────────────────────────────────────────────────────────────────
# Add entries here to advertise services. Future: swap for a DB or CMS.
SERVICES = [
    # {
    #     "icon": "☁️",
    #     "title": "Cloud & Observability Consulting",
    #     "description": "End-to-end setup and tuning of observability stacks on AWS/EKS.",
    #     "tags": ["AWS", "Prometheus", "ELK", "Grafana"],
    # },
]

# ─── ROUTES ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        active_page="home",
        profile=PROFILE,
        about_cards=ABOUT_CARDS,
        highlights=HIGHLIGHTS,
        experience=EXPERIENCE,
        skills=SKILLS,
        education=EDUCATION,
        certifications=CERTIFICATIONS,
    )


@app.route("/blog")
def blog_index():
    return render_template(
        "blog/index.html",
        active_page="blog",
        profile=PROFILE,
        posts=BLOG_POSTS,
    )


@app.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if post is None:
        abort(404)
    return render_template(
        "blog/post.html",
        active_page="blog",
        profile=PROFILE,
        post=post,
    )


@app.route("/services")
def services():
    return render_template(
        "services/index.html",
        active_page="services",
        profile=PROFILE,
        services=SERVICES,
    )


if __name__ == "__main__":
    app.run(debug=True)
