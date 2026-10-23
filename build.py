from pathlib import Path
import json
D=Path(__file__).parent/'dist'
players=[
 dict(id='seo',name='서민준',en='SEO MINJUN',team='서천군청',leg='첫 번째 주자',pos='65%',title='첫 곡선부터,<br>속도를 끌어올리다.',desc='첫 곡선에서 시작된 네 사람의 레이스.',text='서민준은 2026 아이치·나고야 아시안게임 결선의 첫 번째 주자입니다. 가장 안쪽인 1번 레인에서 출발해 속도를 끌어올리고, 나마디 조엘진에게 배턴을 연결했습니다.',extra='2025 구미 아시아육상선수권에서는 한국 남자 400m 계주 첫 우승을 함께했습니다. 출발부터 다음 주자에게 배턴을 넘기는 순간까지, 팀의 레이스를 여는 역할입니다.',source='https://www.chungnamilbo.co.kr/news/articleView.html?idxno=831852'),
 dict(id='joel',name='나마디 조엘진',en='NWAMADI JOELJIN',team='예천군청',leg='두 번째 주자',pos='5%',title='직선 위에서,<br>질주를 이어가다.',desc='이제 이름을 기억할 시간.',text='한국인 어머니와 나이지리아인 아버지 사이에서 태어나 한국에서 자란 나마디 조엘진. 고교 시절부터 단거리 유망주로 주목받았고, 이번 결선에서는 두 번째 주자로 직선 구간을 달렸습니다.',extra='낯설었던 이름을 한 번 더 읽어보세요. 서민준에게 받은 배턴을 이재성에게 연결한 그는, 네 사람의 기록을 만드는 한 축이었습니다.',source='https://www.yna.co.kr/view/AKR20221010035500007'),
 dict(id='lee',name='이재성',en='LEE JAESUNG',team='광주광역시청',leg='세 번째 주자',pos='38%',title='배턴을 잇고,<br>승부를 이어가다.',desc='두 번의 아시안게임, 이어지는 질주.',text='이재성은 세 번째 주자로 달려 마지막 주자 비웨사 다니엘 가사마에게 배턴을 전달했습니다. 2023년에 열린 항저우 아시안게임 계주 동메달에 이어, 아이치·나고야에서도 시상대에 올랐습니다.',extra='2025 라인-루르 세계대학경기대회에서는 한국 남자 400m 계주 금메달을 함께했습니다. 국제무대에서 쌓은 경험이 이번 레이스로 이어졌습니다.',source='https://committee.ikbc.co.kr/스포츠/article/view/kbc202507290049'),
 dict(id='biwesa',name='비웨사 다니엘 가사마',en='BIWESA DANIEL GASSAMA',team='안산시청',leg='마지막 주자',pos='100%',title='마지막 100m,<br>결승선까지 밀어붙이다.',desc='결승선을 향한 마지막 100m.',text='비웨사 다니엘 가사마는 한국에서 태어나 자랐고, 중학교 시절 한국 국적을 취득했습니다. 이번 결선에서는 마지막 주자로 배턴을 받아 38초43의 레이스를 마무리했습니다.',extra='마지막 직선에서 이어진 순위 경쟁. 비웨사는 태국 주자의 추격을 뿌리치고 세 번째로 결승선을 통과했습니다. 네 사람이 함께 만든 한국 신기록이 완성되는 순간입니다.',source='https://www.yna.co.kr/amp/view/AKR20250509081100371')]
bios={
 'seo': dict(paragraphs=[
  '서천군청 소속의 단거리 선수 서민준은 개인 종목과 계주를 함께 뛰며 국제무대 경험을 쌓아왔습니다. 2025 구미 아시아육상선수권 남자 400m 계주에서 한국의 첫 우승을 함께했고, 같은 해 라인-루르 세계대학경기대회에서도 계주 금메달을 목에 걸었습니다.',
  '2026 아시안게임 이후에도 레이스는 이어졌습니다. 제107회 전국체전에서 남자 100m와 200m 은메달을 따냈고, 충남 대표팀의 마지막 주자로 나선 400m 계주에서는 우승을 이끌었습니다.',
  '아이치·나고야 결선에서는 첫 주자로, 전국체전에서는 마지막 주자로. 서로 다른 자리에서 배턴을 이어온 이력이 서민준을 알아보는 또 하나의 관전 포인트입니다.'
 ],highlight='2025 아시아선수권·세계대학경기대회 계주 금메달',sources=[
 ('나무위키 참고 문서 · 미러','https://namu.moe/w/서민준(육상)'),
 ('대한육상연맹 · 2025 세계대학경기대회 계주 우승','https://m.kaaf.or.kr/mobile/community/news_view.asp?RECNO=5123&tn=KAF_NOTICE_BOARD'),
 ('SBS · 2026 전국체전 개인·계주 성적','https://news.sbs.co.kr/news/endPage.do?news_id=N1008806722')]),
 'joel': dict(paragraphs=[
  '나마디 조엘진은 한국인 어머니와 나이지리아인 아버지 사이에서 태어나 한국에서 성장한 단거리 선수입니다. 고교 시절 아시아청소년육상선수권 대표로 선발됐고, 현재는 예천군청 소속으로 트랙을 달리고 있습니다.',
  '어린 시절에는 드라마 ‘태양의 후예’에 아역으로 출연한 이력도 있습니다. 화면 속 소년에서 육상 국가대표로, 조엘진의 이름 뒤에는 서로 다른 무대의 이야기가 담겨 있습니다.',
  '2025 세계대학경기대회에서는 남자 400m 계주 금메달을 함께했습니다. 2026 아시안게임 계주 동메달 이후에는 전국체전 100m와 200m를 모두 제패하며 개인 종목에서도 존재감을 이어갔습니다.'
 ],highlight='청소년 대표에서 실업팀·성인 국가대표로 성장',sources=[
 ('나무위키 참고 문서 · 미러','https://www.namu.moe/w/나마디%20조엘%20진'),
 ('연합뉴스 · 청소년 대표와 성장 배경','https://www.yna.co.kr/view/AKR20221010035500007'),
 ('일간스포츠 · 아역 출연 이력','https://isplus.com/article/view/isp202609260010'),
 ('대한육상연맹 · 2026 전국체전 100m·200m 우승','https://m.kaaf.or.kr/mobile/community/news_view.asp?RECNO=5431&tn=KAF_NOTICE_BOARD')]),
 'lee': dict(paragraphs=[
  '광주광역시청 소속 이재성은 계주뿐 아니라 200m 개인 종목에서도 국제대회 메달을 따낸 단거리 선수입니다. 2025 라인-루르 세계대학경기대회 남자 200m에서 동메달을 획득했고, 같은 대회 400m 계주에서는 동료들과 금메달을 합작했습니다.',
  '2023년에 열린 항저우 아시안게임 계주 동메달, 2025 아시아선수권 계주 금메달, 그리고 2026 아이치·나고야 계주 동메달. 여러 국제대회를 거치며 한국 계주의 메달 역사에 이름을 남겼습니다.',
  '2026 아시안게임 선발전을 겸한 육상경기선수권에서는 남자 200m 우승을 차지했습니다. 개인 레이스에서의 경쟁력과 팀 레이스에서의 경험을 함께 보면 이재성의 역할이 더 선명해집니다.'
 ],highlight='2025 세계대학경기대회 200m 동메달·계주 금메달',sources=[
 ('나무위키 참고 문서 · 미러','https://www.namu.moe/w/이재성(육상)'),
 ('연합뉴스 · 2025 세계대학경기대회 200m 동메달','https://www.yna.co.kr/view/AKR20250725075600007'),
 ('대한육상연맹 · 2025 세계대학경기대회 계주 금메달','https://m.kaaf.or.kr/mobile/community/news_view.asp?RECNO=5123&tn=KAF_NOTICE_BOARD'),
 ('연합뉴스 · 2026 아시안게임 선발전 200m 우승','https://www.yna.co.kr/amp/view/AKR20260514179100007')]),
 'biwesa': dict(paragraphs=[
  '비웨사 다니엘 가사마는 콩고민주공화국 출신 부모님 사이에서 경기도 안산에서 태어나 자랐습니다. 2018년 어머니의 귀화와 함께 한국 국적을 취득했고, 육상선수로서 전국대회와 국가대표 무대를 향한 길을 열었습니다.',
  '2020년 KBS배 전국육상경기대회 남자 고등부 100m 우승으로 주목받았지만, 실업팀 입단 뒤에는 햄스트링 부상과 재활을 거쳤습니다. 안산시청에서 훈련을 이어가며 다시 국제무대에 도전했습니다.',
  '2026 아이치·나고야 아시안게임에서는 계주 마지막 주자로 한국 신기록과 동메달을 완성했습니다. 처음 접한 이름이라면, 부상을 지나 다시 결승선을 향해 달린 과정도 함께 기억해 보세요.'
 ],highlight='고교 단거리 유망주에서 재활을 거쳐 국가대표로',sources=[
 ('나무위키 참고 문서 · 미러','https://namu.moe/w/비웨사%20다니엘%20가사마'),
 ('연합뉴스 · 출생·국적 취득·부상과 복귀 과정','https://www.yna.co.kr/view/AKR20250509081100371'),
 ('SBS · 2026 아시안게임 계주 결선','https://news.sbs.co.kr/news/endPage.do?news_id=N1008773683')])
}
for player in players:
 player['bio']=bios[player['id']]
def biography(player):
 b=player['bio']
 return '<p class="bio-highlight">'+b['highlight']+'</p>'+''.join('<p>'+paragraph+'</p>' for paragraph in b['paragraphs'])
def biography_sources():
 return '<details class="bio-source-details"><summary>선수 소개 참고 자료 · 2026.10.23 확인</summary><p>나무위키 관련 문서는 미러를 통해 참고했으며, 주요 경력과 성장 배경은 대한육상연맹·언론 보도로 대조했습니다. 소개 문장은 확인한 사실을 바탕으로 새로 작성했습니다.</p>'+''.join('<div id="source-'+player['id']+'"><h3>'+player['name']+'</h3><ul>'+''.join('<li><a href="'+url+'" target="_blank" rel="noopener noreferrer">'+name+' ↗</a></li>' for name,url in player['bio']['sources'])+'</ul></div>' for player in players)+'</details>'
(D/'assets/players.json').write_text(json.dumps(players,ensure_ascii=False))
def head(title,desc,root=''):
 return f'''<!doctype html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="https://beyond-the-record-3843.team-4d-1408.chatgpt.site/assets/team.png"><link rel="canonical" href="https://beyond-the-record-3843.team-4d-1408.chatgpt.site/{root}"><link rel="icon" href="/assets/favicon.svg"><link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script></head><body><a class="skip" href="#main">본문 바로가기</a>'''
def nav():
 return '''<header class="header"><button class="menu-toggle" aria-controls="primary-nav" aria-expanded="false" aria-label="메뉴 열기"><span></span><span></span></button><a class="brand" href="/" aria-label="기록 뒤의 얼굴들 · 한국 계주 대표팀 이야기 홈"><span class="brand-icon">4</span><span class="brand-lockup"><span class="brand-name">기록 뒤의 얼굴들</span><span class="brand-sub">한국 계주 대표팀 이야기</span></span></a><nav id="primary-nav" aria-label="주 메뉴"><a href="/#athletes">네 명의 얼굴</a><a href="/#stories">선수 이야기</a><a href="/blog/">블로그 <span>↗</span></a></nav><a class="nav-watch watch" data-position="header" href="https://m.imbc.com/Vod/VodPlay?broadcastID=1006923100831100000&progCode=1006923100000100000" target="_blank" rel="noopener noreferrer">결선 다시보기 <span>↗</span></a></header>'''
def watch(pos,label='계주 결선 다시보기'):
 return f'''<a class="button watch" data-position="{pos}" href="https://m.imbc.com/Vod/VodPlay?broadcastID=1006923100831100000&progCode=1006923100000100000" target="_blank" rel="noopener noreferrer"><span class="play">▶</span>{label}<span class="arrow">↗</span></a><small class="replay-time">영상 03:45:00부터 남자 4×100m 계주 시작</small>'''
def footer():
 return '''<footer><a class="footer-brand" href="/">기록 뒤의 얼굴들<span>한국 계주 대표팀 이야기</span></a><div><a href="/#athletes">대표팀 소개</a><a href="/blog/">블로그</a><a href="/#sources">출처</a></div><p>2026 한국 남자 4×100m 계주 · 학습용 비공식 팬 프로젝트<br>사진: 사용자 제공 · 정보 확인일: 2026.10.23</p><small>FOUR ATHLETES. ONE STORY.</small><p class="site-notice">본 페이지는 수업 실습을 위해 제작한 학습용 기획물입니다. 공식 대회·협회·선수의 운영 페이지가 아닙니다.</p></footer><nav class="mobile-actions" aria-label="빠른 이동"><a href="/#athletes"><span aria-hidden="true">◉</span>선수 소개</a><a href="/blog/"><span aria-hidden="true">▤</span>블로그</a><a class="watch" data-position="mobile_bar" href="https://m.imbc.com/Vod/VodPlay?broadcastID=1006923100831100000&amp;progCode=1006923100000100000" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">▶</span>결선 다시보기</a></nav>'''
cards=''.join(f'''<button class="athlete-card {'is-active' if i==0 else ''}" data-player="{p['id']}" aria-expanded="{'true' if i==0 else 'false'}" aria-controls="info-{p['id']}"><span class="portrait" style="--pos:{p['pos']}" role="img" aria-label="{p['name']} 선수, 제공된 단체 사진에서 확대"></span><span class="card-shade"></span><span class="card-content"><span class="card-no">0{i+1} / {p['leg']}</span><span class="card-name">{p['name']}</span><span class="card-details" id="info-{p['id']}" {'' if i==0 else 'hidden'}><span class="card-team">{p['en']} · {p['team']}</span><span class="card-description">{p['text']}</span><span class="card-caption">{p['desc']}</span></span></span><span class="card-open" aria-hidden="true">{'−' if i==0 else '+'}</span></button>''' for i,p in enumerate(players))
galleries={
 'seo': [('seo-gallery-1.png','서민준 선수 프로필 사진',1122,1402),('seo-gallery-2.png','배턴을 들고 양팔을 펼친 서민준 선수',1122,1402),('seo-gallery-3.png','배턴을 쥐고 트랙을 달리는 서민준 선수',1122,1402)],
 'joel': [('joel-gallery-1.jpeg','나마디 조엘진 선수 프로필 사진',452,678),('joel-gallery-2.svg','경기장에서 앞을 바라보는 나마디 조엘진 선수',1533,2048),('joel-gallery-3.jpg','트랙 위에서 양팔을 펼친 나마디 조엘진 선수',700,1050)],
 'lee': [('lee-gallery-1.jpeg', '이재성 선수 프로필 사진', 452, 678), ('lee-gallery-2-clean.svg', '태극기를 들고 웃는 이재성 선수', 650, 361), ('lee-gallery-3.jpeg', '육상 유니폼을 입고 운동화를 든 이재성 선수', 387, 516)],
 'biwesa': [('biwesa-gallery-1.jpeg', '비웨사 다니엘 가사마 선수 프로필 사진', 452, 678), ('biwesa-gallery-2-clean.svg', '트랙 위를 달리는 비웨사 다니엘 가사마 선수', 1200, 747), ('biwesa-gallery-3-clean.svg', '배턴을 들고 결승선을 향해 달리는 비웨사 다니엘 가사마 선수', 485, 633)]
}
def athlete_photo(p,i):
 if p['id'] not in galleries:
  return f'''<div class="story-photo portrait" style="--pos:{p['pos']}" role="img" aria-label="{p['name']} 선수"><span class="photo-label">{p['en']}<br><b>0{i+1} / TEAM KOREA</b></span></div>'''
 photos=galleries[p['id']]
 slides=''.join(f'''<img class="gallery-image" src="/assets/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" {'' if n==0 else 'hidden'}>''' for n,(src,alt,w,h) in enumerate(photos))
 return f'''<div class="story-photo athlete-gallery" data-gallery="{p['id']}" data-athlete="{p['name']}" role="region" aria-roledescription="사진 슬라이드" aria-label="{p['name']} 선수 사진 {len(photos)}장" tabindex="0"><div class="gallery-stage">{slides}</div><div class="gallery-footer"><span class="gallery-label">{p['en']}<span>PHOTO GALLERY</span></span><div class="gallery-controls"><button type="button" class="gallery-prev" aria-label="{p['name']} 이전 사진">←</button><span class="gallery-count" aria-live="polite" aria-atomic="true">01 / {len(photos):02d}</span><button type="button" class="gallery-next" aria-label="{p['name']} 다음 사진">→</button></div></div></div>'''
stories=''.join(f'''<section class="story {'reverse' if i%2 else ''}" id="story-{p['id']}" aria-labelledby="heading-{p['id']}">{athlete_photo(p,i)}<div class="story-copy"><span class="eyebrow">CHAPTER 0{i+1} — {p['leg']}</span><h2 id="heading-{p['id']}">{p['title']}</h2><h3>{p['name']}</h3><span class="small-meta">{p['en']} · {p['team']}</span>{biography(p)}</div></section>''' for i,p in enumerate(players))
posts=[
 dict(slug='asian-games-relay-bronze',category='RACE REPORT',image='team.png',alt='한국 남자 계주 대표팀 네 선수의 동메달 기념사진',title='아시안게임 남자 400m 계주 동메달, 38초43을 만든 네 번의 질주',summary='한국 신기록과 두 대회 연속 동메달. 선수 명단부터 결선의 흐름, 다시보기까지 한 번에.')]
def news_cards(limit=None):
 return '<div class="news-grid">'+''.join(f'''<a class="news-card" href="/blog/{post['slug']}/"><div class="news-cover"><img src="/assets/{post['image']}" alt="{post['alt']}" loading="lazy"><span>{post['category']}</span></div><div class="news-body"><h3>{post['title']}</h3><p>{post['summary']}</p><div class="news-meta"><time datetime="2026-10-22">2026.10.22</time><span aria-hidden="true">↗</span></div></div></a>''' for post in posts[:limit])+'</div>'
main=head('한국 남자 400m 계주 대표팀 소개 | 기록 뒤의 얼굴들','38초43 한국 신기록을 만든 서민준, 나마디 조엘진, 이재성, 비웨사 다니엘 가사마. 네 선수의 프로필과 결선에서의 역할을 알아보고 경기 영상을 다시 만나보세요.')+nav()+f'''
<main id="main"><section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="tiny-dot"></span> 2026 아이치·나고야 아시안게임 · 남자 4×100m 계주</p><h1>네 번의 질주.<br><span>하나의 신기록.</span></h1><p class="hero-intro"><strong>처음 본 네 선수, 어떤 선수일까?</strong><br>한국 계주 대표팀을 알아보고, 38초43의 결선을 다시 만나보세요.</p><ul class="hero-facts" aria-label="경기 결과 요약"><li><strong>38초43</strong><span>한국 신기록</span></li><li><strong>동메달</strong><span>두 대회 연속 메달</span></li><li><strong>2026.09.28</strong><span>아시안게임 결선</span></li></ul>{watch('hero')}<a class="hero-more" href="#athletes">한국 대표팀 라인업 보기 <span>↓</span></a></div><div class="hero-photo"><img src="/assets/team.png" alt="한국 남자 400m 계주 대표팀 네 선수가 태극기를 펼치고 함께 웃는 모습" fetchpriority="high"><div class="photo-tag">FOUR ATHLETES.<br>ONE FINISH LINE.</div><div class="hero-record"><strong>38<span>.</span>43</strong><span>KOREAN RECORD<br>2026.09.28 · BRONZE MEDAL</span></div></div><div class="hero-bottom"><span>FOUR RUNNERS. FULL SPEED.</span><span>SCROLL TO DISCOVER ↓</span></div></section>
<section class="athletes section" id="athletes"><div class="section-top"><div><span class="eyebrow">01 / MEET THE TEAM</span><h2>이름을 기억해.<br>레이스를 다시 봐.</h2></div><p>트랙 위에서는 하나의 팀.<br>카드를 눌러 네 선수의 프로필을 확인하세요.</p></div><div class="athlete-grid">{cards}</div><div class="section-note"><span>한국 남자 400m 계주 대표팀</span><span>2026 아시안게임 결선 출전 순서 →</span></div></section>
<section class="story-intro" id="stories"><span class="eyebrow">02 / THE RUNNERS</span><h2>출발부터 결승선까지.<br>네 선수의 레이스를 따라가다.</h2><p>스피드를 연결하고, 기록을 완성하다.<br>첫 주자부터 마지막 주자까지, TEAM KOREA.</p><span class="intro-line"></span></section>{stories}
<section class="finale" id="replay"><span class="eyebrow">03 / WATCH IT AGAIN</span><p class="final-record">38.43<span>SECONDS</span></p><h2>38초43.<br>다시, 전력 질주.</h2><p>출발 신호부터 마지막 스퍼트까지.<br>네 선수가 만든 한국 신기록, 다시 확인하세요.</p>{watch('final')}<small>MBC 경기 다시보기 페이지로 이동합니다.<br>해당 페이지에서 남자 4×100m 계주 결선을 확인할 수 있습니다.</small></section>
<section class="journal section" id="blog"><div class="section-top"><div><span class="eyebrow">04 / TEAM KOREA BLOG</span><h2>트랙 밖에서도,<br>계속 달리다.</h2></div><a class="news-more" href="/blog/">블로그 전체 보기 <span>↗</span></a></div>{news_cards(3)}<a class="news-bottom" href="/blog/">MORE STORIES <span>→</span></a></section>
<section class="faq section"><span class="eyebrow">RELAY GUIDE</span><h2>계주, 알고 보면 더 빠져든다.</h2><details><summary>한국 남자 400m 계주 대표팀 선수는 누구인가요?</summary><p>2026 아이치·나고야 아시안게임 결선에는 서민준, 나마디 조엘진, 이재성, 비웨사 다니엘 가사마가 출전했습니다. 대회와 라운드에 따라 출전 명단은 달라질 수 있습니다.</p></details><details><summary>400m 계주와 4×100m 계주는 같은 종목인가요?</summary><p>이 페이지에서 말하는 남자 400m 계주는 네 선수가 각각 100m씩 달리는 4×100m 계주입니다. 각 선수가 400m를 달리는 4×400m 계주와 구분됩니다.</p></details><details><summary>이번 결선에서 어떤 기록을 세웠나요?</summary><p>2026년 9월 28일 결선에서 38초43의 한국 신기록으로 동메달을 획득했습니다. 2023년에 열린 항저우 대회에 이어 두 대회 연속 메달입니다.</p></details></section>
<section class="sources section" id="sources"><h2>이야기의 출처</h2><p>경기 기록·주자 순서: <a href="https://www.yna.co.kr/view/AKR20260928166351007" target="_blank" rel="noopener noreferrer">연합뉴스 경기 보도 ↗</a> · <a href="https://news.sbs.co.kr/news/endPage.do?news_id=N1008773683" target="_blank" rel="noopener noreferrer">SBS 경기 보도 ↗</a></p><p>선수별 경력 자료는 <a href="/blog/asian-games-relay-bronze/#athlete-sources">동메달 글 하단의 선수 참고 자료</a>에서 확인할 수 있습니다. 정보 확인일: 2026년 10월 23일.</p>{biography_sources()}<p>단체 사진과 선수별 사진은 사용자가 제공한 이미지를 활용했습니다.</p></section></main>
'''+footer()
(D/'index.html').write_text(main)
(D/'blog').mkdir(parents=True,exist_ok=True)
(D/'blog/index.html').write_text(head('한국 남자 계주 대표팀 블로그 | 기록 뒤의 얼굴들','한국 남자 400m 계주 대표팀의 선수 프로필, 결선 주자 순서, 38초43 한국 신기록을 소개합니다.','blog/')+nav()+'<main id="main" class="blog-main section"><span class="eyebrow">TEAM KOREA / BLOG</span><h1>트랙 밖에서도,<br>계속 달리다.</h1><p class="blog-lead">선수 라인업부터 경기 기록까지. 한국 계주의 모든 순간을 읽어보세요.</p>'+news_cards()+'</main>'+footer())
bronze_slug='asian-games-relay-bronze'
bronze_path=D/'blog'/bronze_slug
bronze_path.mkdir(parents=True,exist_ok=True)
bronze_body=(Path(__file__).parent/'content/asian-games-relay-bronze.html').read_text().replace('{{WATCH}}',watch('blog'))
(bronze_path/'index.html').write_text(head('아시안게임 남자 400m 계주 동메달·38초43 한국 신기록 | 기록 뒤의 얼굴들','2026 아이치·나고야 아시안게임 한국 남자 400m 계주 동메달을 정리했습니다. 네 선수의 명단과 주자 순서, 38초43 한국 신기록, 경기 다시보기를 확인하세요.','blog/'+bronze_slug+'/')+nav()+bronze_body+footer())
(D/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://beyond-the-record-3843.team-4d-1408.chatgpt.site/sitemap.xml\n')
(D/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>https://beyond-the-record-3843.team-4d-1408.chatgpt.site/{p}</loc></url>' for p in ['', 'blog/','blog/asian-games-relay-bronze/'])+'</urlset>')
(D/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="32"/><text x="32" y="46" fill="white" text-anchor="middle" font-family="Arial" font-size="44" font-weight="bold">4</text></svg>')
