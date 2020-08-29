
const jss = document.querySelector(".jss")
const detail = document.querySelector(".detail")

jss.addEventListener("mouseover", function(){
    detail.innerHTML = "💛 자세한 내용을 확인하려면 박스를 클릭하세요 💛"
})
jss.addEventListener("mouseout", function(){
    detail.innerHTML = ""
})
