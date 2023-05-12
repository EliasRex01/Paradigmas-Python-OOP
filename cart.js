

// 
function loadProductsInCart() {
    let productsInStorage = JSON.parse(localStorage.getItem("products"))
    let products = document.querySelector(".contentProducts")
    for(let i = 0; i < productsInStorage.length; i++) {
        // console.log(productsInStorage[i]);
        products.innerHTML += `
        <div class="product">
            <img src="${productsInStorage[i].itemImg}">
            <div class="title">${productsInStorage[i].itemTitle}</div>
            <div class="price">Price: <span>${productsInStorage[i].itemPrice}</span></div>
            <div class="totalPrice">Total Price: <span>${productsInStorage[i].itemPrice}</span></div>
            </div>
        `
    }
    // console.log(productsInStorage.length);
}



function totalCostFinc() {
    let totalSpan = document.querySelector(".totalCost span")
    totalSpan.innerHTML = JSON.parse(localStorage.getItem("totalPrice"))
}


// 
function discountCouponsFunc() {
    let totalSpan = document.querySelector(".totalCost span").textContent
    let result1 = (totalSpan * 0.1)
    let result2 = totalSpan - result1
    localStorage.setItem("totalPrice", result2)
}



// 
function successFunc() {
    let string = "Your order was successfully"
    let price = localStorage.getItem("totalPrice")
    let chars = "1234567890",
        serialLenght = 6,
        randomSerial = '';
    
    for (let i = 0; i < serialLenght; i++) {
        
        let randomNumber = Math.floor(Math.random() * chars.length);
        
        randomSerial += chars.substring(randomNumber, randomNumber + 1);
    }
    confirm(string + "\n" + "Total Cost for your order is: " + price + "$" + "\n" + "reference number is: " + randomSerial)
}

// 
totalCostFinc()
loadProductsInCart()