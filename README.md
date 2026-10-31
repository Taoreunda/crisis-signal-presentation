# 한국어 위기 신호 감지 모델 개발

개발 목적·System One 접근·판단 사례·상담 데이터·평가 계획을 소개하는 8장짜리 HTML 발표입니다.

- [발표 열기](https://taoreunda.github.io/crisis-signal-presentation/)
- 2026-10-31부터 모델 비교 결과 앞부분까지만 공개합니다. 성능표·혼동행렬·결과 집계 JSON·내부 발표자 노트는 현재 배포 파일에서 제외했습니다.
- 모델 비교 결과는 내부 검토 후 공개 여부를 결정합니다. 이전에 공개한 내용은 과거 Git 커밋에 남아 있습니다.

## 내용

1. 대화 속 위기 신호 포착 모델 개발
2. System One: 추론형 LLM과 선택지 점수 계산 방식의 비교
3. System One 모델의 판단 과정 · 자살
4. System One 모델의 판단 과정 · 자해
5. 상담 데이터
6. 모델 성능 확인 및 조건부 LoRA 파인튜닝 계획
7. 비교 모델과 실행 조건
8. 원본 라벨별 건수

2장의 94%는 구조 설명용 가상 점수입니다. 3·4장은 식별 정보 없는 연속 문답 8턴과 해당 사례의 저장된 선택지 점수를 보여 줍니다. 이 점수는 전체 상담을 입력한 결과이며 정답률이나 임상적 발생 확률이 아닙니다. 원 상담 전체와 건별 응답 파일은 포함하지 않습니다.

공개 데이터와 판단 사례는 아동·청소년 상담에 해당합니다. 성인 면담이나 타해 감지 성능을 검증한 자료가 아니며, 성인 학습·평가 자료 구성은 별도 결정 사항입니다. LoRA 애니메이션은 개념 설명입니다.

## 실행과 조작

이 폴더에서 `python3 -m http.server 8766 --bind 127.0.0.1`을 실행하고 <http://127.0.0.1:8766/>을 엽니다. 모델 실행이나 npm 설치는 필요하지 않습니다.

- **← / →** 또는 하단 화살표: 이전 / 다음 장
- **발표 시작**, **P**: 현재 탭 전체 화면
- **발표 종료**, **Esc**: 일반 화면

`index.html`이 `slides.html`을 불러옵니다. 공개 파일은 내부 연구 저장소에서 생성하며, 결과 집계에 의존하는 제작 스크립트는 이 저장소에 포함하지 않습니다.

## 출처

- [AI Hub 아동·청소년 상담데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71680): 이미지와 출처 정보는 `assets/aihub-child-counseling.source.json`에 있습니다.
- [Nimble 공식 저장소](https://github.com/bespokelabsai/nimble): 모델 구조와 선택지 점수 계산 방식.
- [LoRA 논문](https://arxiv.org/abs/2106.09685): 파인튜닝 원리.
- [Tony Reina의 LoRA 설명](https://tonyreina.github.io/lora/getting-started/what-is-lora/): 행렬 애니메이션 시각 참고.
- [HyperFrames](https://github.com/heygen-com/hyperframes): 플레이어 0.8.146, Apache-2.0. 라이선스는 `assets/vendor/HYPERFRAMES-LICENSE`에 있습니다.
- GSAP 3.14.2: `assets/vendor/gsap.min.js` 상단의 라이선스 안내를 따릅니다.
