'use strict';

window.addEventListener('load', function(){
    firebase.auth().onAuthStateChanged(function(user){
        document.getElementById('formSubmit').onclick = function() {
            var userID = user.uid;
            var userAddress = document.getElementById('addressInput').value;
            var userPostcode = document.getElementById('postcodeInput').value;
            var productID = document.getElementById('productIdText').innerText;
            var postBody = {
                "id": userID,
                "address": userAddress,
                "postcode": userPostcode,
                "product_id": productID
            };
            console.log(postBody);

            // Start HTTP request
            var xhr = new XMLHttpRequest();
            xhr.open("POST", '/order', true); // asynchronous
            xhr.setRequestHeader('Content-Type', 'application/json'); // indicates body of post is JSON data
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    console.log("Success");
                }
            };

            xhr.send(JSON.stringify(postBody));
        }
    });
});