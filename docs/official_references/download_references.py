"""Download the selected publishers' original documents; no installation or execution."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
HOSTS = {"www.analog.com", "analog.com", "ez.analog.com", "www.nxp.com", "cache.nxp.com", "www.ti.com", "www.st.com", "www.st.com.cn", "docs.amd.com",
         "www.amd.com", "www.xilinx.com", "docs.kernel.org", "doc.qt.io",
         "developerhelp.microchip.com", "www.rfc-editor.org", "www.stmcu.jp"}
# filename, publisher, title, original URL, reading focus
DOCUMENTS = [
    ("01_protocols/ADI_UART.pdf", "Analog Devices", "UART: A Hardware Communication Protocol", "https://www.analog.com/media/en/analog-dialogue/volume-54/number-4/uart-a-hardware-communication-protocol.pdf", "start/data/parity/stop, UART 프레임과 송수신"),
    ("01_protocols/ADI_SPI_Introduction.pdf", "Analog Devices", "Introduction to SPI Interface", "https://www.analog.com/media/en/analog-dialogue/volume-52/number-3/introduction-to-spi-interface.pdf", "CS·SCLK·MOSI·MISO, CPOL/CPHA 네 모드"),
    ("01_protocols/ADI_AN1248_SPI_Timing.pdf", "Analog Devices", "AN-1248: SPI Interface", "https://www.analog.com/media/en/technical-documentation/app-notes/an-1248.pdf", "판독/구동 에지, setup/hold, 장치 간 timing 호환"),
    ("01_protocols/NXP_UM10204_I2C_Specification.pdf", "NXP", "UM10204: I2C-bus specification and user manual", "https://www.nxp.com/docs/en/user-guide/UM10204.pdf", "§3.1: START/STOP, ACK/NACK, 7-bit 주소, repeated START, stretching"),
    ("01_protocols/TI_SLVA704_I2C_Introduction.pdf", "Texas Instruments", "SLVA704: Understanding the I2C Bus", "https://www.ti.com/lit/an/slva704/slva704.pdf", "I2C 입문, open-drain과 pull-up, transaction"),
    ("01_protocols/Microchip_UART_Baud.html", "Microchip", "Step 1: UART, Baud Rate and Polling Mechanism", "https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mcu/ap-exercises/lab7/step1/", "UART 기초와 baud"),
    ("01_protocols/Microchip_I2C_Introduction.html", "Microchip", "I2C Bus Introduction", "https://developerhelp.microchip.com/xwiki/bin/view/applications/i2c/", "주소·ACK·write/read 예제"),
    ("02_stm32/ST_RM0383_STM32F411_Reference_Manual.pdf", "STMicroelectronics", "RM0383: STM32F411xC/E Reference Manual", "https://www.st.com/resource/en/reference_manual/rm0383-stm32f411xce-advanced-armbased-32bit-mcus-stmicroelectronics.pdf", "RCC, GPIO, USART, SPI, I2C 장: 시험 신호 생성에 필요한 register·clock"),
    ("02_stm32/ST_UM1724_Nucleo64_MB1136.pdf", "STMicroelectronics", "UM1724: STM32 Nucleo-64 boards (MB1136)", "https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf", "NUCLEO-F411RE의 connector·전원·ST-LINK·board 연결"),
    ("03_fpga_axi_dma/AMD_UG1037_AXI_Reference.pdf", "AMD/Xilinx", "UG1037: Vivado AXI Reference Guide", "https://www.amd.com/content/dam/xilinx/support/documents/ip_documentation/axi_ref_guide/latest/ug1037-vivado-axi-reference-guide.pdf", "AXI4-Lite channel과 handshake, AXI4-Stream 신호"),
    ("03_fpga_axi_dma/AMD_PG021_AXI_DMA.pdf", "AMD/Xilinx", "PG021: AXI DMA v7.1 Product Guide", "https://www.amd.com/content/dam/xilinx/support/documents/ip_documentation/axi_dma/v7_1/pg021_axi_dma.pdf", "S2MM, status/error, Simple/SG, Programming Sequence"),
    ("03_fpga_axi_dma/AMD_UG1092_KR260_User_Guide.pdf", "AMD/Xilinx", "UG1092: Kria KR260 Robotics Starter Kit User Guide", "https://www.xilinx.com/content/dam/xilinx/support/documents/user_guides/som/ug1092-kr260-starter-kit.pdf", "KR260 interfaces와 board flow; 실제 board revision과 대조"),
    ("04_linux_driver/Linux_ioctl.html", "Linux Kernel", "ioctl based interfaces", "https://docs.kernel.org/driver-api/ioctl.html", "UAPI/ABI, ioctl 번호, 구조체 layout와 32/64-bit 호환"),
    ("04_linux_driver/Linux_MMIO_Device_IO.html", "Linux Kernel", "Bus-Independent Device Accesses", "https://docs.kernel.org/driver-api/device-io.html", "MMIO mapping, readl/writel, ordering"),
    ("04_linux_driver/Linux_DMA_API_HOWTO.html", "Linux Kernel", "Dynamic DMA mapping Guide", "https://docs.kernel.org/core-api/dma-api-howto.html", "DMA 주소, coherent/streaming, mapping과 sync"),
    ("04_linux_driver/Linux_DMAengine_Client.html", "Linux Kernel", "DMA Engine API Guide", "https://docs.kernel.org/driver-api/dmaengine/client.html", "channel/prep/submit/issue/callback, terminate와 synchronize"),
    ("04_linux_driver/Linux_Mutex.html", "Linux Kernel", "Generic Mutex Subsystem", "https://docs.kernel.org/locking/mutex-design.html", "잠들 수 있는 문맥의 상호 배제"),
    ("04_linux_driver/Linux_Spinlocks.html", "Linux Kernel", "Locking lessons", "https://docs.kernel.org/locking/spinlocks.html", "IRQ·공유 상태·spinlock"),
    ("04_linux_driver/Linux_Driver_Basics.html", "Linux Kernel", "Driver Basics", "https://docs.kernel.org/driver-api/basics.html", "wait queues, completions, workqueue 등 필요한 항목만 검색"),
    ("04_linux_driver/Linux_Platform_Driver.html", "Linux Kernel", "Platform Devices and Drivers", "https://docs.kernel.org/driver-api/driver-model/platform.html", "platform device, probe/remove, resource와 binding"),
    ("05_tcp_qt/IETF_RFC9293_TCP.pdf", "IETF / RFC Editor", "RFC 9293: Transmission Control Protocol", "https://www.rfc-editor.org/rfc/rfc9293.pdf", "TCP의 byte-stream 서비스; 전체 TCP stack 구현 학습은 후순위"),
    ("05_tcp_qt/Qt_QAbstractSocket.html", "The Qt Company / Qt Project", "QAbstractSocket", "https://doc.qt.io/qt-6/qabstractsocket.html", "readyRead, read/write buffer, 비동기 socket"),
    ("05_tcp_qt/Qt_Threads_and_QObjects.html", "The Qt Company / Qt Project", "Threads and QObjects", "https://doc.qt.io/qt-6/threads-qobject.html", "GUI thread, affinity, event loop, queued connection"),
    ("05_tcp_qt/Qt_QObject.html", "The Qt Company / Qt Project", "QObject", "https://doc.qt.io/qt-6/qobject.html", "signal/slot, thread affinity, 객체 수명"),
    ("01_protocols/TI_SBOA621_SPI_Introduction.pdf", "Texas Instruments", "SBOA621: Understanding the SPI Bus", "https://www.ti.com/lit/ab/sboa621/sboa621.pdf", "SPI 신호와 네 모드; 후반 TXE 장치별 transaction은 예제로 구분"),
    ("01_protocols/TI_SPRADG5_UART_Debug.pdf", "Texas Instruments", "SPRADG5: UART Log Debug System on Jacinto 7 SoC", "https://www.ti.com/lit/an/spradg5/spradg5.pdf", "UART Introduction 먼저 읽기; Jacinto 7 고유 설정은 STM32에 적용하지 않음"),
    ("02_stm32/ST_RM0383_Rev3_Archived.pdf", "STMicroelectronics Japan", "RM0383 Rev 3 (archived reference)", "https://www.stmcu.jp/wp/wp-content/uploads/2017/08/RM0383_Rev3.pdf", "이전 revision: RCC/GPIO/USART/SPI/I2C 개념 참고. 최신 Rev4와 차이·정오표 확인 필수"),
    ("02_stm32/ST_UM1724_Rev16_Archived.pdf", "STMicroelectronics Japan", "UM1724 Rev 16: STM32 Nucleo-64 boards (archived reference)", "https://www.stmcu.jp/wp/wp-content/uploads/2017/08/UM1724_Rev16.pdf", "NUCLEO-F411RE connector·전원·ST-LINK. 공식 보관본 Rev16; 최신판 Rev17과 구분"),
]

ALTERNATES = {
    "01_protocols/ADI_UART.pdf": ["https://analog.com/media/en/analog-dialogue/volume-54/number-4/uart-a-hardware-communication-protocol.pdf"],
    "01_protocols/ADI_SPI_Introduction.pdf": ["https://analog.com/media/en/analog-dialogue/volume-52/number-3/introduction-to-spi-interface.pdf"],
    "01_protocols/ADI_AN1248_SPI_Timing.pdf": ["https://ez.analog.com/cfs-file/__key/telligent-evolution-components-attachments/00-425-00-00-00-02-41-12/AN_2D00_1248.pdf"],
    "01_protocols/NXP_UM10204_I2C_Specification.pdf": ["https://cache.nxp.com/docs/en/user-guide/UM10204.pdf"],
    "02_stm32/ST_RM0383_STM32F411_Reference_Manual.pdf": ["https://www.st.com/resource/en/reference_manual/dm00119316.pdf", "https://www.st.com.cn/resource/en/reference_manual/dm00119316.pdf"],
    "02_stm32/ST_UM1724_Nucleo64_MB1136.pdf": ["https://www.st.com/resource/en/user_manual/dm00105823.pdf", "https://www.st.com.cn/resource/en/user_manual/dm00105823.pdf"],
    "03_fpga_axi_dma/AMD_UG1092_KR260_User_Guide.pdf": ["https://docs.amd.com/api/khub/documents/LiSqDQ7qx0O_Tf2qoAMs0Q/content"],
}


def download(spec):
    relative, publisher, title, url, focus = spec
    result = dict(file=relative, publisher=publisher, title=title, source_url=url, focus=focus)
    target = (ROOT / relative).resolve()
    if ROOT not in target.parents or urlsplit(url).hostname not in HOSTS:
        raise ValueError("Unexpected destination or host")
    try:
        # Preserve already downloaded documents on reruns.
        if target.exists():
            data = target.read_bytes()
            final_url = url
            content_type = "existing local file"
            manifest = ROOT / "download_manifest.json"
            if manifest.exists():
                prior = next((item for item in json.loads(manifest.read_text(encoding="utf-8"))["documents"] if item["file"] == relative), {})
                final_url = prior.get("final_url", url)
                content_type = prior.get("content_type", content_type)
        else:
            errors = []
            # On a retry, use the publisher's alternate static URLs first.
            candidates = ALTERNATES.get(relative, []) + [url]
            for candidate in candidates:
                try:
                    request = Request(candidate, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36"})
                    with urlopen(request, timeout=12) as response:
                        final_url = response.geturl()
                        if urlsplit(final_url).hostname not in HOSTS:
                            raise ValueError("Unexpected redirect host: " + final_url)
                        content_type = response.headers.get("Content-Type", "")
                        data = response.read(60 * 1024 * 1024 + 1)
                    if relative.endswith(".pdf") and not data.lstrip().startswith(b"%PDF-"):
                        raise ValueError("Publisher returned HTML instead of PDF")
                    break
                except Exception as exc:
                    errors.append(candidate + ": " + str(exc))
            else:
                raise ValueError("; ".join(errors))
            if len(data) > 60 * 1024 * 1024:
                raise ValueError("Document exceeds 60 MiB limit")
            if relative.endswith(".pdf"):
                if not data.lstrip().startswith(b"%PDF-") or b"%%EOF" not in data[-16384:]:
                    raise ValueError("Not a complete PDF (possible HTML error page)")
            else:
                text = data.decode("utf-8", errors="replace").lower()
                if "<html" not in text or len(data) < 1000:
                    raise ValueError("Not a usable HTML document")
                if any(marker in text[:16000] for marker in ["<title>access denied", "<title>just a moment", "<title>error 403"]):
                    raise ValueError("Publisher error/challenge page")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        result.update(status="downloaded", final_url=final_url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), content_type=content_type)
    except Exception as exc:
        result.update(status="failed", error=str(exc))
    return result


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    records = []
    selected = DOCUMENTS
    if "--only-new" in sys.argv and (ROOT / "download_manifest.json").exists():
        previous = json.loads((ROOT / "download_manifest.json").read_text(encoding="utf-8"))["documents"]
        previous_names = {record["file"] for record in previous}
        selected = [spec for spec in DOCUMENTS if spec[0] not in previous_names]
        records.extend(previous)
    with ThreadPoolExecutor(max_workers=4) as pool:
        pending = {pool.submit(download, spec): spec for spec in selected}
        for future in as_completed(pending):
            record = future.result()
            records.append(record)
            print(record["status"], record["file"], record.get("bytes", record.get("error", "")), flush=True)
    records.sort(key=lambda item: item["file"])
    report = dict(downloaded_at=datetime.now(timezone(timedelta(hours=9))).isoformat(), documents=records)
    (ROOT / "download_manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("SUMMARY", sum(r["status"] == "downloaded" for r in records), "/", len(records), flush=True)
