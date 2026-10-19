# 최종 발표 자료

대화 속 위기 신호 포착 모델 개발을 소개하는 5장짜리 HTML 발표입니다.

## 공유 URL

- 발표: <https://taoreunda.github.io/crisis-signal-presentation/>
- 공개 저장소: <https://github.com/Taoreunda/crisis-signal-presentation>
- GitHub Pages는 공개 저장소의 `main` 루트에서 배포합니다.
- 발표 HTML·이미지·브라우저 실행 파일만 공개하며 상담 원본·가중치·실험 결과는 포함하지 않습니다.

발표 수정은 이 폴더에서 합니다. 수정 후 발표 파일만 배포 저장소에 반영해 push하면 Pages가 갱신됩니다. 로컬 수정만으로 공유 URL이 바뀌지는 않습니다. 이 프로젝트 전체를 공개 저장소에 push하지 않습니다.

## 실행

저장소 루트에서:

```bash
python3 -m http.server 8766 --bind 127.0.0.1 --directory communication/presentation
```

브라우저에서 <http://127.0.0.1:8766/>을 엽니다. 서버가 이미 실행 중이면 주소만 열면 됩니다.
파일을 더블클릭하는 대신 로컬 서버로 실행합니다. 폴더 전체를 복사하면 다른 컴퓨터에서도 실행할 수 있습니다.
모델 실행, GPU, npm 설치는 필요하지 않습니다.

## 조작

- **발표 시작** 또는 **P**: 현재 탭을 전체 화면으로 전환합니다.
- **발표 종료**, **Esc**: 일반 화면으로 돌아옵니다. **P**, **F**로도 전환할 수 있습니다.
- **← / →** 또는 하단 화살표: 이전 / 다음 장으로 이동합니다.
- 페이지 번호와 이동 버튼은 발표 중에도 표시합니다. 새 청중 탭은 열지 않습니다.
- 1장만 반복 재생합니다. 2~5장은 한 번 재생 후 유지하며 다시 진입하면 재시작합니다.

## 파일

```text
presentation/
├── index.html                 # 발표 실행·페이지 이동·전체 화면
├── slides.html                # 최종 5장과 애니메이션·발표자 노트
├── README.md                  # 실행 방법과 출처
└── assets/
    ├── aihub-child-counseling.png
    ├── aihub-child-counseling.source.json
    └── vendor/
        ├── gsap.min.js
        ├── hyperframes-player.global.js
        ├── hyperframes-slideshow.global.js
        └── HYPERFRAMES-LICENSE
```

`index.html`로 발표를 엽니다. `slides.html`은 플레이어가 불러오는 본문입니다.
슬라이드 순서·발표자 노트는 두 HTML의 `application/hyperframes-slideshow+json`에 있으며 서로 같게 유지합니다.
시안·중복 이미지·예제 컴포넌트·제작 도구 설정·로컬 제작 기록은 정리했습니다.

## 내용과 출처

1. 대화 속 위기 신호 포착 모델 개발
2. System One: 추론형 LLM(GPT·Qwen)과 System One(Nimble·Jev)의 흐름 비교
3. System One 모델의 판단 과정: 0% → 94% → `{"risk": 0.94}`
4. 상담 데이터: 공식 전체 3,596건
5. 모델 성능 확인 및 LoRA 파인튜닝: 아동·청소년 공개 자료 → Qwen·Nimble·Laya·GPT·Jev 평가·비교 → 성능 부족 시 LoRA 파인튜닝. 성인 증강 데이터는 별도 가지에서 LoRA 학습으로 직접 연결하며 결과 모델 상자는 두지 않습니다.

94%는 설명용 가상 모델 점수이며 실제 실행 결과·정답률·임상적 발생 확률이 아닙니다.
LoRA 격자 애니메이션은 개념 설명이며 실제 학습 가중치나 로그가 아닙니다.
공식 데이터 규모, 공개 벤치마크의 조건과 한계, 성인 평가 계획은 발표자 노트에 보존했습니다. 현재 원본만 보관하며 가공 기준은 사용자 결정 전입니다.

- [AI Hub 아동·청소년 상담데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71680): 캡처와 수량 출처는 `assets/aihub-child-counseling.source.json`.
- [Nimble 공식 저장소](https://github.com/bespokelabsai/nimble): 모델 소개와 공개 평가 근거.
- [LoRA 논문](https://arxiv.org/abs/2106.09685): 학습 원리.
- [Tony Reina의 LoRA 행렬 애니메이션](https://tonyreina.github.io/lora/getting-started/what-is-lora/): 시각 참고. GIF를 삽입하지 않고 발표에 맞게 자체 구현했습니다.
- [HyperFrames](https://github.com/heygen-com/hyperframes): 플레이어 0.8.146, Apache-2.0. `stagger-lattice`의 셀 배치·순차 재생 패턴을 응용했습니다. 라이선스는 `assets/vendor/HYPERFRAMES-LICENSE`.
- GSAP 3.14.2: `assets/vendor/gsap.min.js` 상단의 라이선스 안내를 따릅니다.
