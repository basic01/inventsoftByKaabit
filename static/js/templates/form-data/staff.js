// Get form-staff data
async function FormStaffData(user) {
    this.template = {
        showDetails: async (user) => {
            const FORMSTAFF = document.querySelector('#formStaff');
            let privateStaffStorage = "";
            if (localStorage.getItem('staffKey')) {
                privateStaffStorage = localStorage.getItem('staffKey');
                let titulo = document.getElementsByClassName('result-title')[0];
                titulo.innerHTML = '';
                titulo.innerHTML = '<h2>Editar Usuario</h2>';
                async function getProductData() {
                    const response = await fetch(`/get_staff_user/${privateStaffStorage}/`);
                    const data = await response.json();
                    return data.user;
                }
                privateStaffStorage = await getProductData();
                document.getElementById("nombre").value = privateStaffStorage.first_name;
                document.getElementById("apellidos").value = privateStaffStorage.last_name;
                document.getElementById("correo").value = privateStaffStorage.email;
                document.getElementById("contraseña").style.display = 'none';
                document.getElementById("contraseña").value = privateStaffStorage.password
                document.getElementById("area").value = privateStaffStorage.area;
                // document.getElementById('quitar').style.display = 'none';
                if(privateStaffStorage.is_superuser === true){
                    document.getElementById('r3').checked = true;
                } else if(privateStaffStorage.is_areaadmin === true){
                    document.getElementById('r2').checked = true;
                } else if(privateStaffStorage.is_simplemortal === true){
                    document.getElementById('r1').checked = true;
                }
            }

            async function getAdminAreaData() {
                const response = await fetch(`/fetch_area_adminarea/`);
                const data = await response.json();
                return data.area;
            }
            let areaAdmin =  await getAdminAreaData();
            console.log(areaAdmin)
            console.log(getUserType(user))
            if(areaAdmin === 'AA'){
                selectElement = document.getElementById('area');
                const optionElement = document.createElement('option');
                setAttributes(optionElement, {
                    value: areaAdmin,
                });
                optionElement.innerHTML = 'Almacen';
                selectElement.appendChild(optionElement);
            } else if(areaAdmin === 'AC'){
                selectElement = document.getElementById('area');
                const optionElement = document.createElement('option');
                setAttributes(optionElement, {
                    value: areaAdmin,
                });
                optionElement.innerHTML = 'Almacen';
                selectElement.appendChild(optionElement);
            } else if(areaAdmin === 'AV'){
                selectElement = document.getElementById('area');
                const optionElement = document.createElement('option');
                setAttributes(optionElement, {
                    value: areaAdmin,
                });
                optionElement.innerHTML = 'Almacen';
                selectElement.appendChild(optionElement);
            }


            FORMSTAFF.addEventListener('submit', async (e) => {
                e.preventDefault();

                let tipo;
                if (document.getElementById('r1').checked) {
                    tipo = document.getElementById('r1').value;
                } else if (document.getElementById('r2').checked) {
                    tipo = document.getElementById('r2').value;
                } else if (document.getElementById('r3').checked) {
                    tipo = document.getElementById('r3').value;
                }
                console.log(tipo)

                if(document.getElementById('nombre').value !== '' && document.getElementById('apellidos').value !== '' && document.getElementById('correo').value !== '' && document.getElementById('contraseña').value !== '' && document.getElementById('area').value !== '' && tipo !== ''){
                    const form = new FormData();
                    form.append('nombre', document.getElementById('nombre').value);
                    form.append('apellidos', document.getElementById('apellidos').value);
                    form.append('correo', document.getElementById('correo').value);
                    form.append('area', document.getElementById('area').value);
                    form.append('tipo', tipo);
                    if (privateStaffStorage) {
                        form.append('accion', 'EDIT');
                        form.append('id', privateStaffStorage.emp_key);
                        form.append('contraseña', privateStaffStorage.password);
                    } else{
                        form.append('accion', 'NEW');
                        form.append('contraseña', document.getElementById('contraseña').value);
                    }

                    try {
                        const data = await mandarData('http://127.0.0.1:8000/post_staff/', form);
                        if (data.status === 200) {
                            if (privateStaffStorage) {
                                localStorage.removeItem('staffKey');
                                showModal(`${data.info}`, 'fas fa-check-circle', '/staff/');
                            }
                            else {
                                showModal('Usuario agregado <br> correctamente', 'fas fa-check-circle', '/staff/');
                            }
                        } else if (data.status === 400) {
                            showModal('Ya hay un admin, <br> registrado', 'fas fa-times','/staff/');
                        } else if (data.status === 403) {
                            showModal('Ocurrio un error, <br> intentalo más tarde', 'fas fa-times','/staff/');
                        }
                    } catch (error) {
                        console.log('error')
                    }

                } else {
                    showModal('Llena todos los <br> campos', 'fas fa-times',);
                }
            })
        }
    }
    return this.template;
}