// Get form-stock data
async function FormStockData() {
    this.template = {
        showDetails: async () => {

            let privateProductStorage = "";
            privateProductStorage = localStorage.getItem('stockKey');
            const FORMSTOCK = document.querySelector('#formStock');

            async function getStockData() {
                const response = await fetch(`/fetch_stock_product/${privateProductStorage}/`);
                const data = await response.json();
                return data;
            }

            let titulo = document.getElementsByClassName('result-title')[0];
            titulo.innerHTML = '';
            titulo.innerHTML = '<h2>Editar Almacen</h2>';

            privateProductStorage = await getStockData();

            document.getElementById("producto").value = privateProductStorage.stock.product_name;
            document.getElementById("cantidad").value = privateProductStorage.stock.amount;

            FORMSTOCK.addEventListener('submit', async (e) => {
                e.preventDefault();

                if(document.getElementById('producto').value !== '' && document.getElementById('cantidad').value !== ''){
                    const form = new FormData();
                    form.append('producto', privateProductStorage.stock.product);
                    form.append('cantidad', document.getElementById('cantidad').value);

                    try {
                        const data = await mandarData('http://127.0.0.1:8000/edit_stock/', form);
                        if (data.status === 200) {
                            showModal('Almacen actualizado <br> correctamente', 'fas fa-check-circle', '/stock/');
                        } else {
                            showModal('Ocurrió un error, <br> intenta de nuevo', 'fas fa-times',);
                        }
                    } catch (error) {
                        console.log(error)
                    }

                } else {
                    showModal('Llena todos los <br> campos', 'fas fa-times',);
                }
            })

            console.log(privateProductStorage.category);
        }
    }
    return this.template;
}