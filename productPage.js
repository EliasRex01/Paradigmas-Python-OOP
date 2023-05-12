

// 
function loadProduct() {
    let productImg = JSON.parse(localStorage.getItem("product"))
    let content = document.querySelector(".productPage")
    content.innerHTML = `
    <div class="productImg cardImg">
        <img src="${productImg.itemImg}">
    </div>
    <div class="productInfo m-5">
        <h2>${productImg.itemTitle}</h2>
        <h5>${productImg.itemDesc}</h5>
        <span>${productImg.itemPrice}</span>
        <button type="button" class="btn btn-outline-primary mt-4" onclick="addToCart(this)">Add to Cart</button>
    </div>
    `
}


function addToCart(element) {

    cartNumbers()
    let productInfo = element.parentElement.parentElement
    // console.log(productInfo);
    let results = {
        id: cartItem,
        itemImg: productInfo.querySelector(".productImg img").src,
        itemTitle: productInfo.querySelector(".productInfo h2").textContent,
        itemDesc: productInfo.querySelector(".productInfo h5").textContent,
        itemPrice: productInfo.querySelector(".productInfo span").textContent
    }
    cartItem++
    saveProductInStorage(results)
    let costItem = parseInt(results.itemPrice)
    let costInStorage = parseInt(JSON.parse(localStorage.getItem("totalPrice")))
    if (costInStorage) {
        let sum = costItem + costInStorage
        localStorage.setItem("totalPrice", sum)
    } else {
        localStorage.setItem("totalPrice", costItem)
    }
}

loadProduct()