---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
education:
  - institution: "Delft University of Technology"
    credential: "Ph.D. Candidate (cum laude)"
    location: "Delft, The Netherlands"
    years: "2015-2019"
    details:
      - "Thesis: Ontology Alignment: Simulated annealing-based system, statistical evaluation, and application to logistics interoperability."
      - "Advisers: Prof. Yao-Hua Tan and Dr. Wout Hofman."
  - institution: "Ferdowsi University of Mashhad"
    credential: "M.Sc. Artificial Intelligence"
    location: "Mashhad, Iran"
    years: "2012-2015"
    details:
      - "Thesis: Information-theoretic learning approaches to high-dimensional unsupervised data analysis."
      - "Adviser: Prof. G. A. Hodtani."
  - institution: "Ferdowsi University of Mashhad"
    credential: "B.Sc. Software Engineering"
    location: "Mashhad, Iran"
    years: "2007-2011"
    details:
      - "Coursework emphasized software engineering fundamentals, programming, and systems design."
experience:
  - organization: "Utrecht University"
    title: "Postdoctoral Researcher — GenAI in Mass Spectrometry"
    location: "Utrecht, The Netherlands"
    years: "2025-Present"
    bullets:
      - "Develop foundation models for mass spectrometry analysis using advanced state-space approaches."
  - organization: "CISPA Helmholtz Center for Information Security"
    title: "Visiting Researcher — PostNetAI Fellow"
    location: "Saarbrucken, Germany"
    years: "Mar 2025-Present"
    bullets:
      - "Study analytical explanations for kernel-based models and distributional discrepancy measures such as MMD and HSIC."
  - organization: "Vrije Universiteit Amsterdam"
    title: "Postdoctoral Researcher — AI in Medicine"
    location: "Amsterdam, The Netherlands"
    years: "2021-2025"
    bullets:
      - "Designed explainable AI techniques for clinical decision support and interlinked guidelines (e.g., WebOfGuidelines.nl)."
      - "Collaborated with industry partners including myTomorrows and Thuisarts.nl to integrate AI into medical workflows."
  - organization: "Marburg University"
    title: "Visiting Researcher — PostNetAI Fellow"
    location: "Marburg, Germany"
    years: "Oct 2021-Nov 2021"
    bullets:
      - "Investigated explainable AI techniques for fake news detection systems."
  - organization: "Jheronimus Academy of Data Science (JADS)"
    title: "Postdoctoral Researcher"
    location: "'s-Hertogenbosch, The Netherlands"
    years: "2020"
    bullets:
      - "Researched deep learning, cybersecurity, and interpretable AI while supervising multiple M.Sc. theses."
  - organization: "Freelance / Senior Web Developer"
    title: "Web & Desktop Application Developer"
    location: "Mashhad, Iran (remote collaborations)"
    years: "2009-2015"
    bullets:
      - "Delivered web and desktop applications with complex data backends using ASP.NET and ASP.NET MVC for regional clients."
      - "Collaborated with international teams (Omnia, Prototype) to build and maintain scalable ASP.NET/MVC platforms."
      - "Led end-to-end development: requirements gathering, architecture, data modeling, deployment, and maintenance."
---

<div class="cv">
	<section class="cv-section">
		<h2 class="cv-section-title">Education</h2>
		<div class="cv-grid">
			{% for item in page.education %}
				<article class="cv-card">
					<header class="cv-card-header">
						<h3 class="cv-card-title">{{ item.institution }}</h3>
						<div class="cv-card-meta">{{ item.credential }} &middot; {{ item.years }}</div>
						<div class="cv-card-submeta">{{ item.location }}</div>
					</header>
					<ul class="cv-points">
						{% for detail in item.details %}
							<li>{{ detail }}</li>
						{% endfor %}
					</ul>
				</article>
			{% endfor %}
		</div>
	</section>

	<section class="cv-section">
		<h2 class="cv-section-title">Professional Experience</h2>
		<div class="cv-grid">
			{% for role in page.experience %}
				<article class="cv-card">
					<header class="cv-card-header">
						<h3 class="cv-card-title">{{ role.organization }}</h3>
						<div class="cv-card-meta">{{ role.title }}</div>
						<div class="cv-card-submeta">{{ role.location }} &middot; {{ role.years }}</div>
					</header>
					<ul class="cv-points">
						{% for bullet in role.bullets %}
							<li>{{ bullet }}</li>
						{% endfor %}
					</ul>
				</article>
			{% endfor %}
		</div>
	</section>
</div>


