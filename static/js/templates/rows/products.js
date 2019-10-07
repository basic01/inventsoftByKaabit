function getProductsEmployeeData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
        <tr>
            <th scope="row">${element.key}</th>
            <td>${element.name}</td>
            <td>${element.description}</td>
            <td>${element.price}</td>
            <td>${element.category}</td>
            <td>${element.provider}</td>
        </tr>
    `}
    return this.rows;
}

function getProductsAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
        <tr>
            <th scope="row">${element.key}</th>
            <td class="table-actions">
                <a href="/form/form-products/" class="edit-row">
                    <i class="fas fa-pen"></i>
                    <span>Editar</span>
                </a>
                <button id='delete'>
                    <i class="fas fa-trash"></i>
                    <span>Borrar</span>
                </button>
            </td>
            <td>${element.name}</td>
            <td>${element.description}</td>
            <td>${element.price}</td>
            <td>${element.category}</td>
            <td>${element.provider}</td>
        </tr>
    `}
    return this.rows;
}