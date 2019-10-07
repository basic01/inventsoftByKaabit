function getDashboardTitle(area){
    if(area === 'AV' || area === 'AAVEN'){
        return `Dashboard - Ventas</h2>`;
    }
    if(area === 'AC' || area === 'AACOM'){
        return `Dashboard - Compras`;
    }
    if(area === 'AA' || area === 'AAALM'){
        return `Dashboard - Almacen`;
    }
    if(area === 'SADMI'){
        return 'Dashboard';
    }
}

function ViewDashboard(user){
    const title = getDashboardTitle(user.area);
    this.template = `
        <div class="container-fluid main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-table"></i>
                        <h2 id="dashboard-title">${title}</h2>
                    </div>
                    <div class="row dashboard-container">
                        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
                            <a href="/products/">
                                <i class="fas fa-box-open"></i>
                                <span>Productos</span>
                            </a>
                        </div>
                    `;
                    const type = getUserType(user);
                    view = new UserViewFactory(new ViewSuperAdminDashboard(),
                                            new ViewAreaAdminDashboard(user.area),
                                            new ViewEmployeeDashboard(user.area),
                                            ).create(type);
                    this.template += view.template;
                    
                    this.template += `
                        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
                            <a href="/notifications/">
                                <i class="fas fa-bell"></i>
                                <span>Notificaciones</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    return this.template;
}

function ViewEmployeeDashboard(area){
    if(area === 'AV' || area === 'AAVEN'){
        this.template = `
            <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
                <a href="/sales/">
                    <i class="fas fa-dollar-sign"></i>
                    <span>Ventas</span>
                </a>
            </div>
        `;
    }
    if(area === 'AC' || area === 'AACOM'){
        this.template = `
            <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
                <a href="/purchases/">
                    <i class="fas fa-store"></i>
                    <span>Compras</span>
                </a>
            </div>
        `;
    }
    if(area === 'AA' || area === 'AAALM'){
        this.template = `
            <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
                <a href="/stock/">
                    <i class="fas fa-cubes"></i>
                    <span>Almacén</span>
                </a>
            </div>
        `;
    }
    if(area === 'AAVEN' || area === 'AACOM' || area === 'AAALM') {
        return this.template;
    }
}

function ViewAreaAdminDashboard(area){
    const areaOption = new ViewEmployeeDashboard(area);
    this.template = areaOption.template;
    this.template += `
        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
            <a href="/staff/">
                <i class="fas fa-users"></i>
                <span>Personal</span>
            </a>
        </div>
    `;
}

function ViewSuperAdminDashboard(){
    this.template = `
        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
            <a href="/sales/">
                <i class="fas fa-dollar-sign"></i>
                <span>Ventas</span>
            </a>
        </div>

        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
            <a href="/purchases/">
                <i class="fas fa-store"></i>
                <span>Compras</span>
            </a>
        </div>

        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
            <a href="/stock/">
                <i class="fas fa-cubes"></i>
                <span>Almacén</span>
            </a>
        </div>

        <div class="col-lg-3 col-12 col-sm-4 dashboard-option">
            <a href="/staff/">
                <i class="fas fa-users"></i>
                <span>Personal</span>
            </a>
        </div>
    `;
}