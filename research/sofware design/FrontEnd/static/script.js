document.addEventListener('DOMContentLoaded', ()=>{
const neutralizeBtn = document.getElementById('neutralize-btn')
const statusBtn = document.getElementById('status-btn')
const clockEl = document.getElementById('clock')


neutralizeBtn.addEventListener('click', async ()=>{
appendConsole('SENDING NEUTRALIZE...')
try{
const res = await fetch('/neutralize', {method:'POST'})
const j = await res.json()
appendConsole('BACKEND: ' + JSON.stringify(j))
}catch(e){appendConsole('ERROR: ' + e.message)}
})


statusBtn.addEventListener('click', ()=>{
appendConsole('SYSTEM STATUS: OK — placeholders active')
})


function appendConsole(msg){
const targets = document.getElementById('targets')
const li = document.createElement('li')
li.textContent = '[' + new Date().toLocaleTimeString() + '] ' + msg
li.style.color = 'var(--muted)'
targets.prepend(li)
}


// clock
setInterval(()=>{
const now = new Date()
clockEl.textContent = now.toLocaleTimeString()
},1000)


// small subtle pulsing effect on live box to feel alive
const live = document.getElementById('live-box')
let pulse = 0
setInterval(()=>{
pulse = (pulse + 0.02) % (Math.PI * 2)
const s = 1 + Math.sin(pulse) * 0.002
live.style.transform = `scale(${s})`
},16)


})