const BasketLogic = {
    url: `/api/basketitem/`,

    addProduct(productId, quantity) {
        return fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
                'quantity': quantity,
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
            document.getElementById('cart-sidebar').innerHTML = "";
            getCart();
        });
    },
}

const addToBasket = document.querySelectorAll('.add-to-basket');
addToBasket.forEach(item => {
    item.addEventListener('click', function (e) {
        e.preventDefault();
        const productId = this.getAttribute('data');
        let quantity = document.getElementById('qty');
        quantity = quantity ? parseInt(quantity.value) : 1;
        BasketLogic.addProduct(productId, quantity);
    });
});



let addFromWishlist = document.getElementsByClassName('add-from-wishlist');
for (let i = 0; i < addFromWishlist.length; i++) {
    addFromWishlist[i].onclick = function () {
        const productId = this.getAttribute('data');
        const quantity = 1;
        BasketLogic.addProduct(productId, quantity);

    }
}


function getCart() {
    fetch(`/api/basketitem/`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    }).then(response => response.json()).then(data => {
        console.log(data);
        let cart = document.getElementById('cart-sidebar');
        let total = 0;
        data.forEach(item => {
            total += item.price * item.quantity;
            cart.innerHTML += `
                <div class="cart-item">

                    <div class="cart-info">
                        <h4>${item.product.title}</h4>
                        <p>${item.quantity} x ${item.price} = ${item.price * item.quantity}</p>
                    </div>
                    <div class="cart-close">
                        <i class="fa fa-times" aria-hidden="true" onclick="deleteItem(${item.id})"></i>
                    </div>
                </div>
                `
        })
        cart.innerHTML += `
            <div class="cart-total">
                <h3>Total: <span>${total}</span></h3>
            </div>
            `
    });
}


window.addEventListener('DOMContentLoaded', () => {
    getCart();
});


// function deleteItem(id) {
//     fetch(`/api/basketitem/${id}`, {
//         method: 'DELETE',
//         credentials: 'include',
//         headers: {
//             'Content-type': 'application/json',
//             'Authorization': `Bearer ${localStorage.getItem('token')}`
//         },
//     }).then(response => response.json()).then(data => {
//         console.log(data);
//         document.getElementById('cart-sidebar').innerHTML = "";
//         getCart();
//     });
// }

// function removeItemCart() {
// 	var removeItemFromBasket = document.getElementsByClassName('remove-item')
// 	for (let i = 0; i < removeItemFromBasket.length; i++) {
// 		removeItemFromBasket[i].onclick = function () {
// 			console.log(removeItemFromBasket[i]);
// 			const productId = this.getAttribute('data_id');
// 			const action = 'remove'
// 			BasketLogic.addProduct(productId, action, quantity=1);
// 		}
// 	}
// }