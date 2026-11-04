# 이양배 학습용 공식 문서 모음

정리일: 2026-11-04 (Asia/Seoul)

**실제 저장 완료: 20개 — PDF 9개, HTML 11개.** 아래에서 파일을 클릭하면 로컬 문서가 열린다. 원본은 각 제조사·프로젝트·표준 발행기관의 공개 배포 주소에서 받았다. 파일 본문은 번역하거나 편집하지 않았다.

이 모음은 [개발 필수 기술 학습자료](../이양배_개발필수_기술학습자료.md)의 원리를 공식 자료로 공부하기 위한 것이다. 공식 규격서, 장치 reference manual, 제조사 기술 해설, API 문서는 성격이 다르다. 특히 UART·SPI 해설을 모든 장치의 단일 규격서로 취급하지 않는다.

## 먼저 읽을 순서

1. **통신 원리:** UART는 TI SPRADG5의 UART Introduction부터, SPI는 TI SBOA621의 신호·모드 부분부터 읽는다. 두 자료 후반의 Jacinto/TXE 장치 고유 설정은 STM32 공통 규칙이 아니다.
2. **I2C:** TI SLVA704로 구조를 익힌 다음 NXP UM10204 §3.1의 START/STOP·ACK·주소·stretching을 읽는다.
3. **시험 신호 생성:** STM32 RM0383의 RCC/GPIO/USART/SPI/I2C를 찾아보고, UM1724에서 NUCLEO-F411RE 실제 connector를 확인한다.
4. **진단 CLI:** AMD UG1037의 AXI 구조 → PG021의 S2MM·status/error·Programming Sequence → Linux ioctl·MMIO·DMAengine을 연결해서 읽는다.
5. **드라이버 심화:** platform driver → DMA memory → DMAengine의 callback·terminate·synchronize → lock·wait/completion 순서로 공부한다.
6. **PC 프로그램:** Qt QAbstractSocket으로 비동기 수신을 익히고 Threads and QObjects로 GUI·worker 관계를 공부한다. RFC 9293은 우선 byte-stream 서비스 의미를 확인한다.

## 판본과 저장 형식

- **STM32 RM0383은 ST 일본 공식 사이트의 Rev 3 보관본이다.** 최신판 Rev 4는 직접 다운로드가 시간 초과되어 링크만 남겼다. Rev 3에는 SPI CR2의 register map 누락 등 수정 사항이 있으므로 실제 register 구현에는 최신판·정오표를 대조한다. [ST 공식 수정 안내](https://community.st.com/stm32-mcus-products-25/spi-register-cr2-missing-on-register-map-rm-for-stm32f411ret6-rm0383-rev-3-153808)
- **NUCLEO UM1724는 ST 일본 공식 사이트의 Rev 16 보관본이다.** 현재 공식 링크에서 확인한 Rev 17과 구분하며 실제 보드 revision을 확인한다.
- **AMD PG021 PDF는 2022-04-27판, UG1037 PDF는 v4.0/2017-07-15판이다.** [PG021 온라인 문서](https://docs.amd.com/r/en-US/pg021_axi_dma)와 실제 Vivado/IP 버전에 맞춰 대조한다. 기본 원리 학습과 현재 설정 확인을 구분한다.
- **Linux·Qt HTML은 다운로드 시점의 공개 문서다.** 대상 kernel과 Qt 버전을 자동으로 맞춘 문서가 아니다. 대상 버전의 API 서명·지원 여부는 별도 확인한다.
- **HTML은 해당 페이지 본문을 저장한 파일이다.** 사이트 전체·하위 링크·외부 CSS·이미지를 전부 내려받은 오프라인 매뉴얼은 아니다. 본문은 로컬에서 읽을 수 있지만 일부 스타일·이미지·상대 링크는 인터넷이 필요할 수 있다. PDF는 본문과 그림이 포함된 원본 파일이다.

## 통신 프로토콜

| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |
|---|---|---|---|
| [UM10204: I2C-bus specification and user manual](01_protocols/NXP_UM10204_I2C_Specification.pdf) | NXP · 62쪽 PDF | §3.1: START/STOP, ACK/NACK, 7-bit 주소, repeated START, stretching | [원본](https://cache.nxp.com/docs/en/user-guide/UM10204.pdf) |
| [SBOA621: Understanding the SPI Bus](01_protocols/TI_SBOA621_SPI_Introduction.pdf) | Texas Instruments · 5쪽 PDF | SPI 신호와 네 모드; 후반 TXE 장치별 transaction은 예제로 구분 | [원본](https://www.ti.com/lit/ab/sboa621/sboa621.pdf) |
| [SLVA704: Understanding the I2C Bus](01_protocols/TI_SLVA704_I2C_Introduction.pdf) | Texas Instruments · 8쪽 PDF | I2C 입문, open-drain과 pull-up, transaction | [원본](https://www.ti.com/lit/an/slva704/slva704.pdf) |
| [SPRADG5: UART Log Debug System on Jacinto 7 SoC](01_protocols/TI_SPRADG5_UART_Debug.pdf) | Texas Instruments · 19쪽 PDF | UART Introduction 먼저 읽기; Jacinto 7 고유 설정은 STM32에 적용하지 않음 | [원본](https://www.ti.com/lit/an/spradg5/spradg5.pdf) |

## STM32 시험 신호·보드

| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |
|---|---|---|---|
| [RM0383 Rev 3 (archived reference)](02_stm32/ST_RM0383_Rev3_Archived.pdf) | STMicroelectronics Japan · 844쪽 PDF | 이전 revision: RCC/GPIO/USART/SPI/I2C 개념 참고. 최신 Rev4와 차이·정오표 확인 필수 | [원본](https://www.stmcu.jp/wp/wp-content/uploads/2017/08/RM0383_Rev3.pdf) |
| [UM1724 Rev 16: STM32 Nucleo-64 boards (archived reference)](02_stm32/ST_UM1724_Rev16_Archived.pdf) | STMicroelectronics Japan · 91쪽 PDF | NUCLEO-F411RE connector·전원·ST-LINK. 공식 보관본 Rev16; 최신판 Rev17과 구분 | [원본](https://www.stmcu.jp/wp/wp-content/uploads/2017/08/UM1724_Rev16.pdf) |

## FPGA·AXI·DMA

| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |
|---|---|---|---|
| [PG021: AXI DMA v7.1 Product Guide](03_fpga_axi_dma/AMD_PG021_AXI_DMA.pdf) | AMD/Xilinx · 98쪽 PDF | S2MM, status/error, Simple/SG, Programming Sequence | [원본](https://www.amd.com/content/dam/xilinx/support/documents/ip_documentation/axi_dma/v7_1/pg021_axi_dma.pdf) |
| [UG1037: Vivado AXI Reference Guide](03_fpga_axi_dma/AMD_UG1037_AXI_Reference.pdf) | AMD/Xilinx · 175쪽 PDF | AXI4-Lite channel과 handshake, AXI4-Stream 신호 | [원본](https://www.amd.com/content/dam/xilinx/support/documents/ip_documentation/axi_ref_guide/latest/ug1037-vivado-axi-reference-guide.pdf) |

## Linux 드라이버

| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |
|---|---|---|---|
| [Dynamic DMA mapping Guide](04_linux_driver/Linux_DMA_API_HOWTO.html) | Linux Kernel · HTML | DMA 주소, coherent/streaming, mapping과 sync | [원본](https://docs.kernel.org/core-api/dma-api-howto.html) |
| [DMA Engine API Guide](04_linux_driver/Linux_DMAengine_Client.html) | Linux Kernel · HTML | channel/prep/submit/issue/callback, terminate와 synchronize | [원본](https://docs.kernel.org/driver-api/dmaengine/client.html) |
| [Driver Basics](04_linux_driver/Linux_Driver_Basics.html) | Linux Kernel · HTML | wait queues, completions, workqueue 등 필요한 항목만 검색 | [원본](https://docs.kernel.org/driver-api/basics.html) |
| [Bus-Independent Device Accesses](04_linux_driver/Linux_MMIO_Device_IO.html) | Linux Kernel · HTML | MMIO mapping, readl/writel, ordering | [원본](https://docs.kernel.org/driver-api/device-io.html) |
| [Generic Mutex Subsystem](04_linux_driver/Linux_Mutex.html) | Linux Kernel · HTML | 잠들 수 있는 문맥의 상호 배제 | [원본](https://docs.kernel.org/locking/mutex-design.html) |
| [Platform Devices and Drivers](04_linux_driver/Linux_Platform_Driver.html) | Linux Kernel · HTML | platform device, probe/remove, resource와 binding | [원본](https://docs.kernel.org/driver-api/driver-model/platform.html) |
| [Locking lessons](04_linux_driver/Linux_Spinlocks.html) | Linux Kernel · HTML | IRQ·공유 상태·spinlock | [원본](https://docs.kernel.org/locking/spinlocks.html) |
| [ioctl based interfaces](04_linux_driver/Linux_ioctl.html) | Linux Kernel · HTML | UAPI/ABI, ioctl 번호, 구조체 layout와 32/64-bit 호환 | [원본](https://docs.kernel.org/driver-api/ioctl.html) |

## TCP·Qt

| 로컬 파일 | 발행처·분량 | 읽을 부분 | 공식 원본 |
|---|---|---|---|
| [RFC 9293: Transmission Control Protocol](05_tcp_qt/IETF_RFC9293_TCP.pdf) | IETF / RFC Editor · 98쪽 PDF | TCP의 byte-stream 서비스; 전체 TCP stack 구현 학습은 후순위 | [원본](https://www.rfc-editor.org/rfc/rfc9293.pdf) |
| [QAbstractSocket](05_tcp_qt/Qt_QAbstractSocket.html) | The Qt Company / Qt Project · HTML | readyRead, read/write buffer, 비동기 socket | [원본](https://doc.qt.io/qt-6/qabstractsocket.html) |
| [QObject](05_tcp_qt/Qt_QObject.html) | The Qt Company / Qt Project · HTML | signal/slot, thread affinity, 객체 수명 | [원본](https://doc.qt.io/qt-6/qobject.html) |
| [Threads and QObjects](05_tcp_qt/Qt_Threads_and_QObjects.html) | The Qt Company / Qt Project · HTML | GUI thread, affinity, event loop, queued connection | [원본](https://doc.qt.io/qt-6/threads-qobject.html) |

## 다운로드되지 않은 원문

다음 8개는 파일을 저장하지 못했다. 시간 초과 또는 PDF 주소의 웹페이지 전환으로 실패했으며, 파일이 있는 것처럼 표시하지 않았다. 아래는 인터넷에서 여는 공식 링크다. UART·SPI는 위의 TI 자료로, STM32는 명시한 보관본으로 먼저 공부할 수 있다.

| 원문 | 상태 | 공식 링크 |
|---|---|---|
| AN-1248: SPI Interface | 시간 초과 | [공식 링크](https://www.analog.com/media/en/technical-documentation/app-notes/an-1248.pdf) |
| Introduction to SPI Interface | 시간 초과 | [공식 링크](https://www.analog.com/media/en/analog-dialogue/volume-52/number-3/introduction-to-spi-interface.pdf) |
| UART: A Hardware Communication Protocol | 시간 초과 | [공식 링크](https://www.analog.com/media/en/analog-dialogue/volume-54/number-4/uart-a-hardware-communication-protocol.pdf) |
| I2C Bus Introduction | 시간 초과 | [공식 링크](https://developerhelp.microchip.com/xwiki/bin/view/applications/i2c/) |
| Step 1: UART, Baud Rate and Polling Mechanism | 시간 초과 | [공식 링크](https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mcu/ap-exercises/lab7/step1/) |
| RM0383: STM32F411xC/E Reference Manual | 시간 초과 | [공식 링크](https://www.st.com/resource/en/reference_manual/rm0383-stm32f411xce-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) |
| UM1724: STM32 Nucleo-64 boards (MB1136) | 시간 초과 | [공식 링크](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf) |
| UG1092: Kria KR260 Robotics Starter Kit User Guide | 기존 PDF 주소가 웹 문서로 전환 / 직접 PDF 확보 실패 | [공식 링크](https://docs.amd.com/r/en-US/ug1092-kr260-starter-kit) |

CDC와 AXIS handshake는 추가 온라인 공식 자료를 사용한다: [AMD UG949 Multi-Bit CDC](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Multi-Bit-CDC), [AMD AXIS handshake](https://docs.amd.com/r/en-US/ug1483-model-composer-sys-gen-user-guide/AXI4-Stream-Support-in-Model-Composer). 이 두 페이지는 로컬 문서 수에 포함하지 않았다.

## 파일 확인·재다운로드

`download_manifest.json`에 원본·실제 다운로드 URL, 크기, SHA-256, PDF 쪽수 또는 HTML 제목, 성공/실패를 기록했다. PDF header·종료 marker와 parser 로딩, HTML 제목·본문 존재 여부를 확인했다. 원본 문서를 새로 편집한 것은 아니므로 레이아웃을 재생성하지 않았다.

`download_references.py`는 공개 공식 주소에서 재다운로드하는 Python 스크립트다. 파일을 실행하거나 패키지를 설치하지 않고 문서만 저장한다. 기존 파일은 덮어쓰지 않는다. 일반 Python 표준 라이브러리로 실행 가능하다. `prepare_index.py`는 검증·목록·압축파일 생성용이며 pypdf가 필요하다.

[전체 다운로드 기록](download_manifest.json)
