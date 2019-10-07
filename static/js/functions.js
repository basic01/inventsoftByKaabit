// *** async function sendData();
// Send form data to server
async function sendData(url){
    const response = await fetch(url)
    const data = await response.json()
    return data;
}

// *** async function getUserData();
// Get user data from server side
async function getUserData() {
    const response = await fetch('/get_user/');
    const data = await response.json();
    return data.user;
}

// *** async function getSingleton();
// Create Singleton Instance
async function getSingleton(){
    const userData = await getUserData();
    const userInstance = userSingleton.getInstance(userData);
    const user = userInstance.getUser();
    return user;
}

// *** function getUserType()
// Define the type of user: superuser, admin-area or employee
const getUserType = (user) => {
    if(user.is_superuser) return 0;
    if(user.is_areaadmin) return 1;
    if(user.is_simplemortal) return 2;
    else return 3;
}

// ----------- Table Factory Views ------------------

    //*** function factoryTableViewProducts()
    //Create Products table depending on the user type
    const factoryTableViewProducts = (user, data) =>{
        // const type = getUserType(user);
        let view;
        if(user.area === 'AA'){
            view = new ViewStockProductsTable(data);
        }
        else if(user.area === 'AAALM' || user.area === 'SADMI'){
            view = new ViewAdminProductsTable(data);
        }
        else{
            view = new ViewEmployeeProductsTable(data);
        }
        return view.template;
    } 

    //*** function factoryTableViewPurchases()
    //Create Purchases table depending on the user type
    const factoryTableViewPurchases = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminPurchasesTable(data),
                                new ViewAdminPurchasesTable(data),
                                new ViewEmployeePurchasesTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewSales()
    //Create Sales table depending on the user type
    const factoryTableViewSales = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminSalesTable(data),
                                new ViewAdminSalesTable(data),
                                new ViewEmployeeSalesTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStaff()
    //Create Staff table depending on the user type
    const factoryTableViewStaff = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewSuperAdminStaffTable(data),
                                new ViewAdminAreaStaffTable(data),
                                new ViewAdminAreaStaffTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStock()
    //Create Stock table depending on the user type
    const factoryTableViewStock = (user, data) =>{
        const type = getUserType(user);
        const view = new UserViewFactory(new ViewAdminStockTable(data),
                                new ViewAdminStockTable(data),
                                new ViewEmployeeStockTable(data),
                                ).create(type);
        return view.template;
    } 

// ----------- Form Views ------------------
    
    //*** function getFormType()
    //Get Form type: products, stock, sales, purchases, staff, ...
    const getFormType = () =>{
        const url = window.location.href;
        const position = url.search('/form-');
        const type = url.substr(position, url.length);        
        return type;
    }

    //*** function factoryFormView()
    //Create Form depending on the user area
    const factoryFormView = (type) => { 
        return new FormViewFactory().create(type);
    }

    //*** function factoryFormData()
    //Create Form depending on the user area
    const factoryFormData = async (type, user) => { 
        const view = await new FormDataFactory().create(type, user);
        return view.showDetails(user);
    }

    
// ----------- Form Data ------------------
    
    //*** function setAttributes()
    function setAttributes(element, attributes){
        for(const attribute in attributes){
            element.setAttribute(attribute, attributes[attribute])
        }
    }

    //*** function mandarData()
    // const CSRF_TOKEN = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    async function mandarData(url, data){
        const response = await fetch(url, {
            method: 'POST',
            body: data,
            headers: {
                'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        })
        const resp = await response.json();
        return resp;
    }


// ----------- Notifications ------------------
    
    //*** function getNotiData()
    // Get Notification Data
    async function getNotiData(url) {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    }

    //*** function showNotificationCount()
    // Display notification count in nav-bar 
    async function showNotificationCount(){
        let notif = await getNotiData('http://127.0.0.1:8000/fetch_notifications/');
        if(notif.notifications.length > 0){
            document.getElementById('notificaciones').innerHTML+=`
                <span class="notification-count">${notif.notifications.length}</span>
            `;
        }
    }

    //*** function addNotification()
    // Display notification count in nav-bar 
    async function addNotification(){
        let notif = await getNotiData('http://127.0.0.1:8000/fetch_notifications/');
        notif_nav = document.getElementById('notificaciones');    
        last_notif = notif.notifications.find(x => x.notification_key === notif.notifications[0].notification_key);

        if(last_notif){
            try{
                const data = await sendData(`http://127.0.0.1:8000/read_all_notifications/${last_notif.notification_key}/`);
            } catch (error) {
                console.log(error)
            }
        }
    }

// *** getCSV() 
// Get CSV file (Comma Separated Value) -> Excel
async function getCSV(urlData){
    sales_csv = document.getElementById('csv');
    sales_csv.addEventListener('click', async (e) => {
        e.preventDefault()

        try{
            const data = await sendData(urlData);
            console.log(data)
            if (data.status === 200){
                showSuccessModal('Descarga completada.<br> Ir a descargas', 'fas fa-check-circle');
            } else {
                showSuccessModal('Ocurrió un error, <br> intenta de nuevo', 'fas fa-times');
            }
        } catch (error) {
            console.log(error)
        }

    })
}