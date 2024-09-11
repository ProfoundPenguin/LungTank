const pc_menu = document.querySelectorAll('.pc_menu div')
const hover_effect = document.querySelector('#hover_effect')
const banner_bar = document.querySelector('#banner #main_bar')

pc_menu.forEach(element => {
    element.addEventListener('mouseover', ()=> {
        element.style.color = "#000000"
        hover_effect.style.opacity = "1"

        let position = element.getBoundingClientRect().left - banner_bar.getBoundingClientRect().left + (element.offsetWidth)
        
        hover_effect.style.transform = "translateX(" + position + "px)"
        
    })
    element.addEventListener('mouseleave', ()=> {
        element.style.color = "#CDE8E5"
    })
});