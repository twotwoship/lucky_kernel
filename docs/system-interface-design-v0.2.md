# Lucky Kernel 시스템 설계 및 인터페이스 명세 v0.2

작성일: 2026-11-03 (Asia/Seoul)  
상태: 최신 Jira 기반 팀 결정·구현·검증 명세. v1 승인본 아님.  
기준: [SCRUM 프로젝트](https://packetkimjunpyo.atlassian.net/jira/software/projects/SCRUM/boards/1)의 이번 수정 후 38개 이슈, 47개 Blocks 관계.

## 1. 문서의 기준과 읽는 방법

최신 Jira의 Epic/Task 계층·범위·질문·완료 조건을 소스 오브 트루스로 삼는다. 이전 v0.1의 구조 설명을 Jira에 맞추며, 이전 문서에 적힌 숫자나 API 예시를 자동으로 승인된 구현값으로 취급하지 않는다.

- **Jira 작업 기준:** 이번 조회에서 확인한 책임 경계·산출물·완료 조건이다. 이슈가 존재한다는 것이 구현 완료를 뜻하지 않는다.
- **기존 제안:** v0.1과 SYS Description에서 검토 대상으로 사용하는 수치·배치·API 후보이다.
- **팀 결정 필요:** 실제 보드/커널/코드/시험 근거로 담당자가 답을 기록해야 한다.
- **승인 기준선:** SCRUM-5에서 검토자와 문서/헤더/fixture 버전을 기록한 뒤 성립한다.

기존 상세 기술표는 [v0.1 참조본](system-interface-design-v0.1-reference.md)에 보존했다. 참조본의 “SCRUM-5 아래 하위 작업”이라는 구조 설명은 폐기하고 본 문서 2절을 따른다. 참조본의 제안값보다 최신 SYS의 결정 기록이 우선한다. 아직 조회한 Description에는 최종 승인 결과나 실측 증빙이 없으므로 본 문서는 이를 만들어내지 않는다.

## 2. 실제 Jira 구조

### [SCRUM-8](https://packetkimjunpyo.atlassian.net/browse/SCRUM-8) FPGA 수집 및 트리거

- [SCRUM-13](https://packetkimjunpyo.atlassian.net/browse/SCRUM-13) 8채널 입력 동기화 및 샘플링 설정 구현
- [SCRUM-14](https://packetkimjunpyo.atlassian.net/browse/SCRUM-14) Edge Trigger 및 BRAM 버퍼 구현
- [SCRUM-15](https://packetkimjunpyo.atlassian.net/browse/SCRUM-15) AXI4-Stream 출력 및 RTL 검증
- [SCRUM-39](https://packetkimjunpyo.atlassian.net/browse/SCRUM-39) AXI4-Lite 레지스터·명령·진단 조회 RTL 구현

### [SCRUM-9](https://packetkimjunpyo.atlassian.net/browse/SCRUM-9) Linux 및 AXI DMA

- [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) PS/PL 연결 및 MMIO 접근 환경 구성
- [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) AXI DMA 수신 경로 구현
- [SCRUM-18](https://packetkimjunpyo.atlassian.net/browse/SCRUM-18) DMA 인터럽트 및 오류 복구 구현
- [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) logiccap 커널 장치 API·상태·소유권 통합 구현

### [SCRUM-10](https://packetkimjunpyo.atlassian.net/browse/SCRUM-10) Diagnostic Console

- [SCRUM-19](https://packetkimjunpyo.atlassian.net/browse/SCRUM-19) 레지스터 및 Capture 제어 명령 구현
- [SCRUM-20](https://packetkimjunpyo.atlassian.net/browse/SCRUM-20) 기준 패턴 비교 및 오류 위치 출력
- [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) 반복 시험 및 구조화된 로그 저장
- [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) liblogic 공통 Device API 및 Mock Backend 구현

### [SCRUM-11](https://packetkimjunpyo.atlassian.net/browse/SCRUM-11) TCP 및 Qt 분석기

- [SCRUM-22](https://packetkimjunpyo.atlassian.net/browse/SCRUM-22) TCP 서버 및 데이터 전송 형식 구현
- [SCRUM-23](https://packetkimjunpyo.atlassian.net/browse/SCRUM-23) Qt 파형 표시 및 Cursor/Zoom 구현
- [SCRUM-24](https://packetkimjunpyo.atlassian.net/browse/SCRUM-24) UART·I2C·SPI 프로토콜 분석 구현

### [SCRUM-12](https://packetkimjunpyo.atlassian.net/browse/SCRUM-12) 통합 및 검증

- [SCRUM-25](https://packetkimjunpyo.atlassian.net/browse/SCRUM-25) STM32 시험 신호 생성
- [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) 전체 경로 통합 및 성능 측정
- [SCRUM-27](https://packetkimjunpyo.atlassian.net/browse/SCRUM-27) 최종 Demo 및 결과 정리

### [SCRUM-30](https://packetkimjunpyo.atlassian.net/browse/SCRUM-30) 프로젝트 기반 구축

- [SCRUM-4](https://packetkimjunpyo.atlassian.net/browse/SCRUM-4) SYS-01 데이터 경로·모듈 책임 정의
- [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) 인터페이스 명세 v1 리뷰 및 최종 확정
- [SCRUM-6](https://packetkimjunpyo.atlassian.net/browse/SCRUM-6) 프로젝트 핵심 기술 선수학습 및 발표
- [SCRUM-7](https://packetkimjunpyo.atlassian.net/browse/SCRUM-7) 개발 환경구성
- [SCRUM-32](https://packetkimjunpyo.atlassian.net/browse/SCRUM-32) SYS-02 보드 입력·클록·리셋 정의
- [SCRUM-33](https://packetkimjunpyo.atlassian.net/browse/SCRUM-33) SYS-03 레지스터·상태·trigger 명세
- [SCRUM-34](https://packetkimjunpyo.atlassian.net/browse/SCRUM-34) SYS-04 AXIS·DMA 수신 계약
- [SCRUM-35](https://packetkimjunpyo.atlassian.net/browse/SCRUM-35) SYS-05 공통 커널 UAPI 정의
- [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) SYS-06 CLI·TCP·저장 형식 정의
- [SCRUM-37](https://packetkimjunpyo.atlassian.net/browse/SCRUM-37) SYS-07 프로토콜 시험 fixture 정의
- [SCRUM-38](https://packetkimjunpyo.atlassian.net/browse/SCRUM-38) SYS-08 인터페이스 검증 계획 확정

### [SCRUM-31](https://packetkimjunpyo.atlassian.net/browse/SCRUM-31) 프로젝트 관리 자동화

- [SCRUM-28](https://packetkimjunpyo.atlassian.net/browse/SCRUM-28) n8n 설치 및 Jira 상태 변경 수신 실습
- [SCRUM-29](https://packetkimjunpyo.atlassian.net/browse/SCRUM-29) Diagnostic Console 시험결과 Webhook 연동

SYS-01~08은 SCRUM-30 아래의 독립 Task다. SCRUM-5는 SYS 작업의 부모가 아니라 계약을 종합 검토하는 승인 작업이다.

추가한 SCRUM-39는 SYS-03의 RTL 구현, SCRUM-40은 SYS-05의 커널 구현, SCRUM-41은 SYS-05/06을 사용하는 공통 사용자 라이브러리 구현이다. 설계 Task를 구현 Task로 간주해 빠졌던 책임을 별도로 관리한다.

SCRUM-31의 n8n/Jira/Webhook 작업은 운영 자동화다. 제품 필수 경로인 수집→DMA→Linux→TCP→Qt의 완료를 자동화 완료에 종속시키지 않는다. UART/I2C/SPI는 기존 SCRUM-24를 유지하며 프로토콜별 산출물과 검증 결과를 따로 남긴다.

## 3. 시스템 경로와 제어 책임

```text
STM32 외부 시험 신호 ─┐
                      ├→ FPGA 샘플링/트리거 → BRAM → AXIS → AXI DMA → DDR
내부 counter8 패턴 ───┘                                      │
                                               logiccap 커널 드라이버
                                                         │ UAPI
                                                      liblogic
                                                     /        \
                                             logicdiag CLI   logicserver
                                                                 │ TCP
                                                              PC Qt
                                                        파형 / protocol 분석
```

| 경계 | 제공/구현 작업 | 사용하는 작업 | 합의할 계약 |
|---|---|---|---|
| 외부 신호→입력 | SCRUM-25, SCRUM-32 | SCRUM-13 | 핀·전압·GND·채널 번호·clock/reset |
| 샘플링→BRAM | SCRUM-13/14 | SCRUM-15 | tick·trigger sample·N·결과 유지 |
| IP 제어→Linux | SCRUM-39, SCRUM-16 | SCRUM-40 | SYS-03 레지스터·상태·IRQ·오류 |
| BRAM→DDR | SCRUM-15/17/18 | SCRUM-40 | SYS-04 packing·길이·완료·버퍼 수명 |
| 커널→liblogic | SCRUM-40 | SCRUM-41 | SYS-05 공통 UAPI·소유권·상태 |
| liblogic→프로그램 | SCRUM-41 | SCRUM-19/22 | 설정·시작·조회·취소·해제 의미 |
| 보드→PC | SCRUM-22 | SCRUM-23 | SYS-06 framing·metadata·raw bytes |
| CaptureData→decoder | SCRUM-23 | SCRUM-24 | SYS-07 fixture·채널·시간·오류 위치 |

소유권 기준은 SYS-01/05를 따른다. 커널이 하드웨어 상태·DMA 채널·수신 버퍼·capture_id를 소유하고, 사용자 프로그램은 공개 API를 통해 제어한다. CLI와 서버가 각자 DMA MMIO를 제어하는 구조를 만들지 않는다. 직접 CLI와 서버의 동시 장치 사용 정책은 SYS-05에서 확정하며 현재 검토안은 단일 소유자다.

담당자가 지정되지 않은 이슈에 임의 사람을 배정하지 않았다. 이전 문서의 역할 이름은 참고일 뿐 실제 할당은 Jira assignee와 팀 결정 기록을 따른다.

## 4. 계약을 확정할 질문과 산출물

| 계약 | 결정해야 할 핵심 질문 | 검토 가능한 산출물 | 구현 담당 Task |
|---|---|---|---|
| SYS-01 / SCRUM-4 | 누가 어떤 MMIO/DMA/버퍼를 소유하는가? 1회 수집 흐름에 책임 공백이 있는가? | 경로·책임 표, 정상/실패 시퀀스 | 전체 |
| SYS-02 / SCRUM-32 | 실제 핀·bank/전압·GND·clock/reset·CDC는 무엇인가? | 배선표, XDC, clock/reset 표 | 13, 16, 25 |
| SYS-03 / SCRUM-33 | offset/bit/reset/access, trigger 첫 sample, IRQ/W1C, 잘못된 명령은 어떻게 동작하는가? | register map, FSM, cycle 예 | 13, 14, 39 |
| SYS-04 / SCRUM-34 | packing/TLAST/길이, provider 모드, buffer lifetime, terminate/reset 순서는 무엇인가? | packing fixture, DMA/DT 표, 복구 절차 | 15, 17, 18 |
| SYS-05 / SCRUM-35 | ioctl/layout/ABI, 상태·errno·capture_id·read/poll/close 의미는 무엇인가? | 공통 UAPI 헤더, 상태/오류표 | 40, 41 |
| SYS-06 / SCRUM-36 | framing/ID/길이/단절, CLI 구문, 로그·파일 schema는 무엇인가? | 프로토콜 명세, 요청/응답/로그 fixture | 19~23, 41 |
| SYS-07 / SCRUM-37 | UART/I2C/SPI 설정·배선·송신값·기대 decode·incomplete 기준은 무엇인가? | firmware/config, raw+metadata+expected | 24, 25 |
| SYS-08 / SCRUM-38 | IF 시험의 입력·기대값·담당·환경·증빙·실보드 재검증 시점은 무엇인가? | IF-01~15 실행표 | 26, 27 |

각 질문에는 결정값뿐 아니라 선택 이유·담당·검토자·결정일·근거 링크를 남긴다. 미확정 항목은 “나중에” 대신 담당·목표 Sprint·영향받는 Task·mock 대체 범위를 적는다.

## 5. 샘플링·레지스터·AXIS/DMA 계약

### 5.1 현재 검토 중인 수집 모델

현재 SYS는 KR260의 외부 8채널, 단발 수집, BRAM 보관 후 DMA 전송, 1 sample=1 byte(bit k=CHk) 모델을 기준으로 검토한다. 연속 스트리밍·프리트리거·압축·다중 제어 세션은 이번 필수 구현으로 확정하지 않는다.

| 항목 | 이전 제안/현재 검토안 | 확정에 필요한 근거 |
|---|---|---|
| 기준 clock | 목표 100 MHz | 실제 생성 clock·타이밍 결과, SYS-02 |
| 분주 D | 1~1,000,000, clock enable | 허용 범위·첫 tick·counter 폭, SYS-03 |
| 수집 N | 4 이상, 4의 배수 | stream packing·DMA length 범위, SYS-03/04 |
| 최대 샘플 | 65,536 후보 | BRAM 자원·합성 결과·capability |
| trigger | immediate/rising/falling, 선택 1채널 | baseline 처리·첫 저장 index의 cycle 예 |
| 내부 pattern | sample[i]=i mod 256 후보 | ARM reset/저장 시 증가 규칙과 fixture |
| timeout | trigger/DMA 각 1000 ms 후보 | 실제 capture 시간·복구 시험, SYS-05 |

수치가 확정되면 실제 sample_clk_hz와 sample_div를 결과에 기록한다. 시간축은 index×D/clock, 두 sample 사이 시간차는 index 차이×D/clock이다. N개 샘플의 첫/끝 시각 차이 (N−1)×D/clock과 N주기의 수집 구간을 혼동하지 않도록 측정 정의를 함께 적는다.

### 5.2 레지스터 구현의 빈틈 보완

SCRUM-39에서 register map을 실제 RTL로 구현한다. IP_ID/ABI/CAPABILITIES, clock/capacity, 설정, COMMAND, STATE, count, IRQ/ERROR, BRAM 진단 조회를 SYS-03의 동일 표로 관리한다. 정확한 offset·reset 값은 승인된 register map에 기록하고 드라이버가 별도로 추측하지 않는다.

필수 질문은 AW/W의 독립 도착, WSTRB 부분 쓰기, R/B stall, RO/미정의/비정렬 접근, COMMAND pulse, W1C와 새 이벤트 충돌, 설정 변경 가능 상태, BRAM 읽기 지연이다. 실제 MMIO 절대주소는 Vivado와 DT를 대조한다.

### 5.3 전송과 완료 판단

SYS-04의 검토안은 4개 sample을 32-bit TDATA에 낮은 byte부터 배치하고, N이 4의 배수인 경우 TKEEP=0xF 및 마지막 word의 TLAST를 사용한다. 예시 fixture는 raw bytes 00 01 02 03 04 05 06 07 ↔ words 0x03020100, 0x07060504다. DDR/PC에서 원래 byte 순서가 유지되는지 실제로 확인해야 한다.

TVALID/TREADY handshake와 stall 시 payload 유지, 정확한 N bytes, BRAM 읽기 지연 처리는 SCRUM-15의 완료 증빙이다. provider의 Simple/SG·주소/길이 폭·completion/residue 지원은 실제 커널 구성을 확인해 정한다. 단발 수집이라는 이유로 DMA 모드를 추측하지 않는다.

수신 준비 실패 시 SEND하지 않고, DMA 완료 전 결과 공개나 buffer 해제를 하지 않는 경계를 구현한다. STREAM_DONE만으로 사용자 READY를 만들지 않고 DMA 완료·길이·stream 상태를 함께 대조한다. terminate/callback 동기화/source reset의 정확한 순서는 SCRUM-18에서 실환경 fault 시험으로 확인한다.

## 6. 커널 UAPI와 정상·실패 흐름

공통 헤더의 후보 경로는 include/logiccap_uapi.h다. 헤더 정의는 SYS-05, 구현은 SCRUM-40이다. 아래는 현재 SYS에 명시된 연산 의미이며 함수 원형·ioctl 번호·구조체 크기·상태 숫자는 승인 전 확정값이 아니다.

| 연산 | 합의할 의미 |
|---|---|
| open / GET_CAPS | 장치 소유권·ABI/feature/실제 clock·capacity 확인 |
| CONFIG | 전체 설정 검증, 허용 상태, 잘못된 값 처리 |
| START | 비동기 시작·capture_id 발급·설정 고정 |
| GET_STATUS / poll | 진행·완료·오류·취소의 관찰과 알림 |
| GET_RESULT / read / llseek | READY 결과 metadata·부분 읽기·EOF·cursor |
| CANCEL | 취소 요청·정리 완료 시점·허용 상태 |
| RELEASE | 결과 보관 해제·다음 START 허용 시점 |
| DIAG_* | 허용 register/buffer 조회·쓰기 범위 |
| close | 진행 중 작업·callback 정리 후 소유권 반환 |

정상 흐름의 기준은 capability 확인 → CONFIG → START → trigger/capture → DMA 수신 준비 → SEND → DMA/길이/상태 검증 → READY → metadata/raw data → RELEASE다.

| 경계 상황 | 팀이 정할 처리와 필요한 증빙 |
|---|---|
| 잘못된 CONFIG / BUSY | 유효 설정과 진행 중 작업을 훼손하지 않는가? |
| READY 이전 read / stale ID | 상태·errno가 CLI/TCP에 동일하게 전달되는가? |
| trigger 미발생 / capture 지연 | timeout 시작점과 실제 N,D 기반 capture 시간이 구분되는가? |
| DMA 준비/전송 실패 | 불완전 데이터를 성공 결과로 내보내지 않는가? |
| CANCEL / close / 늦은 callback 경합 | 정리가 한 번 수행되고 buffer 수명이 안전한가? |
| 복구 실패 | 새 START 거절과 재초기화 조건을 명확히 알리는가? |
| 네트워크 단절 | 서버 소유 작업·결과가 정리되고 다음 세션과 섞이지 않는가? |

FPGA 상태, 커널 상태, TCP 오류는 같은 숫자로 억지 통일하기보다 의미 대응표로 관리한다. 최초 실패 원인과 복구 결과를 따로 기록한다.

## 7. liblogic은 무엇인가

**liblogic은 이 프로젝트에서 만들 공통 라이브러리의 이름이다.** 이미 설치되어 있는 특정 외부 제품이나 단일 필수 파일을 뜻하지 않는다. 여러 C 소스와 헤더를 묶은 모듈이며, 빌드 방식에 따라 liblogic.a(정적) 또는 liblogic.so(공유) 같은 파일이 될 수 있다. 어느 방식인지는 SCRUM-41에서 결정한다.

- **Driver:** 커널에서 실제 FPGA/DMA/버퍼를 관리한다.
- **liblogic:** 사용자 프로그램에서 장치를 여는 방법, ioctl 호출, 대기, 부분 read, 오류 전달, 취소/해제 절차를 공통 함수로 제공한다.
- **Diagnostic CLI:** 사람의 명령행 입력을 받아 liblogic을 호출하고 결과를 출력한다.
- **TCP Server:** PC 요청을 받아 같은 liblogic을 호출하고 결과를 TCP frame으로 변환한다.
- **Qt:** TCP나 저장 fixture로 받은 데이터를 표시·분석한다. KR260의 Linux 장치 파일을 PC에서 직접 여는 구조가 아니다.

CLI와 TCP 서버에 각각 “설정→수집→기다림→읽기→정리” 코드를 복사하면 한쪽만 수정되어 오류 의미가 달라지기 쉽다. liblogic은 이 공통 처리를 한곳에서 유지하게 한다. 하드웨어의 실제 상태와 소유권은 여전히 커널이 판단하며 liblogic이 별도의 권위 있는 하드웨어 상태머신을 만들어서는 안 된다.

### 7.1 파일/모듈 구조 예시 — 아직 생성된 소스가 아님

```text
include/logiccap_uapi.h                 커널·사용자 공통 ABI
linux/driver/
  logiccap_core.c                       장치·상태·소유권 통합
  logiccap_regs.c                       IP 제어
  logiccap_dma.c                        DMA·버퍼·복구
software/liblogic/
  include/logic.h                       CLI/서버가 include할 공개 API
  src/logic.c                          공통 API·인수/수명 처리
  src/backend.h                        내부 backend 계약
  src/backend_linux.c                  open/ioctl/poll/read 연결
  src/backend_mock.c                   fixture와 오류 시나리오
  tests/                               backend 의미 일치 검증
  CMakeLists.txt                       빌드 방식 후보
software/logicdiag/                     CLI 프로그램
software/logicserver/                   TCP 서버 프로그램
pc/qt/                                 수신·CaptureData·파형·decoder
tests/fixtures/                         raw + metadata + expected
```

위 파일명과 분리는 설명용 제안이다. 실제 파일 목록·함수명·빌드 방식은 팀이 결정하며 이번 작업에서 구현 코드를 만들었다는 뜻이 아니다.

### 7.2 호출 예시 — 함수명은 후보

```text
CLI: 사용자 capture 명령 ─┐
                         ├→ logic_config → logic_start → logic_wait
TCP: PC START/FETCH 요청 ─┘                          ↓
                              logic_result / logic_read → logic_release
실제 장치: backend_linux → /dev/logiccap0 → 커널
보드 없는 시험: backend_mock → 고정 fixture / 오류 시나리오
```

서버는 기다림 때문에 STATUS/CANCEL 수신이 막히지 않도록 비동기 구조를 결정해야 한다. 위 예시는 순서를 설명하며 모든 호출을 네트워크 thread에서 동기 실행하라는 지시가 아니다.

Mock은 실제 DMA를 흉내 내는 하드웨어 드라이버가 아니라, 같은 설정·결과·오류 의미를 반환하는 시험용 연결부다. PC에서 CLI/서버·Qt 흐름을 먼저 검증할 수 있지만 DMA·전압·timing·IRQ 검증을 대신하지 않는다. SCRUM-41 완료에는 Mock 시험과 Linux backend 실장치 시험을 구분해 남긴다.

## 8. TCP·파일·Qt·decoder 계약

SYS-06의 이전 제안은 16-byte header(magic/version/type/payload_length/request_id), big endian 정수, UTF-8 JSON 제어 payload, raw sample DATA다. magic LKLA·port 5000·type 값·DATA prefix의 정확한 layout은 v0.1 참조본의 후보이며 SYS-06의 결정 기록을 통해 고정한다.

구현 전 결정할 내용:

1. header/body의 부분 수신·여러 frame 병합·partial send·느린 수신을 어떤 buffer/parser로 처리하는가?
2. payload 최대 길이와 type/version 검증을 메모리 할당 전에 어떻게 수행하는가?
3. request_id(요청 대응)와 capture_id(수집 결과)를 어떻게 구별하고 FETCH metadata/DATA를 대조하는가?
4. 단절·재접속·중복 요청·stale ID에서 결과가 섞이지 않도록 어떤 규칙을 쓰는가?
5. 원시 파일·metadata·expected decode를 어떻게 버전 묶음으로 관리하는가?

공통 fixture에는 raw bytes, sample_count/payload_bytes, channel_count/encoding, 실제 clock/div, trigger 기준, 입력 source, 프로토콜 설정, 기대 결과, 생성 출처(mock/실측), 버전이 필요하다. 정확한 필수/선택 schema는 SYS-06/07에서 고정한다.

Qt는 수신, CaptureData, 파형, decoder를 분리한다. 채널 숨김이나 zoom이 원시 byte를 변경하면 안 된다. decoder는 CaptureData와 설정을 입력받아 socket/driver 없이 fixture로 검증할 수 있어야 한다.

UART의 baud/data/parity/stop/idle, I2C의 주소·START/STOP/repeated START·ACK/NACK, SPI의 mode/bit order/bits-per-word/CS 지원 범위를 별도로 결정한다. 잘린 frame과 sampling 부족은 정상 byte와 구분한다. 결과 index 범위·끝점 포함 여부·오류 위치를 SYS-07에서 일치시킨다.

## 9. 검증 추적표

설계 Task의 완료는 계약·예제·검토 증빙이다. 구현 Task의 완료는 그 계약에 맞는 코드·시험 결과다. mock 통과와 실보드 통과를 별도 열로 기록한다.

| 시험 | 확인 내용 | 주요 구현/실행 Task |
|---|---|---|
| IF-01 | IP ID/ABI/clock/capacity | 39, 16, 40 |
| IF-02 | AXI-Lite 독립 채널·WSTRB·stall | 39 |
| IF-03 | D 간격·정확한 N개 | 13, 14 |
| IF-04 | rising/falling·첫 저장 sample | 14 |
| IF-05 | counter8 전체 bytes·경계 N | 14, 15, 17, 20 |
| IF-06 | AXIS stall·TLAST·누락/중복 | 15 |
| IF-07 | DMA 길이·DDR byte 순서 | 17 |
| IF-08 | 잘못된 설정·상태·ID | 39, 40, 41, 19 |
| IF-09 | timeout·CANCEL·부분 결과 차단 | 14, 18, 40, 41 |
| IF-10 | DMA fault·늦은 callback·복구 | 18, 40 |
| IF-11 | 100회 반복·traceable log | 20, 21 |
| IF-12 | TCP 분할·병합 | 22, 23 |
| IF-13 | 단절·stale ID·길이 오류 | 22, 23, 41 |
| IF-14 | fixture/mock/실측의 파형·시간·decode | 23, 24 |
| IF-15 | STM32 송신값↔decode | 25, 24, 26 |

SCRUM-26이 전체 결과를 모으고 SCRUM-27이 최종 Demo와 버전 묶음을 만든다. 단위 시험은 mock/RTL에서 먼저 진행할 수 있지만 실제 경로의 성능·복구 주장은 실제 측정 증빙을 요구한다.

시험 기록 최소 형식: 시험 ID / 계약 버전 / 보드·kernel·bitstream·app 버전 / fixture / 입력 설정 / 실행 절차 / 기대값 / 실제값 / PASS·FAIL·미실행 / 로그 경로 / 실행자 / 재시험 이슈.

성능은 sampling rate, capture 시간, DMA 전송률, TCP 전송률, UI 지연을 분리한다. 시작·끝 이벤트와 bytes 단위를 기록하고 미측정값은 null/미측정으로 표시한다. IRQ 횟수와 DMA callback 횟수를 같은 수치로 표기하지 않는다.

## 10. Issue link 운영법

이번에 추가한 47개 관계는 모두 A blocks B 방향이다. A의 산출물이 있어야 B의 최종 통합/완료를 검증할 수 있다는 뜻이다. B에서 보면 A는 is blocked by로 표시된다. 같은 관계를 두 번 생성하지 않는다.

대표 연결:

- SYS-01~08 → SCRUM-5: 개별 계약 검토가 종합 승인에 필요하다.
- SCRUM-33 → SCRUM-39 → SCRUM-16: register 계약→RTL→보드 MMIO 검증.
- SCRUM-17 → SCRUM-18 → SCRUM-40 → SCRUM-41: DMA 정상→복구→장치 API→공통 API 실장치 검증.
- SCRUM-41 → SCRUM-19 및 SCRUM-22: CLI와 TCP의 공통 API 의존.
- SCRUM-21/22/23/24/25/38/5 → SCRUM-26 → SCRUM-27: 통합 증빙과 Demo.
- SCRUM-21 및 SCRUM-28 → SCRUM-29: 로그·n8n이 Webhook 연동의 선행 조건.

의존 관계는 자동으로 상태를 바꾸거나 작업 시작을 금지하는 기능을 설정한 것이 아니다. mock/단위 작업은 합의한 계약으로 병렬 진행할 수 있다. 팀은 최종 완료 시 선행 증빙을 확인한다.

링크 추가 방법: 이슈의 연결된 업무/이슈 링크 영역에서 연결 기능을 열고, 선행 이슈 A에서 관계 blocks와 후행 이슈 B를 선택한다. B에서 시작한다면 is blocked by와 A를 선택한다. 사이트 언어에 따라 차단 관련 한글 명칭으로 보일 수 있다. 저장 후 양쪽 이슈에서 방향을 확인한다. Epic 소속은 Parent로 관리하며 Blocks로 대체하지 않는다.

이번 관계는 순환이 없음을 조회 후 검사했다. 상세 목록과 각각의 이유는 [변경 전후 보고서](jira-change-report-v0.2.md)에 있다.

## 11. 미결정 항목과 v1 승인 절차

| 결정 항목 | 관리 위치 | 필요한 답/근거 |
|---|---|---|
| 실제 핀·전기·clock/reset | SYS-02 | 보드·회로도·XDC·timing 검토 |
| 최종 register/trigger/길이 | SYS-03 | register 표·cycle 예·RTL 검증 |
| DMA provider·모드·수명·복구 | SYS-04 | 실제 커널 구성·DT·fault 결과 |
| ioctl/layout/ABI/오류 | SYS-05 | 공통 헤더·layout 검사·호출 예 |
| TCP/로그/파일 schema | SYS-06 | 상호 파싱 fixture·오류 예 |
| protocol 지원/expected | SYS-07 | STM32 설정·raw·expected |
| 개인 담당·목표 Sprint | 각 Task | 팀의 할당/일정 결정 |
| 최종 기준선·변경 영향 | SCRUM-5 | 버전 목록·리뷰·승인/보류 |

기록 양식: 질문 ID / 결정 또는 미결정 / 선택 이유 / 담당 / 검토자 / 목표 Sprint / 근거 / 영향 Task / 검증 ID.

v0.2 작성 자체를 SYS 완료 또는 v1 승인으로 처리하지 않았다. 새로운 결정을 내리면 Jira 해당 SYS/Task와 연결된 명세·헤더·fixture를 함께 갱신하고, ABI/TCP/fixture 호환 영향 및 재검증 범위를 SCRUM-5에 기록한다.

## 12. 이번 변경의 범위와 기록

기존 Task 20개와 Epic 7개의 Description을 보완하고 Task 3개를 추가했다. SYS 8개의 Description과 기존 계층·제목·담당·상태를 유지했다. SCRUM-8의 잘못된 Zybo Z7-20 표기는 KR260으로 정정했다. 비밀번호 관련 내용은 수정하지 않았다.

이번 산출물은 Jira 작업 정의와 Markdown 문서다. RTL·커널·라이브러리·Qt 코드를 구현하거나 IF 시험을 실행한 결과가 아니다.

- [변경 전후 보고서](jira-change-report-v0.2.md): 이슈별 변경 전/후 전문, 새 Task, 의존 관계 이유.
- [변경 전 스냅샷](jira-before-2026-11-03.json)
- [변경 후 스냅샷](jira-after-2026-11-03.json)
- [v0.1 기술 참조본](system-interface-design-v0.1-reference.md)

