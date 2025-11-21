---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs = site.publications | sort: 'year' | reverse %}
{% assign years = pubs | map: 'year' | uniq %}

{% for y in years %}
## {{ y }}
<ul>
{% for p in pubs %}{% if p.year == y %}<li>{% if p.link %}<a href="{{ p.link }}">{% endif %}{{ p.title | markdownify | remove: '"' | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href="https://doi.org/{{ p.doi }}">{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>
{% endfor %}
