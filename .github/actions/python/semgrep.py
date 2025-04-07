from dataclasses import dataclass
import json
from typing import List


@dataclass
class line:
    line: int
    col: int
    offset: int


@dataclass
class metadata:
    owasp: List
    cwe: List
    category: str
    technology: List
    confidence: str
    references: List
    subcategory: List
    likelihood: str
    impact: str
    license: str
    vulnerability_class: List
    source: str
    shortlink: str


@dataclass
class results:
    check_id: str
    path: str
    start: line
    end: line
    extra: line
    message: str
    metadata: metadata
    severity: str
    fingerprint: str
    lines: str
    validation_state: str
    engine_kind: str


@dataclass
class typeline:
    path: str
    start: line
    end: line


@dataclass
class span:
    file: str
    start: line
    end: line


@dataclass
class PartialParsing:
    PartialParsing: typeline


@dataclass
class errors:
    code: int
    level: str
    type: List[PartialParsing]
    message: str
    path: str
    spans: List[span]


@dataclass
class paths:
    scanned: List


@dataclass
class SemgrepResponse:
    version: str
    results: List[results]
    errors: List[errors]
    paths: paths
    skipped_rules: List


def genHTML(errarr: List[errors]) -> str:
    html = "<h1>Semgrep Results :test_tube:</h1>"
    html += "<table>"
    html += " <tr> <th>level</th> <th>message</th> <th>path</th> </tr>"
    # ----
    html += "<tr>"
    for err in errarr:
        html += "<td>" + dict(err).get("level") + "</td>"
    html += "</tr>"
    # ----
    html += "<tr>"
    for err in errarr:
        html += "<td>" + dict(err).get("message") + "</td>"
    html += "</tr>"
    # ----
    html += "<tr>"
    for err in errarr:
        html += "<td>" + dict(err).get("path") + "</td>"
    html += "</tr>"
    html += "</table>"
    return html


with open("semgrep") as f:
    file = json.load(f)
    semgrepResponse = SemgrepResponse(
        file["version"],
        file["results"],
        file["errors"],
        file["paths"],
        file["skipped_rules"],
    )
    print(genHTML(semgrepResponse.errors))
