const pc_menu = document.querySelectorAll('.pc_menu div')
const hover_effect = document.querySelector('#hover_effect')
const banner_bar = document.querySelector('#banner #main_bar')

pc_menu.forEach(element => {
    element.addEventListener('mouseover', ()=> {
        pc_menu.forEach(theElement => {
            theElement.style.color = "#CDE8E5"
        })
        element.style.color = "#000000"
        // hover_effect.style.opacity = "1"

        let position = element.getBoundingClientRect().left - banner_bar.getBoundingClientRect().left
        
        hover_effect.style.width = (element.offsetWidth + 0) + "px"

        

        hover_effect.style.transform = "translateX(" + (position - 0) + "px)"
        // setTimeout(()=> {
        //     hover_effect.style.transition = "0.2s"
        // }, 100)
        
    })
    // element.addEventListener('mouseleave', ()=> {
    //     element.style.color = "#CDE8E5"
    // })
});

banner_bar.addEventListener('mouseleave', ()=> {
    pc_menu.forEach(theElement => {
        theElement.style.color = "#CDE8E5"
    })
})

