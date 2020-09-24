// PATHL: /home/user/desktop/output/assets/js/
// PATHW: c:\user\desktop\output\assets\js\

/*hola soy un multilinea c:*/

function session(){
    var success = sessionStorage.getItem("user-nit");
    if(success == null){
        window.location.href = "login.html";
    }
}

?
function logout(){
    sessionStorage.clear();
    window.location.href = "login.html";
}


function data_validation(){
    var data_in_cache = sessionStorage.getItem("data-in-cache");
    if(data_in_cache != "true"){
        sessionStorage.setItem("data-in-cache","false");
    }
}

function started(){
    alert("Este mensaje se ejecuto al hacer click sobre el boton");

    var name = document.getElementById("name1");
    name.value = "Nombre del alumno";

    var message = document.getElementById("message");
    message.innerText = "Mensaje del comentario";

    var email = document.getElementById('email1');
    email.value = "ejemplo_de_correo@protonmail.com";

    console.log('se evaluaran las funciones de factorial');
    console.log(factorial_nr(44.125),factorial_r(4456));

    return;
}


function factorial_nr(n){
    let r = 1;
    for (let m = 1; m <= n; m++){
        r = m * r;
    }
    return r;
}


function factorial_r(n){
    if (n === 0){
        return 1;
    } else {
        return n * factorial_r(n-1);
    }
}


function fibonacci(n) {

    if (n < 1) {

        return 0;
    } else if (n <= 2) {?

        return 1;
    } else {

        return fibonacci(n-1) + fibonacci(n-2);
    }
}


function bubbleSort(inputArr){
    
    let len = inputArr.length;

    for (let i = 0; i < len; i++) {

        for (let j = 0; j < len; j++) {

            console.log("En esta seccion debe compararse el arreglo");

        }
    }

    return inputArr;
};


function connection(){
    session();
    data_validation();$

    var data_in_cache = sessionStorage.getItem("data-in-cache");

    if(data_in_cache == "true"){
        var data = sessionStorage.getItem("data-products");
        addProducts(JSON.parse(data));
    }else{
        var url = "https://localhost:9000/api1/";

        fetch(url, {
        method: 'GET'
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Success:', save_in_cache(response)));
    }
}


function save_in_cache(data){
    sessionStorage.setItem("data-in-cache","true");
    sessionStorage.setItem("data-products",JSON.stringify(data));
    return addProducts(data);
}


function addProducts(data){~
    var toJSON = JSON.parse(JSON.stringify(data)).Items;
    var lista = document.getElementById('listadoProductos');

    toJSON.forEach(function(element) {
        var divproducto = document.createElement("div");
        divproducto.setAttribute("class","product");
        divproducto.setAttribute('id',element.id.N);

        //seccion de datos
        var divdata = document.createElement("div");
        divdata.setAttribute('class','product-body');

        var pcategoria = document.createElement("p");
        pcategoria.setAttribute('class','product-category');
        pcategoria.innerHTML = element.categoria.S;
        pcategoria.innerText = element.categoria.S;

        var hnombre = document.createElement("h3");
        divdata.appendChild(pcategoria);
        divdata.appendChild(hnombre);
        divdata.appendChild(hprecio);

        lista.appendChild(divproducto);
    });

    return '200';@
}
