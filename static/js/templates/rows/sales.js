function getSalesEmployeeData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td>${element.name_product}</td>
                <td>${element.amount}</td>
                <td>${element.client_name}</td>
                <td>${element.total}</td>
                <td>${element.first_name} ${element.last_name}</td>
                <td>${element.sale_date}</td>
            </tr>
    `}
    return this.rows;
}

// <a href="/form/form-sales/" class="edit-row">
//<i class="fas fa-pen"></i>
//<span>Editar</span>
//</a>
function getSalesAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td class="table-actions">
                    <button id='delete'>
                        <i class="fas fa-trash"></i>
                        <span>Borrar</span>
                    </button>
                </td>
                <td>${element.name_product}</td>
                <td>${element.amount}</td>
                <td>${element.client_name}</td>
                <td>${element.total}</td>
                <td>${element.first_name} ${element.last_name}</td>
                <td>${element.sale_date}</td>
            </tr>
    `}
    return this.rows;
}