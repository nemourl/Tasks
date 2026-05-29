import re


def extract_domain(url):
    pattern = r'^(?:https?://)?([^/:]+)'

    compliance = re.search(pattern, url)

    if compliance:
        return compliance.group(1)

    return None

print(extract_domain("https://www.example.com/path"))
print(extract_domain("sub.domain.org:8080/page"))