function getStaffAdminAreaData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.emp_key}</th>
                    <td>${element.email}</td>
                    <td>${element.first_name}</td>
                    <td>${element.last_name}</td>
                    <td>${element.date_joined}</td>
            </tr>
    `}
    return this.rows;
}

function getStaffSuperAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.emp_key}</th>`

                if(!element.is_simplemortal){
                this.rows += `
                <td class="table-actions">
                    <button id='delete'>
                            <i class="fas fa-trash"></i>
                            <span>Borrar</span>
                        </button>
                    </td>`
                } else {
                this.rows += `
                <td class="table-actions">
                    <a href="/form/form-staff-admin/" class="edit-row">
                        <i class="fas fa-pen"></i>
                        <span>Editar</span>
                    </a>
                    <button id='delete'>
                        <i class="fas fa-trash"></i>
                        <span>Borrar</span>
                    </button>
                </td>`
                }
                this.rows += `<td>${element.email}</td>
                <td>${element.first_name}</td>
                <td>${element.last_name}</td>
                <td>${element.date_joined}</td>
                <td>${element.area}</td>
                <td>${element.is_superuser}</td>
                <td>${element.is_areaadmin}</td>
                <td>${element.is_simplemortal}</td>
            </tr>
    `}
    return this.rows;
}