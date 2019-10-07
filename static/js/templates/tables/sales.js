function ViewEmployeeSalesTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-dollar-sign"></i>
                        <h2>Registros - Ventas</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-sales/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'ventas')">Crear reporte</button>
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
                                <th scope="col">Vendedor</th>
                                <th scope="col">Fecha Venta</th>
                            </thead>
                            <tbody>`;
                                this.template += getSalesEmployeeData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminSalesTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-dollar-sign"></i>
                        <h2>Registros - Ventas</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-sales/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'ventas')">Crear reporte</button>
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
                                <th scope="col">Vendedor</th>
                                <th scope="col">Fecha Venta</th>
                            </thead>
                            <tbody>`;
                                this.template += getSalesAdminData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}