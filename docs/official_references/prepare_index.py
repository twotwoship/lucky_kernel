"""Validate downloads and build the Korean reading index (no network access)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import quote
import hashlib
import json
import zipfile
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent


class Title(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.active = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)


report = json.loads((ROOT / "download_manifest.json").read_text(encoding="utf-8"))
docs = report["documents"]
for doc in docs:
    if doc["status"] != "downloaded":
        continue
    path = ROOT / doc["file"]
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == doc["sha256"], path
    assert len(data) == doc["bytes"], path
    if path.suffix == ".pdf":
        reader = PdfReader(path)
        assert len(reader.pages) > 0
        first = reader.pages[0].extract_text() or ""
        assert first.strip(), path
        reader.pages[-1].get_contents()
        doc["pdf_pages"] = len(reader.pages)
        doc["pdf_metadata_title"] = str((reader.metadata or {}).get("/Title", ""))
    else:
        parser = Title()
        parser.feed(data.decode("utf-8", errors="replace"))
        title = "".join(parser.parts).strip()
        assert title and not any(x in title.lower() for x in ["access denied", "just a moment", "404 not found"]), path
        doc["html_title"] = title
    doc["verified"] = True

pdf_count = sum(d["status"] == "downloaded" and d["file"].endswith(".pdf") for d in docs)
html_count = sum(d["status"] == "downloaded" and d["file"].endswith(".html") for d in docs)
(ROOT / "download_manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
lines = [
    "# 이양배 학습용 공식 문서 모음",
    "",
    "정리일: 2026-11-04 (Asia/Seoul)",
    "",
    f"**실제 저장 완료: {pdf_count+html_count}개 — PDF {pdf_count}개, HTML {html_count}개.** 아래에서 파일을 클릭하면 로컬 문서가 열린다. 원본은 각 제조사·프로젝트·표준 발행기관의 공개 배포 주소에서 받았다. 파일 본문은 번역하거나 편집하지 않았다.",
    "",
    "이 모음은 [개발 필수 기술 학습자료](../이양배_개발필수_기술학습자료.md)의 원리를 공식 자료로 공부하기 위한 것이다. 공식 규격서, 장치 reference manual, 제조사 기술 해설, API 문서는 성격이 다르다. 특히 UART·SPI 해설을 모든 장치의 단일 규격서로 취급하지 않는다.",
    "",
    "## 먼저 읽을 순서",
    "",
    "1. **통신 원리:** UART는 TI SPRADG5의 UART Introduction부터, SPI는 TI SBOA621의 신호·모드 부분부터 읽는다. 두 자료 후반의 Jacinto/TXE 장치 고유 설정은 STM32 공통 규칙이 아니다.",
    "2. **I2C:** TI SLVA704로 구조를 익힌 다음 NXP UM10204 §3.1의 START/STOP·ACK·주소·stretching을 읽는다.",
    "3. **시험 신호 생성:** STM32 RM0383의 RCC/GPIO/USART/SPI/I2C를 찾아보고, UM1724에서 NUCLEO-F411RE 실제 connector를 확인한다.",
    "4. **진단 CLI:** AMD UG1037의 AXI 구조 → PG021의 S2MM·status/error·Programming Sequence → Linux ioctl·MMIO·DMAengine을 연결해서 읽는다.",
    "5. **드라이버 심화:** platform driver → DMA memory → DMAengine의 callback·terminate·synchronize → lock·wait/completion 순서로 공부한다.",
    "6. **PC 프로그램:** Qt QAbstractSocket으로 비동기 수신을 익히고 Threads and QObjects로 GUI·worker 관계를 공부한다. RFC 9293은 우선 byte-stream 서비스 의미를 확인한다.",
    "",
    "## 판본과 저장 형식",
    "",
    "- **STM32 RM0383은 ST 일본 공식 사이트의 Rev 3 보관본이다.** 최신판 Rev 4는 직접 다운로드가 시간 초과되어 링크만 남겼다. Rev 3에는 SPI CR2의 register map 누락 등 수정 사항이 있으므로 실제 register 구현에는 최신판·정오표를 대조한다. [ST 공식 수정 안내](https://community.st.com/stm32-mcus-products-25/spi-register-cr2-missing-on-register-map-rm-for-stm32f411ret6-rm0383-rev-3-153808)",
    "- **NUCLEO UM1724는 ST 일본 공식 사이트의 Rev 16 보관본이다.** 현재 공식 링크에서 확인한 Rev 17과 구분하며 실제 보드 revision을 확인한다.",
    "- **AMD PG021 PDF는 2022-04-27판, UG1037 PDF는 v4.0/2017-07-15판이다.** [PG021 온라인 문서](https://docs.amd.com/r/en-US/pg021_axi_dma)와 실제 Vivado/IP 버전에 맞춰 대조한다. 기본 원리 학습과 현재 설정 확인을 구분한다.",
    "- **Linux·Qt HTML은 다운로드 시점의 공개 문서다.** 대상 kernel과 Qt 버전을 자동으로 맞춘 문서가 아니다. 대상 버전의 API 서명·지원 여부는 별도 확인한다.",
    "- **HTML은 해당 페이지 본문을 저장한 파일이다.** 사이트 전체·하위 링크·외부 CSS·이미지를 전부 내려받은 오프라인 매뉴얼은 아니다. 본문은 로컬에서 읽을 수 있지만 일부 스타일·이미지·상대 링크는 인터넷이 필요할 수 있다. PDF는 본문과 그림이 포함된 원본 파일이다.",
    "",
]
groups = {"01_protocols": "통신 프로토콜", "02_stm32": "STM32 시험 신호·보드", "03_fpga_axi_dma": "FPGA·AXI·DMA", "04_linux_driver": "Linux 드라이버", "05_tcp_qt": "TCP·Qt"}
for group, heading in groups.items():
    lines += [f"## {heading}", "", "| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |", "|---|---|---|---|"]
    for doc in docs:
        if doc["status"] != "downloaded" or not doc["file"].startswith(group + "/"):
            continue
        size = f'{doc["pdf_pages"]}쪽 PDF' if "pdf_pages" in doc else "HTML"
        href = quote(doc["file"], safe="/")
        source = doc.get("final_url", doc["source_url"])
        lines.append(f'| [{doc["title"]}]({href}) | {doc["publisher"]} · {size} | {doc["focus"]} | [원본]({source}) |')
    lines += [""]
lines += ["## 다운로드되지 않은 원문", "", "다음 8개는 파일을 저장하지 못했다. 시간 초과 또는 PDF 주소의 웹페이지 전환으로 실패했으며, 파일이 있는 것처럼 표시하지 않았다. 아래는 인터넷에서 여는 공식 링크다. UART·SPI는 위의 TI 자료로, STM32는 명시한 보관본으로 먼저 공부할 수 있다.", "", "| 원문 | 상태 | 공식 링크 |", "|---|---|---|"]
for doc in docs:
    if doc["status"] == "downloaded":
        continue
    reason = "시간 초과" if "timed out" in doc.get("error", "") else "기존 PDF 주소가 웹 문서로 전환 / 직접 PDF 확보 실패"
    source = doc["source_url"]
    if "UG1092" in doc["file"]:
        source = "https://docs.amd.com/r/en-US/ug1092-kr260-starter-kit"
    lines.append(f'| {doc["title"]} | {reason} | [공식 링크]({source}) |')
lines += ["", "CDC와 AXIS handshake는 추가 온라인 공식 자료를 사용한다: [AMD UG949 Multi-Bit CDC](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Multi-Bit-CDC), [AMD AXIS handshake](https://docs.amd.com/r/en-US/ug1483-model-composer-sys-gen-user-guide/AXI4-Stream-Support-in-Model-Composer). 이 두 페이지는 로컬 문서 수에 포함하지 않았다.", "", "## 파일 확인·재다운로드", "", "`download_manifest.json`에 원본·실제 다운로드 URL, 크기, SHA-256, PDF 쪽수 또는 HTML 제목, 성공/실패를 기록했다. PDF header·종료 marker와 parser 로딩, HTML 제목·본문 존재 여부를 확인했다. 원본 문서를 새로 편집한 것은 아니므로 레이아웃을 재생성하지 않았다.", "", "`download_references.py`는 공개 공식 주소에서 재다운로드하는 Python 스크립트다. 파일을 실행하거나 패키지를 설치하지 않고 문서만 저장한다. 기존 파일은 덮어쓰지 않는다. 일반 Python 표준 라이브러리로 실행 가능하다. `prepare_index.py`는 검증·목록·압축파일 생성용이며 pypdf가 필요하다.", "", "[전체 다운로드 기록](download_manifest.json)", ""]
(ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
archive = ROOT.parent / "이양배_공식학습문서_모음.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix != ".part" and "__pycache__" not in path.parts:
            z.write(path, Path("official_references") / path.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
print(json.dumps(dict(downloaded=pdf_count+html_count, pdf=pdf_count, html=html_count, failed=sum(d["status"] != "downloaded" for d in docs), archive_bytes=archive.stat().st_size, archive=str(archive)),ensure_ascii=False))
