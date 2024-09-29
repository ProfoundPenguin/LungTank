const pc_menu = document.querySelectorAll('.pc_menu div')
const hover_effect = document.querySelector('#the_hover_effect')
const banner_bar = document.querySelector('#banner #main_bar')

const listItems = document.querySelectorAll('#faq li');




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



listItems.forEach(item => {
    item.addEventListener('click', function() {
        // If the clicked item is already active, remove the 'active' class
        if (this.classList.contains('active')) {
            this.classList.remove('active');
        } else {
            // Remove 'active' class from all list items
            listItems.forEach(li => li.classList.remove('active'));

            // Add 'active' class to the clicked item
            this.classList.add('active');
        }
    });
});



