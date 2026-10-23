'use strict';
window.dataLayer = window.dataLayer || [];
function track(event,params){window.dataLayer.push({event,...params});}
document.querySelectorAll('.watch').forEach(a=>a.addEventListener('click',()=>track('cta_click',{cta_position:a.dataset.position,link_url:a.href,content_name:'2026 남자 4×100m 계주 결선'})));
document.querySelectorAll('a[href="/#athletes"]').forEach(a=>a.addEventListener('click',()=>{if(location.pathname.startsWith('/blog/'))track('blog_to_landing_click',{link_url:a.href});}));
const cards=[...document.querySelectorAll('.athlete-card')];
function selectAthlete(card){
 cards.forEach(other=>{
  const selected=other===card;
  other.classList.toggle('is-active',selected);
  other.setAttribute('aria-expanded',String(selected));
  other.querySelector('.card-details').hidden=!selected;
  other.querySelector('.card-open').textContent=selected?'−':'+';
 });
 track('athlete_profile_open',{athlete_name:card.querySelector('.card-name').textContent});
}
cards.forEach((card,index)=>{
 card.addEventListener('click',()=>selectAthlete(card));
 card.addEventListener('keydown',event=>{
  let next=null;
  if(event.key==='ArrowRight'||event.key==='ArrowDown')next=(index+1)%cards.length;
  if(event.key==='ArrowLeft'||event.key==='ArrowUp')next=(index-1+cards.length)%cards.length;
  if(event.key==='Home')next=0;
  if(event.key==='End')next=cards.length-1;
  if(next!==null){event.preventDefault();selectAthlete(cards[next]);cards[next].focus({preventScroll:true});}
 });
});
const menuToggle=document.querySelector('.menu-toggle');
const primaryNav=document.querySelector('#primary-nav');
if(menuToggle&&primaryNav){
 function setMenu(open){menuToggle.setAttribute('aria-expanded',String(open));menuToggle.setAttribute('aria-label',open?'메뉴 닫기':'메뉴 열기');primaryNav.classList.toggle('menu-open',open);}
 menuToggle.addEventListener('click',()=>setMenu(menuToggle.getAttribute('aria-expanded')!=='true'));
 primaryNav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
 document.addEventListener('keydown',event=>{if(event.key==='Escape')setMenu(false);});
}
const athleteGrid=document.querySelector('.athlete-grid');
if(athleteGrid&&cards.length){
 function setProfileTextWidth(){
  const gridStyle=getComputedStyle(athleteGrid);
  const mobile=matchMedia('(max-width: 650px)').matches;
  const weight=parseFloat(gridStyle.getPropertyValue('--profile-expanded-weight'))||3.3;
  const gap=parseFloat(gridStyle.columnGap)||0;
  const contentStyle=getComputedStyle(cards[0].querySelector('.card-content'));
  const padding=parseFloat(contentStyle.paddingLeft)+parseFloat(contentStyle.paddingRight);
  const cardWidth=mobile?athleteGrid.clientWidth:(athleteGrid.clientWidth-gap*(cards.length-1))*weight/(weight+cards.length-1);
  athleteGrid.style.setProperty('--profile-text-width',Math.max(0,Math.min(340,cardWidth-padding))+'px');
 }
 setProfileTextWidth();
 if(typeof ResizeObserver!=='undefined')new ResizeObserver(setProfileTextWidth).observe(athleteGrid);
 window.addEventListener('resize',setProfileTextWidth);
}
document.querySelectorAll('[data-gallery]').forEach(gallery=>{
 const slides=[...gallery.querySelectorAll('.gallery-image')];
 const counter=gallery.querySelector('.gallery-count');
 let index=0;
 function show(next){
  index=(next+slides.length)%slides.length;
  slides.forEach((slide,i)=>{slide.hidden=i!==index;});
  counter.textContent=String(index+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0');
  track('athlete_photo_view',{athlete_name:gallery.dataset.athlete,photo_number:index+1});
 }
 gallery.querySelector('.gallery-prev').addEventListener('click',()=>show(index-1));
 gallery.querySelector('.gallery-next').addEventListener('click',()=>show(index+1));
 gallery.addEventListener('keydown',event=>{
  if(event.key==='ArrowLeft'){event.preventDefault();show(index-1);}
  if(event.key==='ArrowRight'){event.preventDefault();show(index+1);}
 });
 let touchStart=null;
 const stage=gallery.querySelector('.gallery-stage');
 stage.addEventListener('touchstart',event=>{if(event.touches.length===1)touchStart={x:event.touches[0].clientX,y:event.touches[0].clientY};else touchStart=null;},{passive:true});
 stage.addEventListener('touchend',event=>{
  if(!touchStart||!event.changedTouches.length)return;
  const dx=event.changedTouches[0].clientX-touchStart.x;
  const dy=event.changedTouches[0].clientY-touchStart.y;
  if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy)*1.3)show(index+(dx<0?1:-1));
  touchStart=null;
 },{passive:true});
 stage.addEventListener('touchcancel',()=>{touchStart=null;},{passive:true});
});
