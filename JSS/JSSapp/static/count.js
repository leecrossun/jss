const targetform = document.querySelector('.jss_content_form')
const counted_text = document.querySelector('.counted_text')

// 요소.addEventListener("이벤트", 실행함수)
targetform.addEventListener("keyup", function(){
    counted_text.innerHTML = '글자수 : ' + targetform.value.length
})

