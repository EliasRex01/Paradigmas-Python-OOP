const url = 'products.json'
let cartItem = 1


async function getInfo() {
    try {
        let res = await fetch(url)
        const data = await res.json()
        showInfo(data)
    } catch (err) {
        console.log(err);
    }
}

function showInfo(data) {

    // Sections Part
    let listSections = document.getElementById("f-list")
    let sectionResult = data.secionImg
    for (let i = 0; i < sectionResult.length; i++) {
        listSections.innerHTML += `
            <li>
                <img src="${sectionResult[i].image}" width="65" height="65">
                <span>${sectionResult[i].title}</span>
            </li>
        `
    }


    // Trending Products
    let trendsPro = document.querySelector(".trendProducts")
    let trendsResult = data.trendProducts
    for (let i = 0; i < trendsResult.length; i++) {
        trendsPro.innerHTML += `
        <div class="col">
            <div class="card">
                <img src="${trendsResult[i].image}" class="card-img-top p-3" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${trendsResult[i].title}</h5>
                    <p class="card-text">${trendsResult[i].price}</p>
                    <p class="card-text desc" style="display: none">${trendsResult[i].desc}</p>
                    <a href="#" class="btn btn-primary" onclick="show(this)">Add to Card</a>
                </div>
            </div>
        </div>
        `
    }





    // men Products part
    let menItems = document.querySelector(".menItems")
    let mentItemProducts = data.menImg
    for (let i = 0; i < mentItemProducts.length; i++) {
        menItems.innerHTML += `
        <div class="col">
            <div class="card">
                <img src="${mentItemProducts[i].image}" class="card-img-top p-3" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${mentItemProducts[i].title}</h5>
                    <p class="card-text">${mentItemProducts[i].price}</p>
                    <p class="card-text desc" style="display: none">${mentItemProducts[i].desc}</p>
                    <a href="#" class="btn btn-primary" onclick="show(this)">Add to Card</a>
                    <a href="#" class="btn btn-light" onclick="productPage(this)">Product Info</a>
                </div>
            </div>
        </div>
        `
        // <p>${mentItemProducts[i].desc}</p>
        // console.log(nn);
    }



    // 
    let womenItems = document.querySelector(".womenItems")
    let womenItemProducts = data.womenImg 
    // console.log(womenItemProducts);
    for (let i = 0; i < womenItemProducts.length; i++) {
        womenItems.innerHTML += `
        <div class="col">
            <div class="card">
                <img src="${womenItemProducts[i].image}" class="card-img-top p-3" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${womenItemProducts[i].title}</h5>
                    <p class="card-text">${womenItemProducts[i].price}</p>
                    <p class="card-text desc" style="display: none">${mentItemProducts[i].desc}</p>
                    <a href="#" class="btn btn-primary" onclick="show(this)">Add to Card</a>
                    <a href="#" class="btn btn-light" onclick="productPage(this)">Product Info</a>
                </div>
            </div>
        </div>
        `
    }




    // 
    let brandsSection = document.querySelector(".brandsSection")
    let brands = data.brandImg
    // console.log(brands);
    for (let i = 0; i < brands.length; i++) {
        brandsSection.innerHTML += `
        <div class="col-md-3 col-sm-4 col-6">
            <a class="d-block bg-white shadow-sm rounded-3 py-3 py-sm-4 mb-grid-gutter" href="${brands[i].url}" target="_blank"><img class="d-block mx-auto" src="${brands[i].image}" style="width: 150px;" alt="Brand">
            </a>
        </div>
        `
    }


    let kindSection = document.querySelector(".kindSection")
    let kidsItemProducts = data.kindImg
    // console.log(kidsItemProducts);
    for (let i = 0; i < kidsItemProducts.length; i++) {
        kindSection.innerHTML += `
            <div class="col">
                <div class="card">
                    <img src="${kidsItemProducts[i].image}" class="card-img-top p-3" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${kidsItemProducts[i].title}</h5>
                        <p class="card-text">${kidsItemProducts[i].price}</p>
                        <p class="card-text desc" style="display: none">${mentItemProducts[i].desc}</p>
                        <a href="#" class="btn btn-primary" onclick="show(this)">Add to Card</a>
                        <a href="#" class="btn btn-light" onclick="productPage(this)">Product Info</a>
                    </div>
                </div>
            </div>
        `
    }

}


function show(element) {

    cartNumbers()
    let productInfo = element.parentElement.parentElement
    let results = {
        id: cartItem,
        itemImg: productInfo.querySelector(".card img").src,
        itemTitle: productInfo.querySelector(".card-title").textContent,
        itemDesc: productInfo.querySelector(".desc").textContent,
        itemPrice: productInfo.querySelector(".card-text").textContent
    }
    cartItem++
    saveProductInStorage(results)
    totlaPriceFunc(parseInt(results.itemPrice))
}


function cartNumbers() {
    let productNumbers = localStorage.getItem("cartNumbers")
    productNumbers = parseInt(productNumbers)

    if(productNumbers) {
        localStorage.setItem("cartNumbers", productNumbers + 1)
        document.querySelector(".collapse span").textContent = productNumbers + 1
    } else {
        localStorage.setItem("cartNumbers", 1)
        document.querySelector(".collapse span").textContent = 1
    }
}

function onLoadPage() {
    let productNumbers = localStorage.getItem("cartNumbers")
    if(productNumbers) {
        document.querySelector(".collapse span").textContent = productNumbers
    }
    // localStorage.removeItem("product")
}



// save Product
function saveProductInStorage(item) {
    let products = getProductsFromStorage()
    products.push(item)
    localStorage.setItem("products", JSON.stringify(products))
}
// get Product
function getProductsFromStorage(item) {
    return localStorage.getItem("products") ? JSON.parse(localStorage.getItem("products")) : []

}


function productPage(element) {
    let productInfo = element.parentElement.parentElement
    let results = {
        id: cartItem,
        itemImg: productInfo.querySelector(".card img").src,
        itemTitle: productInfo.querySelector(".card-title").textContent,
        itemDesc: productInfo.querySelector(".desc").textContent,
        itemPrice: productInfo.querySelector(".card-text").textContent
    }
    cartItem++
    localStorage.setItem("product", JSON.stringify(results))
    window.location.replace("productPage.html")
}


// 
function totlaPriceFunc(ele) {

    // localStorage.setItem("totalPrice", 0)
    let priceInStorage = parseInt(JSON.parse(localStorage.getItem("totalPrice")))
    if (priceInStorage) {
        let totalPrice = priceInStorage + ele
        localStorage.setItem("totalPrice", totalPrice)
    } else {
        localStorage.setItem("totalPrice", ele)
    }

    // console.log(priceInStorage);
    // totalPrice = ele + totalPrice
    // // let price = ele
    // // totalPrice = price + totalPrice
    // alert("Current Total Price is: " + totalPrice)
    // localStorage.setItem("totalPrice", totalPrice)
}


// 
function loadProductsInCart() {
    let products = localStorage.getItem("products")
    console.log(products);
}


// exicute
onLoadPage()


 