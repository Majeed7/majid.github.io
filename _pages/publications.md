---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign pubs = site.publications | where_exp: 'item', 'item.year' %}
{% assign pubs = pubs | sort: 'year' %}
{% assign years = pubs | map: 'year' | uniq | sort | reverse %}

<div class="pubs">

	{% for year in years %}
		<h2 class="pubs-year">{{ year }}</h2>

		<ul class="pubs-list">
			{% for p in pubs reversed %}
				{% if p.year == year %}

					{% assign href = nil %}
					{% if p.link %}
						{% assign href = p.link %}
					{% elsif p.url %}
						{% assign href = p.url | relative_url %}
					{% endif %}

					<li class="pubs-item">
						{% assign normalized_citation = p.citation | default: '' %}
						{% assign normalized_citation = normalized_citation | replace: '\n', ' ' %}
						{% assign normalized_citation = normalized_citation | replace: '{', '' %}
						{% assign normalized_citation = normalized_citation | replace: '}', '' %}
						{% assign normalized_citation = normalized_citation | replace: '“', '"' %}
						{% assign normalized_citation = normalized_citation | replace: '”', '"' %}
						{% assign normalized_citation = normalized_citation | replace: '’', "'" %}
						{% assign normalized_citation = normalized_citation | replace: "\\'", '' %}
						{% assign normalized_citation = normalized_citation | replace: '  ', ' ' %}
						{% assign normalized_citation = normalized_citation | replace: '  ', ' ' %}
						{% assign normalized_citation = normalized_citation | strip %}
						{% if normalized_citation != '' %}
							{% assign citation_parts = normalized_citation | split: '. ' %}
							{% assign authors_part = citation_parts[0] | default: '' %}
							{% assign remainder_parts = citation_parts | slice: 1, citation_parts.size %}
							{% assign remainder_text = remainder_parts | join: '. ' | strip %}
						{% else %}
							{% assign authors_part = '' %}
							{% assign remainder_text = '' %}
						{% endif %}
						{% assign author_tokens = authors_part | split: ', ' %}
						{% assign formatted_authors = '' %}
						{% assign pending_last = '' %}
						{% for token in author_tokens %}
							{% assign clean_token = token | strip %}
							{% if pending_last == '' %}
								{% assign pending_last = clean_token %}
							{% else %}
								{%- capture formatted_authors -%}{{ formatted_authors }}{% if formatted_authors != '' %}, {% endif %}{{ clean_token }} {{ pending_last }}{%- endcapture -%}
								{% assign pending_last = '' %}
							{% endif %}
						{% endfor %}
						{% if pending_last != '' %}
							{%- capture formatted_authors -%}{{ formatted_authors }}{% if formatted_authors != '' %}, {% endif %}{{ pending_last }}{%- endcapture -%}
						{% endif %}
						{%- capture highlighted_authors -%}{{ formatted_authors | strip
								| replace: ' ,', ', '
								| replace: ' ,', ', '
								| replace: ',,', ', '
								| replace: ',  ', ', '
								| replace: 'Majid Mohammadi', '<span class="pubs-highlight">Majid Mohammadi</span>'
								| replace: 'Majeed Mohammadi', '<span class="pubs-highlight">Majeed Mohammadi</span>'
								| replace: 'Mohammadi Majid', '<span class="pubs-highlight">Mohammadi Majid</span>'
						}}{%- endcapture -%}
						{% assign highlighted_authors = highlighted_authors | strip %}

						{% assign title_text = p.title | markdownify | strip_html | strip %}
						{% assign remaining_parts = remainder_parts %}
						{% if remaining_parts.size > 0 %}
							{% assign derived_title = remaining_parts[0] | strip %}
							{% capture title_norm %}
								{{ title_text | downcase
									| replace: '"', '' | replace: "'", '' | replace: ':', '' | replace: ',', '' | replace: '.', '' | replace: '-', '' | replace: '–', '' | replace: '—', '' | replace: ' ', '' | replace: '&nbsp;', '' | replace: ' ', ''
									| replace: 'á', 'a' | replace: 'à', 'a' | replace: 'â', 'a' | replace: 'ä', 'a' | replace: 'ã', 'a' | replace: 'å', 'a'
									| replace: 'é', 'e' | replace: 'è', 'e' | replace: 'ê', 'e' | replace: 'ë', 'e'
									| replace: 'í', 'i' | replace: 'ì', 'i' | replace: 'î', 'i' | replace: 'ï', 'i'
									| replace: 'ó', 'o' | replace: 'ò', 'o' | replace: 'ô', 'o' | replace: 'ö', 'o' | replace: 'õ', 'o'
									| replace: 'ú', 'u' | replace: 'ù', 'u' | replace: 'û', 'u' | replace: 'ü', 'u'
									| replace: 'ñ', 'n' | replace: 'ç', 'c' | replace: 'ß', 'ss' | replace: 'œ', 'oe' | replace: 'æ', 'ae'
								}}
							{% endcapture %}
							{% assign title_norm = title_norm | strip %}
							{% capture derived_norm %}
								{{ derived_title | downcase
									| replace: '"', '' | replace: "'", '' | replace: ':', '' | replace: ',', '' | replace: '.', '' | replace: '-', '' | replace: '–', '' | replace: '—', '' | replace: ' ', '' | replace: '&nbsp;', '' | replace: ' ', ''
									| replace: 'á', 'a' | replace: 'à', 'a' | replace: 'â', 'a' | replace: 'ä', 'a' | replace: 'ã', 'a' | replace: 'å', 'a'
									| replace: 'é', 'e' | replace: 'è', 'e' | replace: 'ê', 'e' | replace: 'ë', 'e'
									| replace: 'í', 'i' | replace: 'ì', 'i' | replace: 'î', 'i' | replace: 'ï', 'i'
									| replace: 'ó', 'o' | replace: 'ò', 'o' | replace: 'ô', 'o' | replace: 'ö', 'o' | replace: 'õ', 'o'
									| replace: 'ú', 'u' | replace: 'ù', 'u' | replace: 'û', 'u' | replace: 'ü', 'u'
									| replace: 'ñ', 'n' | replace: 'ç', 'c' | replace: 'ß', 'ss' | replace: 'œ', 'oe' | replace: 'æ', 'ae'
								}}
							{% endcapture %}
							{% assign derived_norm = derived_norm | strip %}
							{% if title_text == '' %}
								{% assign title_text = derived_title %}
								{% assign remaining_parts = remaining_parts | slice: 1, remaining_parts.size %}
							{% elsif derived_norm == title_norm or derived_norm contains title_norm or title_norm contains derived_norm %}
								{% assign remaining_parts = remaining_parts | slice: 1, remaining_parts.size %}
							{% endif %}
						{% endif %}

						{% assign details_text = remaining_parts | join: '. ' | strip %}
						{% if details_text == '' %}
							{% assign venue_text = p.venue | default: '' | strip %}
							{% assign year_text = p.year | default: '' | append: '' %}
							{% if venue_text != '' %}
								{% assign details_text = venue_text %}
								{% if year_text != '' %}
									{% assign details_text = details_text | append: ' ' | append: year_text %}
								{% endif %}
							{% elsif year_text != '' %}
								{% assign details_text = year_text %}
							{% endif %}
						{% endif %}

						{% if highlighted_authors != '' %}
							<div class="pubs-authors">{{ highlighted_authors }}</div>
						{% endif %}

						{% if title_text != '' %}
							<div class="pubs-title">{{ title_text }}</div>
						{% endif %}

						{% if details_text != '' %}
							<div class="pubs-details">{{ details_text }}</div>
						{% endif %}

						<div class="pubs-meta">
							{% if href %}
								<a class="pubs-link" href="{{ href }}">details</a>
							{% endif %}
							{% if p.doi %}
								{% if href %}<span class="pubs-separator">•</span>{% endif %}
								<a class="pubs-doi" href="https://doi.org/{{ p.doi }}">DOI: {{ p.doi }}</a>
							{% endif %}
						</div>
					</li>

				{% endif %}
			{% endfor %}
		</ul>

	{% endfor %}

</div>
