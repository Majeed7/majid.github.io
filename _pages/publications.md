---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs = site.publications | sort: 'year' | reverse %}
## 2025

<ul>
{% for p in pubs %}{% if p.year == '2025' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2024

<ul>
{% for p in pubs %}{% if p.year == '2024' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2023

<ul>
{% for p in pubs %}{% if p.year == '2023' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2022

<ul>
{% for p in pubs %}{% if p.year == '2022' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2021

<ul>
{% for p in pubs %}{% if p.year == '2021' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2020

<ul>
{% for p in pubs %}{% if p.year == '2020' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2019

<ul>
{% for p in pubs %}{% if p.year == '2019' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2018

<ul>
{% for p in pubs %}{% if p.year == '2018' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2017

<ul>
{% for p in pubs %}{% if p.year == '2017' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2016

<ul>
{% for p in pubs %}{% if p.year == '2016' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>

## 2015

<ul>
{% for p in pubs %}{% if p.year == '2015' %}<li>{% if p.link %}<a href='{{ p.link }}'>{% endif %}{{ p.title | markdownify | strip_html }}{% if p.link %}</a>{% endif %}. {{ p.citation }}{% if p.doi %} DOI: <a href='https://doi.org/{{ p.doi }}'>{{ p.doi }}</a>{% endif %}</li>{% endif %}{% endfor %}
</ul>
