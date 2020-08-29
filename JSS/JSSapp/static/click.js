// write 박스 hover 시 글귀변경 (연습)
const write_link = document.querySelector(".make_jss")
const plus = document.querySelector(".plus_btn")

write_link.addEventListener("mouseover", function(){
    plus.style.fontSize = "20px"
    plus.innerHTML = '자기소개서 추가';
})

write_link.addEventListener("mouseout", function(){
    plus.style.fontSize = "5rem"
    plus.innerHTML = "+";
})