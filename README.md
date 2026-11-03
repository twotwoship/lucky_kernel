# lucky_kernel

최종 프로젝트 수행 기간 (26.11.12. ~ 26.12.18.)  
깃 개설일 26.10.27

팀명 : Lucky_Kernel  
팀장 : 이양배  
팀원 : 석민정, 신유지  
주제 : 로직분석기
구현사항 : ...........  
결과물목록 : FSM, FLOWCHART

구성환경 및 툴  
Vivado 2026.1  
Vitis 2026.1  
ubuntu 24.04.2 LTS  
fpga kr 260  
wsl2  
MobaXterm  
ssh  

개발 방식
| 종류 | 작성 | 빌드 | 실행 |
|---|---|---|---|
| Verilog/SystemVerilog | Windows | Vivado | KR260 FPGA |
| Device Tree | WSL | WSL 또는 KR260 | KR260 |
| Kernel Driver | WSL | **KR260** | KR260 |
| DMA/MMIO 테스트 | WSL | **KR260** | KR260 |
| TCP Server | WSL | KR260 | KR260 |
| Diagnostic Console | WSL | KR260 | KR260 |
| Qt Viewer | Windows | Windows | Windows |
| STM32 | Windows | Windows | STM32 |
