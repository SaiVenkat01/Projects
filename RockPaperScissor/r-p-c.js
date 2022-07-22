function playRound(psel,csel){
let x='';
if(psel=="rock"){
if(csel=="paper"){
x="You Lose! paper beats rock";
bot++;
if (bot==5){restrt();}
}if(csel=="scissors"){
x="You Win! rock beats scissors";
p2++;
if(p2==5){restrt();}
}
if(csel==psel){
x="Draw :V";
}
}
else if(psel=="paper"){
if(csel=="rock"){
x="You Win! paper beats rock";
p2++;
if(p2==5){restrt();}
}
if(csel=="scissors"){
x="You Lose! scissors beats paper";
bot++;
if (bot==5){restrt();}
}
if(csel==psel){
x="Draw :V";
}
}
else if(psel=="scissors"){
if(csel=="rock"){
x="You Lose! rock beats scissors";
bot++;
if (bot==5){restrt();}
}
if(csel=="paper"){
x="You Win! scissors beats paper";
p2++;
if(p2==5){restrt();}
}
if(csel==psel){
x="Draw :V";
}
}
score.textContent=`Player : ${p2} , Computer : ${bot}`;
return x;
}
function random(){
let arr=["rock","paper","scissors"];
let x=Math.floor(Math.random(1)*2);
return arr[x];
}
function rockfun(){
let csel=random();
text=playRound("rock",csel);
para.textContent=text;
score.textContent=`Player : ${p2} , Computer : ${bot}`;
}
function paperfun(){
let csel=random();
text=playRound("paper",csel);
para.textContent=text;
score.textContent=`Player : ${p2} , Computer : ${bot}`;
}
function scissorfun(){
let csel=random();
text=playRound("scissors",csel);
para.textContent=text;
score.textContent=`Player : ${p2} , Computer : ${bot}`;
}
function rel(){
location.reload();
}
function restrt(){
score.textContent=`Player : ${p2} , Computer : ${bot}`;
rock.disabled="true";
paper.disabled="true";
scissors.disabled="true";
const endgame=document.querySelector('#endgame');
const res=document.createElement('h4');
endgame.appendChild(res);
if(bot==5){
res.textContent=" Computer wins ;-;";
}
else { res.textContent="Player Wins :)(:";
}
const r=document.querySelector('#restart');
const rbutton=document.createElement('button');
r.appendChild(rbutton);
rbutton.textContent="PLAY AGAIN ;p";
rbutton.style.backgroundColor="black";
rbutton.style.color="cadetblue";
rbutton.addEventListener('click',rel);
}
let bot=0;
let p2=0;
const g=document.querySelector('#game');
const para=document.createElement('h6');
g.appendChild(para);
para.textContent='';
const rock=document.querySelector('#bt1');
const paper=document.querySelector('#bt2');
const scissors=document.querySelector('#bt3');
rock.addEventListener('click',rockfun);
paper.addEventListener('click',paperfun);
scissors.addEventListener('click',scissorfun);
const score=document.createElement('h6');
g.appendChild(score);