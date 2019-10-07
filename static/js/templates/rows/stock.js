function getStockEmployeeData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td>${element.product}</td>
                <td>${element.amount}</td>
            </tr>
    `}
    return this.rows;
}

//<a href="">
//    <i class="fas fa-trash"></i>
//    <span>Borrar</span>
//</a>
function getStockAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td class="table-actions">
                    <a href="/form/form-stock/" class="edit-row">
                        <i class="fas fa-pen"></i>
                        <span>Editar</span>
                    </a>
                </td>
                <td>${element.product_name}</td>
                <td>${element.amount}</td>
            </tr>
    `}
    return this.rows;
}