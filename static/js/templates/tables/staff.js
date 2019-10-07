function ViewAdminAreaStaffTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-users"></i>
                        <h2>Registros - Personal</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-staff/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'personal')">Crear reporte</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Correo</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Apellido(s)</th>
                                <th scope="col">Fecha Inicio</th>
                            </thead>
                            <tbody>`;
                                this.template += getStaffAdminAreaData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewSuperAdminStaffTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-users"></i>
                        <h2>Registros - Personal</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-staff-admin/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn" onclick="getPDF('table', 'personal')">Crear reporte</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Acciones</th>
                                <th scope="col">Correo</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Apellido(s)</th>
                                <th scope="col">Fecha Inicio</th>
                                <th scope="col">Area</th>
                                <th scope="col">Super Admin</th>
                                <th scope="col">Area Admin</th>
                                <th scope="col">Empleado</th>
                            </thead>
                            <tbody>`;
                                this.template += getStaffSuperAdminData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}