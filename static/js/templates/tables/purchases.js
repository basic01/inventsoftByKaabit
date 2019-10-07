function ViewEmployeePurchasesTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-store"></i>
                        <h2>Registros - Compras</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-purchases/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'compras')">Crear reporte</button>
                        <button id="csv" class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Producto</th>
                                <th scope="col">Cantidad</th>
                                <th scope="col">Cliente</th>
                                <th scope="col">Total</th>
                                <th scope="col">Comprador</th>
                                <th scope="col">Fecha Compra</th>
                            </thead>
                            <tbody>`;
                                this.template += getPurchasesEmployeeData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminPurchasesTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-store"></i>
                        <h2>Registros - Compras</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-purchases/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'compras')">Crear reporte</button>
                        <button id="csv" class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Acciones</th>
                                <th scope="col">Producto</th>
                                <th scope="col">Cantidad</th>
                                <th scope="col">Cliente</th>
                                <th scope="col">Total</th>
                                <th scope="col">Comprador</th>
                                <th scope="col">Fecha Compra</th>
                            </thead>
                            <tbody>`;
                                this.template += getPurchasesAdminData(data);
                                this.template += `</tbody
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}