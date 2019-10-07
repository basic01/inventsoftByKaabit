function ViewFormPurchases(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Compra</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form action="." id="formPurchase" method="POST" class="form">
                                    <select name="" id="producto" placeholder="Producto">
                                    </select>
                                    <input type="number" id="cantidad" placeholder="Cantidad" onkeydown="return false">
                                    <input type="text" id="stock" readonly>
                                    <input type="text" id="total" placeholder="Total:" readonly>
                                    <input type="text" id="proveedor" placeholder="Proveedor:" readonly>
                                    <input type="hidden" id='idProveedor'>
                                    <select name="" id="vendedor" placeholder="Vendedor">
                                    </select>
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewFormSales(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Venta</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form action="." id="formSales" method="POST" class="form">
                                    <select name="" id="producto" placeholder="Producto">
                                    </select>
                                    <input type="number" id="cantidad" placeholder="Cantidad" onkeydown="return false">
                                    <input type="text" id="total" placeholder="Total:" readonly>
                                    <select name="" id="cliente" placeholder="Cliente">
                                    </select>
                                    <select name="" id="vendedor" placeholder="Vendedor">
                                    </select>
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="/sales/" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewFormStock(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Almacén</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-7 col-lg-5 col-xl-3 col-form-container">
                            <div class="form-container">
                                <form id="formStock" action="." method="POST" class="form">
                                    <input type="text" id="producto" placeholder="Producto:" readonly disabled>                                    
                                    <input type="number" id="cantidad" placeholder="Cantidad:" min="1">
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="/stock/" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewFormProduct(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Producto</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form id="formProducto" action="." method="POST" class="form">
                                    <input type="text"id="nombre" placeholder="Nombre:">
                                    <textarea id="descripcion" placeholder="Descripción..."></textarea>
                                    <input type="text" id="precio" placeholder="Precio:">
                                    <select id="categoria" placeholder="Categoría">
                                    </select>
                                    <select id="proveedor" placeholder="Proveedor">
                                    </select>
                                    <input id="cantidad" type="text" placeholder="Cantidad:">
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="/products/" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}


function ViewFormStaff(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Personal</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form id="formStaff" method="POST" action="." class="form">
                                    <input type="text"id="nombre" placeholder="Nombre:">
                                    <input type="text"id="apellidos" placeholder="Apellido(s):">
                                    <input type="email" id="correo" placeholder="Correo:" name="" id="">
                                    <input type="password" id="contraseña" placeholder="Contraseña:">
                                    <select name="" id="area" placeholder="Area">
                                    </select>
                                    <div id="quitar" class="type-user">
                                        <p>Tipo de usuario:</p>
                                        <div class="option-user">
                                            <input type="radio" name="type-user" id="r1" value="employee" checked disabled>
                                            <span>Empleado</span>
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewFormStaffAdmin(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Personal</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form id="formStaff" method="POST" action="." class="form">
                                    <input type="text" id="nombre" placeholder="Nombre:">
                                    <input type="text" id="apellidos" placeholder="Apellido(s):">
                                    <input type="email" placeholder="Correo:" name="" id="correo">
                                    <input type="password" id="contraseña" placeholder="Contraseña:">
                                    <select name="" id="area" placeholder="Area">
                                        <option value="AA">Almacen</option>
                                        <option value="AV">Ventas</option>
                                        <option value="AC">Compras</option>
                                    </select>
                                    <div id="quitar" class="type-user">
                                        <p>Tipo de usuario:</p>
                                        <div class="option-user">
                                            <input type="radio" name="type-user" id="r1" value="employee">
                                            <span>Empleado</span>
                                        </div>
                                        <div class="option-user">
                                            <input type="radio" name="type-user" id="r2" value="adminarea">
                                            <span>Admin. de área</span>
                                        </div>
                                        <div class="option-user">
                                            <input type="radio" name="type-user" id="r3" value="superuser">
                                            <span>Súper usuario</span>
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="/staff/" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}