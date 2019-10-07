// Get form-products data
async function FormProductData() {
    this.template = {
        showDetails: async () => {
            
            let privateProductStorage = "";
            async function getCatAndProvData() {
                const response = await fetch('/categories_and_providers/');
                const data = await response.json();
                return data;
            }
            const data = await getCatAndProvData();
            function addOptions(selectName, data) {
                selectElement = document.getElementById(selectName);
                for (let i = 0; i < data.length; i++) {
                    const optionElement = document.createElement('option');
                    setAttributes(optionElement, {
                        value: data[i].key,
                    });
                    optionElement.innerHTML = data[i].name;
                    selectElement.appendChild(optionElement);
                }
            }
            addOptions('categoria', data.categories);
            addOptions('proveedor', data.providers);
            const precio = new Cleave('#precio', {
                blocks: [10],
                uppercase: true
            });
            const cantidad = new Cleave('#cantidad', {
                blocks: [10],
                uppercase: true
            });
            const FORMPRODUCTO = document.querySelector('#formProducto');
            if (localStorage.getItem('productKey')) {
                privateProductStorage = localStorage.getItem('productKey');
                let titulo = document.getElementsByClassName('result-title')[0];
                titulo.innerHTML = '';
                titulo.innerHTML = '<h2>Editar Producto</h2>';
                async function getProductData() {
                    const response = await fetch(`/fetch_product/${privateProductStorage}/`);
                    const data = await response.json();
                    return data.product;
                }
                privateProductStorage = await getProductData();
                document.getElementById("nombre").value = privateProductStorage.name;
                document.getElementById("descripcion").value = privateProductStorage.description;
                document.getElementById("precio").value = privateProductStorage.price;
                document.getElementById("categoria").value = privateProductStorage.category;
                document.getElementById("proveedor").value = privateProductStorage.provider;
                document.getElementById("cantidad").value = privateProductStorage.amount;
            }
            FORMPRODUCTO.addEventListener('submit', async (e) => {
                e.preventDefault();
                if (document.getElementById('nombre').value !== '' && document.getElementById('descripcion').value !== '' && document.getElementById('precio').value !== '' && document.getElementById('categoria').value !== '' && document.getElementById('proveedor').value !== '' && document.getElementById('cantidad').value !== '') {
                    const form = new FormData();
                    form.append('nombre', document.getElementById('nombre').value);
                    form.append('descripcion', document.getElementById('descripcion').value);
                    form.append('precio', document.getElementById('precio').value);
                    form.append('categoria', document.getElementById('categoria').value);
                    form.append('proveedor', document.getElementById('proveedor').value);
                    form.append('cantidad', document.getElementById('cantidad').value);
                    if (privateProductStorage) {
                        form.append('accion', 'EDIT');
                        form.append('id', privateProductStorage.product_key);
                    }
                    else {
                        form.append('accion', 'NEW');
                    }
                    try {
                        const data = await mandarData('http://127.0.0.1:8000/post_product/', form);
                        if (data.status === 200) {
                            if (privateProductStorage) {
                                localStorage.removeItem('productKey');
                                showModal('Producto actualizado <br> correctamente', 'fas fa-check-circle', '/products/');
                            }
                            else {
                                showModal('Producto registrado <br> exitosamente', 'fas fa-check-circle', '/products/');
                            }
                        }
                        else {
                            showModal('Ocurrió un error, <br> intenta de nuevo', 'fas fa-times',);
                        }
                    }
                    catch (error) {
                    }
                }
                else {
                    showModal('Llena todos los <br> campos', 'fas fa-times',);
                }
            });
        }
    };
    return this.template;
}
