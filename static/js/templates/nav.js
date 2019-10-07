function ViewNav(user){
    this.template = `
        <nav class="nav">
            <label>&copy Inventsoft</label>
            <div class="active-user-container">
                <p>Bienvenido, 
                    <button id="active-user" onclick="changeClass('nav-logout-show', 'nav-logout')">
                        ${user.first_name} ${user.last_name}
                    </button>
                </p>
            </div>
        </nav>

        <div class="nav-logout" id="nav-logout">
            <a href="/logout">Cerrar Sesión</a>
        </div>

        <section class="options-container" id="options-container">
            <a href="/dashboard/" class="option">
                <i class="fas fa-table"></i>
                <span>Dashboard</span>
            </a>

            <a href="/products/" class="option">
                <i class="fas fa-box-open"></i>
                <span>Productos</span>
            </a>`;

            const type = getUserType(user);
            view = new UserViewFactory(new ViewSuperAdminNav(),
                                       new ViewAreaAdminNav(user.area),
                                       new ViewEmployeeNav(user.area),
                                       ).create(type);
            this.template += view.template;
            
            this.template += `

            <a href="/notifications/" id="notificaciones" class="option">
                <i class="fas fa-bell"></i>
                <span>Notificaciones</span>
            </a>
        </section>
    `;
    return this.template
}

function ViewEmployeeNav(area){
    
    if(area === 'AV' || area === 'AAVEN'){
        this.template = `
            <a href="/sales/" class="option">
                <i class="fas fa-dollar-sign"></i>
                <span>Ventas</span>
            </a>
        `;
    }
    if(area === 'AC' || area === 'AACOM'){
        this.template = `
            <a href="/purchases/" class="option">
                <i class="fas fa-store"></i>
                <span>Compras</span>
            </a>
        `;
    }
    if(area === 'AA' || area === 'AAALM'){
        this.template = `
            <a href="/stock/" class="option" id="">
                <i class="fas fa-cubes"></i>
                <span>Almacen</span>
            </a>
        `;
    }
    if(area === 'AAVEN' || area === 'AACOM' || area === 'AAALM') {
        return this.template;
    }
}


function ViewAreaAdminNav(area){
    const areaOption = new ViewEmployeeNav(area);
    this.template = areaOption.template;
    this.template += `
        <a href="/staff/" class="option">
            <i class="fas fa-users"></i>
            <span>Personal</span>
        </a>
    `;
}

function ViewSuperAdminNav(){
    this.template = `
        <a href="/sales/" class="option">
            <i class="fas fa-dollar-sign"></i>
            <span>Ventas</span>
        </a>

        <a href="/purchases/" class="option">
            <i class="fas fa-store"></i>
            <span>Compras</span>
        </a>

        <a href="/stock/" class="option">
            <i class="fas fa-cubes"></i>
            <span>Almacen</span>
        </a>

        <a href="/staff/" class="option">
            <i class="fas fa-users"></i>
            <span>Personal</span>
        </a>
    `;
}