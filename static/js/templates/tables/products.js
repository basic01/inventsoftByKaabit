function ViewEmployeeProductsTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-box-open"></i>
                        <h2>Registros - Productos</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'productos')">Crear reporte</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Precio</th>
                                <th scope="col">Categoría</th>
                                <th scope="col">Proveedor</th>
                            </thead>
                            <tbody>`;
                            this.template += getProductsEmployeeData(data);
                            this.template += `</tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminProductsTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-box-open"></i>
                        <h2>Registros - Productos</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-products/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'productos')">Crear reporte</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Acciones</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Precio</th>
                                <th scope="col">Categoría</th>
                                <th scope="col">Proveedor</th>
                            </thead>
                            <tbody>`;
                                this.template += getProductsAdminData(data);
                                this.template += `</tbody
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}


function ViewStockProductsTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-box-open"></i>
                        <h2>Registros - Productos</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-products/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'productos')">Crear reporte</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Precio</th>
                                <th scope="col">Categoría</th>
                                <th scope="col">Proveedor</th>
                            </thead>
                            <tbody>`;
                                this.template += getProductsEmployeeData(data);
                                this.template += `</tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}