# 기록 뒤의 얼굴들 · 한국 계주 대표팀 이야기

한국 남자 4×100m 계주 대표팀 소개와 아시안게임 동메달 블로그를 제공하는 정적 웹사이트입니다.

## 구조

- `dist/`: 실제 서비스할 HTML, CSS, JavaScript, 사진
- `build.py`: 페이지 생성 코드
- `content/`: 블로그 본문 원본
- `image-edit-notes.md`: 이미지 편집 기록

## 수정 및 빌드

```sh
python3 build.py
```

디자인과 인터랙션은 `dist/style.css`, `dist/app.js`를 수정합니다. 페이지 문구·구조는 `build.py`, 블로그 본문은 `content/`에서 수정한 뒤 빌드하세요. 빌드는 외부 Python 패키지가 필요하지 않습니다.

## 확인

```sh
python3 -m http.server 8000 --directory dist
```

브라우저에서 `http://localhost:8000/`를 엽니다.

## 배포와 측정 상태

현재 사이트: https://beyond-the-record-3843.team-4d-1408.chatgpt.site

이 저장소 업로드만으로 현재 Sites 주소가 자동 갱신되지는 않습니다. 기존 사이트는 별도의 배포 절차를 사용합니다. 배포 대상 공개 폴더는 `dist/`입니다.

GTM·GA4·Meta 설치 코드는 아직 적용되지 않았습니다. `/app.js`에 기존 `cta_click` 신호가 있으므로 추가 리스너를 중복 설치하지 마세요. 외부 전송 설치 및 GTM 발행은 사용자 승인 후 진행합니다.

## 안내

본 페이지는 수업 실습을 위해 제작한 학습용 기획물입니다. 공식 대회·협회·선수의 운영 페이지가 아닙니다.
