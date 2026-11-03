# SCRUM Jira 변경 전후 보고서 v0.2

작성일: 2026-11-03 (Asia/Seoul)  
대상: [SCRUM 프로젝트](https://packetkimjunpyo.atlassian.net/jira/software/projects/SCRUM/boards/1)

## 1. 실제 반영 결과

| 항목 | 변경 전 | 변경 후 |
|---|---|---|
| 전체 이슈 | 35 | 38 |
| Epic | 7 | 7, 기존 계층 유지 |
| 기존 일반 Task | 28 | 28 유지, 비-SYS 20개 상세화 |
| 추가 Task | 없음 | 39·40·41, 총 3개 |
| SYS Description | 8개 상세 계약 | 원문 유지 |
| Epic Description | 짧은 범위 설명 | 7개 모두 범위·소속 작업·질문·완료 조건 보강 |
| 이슈 간 의존 관계 | 0 | Blocks 47개, 순환 없음 |
| SCRUM-8 보드명 | Zybo Z7-20 | KR260 |
| 명세의 SYS 계층 | SCRUM-5 하위 작업이라는 구버전 설명 | SCRUM-30 아래 독립 Task, SCRUM-5는 종합 승인 |
| 담당·상태·제목·기존 Parent | 기존 값 | 변경 없음 |

비밀번호 관련 내용은 수정하지 않았다. 새 Task의 담당자·Sprint·기한은 임의 확정하지 않았다. 이번 작업에서는 Jira 상태 전환이나 팀원에게 댓글/메시지 전송을 하지 않았다.

## 2. 왜 Task를 추가했는가

| 추가 이슈 | Parent | 발견한 누락 | 기존 작업과 경계 |
|---|---|---|---|
| [SCRUM-39](https://packetkimjunpyo.atlassian.net/browse/SCRUM-39) AXI4-Lite 레지스터·명령·진단 조회 RTL 구현 | SCRUM-8 | SYS-03 설계는 있으나 register slave 구현 책임이 없었음 | 13=입력/tick, 14=trigger/BRAM, 15=stream, 39=register/명령/IRQ |
| [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) logiccap 커널 장치 API·상태·소유권 통합 구현 | SCRUM-9 | DMA 구현과 사용자 UAPI 사이의 장치 등록·상태·read/poll·소유권 구현이 명시되지 않았음 | 17=DMA 정상, 18=DMA 복구, 40=사용자 장치 및 통합 |
| [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) liblogic 공통 Device API 및 Mock Backend 구현 | SCRUM-10 | SYS에 공통 API가 있으나 실제 라이브러리·mock 구현 Task가 없었음 | 19=CLI, 22=TCP server, 41=두 프로그램이 공유하는 코드 |

Qt 수신부와 CaptureData는 SCRUM-23에, fixture 기반 decoder 검증은 SCRUM-24에, 배포·복구 재현은 SCRUM-7에 보강했다. 이미 있는 책임을 별도 Task로 중복 생성하지 않았다. UART/I2C/SPI는 기존 통합 Task를 유지하고 프로토콜별 검증 증빙을 요구하도록 했다.

## 3. Description 작성 원칙

기존 일반 Task의 짧은 설명은 “기존 작업 범위 (보존)” 아래에 그대로 남겼다. 이후 목적, 구현 전에 팀이 결정할 질문, 산출물, 체크 가능한 완료 조건, 관련 계약/IF 시험, 결정 기록 방법을 추가했다.

예를 들어 SCRUM-22는 “분할 수신, 종료, 재접속 처리”라는 한 문장에서 다음 질문으로 구체화됐다: header/body가 나뉘거나 합쳐지면 어떻게 파싱하는가? request_id와 capture_id는 어떻게 구분하는가? 느린 송신 중에도 CANCEL이 가능한가? 단절 시 누구의 결과를 언제 정리하는가? 완료는 golden fixture와 분할·병합·단절 시험 증빙으로 판단한다.

질문에 대한 최종 답을 임의로 정하지 않았다. SYS의 기존 계약/검토안과 일치하도록 질문을 세웠으며, 결정값·이유·담당·검토자·기한·근거를 팀이 남기도록 했다.

## 4. 의존 관계와 이유

표의 방향은 **선행 A blocks 후행 B**다. 후행 B에서는 **is blocked by A**로 보인다. 두 표시는 하나의 링크다. 링크는 후행의 최종 통합/완료에 선행 산출물이 필요함을 기록한다. 확정된 계약을 사용하는 mock·단위 개발까지 금지하는 의미는 아니다.

| 선행 A | 후행 B | 연결 이유 |
|---|---|---|
| [SCRUM-4](https://packetkimjunpyo.atlassian.net/browse/SCRUM-4) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-32](https://packetkimjunpyo.atlassian.net/browse/SCRUM-32) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-33](https://packetkimjunpyo.atlassian.net/browse/SCRUM-33) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-34](https://packetkimjunpyo.atlassian.net/browse/SCRUM-34) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-35](https://packetkimjunpyo.atlassian.net/browse/SCRUM-35) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-37](https://packetkimjunpyo.atlassian.net/browse/SCRUM-37) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-38](https://packetkimjunpyo.atlassian.net/browse/SCRUM-38) | [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | SYS 계약 검토가 종합 승인에 필요 |
| [SCRUM-32](https://packetkimjunpyo.atlassian.net/browse/SCRUM-32) | [SCRUM-13](https://packetkimjunpyo.atlassian.net/browse/SCRUM-13) | 핀·클록·reset 계약 |
| [SCRUM-33](https://packetkimjunpyo.atlassian.net/browse/SCRUM-33) | [SCRUM-13](https://packetkimjunpyo.atlassian.net/browse/SCRUM-13) | 분주·설정 범위 |
| [SCRUM-13](https://packetkimjunpyo.atlassian.net/browse/SCRUM-13) | [SCRUM-14](https://packetkimjunpyo.atlassian.net/browse/SCRUM-14) | 동기화된 샘플과 tick |
| [SCRUM-33](https://packetkimjunpyo.atlassian.net/browse/SCRUM-33) | [SCRUM-14](https://packetkimjunpyo.atlassian.net/browse/SCRUM-14) | trigger·BRAM 상태 |
| [SCRUM-14](https://packetkimjunpyo.atlassian.net/browse/SCRUM-14) | [SCRUM-15](https://packetkimjunpyo.atlassian.net/browse/SCRUM-15) | 고정된 BRAM 결과 |
| [SCRUM-34](https://packetkimjunpyo.atlassian.net/browse/SCRUM-34) | [SCRUM-15](https://packetkimjunpyo.atlassian.net/browse/SCRUM-15) | AXIS packing·handshake |
| [SCRUM-33](https://packetkimjunpyo.atlassian.net/browse/SCRUM-33) | [SCRUM-39](https://packetkimjunpyo.atlassian.net/browse/SCRUM-39) | 레지스터 계약 |
| [SCRUM-7](https://packetkimjunpyo.atlassian.net/browse/SCRUM-7) | [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) | 재현 가능한 빌드·부팅 환경 |
| [SCRUM-32](https://packetkimjunpyo.atlassian.net/browse/SCRUM-32) | [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) | 클록·reset·배선 |
| [SCRUM-39](https://packetkimjunpyo.atlassian.net/browse/SCRUM-39) | [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) | 실제 MMIO 레지스터 검증 |
| [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) | [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) | PS/PL·DT·DMA 경로 |
| [SCRUM-34](https://packetkimjunpyo.atlassian.net/browse/SCRUM-34) | [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) | DMA provider·버퍼 계약 |
| [SCRUM-15](https://packetkimjunpyo.atlassian.net/browse/SCRUM-15) | [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) | 실제 stream 송신 |
| [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) | [SCRUM-18](https://packetkimjunpyo.atlassian.net/browse/SCRUM-18) | 정상 DMA 경로 |
| [SCRUM-35](https://packetkimjunpyo.atlassian.net/browse/SCRUM-35) | [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) | UAPI ABI·상태·소유권 계약 |
| [SCRUM-18](https://packetkimjunpyo.atlassian.net/browse/SCRUM-18) | [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) | DMA 취소·복구 통합 |
| [SCRUM-35](https://packetkimjunpyo.atlassian.net/browse/SCRUM-35) | [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) | 공통 장치 연산 의미 |
| [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) | [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) | CLI/TCP·fixture 의미 |
| [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) | [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) | Linux backend 실장치 검증 |
| [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) | [SCRUM-19](https://packetkimjunpyo.atlassian.net/browse/SCRUM-19) | CLI 공통 API |
| [SCRUM-19](https://packetkimjunpyo.atlassian.net/browse/SCRUM-19) | [SCRUM-20](https://packetkimjunpyo.atlassian.net/browse/SCRUM-20) | 수집 결과·오류 제공 |
| [SCRUM-20](https://packetkimjunpyo.atlassian.net/browse/SCRUM-20) | [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) | 검증 결과 집계 |
| [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) | [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) | 로그 schema |
| [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) | [SCRUM-22](https://packetkimjunpyo.atlassian.net/browse/SCRUM-22) | 서버 공통 API |
| [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) | [SCRUM-22](https://packetkimjunpyo.atlassian.net/browse/SCRUM-22) | TCP framing 계약 |
| [SCRUM-36](https://packetkimjunpyo.atlassian.net/browse/SCRUM-36) | [SCRUM-23](https://packetkimjunpyo.atlassian.net/browse/SCRUM-23) | 수신·파일·metadata 형식 |
| [SCRUM-37](https://packetkimjunpyo.atlassian.net/browse/SCRUM-37) | [SCRUM-24](https://packetkimjunpyo.atlassian.net/browse/SCRUM-24) | protocol golden fixture |
| [SCRUM-32](https://packetkimjunpyo.atlassian.net/browse/SCRUM-32) | [SCRUM-25](https://packetkimjunpyo.atlassian.net/browse/SCRUM-25) | 실제 배선·전기 조건 |
| [SCRUM-37](https://packetkimjunpyo.atlassian.net/browse/SCRUM-37) | [SCRUM-25](https://packetkimjunpyo.atlassian.net/browse/SCRUM-25) | STM32 송신 fixture |
| [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | 반복·데이터 정확성 증빙 |
| [SCRUM-22](https://packetkimjunpyo.atlassian.net/browse/SCRUM-22) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | 보드 TCP 경로 |
| [SCRUM-23](https://packetkimjunpyo.atlassian.net/browse/SCRUM-23) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | Qt 수신·표시 |
| [SCRUM-24](https://packetkimjunpyo.atlassian.net/browse/SCRUM-24) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | decoder 정확성 |
| [SCRUM-25](https://packetkimjunpyo.atlassian.net/browse/SCRUM-25) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | 실제 시험 신호 |
| [SCRUM-38](https://packetkimjunpyo.atlassian.net/browse/SCRUM-38) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | 통합 시험 기준 |
| [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) | [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | 승인된 인터페이스 기준선 |
| [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) | [SCRUM-27](https://packetkimjunpyo.atlassian.net/browse/SCRUM-27) | 최종 통합·성능 결과 |
| [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) | [SCRUM-29](https://packetkimjunpyo.atlassian.net/browse/SCRUM-29) | 구조화 원본 시험결과 |
| [SCRUM-28](https://packetkimjunpyo.atlassian.net/browse/SCRUM-28) | [SCRUM-29](https://packetkimjunpyo.atlassian.net/browse/SCRUM-29) | n8n 실행·수신 환경 |

제품 통합 SCRUM-26/27을 운영 자동화 SCRUM-28/29의 완료에 종속시키지 않았다. 전체 승인 SCRUM-5를 모든 개발 착수의 선행 조건으로 걸지 않았고, 최종 통합 기준선 확인에 사용했다.

이슈 링크를 활용하면 어떤 산출물이 아직 필요한지, 변경이 어느 후행 작업에 영향을 주는지, 무엇을 먼저 합의해야 하는지 확인할 수 있다. 자동으로 완료 상태를 바꾸는 규칙은 설정하지 않았다.

수동 추가 방법: 선행 이슈를 열고 연결된 업무/이슈 링크의 연결 기능에서 blocks와 후행 이슈 키를 선택한다. 후행에서 추가할 때는 is blocked by와 선행 키를 선택한다. 저장 후 양쪽 표시 방향을 확인한다. Epic 소속은 Parent 필드이며 이 링크와 별개다.

## 5. 수정한 이슈별 변경 전후 전문

아래 변경 후는 실제 Jira를 다시 읽은 내용이다. Jira 변환 과정에서 Markdown 목록 기호·이스케이프 표기가 바뀔 수 있으나 문장·숫자 내용은 작성본과 대조했다.

### [SCRUM-5](https://packetkimjunpyo.atlassian.net/browse/SCRUM-5) 인터페이스 명세 v1 리뷰 및 최종 확정

#### 변경 전

전체 블록도, 레지스터 맵 초안, 샘플 데이터 형식, TCP 메시지 형식, 모듈별 역할을 문서로 정리하고 팀 검토를 받는다.

#### 변경 후

## 기존 작업 범위 (보존)

전체 블록도, 레지스터 맵 초안, 샘플 데이터 형식, TCP 메시지 형식, 모듈별 역할을 문서로 정리하고 팀 검토를 받는다.

## 목적

SYS 계약을 종합 검토하여 구현 기준선과 변경 절차를 남긴다.

## 구현 전에 팀이 결정할 질문

1. SYS-01\~08 사이에 샘플 길이·상태·취소·소유권이 충돌하는가?
2. 어떤 문서/헤더/fixture 버전을 v1으로 승인할 것인가?
3. 미확정 항목 중 실제 구현을 막는 것은 무엇이며 누가 언제 확정하는가?
4. 변경 시 FPGA ABI·UAPI·TCP·fixture 영향을 누가 검토하는가?

## 산출물

* 계약별 리뷰표와 버전 목록
* 미결정 항목·담당·목표 Sprint·영향 작업 목록
* 승인/보류 근거와 변경 기록

## 완료 조건

- [ ] SYS-01\~08 각각에 검토 결과와 근거 링크가 있다.
- [ ] 레지스터/AXIS/UAPI/TCP/fixture 간 길이·상태·오류 대응을 교차 확인했다.
- [ ] 막히는 항목을 해결하거나 해당 구현을 보류한 범위를 명시했다.
- [ ] 회의 개최만으로 완료하지 않고 검토자가 기준선 버전을 확인했다.

## 관련 계약·검증

SCRUM-4, SCRUM-32\~38

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-6](https://packetkimjunpyo.atlassian.net/browse/SCRUM-6) 프로젝트 핵심 기술 선수학습 및 발표

#### 변경 전

FPGA 수집·트리거, MMIO·DMA, TCP·Qt의 역할과 데이터 흐름을 정리하고 담당 영역의 학습 결과를 발표한다.

#### 변경 후

## 기존 작업 범위 (보존)

FPGA 수집·트리거, MMIO·DMA, TCP·Qt의 역할과 데이터 흐름을 정리하고 담당 영역의 학습 결과를 발표한다.

## 목적

개인 학습을 인터페이스 이해와 재현 가능한 작은 실습으로 연결한다.

## 구현 전에 팀이 결정할 질문

1. 각 담당자가 직접 구현할 영역과 읽고 설명할 영역은 어디까지인가?
2. MMIO 제어와 DMA 데이터 이동, 커널 UAPI와 liblogic의 차이를 설명할 수 있는가?
3. TCP 스트림의 분할·병합과 Qt UI 비동기를 어떤 실습으로 확인할 것인가?
4. 모르는 항목을 어떤 SYS 질문과 구현 Task에 연결할 것인가?

## 산출물

* 담당별 학습표·발표자료
* 최소 실습 코드/실행법/결과
* 질문·후속 학습 목록

## 완료 조건

- [ ] 각 담당자가 자기 모듈의 입력·출력·오류를 설명했다.
- [ ] 작은 실습 하나 이상을 다른 팀원이 재현했다.
- [ ] 남은 질문을 담당·기한과 함께 해당 Jira에 연결했다.

## 관련 계약·검증

SCRUM-4

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-7](https://packetkimjunpyo.atlassian.net/browse/SCRUM-7) 개발 환경구성

#### 변경 전

개발보드, pc 환경 구성

#### 변경 후

## 기존 작업 범위 (보존)

개발보드, pc 환경 구성

## 목적

팀원이 동일한 개발·부팅·빌드 환경을 재현할 수 있게 한다.

## 구현 전에 팀이 결정할 질문

1. Vivado/보드파일/Linux 이미지/커널/컴파일러/Qt 버전을 어떤 조합으로 고정할 것인가?
2. KR260 부팅·bitstream·DT·드라이버 배포와 이전 버전 복구 절차는 무엇인가?
3. 보드 프로그램과 PC 프로그램의 빌드 대상을 어떻게 구분하는가?
4. 저장소 디렉터리·빌드 명령·장치 접근 확인 방법은 무엇인가?
5. 보드 없이 실행할 mock 환경은 무엇인가?

## 산출물

* 버전·환경표
* 설치/빌드/부팅/배포/복구 안내
* 최소 실행 결과

## 완료 조건

- [ ] 다른 팀원이 문서만으로 최소 빌드와 실행을 재현했다.
- [ ] 실제 커널과 DMA provider 확인 결과 또는 미결정 담당·기한이 있다.
- [ ] 배포 실패 시 이전 검증 버전으로 복구하는 절차를 확인했다.

## 관련 계약·검증

SCRUM-32, SCRUM-34

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-8](https://packetkimjunpyo.atlassian.net/browse/SCRUM-8) FPGA 수집 및 트리거

#### 변경 전

Zybo Z7-20에서 디지털 신호를 수집한다. 입력 동기화, 샘플링 설정, 트리거, BRAM 버퍼, AXI4-Stream 출력을 구현하고 RTL 시험으로 검증한다.

#### 변경 후

## 목적·범위

KR260에서 외부 8채널 신호를 수집한다. 입력 동기화, 샘플링 설정, 트리거, BRAM 버퍼, AXI4-Stream 출력을 구현하고 RTL 및 실제 보드 시험으로 검증한다.

## 소속 작업

SCRUM-13, SCRUM-14, SCRUM-15, SCRUM-39

## 팀이 결정할 질문

* 목표 clock/BRAM 용량과 실제 합성·타이밍 결과는 일치하는가?
* 샘플링·trigger·register·stream 경계를 어떤 공통 fixture로 검증하는가?

## 완료 조건

- [ ] SYS-02\~04 계약과 RTL/보드 결과를 대조하고 IF-01\~06, IF-08의 해당 증빙을 연결한다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-9](https://packetkimjunpyo.atlassian.net/browse/SCRUM-9) Linux 및 AXI DMA

#### 변경 전

Zynq PS/PL 연결과 Linux 실행 환경을 구성한다. MMIO 레지스터 제어, AXI DMA 수신, 인터럽트 및 오류 처리를 구현한다.

#### 변경 후

## 목적·범위

Zynq PS/PL 연결과 Linux 실행 환경을 구성한다. MMIO 레지스터 제어, AXI DMA 수신, 인터럽트 및 오류 처리를 구현한다.

## 소속 작업

SCRUM-16, SCRUM-17, SCRUM-18, SCRUM-40

## 팀이 결정할 질문

* MMIO·DMA provider·사용자 장치의 소유권은 명확한가?
* 정상 완료와 timeout/cancel/close 정리는 어느 모듈이 책임지는가?

## 완료 조건

- [ ] DT·DMA·UAPI 통합 결과와 IF-01, IF-07\~10 증빙을 연결한다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-10](https://packetkimjunpyo.atlassian.net/browse/SCRUM-10) Diagnostic Console

#### 변경 전

레지스터와 수집 상태를 확인하는 진단 도구를 구현한다. 기준 패턴 비교, 반복 시험, 시험 결과 저장을 지원한다.

#### 변경 후

## 목적·범위

레지스터와 수집 상태를 확인하는 진단 도구를 구현한다. 기준 패턴 비교, 반복 시험, 시험 결과 저장을 지원한다.

## 소속 작업

SCRUM-19, SCRUM-20, SCRUM-21, SCRUM-41

## 팀이 결정할 질문

* CLI와 서버가 공유할 liblogic API는 어디까지인가?
* 패턴 비교·반복 로그를 어떤 fixture와 schema로 재현하는가?

## 완료 조건

- [ ] 공통 API 기반 명령·비교·반복 실행을 검증하고 IF-05, IF-08\~11 증빙을 연결한다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-11](https://packetkimjunpyo.atlassian.net/browse/SCRUM-11) TCP 및 Qt 분석기

#### 변경 전

보드와 PC 사이의 TCP 통신을 구현한다. Qt에서 파형을 표시하고 UART, I2C, SPI 데이터를 분석한다.

#### 변경 후

## 목적·범위

보드와 PC 사이의 TCP 통신을 구현한다. Qt에서 파형을 표시하고 UART, I2C, SPI 데이터를 분석한다.

## 소속 작업

SCRUM-22, SCRUM-23, SCRUM-24

## 팀이 결정할 질문

* TCP 수신·CaptureData·UI·decoder를 어떻게 분리하는가?
* UART/I2C/SPI별 지원 범위와 완료 증빙은 무엇인가?

## 완료 조건

- [ ] 분할/병합/단절과 파형·시간축·decoder fixture 결과를 IF-12\~15에 연결한다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-12](https://packetkimjunpyo.atlassian.net/browse/SCRUM-12) 통합 및 검증

#### 변경 전

STM32 시험 신호로 전체 경로를 검증한다. 성능과 오류를 측정하고 최종 시연 및 시험결과 자동화를 준비한다.

#### 변경 후

## 목적·범위

STM32 시험 신호로 전체 경로를 검증한다. 성능과 오류를 측정하고 최종 시연 및 시험결과 자동화를 준비한다.

## 소속 작업

SCRUM-25, SCRUM-26, SCRUM-27

## 팀이 결정할 질문

* 실제 신호와 mock 검증을 어떻게 구분하는가?
* 전체 경로 정확성·성능·최종 Demo의 합격 기준은 무엇인가?

## 완료 조건

- [ ] IF 전체 결과·실측 한계·재현 절차·최종 버전 묶음을 남긴다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-13](https://packetkimjunpyo.atlassian.net/browse/SCRUM-13) 8채널 입력 동기화 및 샘플링 설정 구현

#### 변경 전

채널 입력과 샘플링 설정을 구현하고, 알려진 입력 패턴이 설정에 맞게 수집되는지 시험한다.

#### 변경 후

## 기존 작업 범위 (보존)

채널 입력과 샘플링 설정을 구현하고, 알려진 입력 패턴이 설정에 맞게 수집되는지 시험한다.

## 목적

외부 8채널 입력을 합의된 샘플 시점과 채널 순서로 수집부에 제공한다.

## 구현 전에 팀이 결정할 질문

1. CH0\~7 핀·비트 순서와 입력 동기화 단계는 어떻게 맞출 것인가?
2. sample_div의 범위·첫 tick 시점·변경 가능 상태를 어떻게 구현할 것인가?
3. 짧은 펄스·채널 간 skew를 어떤 한계로 기록할 것인가?
4. reset/ARM/설정 변경 시 카운터와 동기화 출력은 어떻게 되는가?

## 산출물

* 입력 동기화·sample tick RTL
* 경계값/리셋 testbench와 파형
* 배선·XDC 대응표

## 완료 조건

- [ ] 합의한 D별 tick 간격과 첫 tick을 assertion/파형으로 확인했다.
- [ ] CH0\~7 walking-bit 입력에서 채널 뒤바뀜이 없다.
- [ ] 최소/최대/잘못된 분주와 reset 조건을 시험했다.
- [ ] 검출하지 못하는 펄스 조건을 문서화했다.

## 관련 계약·검증

SCRUM-32, SCRUM-33 / IF-03, IF-08

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-14](https://packetkimjunpyo.atlassian.net/browse/SCRUM-14) Edge Trigger 및 BRAM 버퍼 구현

#### 변경 전

상승·하강 에지 조건에서 수집이 시작되고 지정한 길이의 샘플이 버퍼에 저장되는지 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

상승·하강 에지 조건에서 수집이 시작되고 지정한 길이의 샘플이 버퍼에 저장되는지 확인한다.

## 목적

트리거 조건에 맞는 정확한 N개 샘플을 보관한다.

## 구현 전에 팀이 결정할 질문

1. ARM 직후 baseline과 첫 유효 edge를 어떻게 구분하는가?
2. trigger sample을 어느 index에 저장하며 경계에서 한 개가 빠지지 않는가?
3. BRAM 깊이·읽기 지연·저장/조회/전송 포트 소유권은 어떻게 정하는가?
4. counter8 초기화·증가 시점은 언제인가?
5. 대기 중 CANCEL, 캡처 중 ABORT, 결과 보관 중 새 START는 어떻게 처리하는가?

## 산출물

* trigger/capture/BRAM RTL
* immediate/rising/falling timing 예제
* counter8 및 취소 testbench

## 완료 조건

- [ ] 각 trigger에서 첫 샘플·마지막 샘플·총 N개가 기대값과 일치한다.
- [ ] counter8 경계 길이에서 모든 바이트를 비교했다.
- [ ] 결과 유지 중 덮어쓰기가 없고 잘못된 상태 명령 결과가 계약과 일치한다.
- [ ] 트리거 미발생과 취소 경로를 재현했다.

## 관련 계약·검증

SCRUM-13, SCRUM-33 / IF-03\~05, IF-09

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-15](https://packetkimjunpyo.atlassian.net/browse/SCRUM-15) AXI4-Stream 출력 및 RTL 검증

#### 변경 전

수집 데이터를 AXI4-Stream으로 출력하고, 전송 대기 상황에서도 데이터 순서와 개수가 유지되는지 Testbench로 검증한다.

#### 변경 후

## 기존 작업 범위 (보존)

수집 데이터를 AXI4-Stream으로 출력하고, 전송 대기 상황에서도 데이터 순서와 개수가 유지되는지 Testbench로 검증한다.

## 목적

BRAM 샘플을 손실 없이 AXIS 패킷으로 전송한다.

## 구현 전에 팀이 결정할 질문

1. BRAM 지연을 staging/FIFO로 어떻게 흡수하는가?
2. sample byte를 TDATA에 어떤 순서로 넣고 TKEEP/TLAST는 언제 유효한가?
3. TREADY가 오래 내려가거나 마지막 beat에서 멈추면 무엇을 유지하는가?
4. 전송 카운터와 STREAM_DONE은 어느 handshake에서 갱신하는가?
5. reset/취소 중 source stream 정리는 DMA 측과 어떻게 맞추는가?

## 산출물

* stream RTL·scoreboard
* stall/마지막 beat/reset 시험
* packing fixture와 전송 카운터 결과

## 완료 조건

- [ ] 무작위 stall에서 N bytes 전체가 중복·누락 없이 일치한다.
- [ ] stall 동안 TDATA/TKEEP/TLAST가 안정적이고 TLAST가 한 번 수락된다.
- [ ] N 최소/대표/최대 조건을 확인했다.
- [ ] DMA 복구와 source reset 경계를 문서와 일치시켰다.

## 관련 계약·검증

SCRUM-14, SCRUM-34 / IF-06, IF-07

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-16](https://packetkimjunpyo.atlassian.net/browse/SCRUM-16) PS/PL 연결 및 MMIO 접근 환경 구성

#### 변경 전

하드웨어 연결과 Device Tree를 구성하고, Linux에서 식별·설정 레지스터를 읽고 쓸 수 있는지 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

하드웨어 연결과 Device Tree를 구성하고, Linux에서 식별·설정 레지스터를 읽고 쓸 수 있는지 확인한다.

## 목적

KR260 PS/PL·주소·IRQ·DT가 일치하는 재현 가능한 시스템을 구성한다.

## 구현 전에 팀이 결정할 질문

1. AXI-Lite base/범위와 DMA DDR 접근 경로를 어떻게 배치하는가?
2. 클록·reset·IRQ 번호/극성과 DT binding은 실제 커널에 맞는가?
3. MMIO 자원은 어느 드라이버가 단독 소유하는가?
4. IP ID/ABI/clock/capacity 불일치와 probe 실패를 어떻게 드러내는가?

## 산출물

* Vivado BD/Tcl/XDC와 주소표
* Device Tree/overlay·배포법
* probe·ID 조회 로그

## 완료 조건

- [ ] 주소/IRQ/clock/reset을 Vivado와 DT에서 대조했다.
- [ ] Linux에서 실제 IP 식별·capability를 읽고 예상값과 비교했다.
- [ ] 자원 충돌과 probe 실패가 진단 가능하다.
- [ ] 생성물의 소스·버전·재현 절차가 있다.

## 관련 계약·검증

SCRUM-7, SCRUM-32, SCRUM-33 / IF-01

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-17](https://packetkimjunpyo.atlassian.net/browse/SCRUM-17) AXI DMA 수신 경로 구현

#### 변경 전

드라이버와 수신 버퍼를 구성하고, 알려진 패턴이 지정한 길이로 수신되는지 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

드라이버와 수신 버퍼를 구성하고, 알려진 패턴이 지정한 길이로 수신되는지 확인한다.

## 목적

합의된 DMA provider를 이용해 N bytes를 DDR로 수신한다.

## 구현 전에 팀이 결정할 질문

1. 현재 커널 provider의 지원 모드·채널·주소/길이 폭은 무엇인가?
2. 버퍼 할당·mapping·CPU/DMA 소유권 전환은 어떤 API로 구현하는가?
3. prepare/submit/issue와 SEND 순서를 어떻게 보장하는가?
4. callback·residue·STREAM_DONE·길이를 어떤 조합으로 검증하는가?
5. 준비 실패·부분 수신 시 결과 공개를 어떻게 막는가?

## 산출물

* DMA 수신 구현
* provider·버퍼 수명 기록
* counter8 수신/길이/바이트 순서 로그

## 완료 조건

- [ ] N 최소/대표/최대 조건에서 수신 데이터와 길이가 일치한다.
- [ ] DMA 준비 실패 시 SEND하지 않는다.
- [ ] DMA 완료 전 CPU 결과 공개·버퍼 해제가 없다.
- [ ] 지원되지 않는 residue를 정상값으로 꾸미지 않는다.

## 관련 계약·검증

SCRUM-16, SCRUM-34 / IF-05, IF-07

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-18](https://packetkimjunpyo.atlassian.net/browse/SCRUM-18) DMA 인터럽트 및 오류 복구 구현

#### 변경 전

전송 완료, 오류, 타임아웃을 구분하고 실패 후 재수집할 수 있는지 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

전송 완료, 오류, 타임아웃을 구분하고 실패 후 재수집할 수 있는지 확인한다.

## 목적

DMA 완료와 실패를 구분하고 취소·close 이후 안전하게 재사용한다.

## 구현 전에 팀이 결정할 질문

1. IP IRQ와 DMA callback을 어떻게 별도 기록하는가?
2. trigger/capture/DMA timeout의 시작점과 경계는 무엇인가?
3. CANCEL·close·timeout·callback이 경합하면 누가 정리를 한 번 수행하는가?
4. terminate/동기화/source reset 순서가 실제 provider에서 안전한가?
5. 복구 실패 시 lockout 해제 조건은 무엇인가?

## 산출물

* 오류·복구 코드와 상태표
* fault injection 절차
* 늦은 callback/close 경합 로그

## 완료 조건

- [ ] timeout·TLAST 누락·전송 오류·늦은 callback을 각각 시험했다.
- [ ] 정리 완료 전 버퍼 해제와 다음 START가 일어나지 않는다.
- [ ] 최초 오류와 복구 결과를 별도 보존한다.
- [ ] 복구 후 새 capture 성공 또는 명확한 lockout을 증빙했다.

## 관련 계약·검증

SCRUM-17, SCRUM-34, SCRUM-35 / IF-09, IF-10

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-19](https://packetkimjunpyo.atlassian.net/browse/SCRUM-19) 레지스터 및 Capture 제어 명령 구현

#### 변경 전

Register Read/Write, Capture Start/Stop, 상태 조회 명령을 구현하고 정상·잘못된 입력을 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

Register Read/Write, Capture Start/Stop, 상태 조회 명령을 구현하고 정상·잘못된 입력을 확인한다.

## 목적

liblogic을 사용해 진단 명령과 정상/오류 메시지를 제공한다.

## 구현 전에 팀이 결정할 질문

1. info/regs/config/capture/status/cancel의 구문·기본값·exit code는 무엇인가?
2. 기존 Start/Stop 표현은 START/CANCEL/RELEASE에 어떻게 대응하는가?
3. 허용된 레지스터만 어떻게 노출하며 잘못된 입력을 어디서 거절하는가?
4. 직접 모드와 서버 원격 모드에서 장치 소유권 충돌을 어떻게 알리는가?
5. 중간 실패와 사용자 중단에서도 결과/장치 해제를 어떻게 보장하는가?

## 산출물

* CLI 명령 도움말·구현
* 정상/오류 실행 예
* liblogic 호출 대응표

## 완료 조건

- [ ] 설정→시작→대기→결과→해제 흐름을 재현했다.
- [ ] 잘못된 인수·BUSY·stale ID·취소의 exit code/메시지가 계약과 같다.
- [ ] CLI가 DMA MMIO나 별도 수집 상태머신을 만들지 않는다.
- [ ] 직접/원격 모드의 지원 범위와 미지원 명령을 명시했다.

## 관련 계약·검증

SCRUM-35, SCRUM-36 / IF-08, IF-09

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-20](https://packetkimjunpyo.atlassian.net/browse/SCRUM-20) 기준 패턴 비교 및 오류 위치 출력

#### 변경 전

기대 데이터와 수집 데이터를 비교해 PASS/FAIL, 불일치 개수, 첫 오류 위치를 출력한다.

#### 변경 후

## 기존 작업 범위 (보존)

기대 데이터와 수집 데이터를 비교해 PASS/FAIL, 불일치 개수, 첫 오류 위치를 출력한다.

## 목적

기준 패턴과 수집 결과를 바이트 단위로 비교하여 오류 위치를 찾는다.

## 구현 전에 팀이 결정할 질문

1. 기대값은 어떤 fixture/패턴 버전으로 생성하는가?
2. 길이 부족·초과와 byte mismatch를 어떻게 구분하는가?
3. 첫 오류 index·expected/actual·총 불일치를 어떤 형식으로 출력하는가?
4. 실패·취소·미완료 데이터를 비교 성공으로 오인하지 않으려면 무엇을 검사하는가?

## 산출물

* 비교 모듈·출력 예
* 정상/길이 오류/바이트 오류 fixture
* 검증 결과

## 완료 조건

- [ ] 정상 fixture는 PASS이고 인위적 한 바이트 오류는 정확한 index/value로 FAIL이다.
- [ ] 짧거나 긴 입력을 별도 길이 오류로 검출한다.
- [ ] 전체 샘플을 검사하며 일부 일치만으로 PASS하지 않는다.
- [ ] 로그와 화면의 오류 수·위치가 일치한다.

## 관련 계약·검증

SCRUM-19, SCRUM-36 / IF-05, IF-11

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-21](https://packetkimjunpyo.atlassian.net/browse/SCRUM-21) 반복 시험 및 구조화된 로그 저장

#### 변경 전

반복 횟수에 따라 시험하고 시간, 시험명, 결과, 샘플 수, 오류 수, 타임아웃을 JSON 또는 CSV로 저장한다.

#### 변경 후

## 기존 작업 범위 (보존)

반복 횟수에 따라 시험하고 시간, 시험명, 결과, 샘플 수, 오류 수, 타임아웃을 JSON 또는 CSV로 저장한다.

## 목적

반복 결과를 누락 없이 기록하고 실패 원인을 추적한다.

## 구현 전에 팀이 결정할 질문

1. 반복마다 새 capture_id와 run_id를 어떻게 연계하는가?
2. 실패 시 중단/계속 정책과 정리 성공 여부를 어떻게 기록하는가?
3. JSONL/CSV 중 표준과 필수 필드·단위·null 규칙은 무엇인가?
4. 파일 쓰기 실패·사용자 중단·재실행을 어떻게 처리하는가?
5. IRQ 횟수와 callback 횟수를 어떤 이름으로 구분하는가?

## 산출물

* 반복 실행기·구조화 로그
* 로그 스키마와 예
* 성공/실패/timeout 집계

## 완료 조건

- [ ] 합의된 반복 수(현 SYS-08 기준 100회) 각각에 결과 레코드가 있다.
- [ ] 실패를 재시도 성공으로 덮어쓰지 않고 미측정값을 구분한다.
- [ ] 총 실행 수와 PASS/FAIL/timeout/취소 집계가 일치한다.
- [ ] 파일 쓰기 실패를 성공 종료로 숨기지 않는다.

## 관련 계약·검증

SCRUM-20, SCRUM-36, SCRUM-38 / IF-11

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-22](https://packetkimjunpyo.atlassian.net/browse/SCRUM-22) TCP 서버 및 데이터 전송 형식 구현

#### 변경 전

제어 명령과 샘플 전송 형식을 정의하고 분할 수신, 연결 종료, 재접속을 처리한다.

#### 변경 후

## 기존 작업 범위 (보존)

제어 명령과 샘플 전송 형식을 정의하고 분할 수신, 연결 종료, 재접속을 처리한다.

## 목적

liblogic 제어 의미를 TCP 요청·응답과 샘플 전송에 연결한다.

## 구현 전에 팀이 결정할 질문

1. header/body 부분 수신과 여러 frame 동시 수신을 어떤 parser로 처리하는가?
2. 잘못된 magic/version/type/length를 어느 단계에서 거절하는가?
3. request_id와 capture_id를 어떻게 구분하고 FETCH metadata/DATA를 묶는가?
4. 느린 클라이언트와 partial send 중에도 STATUS/CANCEL을 어떻게 처리하는가?
5. 연결 단절·재접속·중복 요청 시 결과 소유권과 정리는 어떻게 되는가?

## 산출물

* 서버·framing parser
* 요청/응답 golden fixture
* 분할·병합·단절·느린 수신 시험

## 완료 조건

- [ ] 1바이트 단위 분할과 연속 frame을 정확히 복원한다.
- [ ] 잘못된 길이를 큰 메모리 할당 전에 거절한다.
- [ ] 수집 대기 중 STATUS/CANCEL이 처리되고 응답 ID가 일치한다.
- [ ] 단절 후 작업·결과가 정리되고 재접속에 이전 결과가 섞이지 않는다.
- [ ] FETCH 길이·capture_id·raw bytes가 metadata와 일치한다.

## 관련 계약·검증

SCRUM-35, SCRUM-36 / IF-12, IF-13

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-23](https://packetkimjunpyo.atlassian.net/browse/SCRUM-23) Qt 파형 표시 및 Cursor/Zoom 구현

#### 변경 전

수신한 채널별 파형을 표시하고 확대·축소와 커서 간 시간 측정을 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

수신한 채널별 파형을 표시하고 확대·축소와 커서 간 시간 측정을 확인한다.

## 목적

수신·저장 fixture를 같은 CaptureData로 읽어 정확한 파형과 시간을 표시한다.

## 구현 전에 팀이 결정할 질문

1. Qt 네트워크 수신·frame parsing·CaptureData·UI thread를 어떻게 분리하는가?
2. 연결/수집/취소/오류 상태를 어떤 UI로 알리는가?
3. sample index와 실제 clock/div를 시간축·cursor 차이에 어떻게 반영하는가?
4. zoom-out에서 짧은 펄스를 놓치지 않게 어떤 표시 정책을 쓸 것인가?
5. 중간 DATA·오래된 응답·metadata 불일치를 어떻게 차단하는가?

## 산출물

* Qt 수신부·CaptureData·파형/커서/zoom
* mock/파일 불러오기
* 시간축·채널 표시 검증 기록

## 완료 조건

- [ ] 동일 fixture의 byte·채널·시간축이 mock과 보드 경로에서 일치한다.
- [ ] 알려진 두 index 간 cursor 시간이 기대값과 일치한다.
- [ ] 채널 숨김/zoom이 원시 데이터나 채널 번호를 바꾸지 않는다.
- [ ] 수신·분석 중 UI가 응답하며 불완전 capture를 정상으로 표시하지 않는다.

## 관련 계약·검증

SCRUM-36, SCRUM-37 / IF-14

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-24](https://packetkimjunpyo.atlassian.net/browse/SCRUM-24) UART·I2C·SPI 프로토콜 분석 구현

#### 변경 전

각 프로토콜의 설정과 분석 결과를 표시하고 알려진 송신 데이터와 비교한다. 필요하면 프로토콜별 Task로 나눈다.

#### 변경 후

## 기존 작업 범위 (보존)

각 프로토콜의 설정과 분석 결과를 표시하고 알려진 송신 데이터와 비교한다. 필요하면 프로토콜별 Task로 나눈다.

## 목적

공통 CaptureData로 UART→I2C→SPI 분석을 단계적으로 검증한다.

## 구현 전에 팀이 결정할 질문

1. UART baud/data/parity/stop/idle 및 sampling ratio의 지원 범위는 어디까지인가?
2. I2C START/STOP/repeated START/ACK/NACK과 지원 주소 범위는 무엇인가?
3. SPI CPOL/CPHA/bit order/CS/bits-per-word 중 무엇을 지원하는가?
4. decode 결과 index 범위와 incomplete/parity/framing 오류를 어떻게 표현하는가?
5. 프로토콜별 완료를 어떻게 따로 기록하고 어떤 순서로 통합하는가?

## 산출물

* 공통 decoder 인터페이스
* UART/I2C/SPI별 구현·설정표
* 정상/경계 잘림/오류 golden tests

## 완료 조건

- [ ] decoder가 socket/장치에 직접 의존하지 않고 fixture만으로 실행된다.
- [ ] 각 프로토콜의 송신값·해석값·시작/끝 위치를 비교했다.
- [ ] 잘린 frame과 부족한 sample을 정상 byte로 확정하지 않는다.
- [ ] 지원/미지원 mode를 명시하고 각 프로토콜 증빙을 별도로 남겼다.

## 관련 계약·검증

SCRUM-37 / IF-14, IF-15

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-25](https://packetkimjunpyo.atlassian.net/browse/SCRUM-25) STM32 시험 신호 생성

#### 변경 전

UART·I2C·SPI의 알려진 시험 패턴을 생성하고 배선, 설정값, 기대 결과를 정리한다.

#### 변경 후

## 기존 작업 범위 (보존)

UART·I2C·SPI의 알려진 시험 패턴을 생성하고 배선, 설정값, 기대 결과를 정리한다.

## 목적

정해진 배선·설정·송신값을 가진 재현 가능한 STM32 신호를 만든다.

## 구현 전에 팀이 결정할 질문

1. STM32 핀과 KR260 채널·GND·전기 조건은 어떻게 대조하는가?
2. UART 반복 패턴과 속도·간격을 어떻게 고정하는가?
3. I2C 상대 장치·주소·pull-up·응답 조건은 무엇인가?
4. SPI mode별 송신/수신·CS 타이밍은 어떻게 만들 것인가?
5. 합성 fixture와 실제 측정 신호를 어떻게 구분할 것인가?

## 산출물

* firmware·빌드/실행법
* 배선·프로토콜 설정표
* 송신 기대값과 실측 캡처

## 완료 조건

- [ ] SYS-02와 실제 배선을 대조한 뒤 시험했다.
- [ ] 동일 firmware/config로 동일 송신값을 재현했다.
- [ ] 각 protocol에 송신값·metadata·기대 decode를 연결했다.
- [ ] 미확정 상대 장치/모드는 담당·확정 시점과 함께 남겼다.

## 관련 계약·검증

SCRUM-32, SCRUM-37 / IF-15

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-26](https://packetkimjunpyo.atlassian.net/browse/SCRUM-26) 전체 경로 통합 및 성능 측정

#### 변경 전

STM32→FPGA→DMA→Linux→TCP→Qt 경로를 시험하고 실제 샘플링 속도, DMA 전송률, 누락·불일치 결과를 기록한다.

#### 변경 후

## 기존 작업 범위 (보존)

STM32→FPGA→DMA→Linux→TCP→Qt 경로를 시험하고 실제 샘플링 속도, DMA 전송률, 누락·불일치 결과를 기록한다.

## 목적

전체 경로에서 데이터 정확성과 단계별 성능을 증빙한다.

## 구현 전에 팀이 결정할 질문

1. IF-01\~15를 어떤 순서·버전·설정으로 실행하는가?
2. 샘플률과 수집 시간, DMA 전송률, TCP 전송률, UI 지연을 어디서 측정하는가?
3. 각 단계의 시간 시작/종료와 bytes 단위는 무엇인가?
4. mock 통과와 실보드 통과를 어떻게 구분하는가?
5. 실패 시 어느 경계의 raw data/log로 원인을 좁히는가?

## 산출물

* IF 시험 결과표
* 단계별 성능 측정·설정/버전
* 실패 이슈와 증빙 링크

## 완료 조건

- [ ] 전체 raw byte·길이·capture_id를 경계별로 비교했다.
- [ ] IF-01\~15의 PASS/FAIL/미실행과 이유를 기록했다.
- [ ] 실제 clock·용량·검증된 신호 속도를 측정 근거와 함께 제시했다.
- [ ] 실패한 필수 시험을 성공으로 집계하지 않고 재시험 결과를 연결했다.

## 관련 계약·검증

SCRUM-18\~25, SCRUM-38 / IF-01\~15

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-27](https://packetkimjunpyo.atlassian.net/browse/SCRUM-27) 최종 Demo 및 결과 정리

#### 변경 전

수집, 파형 표시, 프로토콜 분석, 진단 결과를 재현하는 시연 절차와 측정 결과를 정리한다.

#### 변경 후

## 기존 작업 범위 (보존)

수집, 파형 표시, 프로토콜 분석, 진단 결과를 재현하는 시연 절차와 측정 결과를 정리한다.

## 목적

다른 팀원이 재현할 수 있는 시연과 최종 결과를 묶는다.

## 구현 전에 팀이 결정할 질문

1. 어떤 필수 시나리오와 실패/복구 시나리오를 보여줄 것인가?
2. 부팅부터 배선·서버·Qt·분석까지 어떤 순서로 재현하는가?
3. 최종 bitstream/DT/driver/app/fixture 버전을 어떻게 묶는가?
4. 미완료 기능과 실측 한계를 어떻게 표시하는가?

## 산출물

* Demo runbook
* 최종 버전 manifest·결과 묶음
* 알려진 한계와 후속 작업

## 완료 조건

- [ ] 새 실행 환경에서 runbook 순서대로 시연을 재현했다.
- [ ] 화면 결과에서 원시 capture와 로그까지 추적된다.
- [ ] SCRUM-26 결과와 발표 수치가 일치한다.
- [ ] 필수 실패 항목의 처리·잔여 범위를 명확히 기록했다.

## 관련 계약·검증

SCRUM-26

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-28](https://packetkimjunpyo.atlassian.net/browse/SCRUM-28) n8n 설치 및 Jira 상태 변경 수신 실습

#### 변경 전

n8n 실행 환경을 구성하고, 시험용 Jira Task의 상태 변경 이벤트가 n8n에 수신되는지 확인한다.

#### 변경 후

## 기존 작업 범위 (보존)

n8n 실행 환경을 구성하고, 시험용 Jira Task의 상태 변경 이벤트가 n8n에 수신되는지 확인한다.

## 목적

제품 경로와 분리된 Jira→n8n 이벤트 실습을 재현한다.

## 구현 전에 팀이 결정할 질문

1. 어떤 시험 이슈·이벤트 범위만 받을 것인가?
2. 같은 이벤트 재수신과 순서 뒤바뀜을 어떻게 식별하는가?
3. 수신 성공·실패를 어떤 로그와 실행 기록으로 확인하는가?
4. 자동 상태 변경을 할지 수신만 할지 범위를 어떻게 고정하는가?

## 산출물

* n8n workflow와 실행법
* 시험 이벤트·수신 기록
* 중복/실패 처리표

## 완료 조건

- [ ] 시험용 Jira 상태 변경과 수신 기록이 대응한다.
- [ ] 중복 이벤트를 구분하고 실패를 확인할 수 있다.
- [ ] 제품 수집·TCP·Qt 동작이 n8n 가용성에 의존하지 않는다.

## 관련 계약·검증

SCRUM-31의 운영 자동화 범위

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-29](https://packetkimjunpyo.atlassian.net/browse/SCRUM-29) Diagnostic Console 시험결과 Webhook 연동

#### 변경 전

시험결과 JSON을 n8n으로 전송하고 PASS/FAIL 분기를 확인한다. 동일 시험의 중복 전송을 구분할 run_id를 포함한다.

#### 변경 후

## 기존 작업 범위 (보존)

시험결과 JSON을 n8n으로 전송하고 PASS/FAIL 분기를 확인한다. 동일 시험의 중복 전송을 구분할 run_id를 포함한다.

## 목적

구조화 시험결과를 n8n에 전달하되 제품 시험 판정을 보존한다.

## 구현 전에 팀이 결정할 질문

1. run_id/capture_id와 event 식별자를 어떻게 조합하는가?
2. PASS/FAIL/timeout/미실행을 어떤 schema로 전송하는가?
3. 중복 전송·응답 지연·서버 장애의 재시도/포기 조건은 무엇인가?
4. Webhook 전송 실패와 수집 시험 실패를 어떻게 분리하는가?

## 산출물

* Webhook 전송기와 payload 예
* n8n 분기 workflow
* 중복/장애 시험 로그

## 완료 조건

- [ ] 같은 시험결과 중복 전송을 식별한다.
- [ ] PASS/FAIL 분기가 원본 로그와 일치한다.
- [ ] n8n 장애가 원본 시험결과를 변경하거나 수집 기능을 막지 않는다.
- [ ] 재시도/최종 실패 기록과 원본 run_id가 연결된다.

## 관련 계약·검증

SCRUM-21, SCRUM-28

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-30](https://packetkimjunpyo.atlassian.net/browse/SCRUM-30) 프로젝트 기반 구축

#### 변경 전

Sprint 0의 설계·선수학습·개발환경 구축 작업을 묶는 기반 Epic. 시스템 인터페이스 계약과 개발 시작 조건을 정리한다.

#### 변경 후

## 목적·범위

Sprint 0의 설계·선수학습·개발환경 구축 작업을 묶는 기반 Epic. 시스템 인터페이스 계약과 개발 시작 조건을 정리한다.

## 소속 작업

SCRUM-4, SCRUM-5, SCRUM-6, SCRUM-7, SCRUM-32\~38

## 팀이 결정할 질문

* SYS별 계약의 충돌과 미결정 항목을 누가 언제 해결하는가?
* SCRUM-5에서 어떤 버전을 승인하고 이후 변경을 어떻게 추적하는가?

## 완료 조건

- [ ] SYS 산출물과 환경 재현 결과를 연결하고 SCRUM-5에 승인/보류 근거를 기록한다. SYS는 본 Epic 아래 독립 Task이며 SCRUM-5의 하위 Task가 아니다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

---

### [SCRUM-31](https://packetkimjunpyo.atlassian.net/browse/SCRUM-31) 프로젝트 관리 자동화

#### 변경 전

Jira 상태 변경, Diagnostic Console 시험결과, Webhook/n8n 연동 등 프로젝트 운영 자동화 실습을 묶는 Epic. 제품 필수 기능과 분리해 관리한다.

#### 변경 후

## 목적·범위

Jira 상태 변경, Diagnostic Console 시험결과, Webhook/n8n 연동 등 프로젝트 운영 자동화 실습을 묶는 Epic. 제품 필수 기능과 분리해 관리한다.

## 소속 작업

SCRUM-28, SCRUM-29

## 팀이 결정할 질문

* 이벤트 수신·중복·실패를 어떻게 판정하는가?
* 운영 자동화가 제품 시험의 결과나 동작에 영향을 주지 않도록 어떻게 분리하는가?

## 완료 조건

- [ ] Jira 이벤트 수신과 결과 Webhook 분기를 각각 재현한다. 제품 필수 완료를 이 Epic의 완료에 종속시키지 않는다.
- [ ] 각 소속 Task의 구현·시험 산출물과 미해결 항목을 검토했다.

기존 Epic/Task 계층을 유지한다. 구체적인 결정값은 해당 SYS 계약과 Task의 검토 기록을 따른다.

## 6. 새 Task Description 전문

### [SCRUM-39](https://packetkimjunpyo.atlassian.net/browse/SCRUM-39) AXI4-Lite 레지스터·명령·진단 조회 RTL 구현

Parent: [SCRUM-8](https://packetkimjunpyo.atlassian.net/browse/SCRUM-8)

## 목적

SYS-03의 계약을 실제 RTL로 구현하여 드라이버 제어 경계를 완성한다.

## 구현 전에 팀이 결정할 질문

1. AW/W 독립 도착과 R/B stall을 어떤 구조로 처리하는가?
2. WSTRB 병합 후 검증·RO/미정의/비정렬 접근 응답은 무엇인가?
3. COMMAND pulse·W1C·새 이벤트 동시 발생의 우선순위는 무엇인가?
4. 설정 잠금과 BRAM 진단 읽기 지연/포트 소유권은 어떻게 보장하는가?

## 산출물

* axi_regs RTL·register 정의
* AXI-Lite bus testbench
* IP ID/ABI/진단 조회 결과

## 완료 조건

- [ ] 모든 레지스터의 reset/access/bitfield를 계약과 비교했다.
- [ ] AW/W 독립·WSTRB·stall·잘못된 접근 시험이 통과했다.
- [ ] W1C와 새 이벤트가 겹쳐도 합의한 우선순위가 유지된다.
- [ ] BRAM 조회가 이전 index 데이터를 반환하지 않는다.

## 관련 계약·검증

SCRUM-33 / IF-01, IF-02, IF-08

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-40](https://packetkimjunpyo.atlassian.net/browse/SCRUM-40) logiccap 커널 장치 API·상태·소유권 통합 구현

Parent: [SCRUM-9](https://packetkimjunpyo.atlassian.net/browse/SCRUM-9)

## 목적

MMIO와 DMA 구현을 단일 사용자 장치 계약으로 연결한다.

## 구현 전에 팀이 결정할 질문

1. 단일 장치 등록·open 소유권·close 정리는 누가 담당하는가?
2. 공통 UAPI header와 ioctl layout/reserved/ABI 검증은 어떻게 적용하는가?
3. CONFIG/START/READY/read/poll/llseek/CANCEL/RELEASE와 capture_id 수명은 어떻게 구현하는가?
4. process mutex·IRQ·callback·worker의 상태 갱신과 정리 책임은 어디인가?
5. MMIO/DMA의 중복 소유를 어떻게 방지하는가?

## 산출물

* 장치 API와 상태머신 구현
* 공통 UAPI 사용 예
* 정상/오류/경합 시험

## 완료 조건

- [ ] 공통 header만 사용하며 ABI/잘못된 설정을 거절한다.
- [ ] 두 번째 open·READY 전 read·stale ID·부분 read/EOF가 계약과 같다.
- [ ] 결과 유지·RELEASE·다음 START 순서를 검증했다.
- [ ] CANCEL/close/callback 경합에서 조기 해제와 중복 정리가 없다.
- [ ] 실제 DMA와 연결한 정상 수집 및 복구를 증빙했다.

## 관련 계약·검증

SCRUM-35, SCRUM-17, SCRUM-18 / IF-08\~10

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

---

### [SCRUM-41](https://packetkimjunpyo.atlassian.net/browse/SCRUM-41) liblogic 공통 Device API 및 Mock Backend 구현

Parent: [SCRUM-10](https://packetkimjunpyo.atlassian.net/browse/SCRUM-10)

## 목적

CLI와 TCP 서버가 같은 장치 접근·오류 의미를 재사용하고 보드 없이 개발하게 한다.

## 구현 전에 팀이 결정할 질문

1. 공개 C API의 handle/config/result/error 표현과 메모리 소유권은 무엇인가?
2. Linux backend의 open/ioctl/poll/read와 mock backend를 어떻게 교체하는가?
3. 비동기 START·wait timeout·CANCEL·RELEASE 의미를 UAPI와 어떻게 맞추는가?
4. 부분 read/EINTR/장치 종료·stale ID를 어떻게 처리하는가?
5. mock의 정상·BUSY·timeout·취소·길이 오류를 어떻게 재현하는가?
6. 정적/공유 라이브러리와 헤더·소스·빌드 대상은 어떻게 구성하는가?

## 산출물

* 공개 헤더·Linux/Mock backend
* CLI·서버 연동 예
* backend 공통 계약 시험과 fixture

## 완료 조건

- [ ] CLI·서버가 동일 공개 API를 사용하고 상태 전이를 각각 복제하지 않는다.
- [ ] 같은 fixture가 두 호출 경로에서 같은 metadata/bytes로 나온다.
- [ ] mock 정상/오류/취소/해제 흐름과 UAPI 의미를 대조했다.
- [ ] Linux backend가 실제 장치에서 전체 수집·해제를 완료했다.
- [ ] 지원 플랫폼·빌드법·메모리 소유권·미지원 기능을 문서화했다.

## 관련 계약·검증

SCRUM-35, SCRUM-36 / IF-08\~14

blocks 링크는 연결된 작업의 최종 통합/완료에 필요한 선행 증빙을 뜻한다. 확정된 계약에 따른 mock·단위 개발은 병렬 진행할 수 있다.

## 결정 기록 방법

각 질문에 결정값·선택 이유·담당자·검토자·결정일·근거 문서/코드/시험 링크를 남긴다. 미결정이면 담당자·목표 Sprint·영향 작업과 mock으로 진행 가능한 범위를 기록한다. 아래 질문은 구현 결론을 대신하지 않는다. 실제 구현 Task의 완료에는 결정 문서뿐 아니라 코드와 실행 증빙이 필요하다.

## 7. 검증 결과와 제한

- 최신 프로젝트 검색 마지막 페이지까지 조회: 38개.
- 기존 Description 수정: 27개(일반 Task 20개 + Epic 7개), 작성 문장/숫자와 Jira 재조회 내용 일치.
- SYS 8개 Description 원문 유지 확인.
- 새 Task 3개의 Parent: SCRUM-39→8, SCRUM-40→9, SCRUM-41→10 확인.
- 기존 35개 이슈의 제목·상태·담당·이슈 유형·Parent 보존 확인.
- 요청한 Blocks 47개를 양방향 저장 표현 중 outward 관계로 집계하여 중복 없이 확인.
- 전체 Blocks 그래프의 순환 없음 확인.
- RTL/커널/소프트웨어 구현이나 하드웨어 시험을 수행했다는 의미가 아니다.

최신 Jira가 앞으로 바뀌면 이 보고서와 v0.2는 작성 시점 스냅샷이다. 새 합의는 Jira와 명세에 함께 반영한다.

[새 명세](system-interface-design-v0.2.md) · [변경 전 JSON](jira-before-2026-11-03.json) · [변경 후 JSON](jira-after-2026-11-03.json)

