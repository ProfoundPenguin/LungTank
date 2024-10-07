function addToCart(productId) {
    const element = document.querySelector('.b' + productId);
    if (element) {
        element.classList.add("on_wait");
    }
    fetch(`/cart/add_to_cart/${productId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            if (element) {
                element.classList.remove("on_wait");
            }
            drawCart()
            animateCartButton()
            // Update the cart UI, e.g., refresh cart count or display message
        } else {
            console.log('Error adding item:', data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

function animateCartButton() {
    document.querySelectorAll('#cart_button').forEach(theE => {
        let element = theE.querySelector("svg")
        let animation = "animate__headShake"
        element.classList.add('animate__animated', animation);

        element.addEventListener('animationend', () => {
            element.classList.remove(animation);
        });
    });
}

function removeFromCart(productId) {
    fetch(`/cart/remove_from_cart/${productId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            drawCart()
            return response.json();
        } else {
            throw new Error('Item could not be removed.');
        }
    })
}

function decrementCart(productId) {
    fetch(`/cart/decrement_from_cart/${productId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            drawCart();
        } else {
            console.log('Error decrementing item:', data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

function viewCart() {
    fetch('/cart/cart/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Cart:', data.cart);
        // Use this data to update your cart display
    })
    .catch(error => console.error('Error:', error));
}

function drawCart() {
    fetch('/cart/cart/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const cart = data.cart;
        cart_lenght = Object.keys(cart).length

        document.querySelectorAll('#cart_count').forEach(element => {
            element.innerHTML = cart_lenght
        });
        // document.querySelector("#cart_button.pc_only #cart_count").innerHTML = cart_lenght
        document.querySelector("#pc_cart #items p").innerHTML = cart_lenght + " Items"

        const pc_cart_list = document.querySelector("#pc_cart #cart_content");
        const mobile_cart_list = document.querySelector("#cart #cart_content");

        pc_cart_list.innerHTML = '';
        mobile_cart_list.innerHTML = '';

        let total = 0;

        // Loop through the cart object
        for (const [productId, item] of Object.entries(cart)) {
            // Convert price to a number and multiply by quantity
            const itemTotal = parseFloat(item.price) * item.quantity;
            total += itemTotal;
        }

        document.querySelectorAll("#cart_footer .total").forEach(element => {
            element.innerHTML = `Your Total: ${total} USD (Without taxes)`
        });
         total.toFixed(2);
         
        // Loop through the cart items and create rows for each
        if (Object.entries(cart).length == 0) {
            pc_cart_list.innerHTML = `<p id="empty_cart">Your cart is empty for now, want to explore <a href="/products">Products</a>?</p>`;
            mobile_cart_list.innerHTML = `<p id="empty_cart">Your cart is empty for now, want to explore <a href="/products">Products</a>?</p>`;
            
        }
        for (const [productId, item] of Object.entries(cart)) {
            
            
            const totalPrice = (parseFloat(item.price) * item.quantity).toFixed(2);
            let item_content = `
                <div id="item">
                    <div id="img">
                        <img src="${item.image}">
                        
                    </div>
                    <div id="description">
                        <p class="name">${item.name}</p>
                        <p class="price">${item.price} USD</p>
                    </div>
                    <div id="amount">
                        <svg class="cursor" onclick="addToCart(${productId})"  width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="8" cy="8" r="8" fill="#CDE8E5"/>
                            <path d="M7.10086 5.84721C7.46582 5.09743 8.53418 5.09743 8.89914 5.84721L9.96 8.02667L10.7791 9.62204C11.2015 10.4447 10.3767 11.3507 9.51811 11.0073L8.37135 10.5486C8.13293 10.4532 7.86697 10.4532 7.62856 10.5486L6.48191 11.0072C5.62327 11.3507 4.79853 10.4447 5.22091 9.62201L6.04 8.02667L7.10086 5.84721Z" fill="black"/>
                        </svg>
                        <p id="unit">${item.quantity}</p>
                        <svg class="cursor" onclick="decrementCart(${productId})" style="transform: rotate(180deg)" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="8" cy="8" r="8" fill="#CDE8E5"/>
                            <path d="M7.10086 5.84721C7.46582 5.09743 8.53418 5.09743 8.89914 5.84721L9.96 8.02667L10.7791 9.62204C11.2015 10.4447 10.3767 11.3507 9.51811 11.0073L8.37135 10.5486C8.13293 10.4532 7.86697 10.4532 7.62856 10.5486L6.48191 11.0072C5.62327 11.3507 4.79853 10.4447 5.22091 9.62201L6.04 8.02667L7.10086 5.84721Z" fill="black"/>
                        </svg>                                            
                    </div>
                    <div id="delete" class="cursor" onclick="removeFromCart(${productId})">
                        <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                            <rect width="14" height="20" fill="url(#pattern0_132_43)"/>
                            <defs>
                            <pattern id="pattern0_132_43" patternContentUnits="objectBoundingBox" width="1" height="1">
                            <use xlink:href="#image0_132_43" transform="matrix(0.014881 0 0 0.0104167 -0.214286 0)"/>
                            </pattern>
                            <image id="image0_132_43" width="96" height="96" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAADIklEQVR4nO2dOayMURiG31xBaU0QEQkay43OUhGJwtIIUVkrokN3LVEQKpSWDo0QW2K5GqKxlZZG0LmREHcpZC73vvIlv0ZMcsecc+b9ft+TPO1kznOS/5/M/80ZIAiCIAiCIAiCQItpAA4BeAbgKwCO0S8AngLoATC104vwynYA/S1Eb6a9xrZOL8YbRxOE/1N7zWAMHMsQ/7en6rIDiwHcATCQMRadaA1uA1hUKn43gCGBhVPMoapNdh4KLJai9uaOPw7AsMBCKepw1Sg2ADXdACMuQWi6AQ9QgLgJ46/xB0vdhFF95LoF4JvAdZcd1hrcBLCwVPwgCIIgCIIgCAJUz235n9mjtPU7BIKwsPbMWobVAkFY2FUQYr5AEBZ2HoSYAGBEIAoLOVKtWYo+gTAs5CcI8kIgDAv5HIJcFwjDQl6DIGcEwrCQpyHIAYEwLOR+CLJFIAwLuRmCLBcIw0IugyCzBMKwkDMhSBeAhkAcZrZRrVWSDwKBmNn3EOaxQCBm9hGEuSwQiJm9BGFOCARiZo9DmL0CgZjZPRBmg0AgZnY9hOkWCMTMLoEwkwUCMbOTIM5AzX8DIM8bgVDM5Cs44L5AKGbyHhxwQSAUM3kODjgiEIqZtAlAeXYKhGImbQJQnjUCoZhJmwCUZ4FAKGbSJgDlmQhgVCAWEztarc0FnwWCMbE2+eeGlwLBmFib/HPDDYFgTKxN/rnhrEAwJtYm/9xwUCAYE2uTf27YKhCMibXJPzesEAjGxNrknxtmCwRjYm3yzw1dNTtbrqE8DdeMjwLhmEib+HPHE4FwTKRN/LnjikA4JtIm/txxUiAcE2kTf+7YJxCOibSJP3dsFAjHRNrEnzuWCoRjIoudB5qSKQLhmEib+HNJHY65H4Rj3goEZJu+hmN6BQKyTW3Szy0XBQKyTc/DMTn+DYmFPQzH1OH4gk1wzAwAPwQiso2voafDOVcFQvIftS8U3TO3+ixNZ/YDmIOasBbAd4GobOHSsw41Y2V1zgLFfeftAXwr2FGPu6uf+vSJHHX5s3ovdwHsAjC+05GCIAiCIAiCIECt+QWhxg3O/REwaQAAAABJRU5ErkJggg=="/>
                            </defs>
                            </svg>
                                                                     
                    </div>
                </div>
            `;


            let mobile_item_content = `
            <div id="item">
                <div id="img">
                    <img src="${item.image}">
                    
                </div>
                <div id="description">
                    <p class="name">${item.name}</p>
                    <p class="price">${item.price} USD</p>
                </div>
                <div id="amount">
                    <svg onclick="addToCart(${productId})" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="8" cy="8" r="8" fill="#CDE8E5"/>
                        <path d="M7.10086 5.84721C7.46582 5.09743 8.53418 5.09743 8.89914 5.84721L9.96 8.02667L10.7791 9.62204C11.2015 10.4447 10.3767 11.3507 9.51811 11.0073L8.37135 10.5486C8.13293 10.4532 7.86697 10.4532 7.62856 10.5486L6.48191 11.0072C5.62327 11.3507 4.79853 10.4447 5.22091 9.62201L6.04 8.02667L7.10086 5.84721Z" fill="black"/>
                    </svg>
                    <p id="unit">${item.quantity}</p>
                    <svg onclick="decrementCart(${productId})" style="transform: rotate(180deg)" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="8" cy="8" r="8" fill="#CDE8E5"/>
                        <path d="M7.10086 5.84721C7.46582 5.09743 8.53418 5.09743 8.89914 5.84721L9.96 8.02667L10.7791 9.62204C11.2015 10.4447 10.3767 11.3507 9.51811 11.0073L8.37135 10.5486C8.13293 10.4532 7.86697 10.4532 7.62856 10.5486L6.48191 11.0072C5.62327 11.3507 4.79853 10.4447 5.22091 9.62201L6.04 8.02667L7.10086 5.84721Z" fill="black"/>
                    </svg>                                            
                </div>
                <div id="delete" onclick="removeFromCart(${productId})">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                        <rect width="14" height="20" fill="url(#pattern0_1124332_43)"/>
                        <defs>
                        <pattern id="pattern0_1124332_43" patternContentUnits="objectBoundingBox" width="1" height="1">
                        <use xlink:href="#image0_132_43" transform="matrix(0.014881 0 0 0.0104167 -0.214286 0)"/>
                        </pattern>
                        <image id="image0_132_43" width="96" height="96" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAADIklEQVR4nO2dOayMURiG31xBaU0QEQkay43OUhGJwtIIUVkrokN3LVEQKpSWDo0QW2K5GqKxlZZG0LmREHcpZC73vvIlv0ZMcsecc+b9ft+TPO1kznOS/5/M/80ZIAiCIAiCIAiCQItpAA4BeAbgKwCO0S8AngLoATC104vwynYA/S1Eb6a9xrZOL8YbRxOE/1N7zWAMHMsQ/7en6rIDiwHcATCQMRadaA1uA1hUKn43gCGBhVPMoapNdh4KLJai9uaOPw7AsMBCKepw1Sg2ADXdACMuQWi6AQ9QgLgJ46/xB0vdhFF95LoF4JvAdZcd1hrcBLCwVPwgCIIgCIIgCAJUz235n9mjtPU7BIKwsPbMWobVAkFY2FUQYr5AEBZ2HoSYAGBEIAoLOVKtWYo+gTAs5CcI8kIgDAv5HIJcFwjDQl6DIGcEwrCQpyHIAYEwLOR+CLJFIAwLuRmCLBcIw0IugyCzBMKwkDMhSBeAhkAcZrZRrVWSDwKBmNn3EOaxQCBm9hGEuSwQiJm9BGFOCARiZo9DmL0CgZjZPRBmg0AgZnY9hOkWCMTMLoEwkwUCMbOTIM5AzX8DIM8bgVDM5Cs44L5AKGbyHhxwQSAUM3kODjgiEIqZtAlAeXYKhGImbQJQnjUCoZhJmwCUZ4FAKGbSJgDlmQhgVCAWEztarc0FnwWCMbE2+eeGlwLBmFib/HPDDYFgTKxN/rnhrEAwJtYm/9xwUCAYE2uTf27YKhCMibXJPzesEAjGxNrknxtmCwRjYm3yzw1dNTtbrqE8DdeMjwLhmEib+HPHE4FwTKRN/LnjikA4JtIm/txxUiAcE2kTf+7YJxCOibSJP3dsFAjHRNrEnzuWCoRjIoudB5qSKQLhmEib+HNJHY65H4Rj3goEZJu+hmN6BQKyTW3Szy0XBQKyTc/DMTn+DYmFPQzH1OH4gk1wzAwAPwQiso2voafDOVcFQvIftS8U3TO3+ixNZ/YDmIOasBbAd4GobOHSsw41Y2V1zgLFfeftAXwr2FGPu6uf+vSJHHX5s3ovdwHsAjC+05GCIAiCIAiCIECt+QWhxg3O/REwaQAAAABJRU5ErkJggg=="/>
                        </defs>
                        </svg>
                        
                                                                    
                </div>
            </div>`
           
            pc_cart_list.innerHTML += item_content;
            mobile_cart_list.innerHTML += mobile_item_content;
            
        }
    })
    .catch(error => console.error('Error fetching cart:', error));
}
