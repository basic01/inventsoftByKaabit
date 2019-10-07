function ViewError(){
    // this.template = "<h3>Error: User type invalid</h3>";
    window.location.href = '/logout/';
}

function UserViewFactory(ViewSuperAdmin, ViewAreaAdmin, ViewEmployee){
    this.create = (type) =>{        
        if (type === 0) return ViewSuperAdmin;
        if (type === 1) return ViewAreaAdmin;
        if (type === 2) return ViewEmployee;
        if (type != 0 && type != 1 && type != 2) return new ViewError();
    }
}

function FormViewFactory(){
    this.create = (type) =>{
        if(type === '/form-sales/') return ViewFormSales();
        if(type === '/form-purchases/') return ViewFormPurchases();
        if(type === '/form-stock/') return ViewFormStock();
        if(type === '/form-products/') return ViewFormProduct();
        if(type === '/form-staff/') return ViewFormStaff();
        if(type === '/form-staff-admin/') return ViewFormStaffAdmin();
    }
}

function FormDataFactory(){
    this.create = async (type, user) =>{
        if(type === '/form-sales/') return FormSalesData(user);
        if(type === '/form-purchases/') return FormPurchasesData(user);
        if(type === '/form-stock/') return FormStockData();
        if(type === '/form-products/') return FormProductData();
        if(type === '/form-staff/') return FormStaffData(user);
        if(type === '/form-staff-admin/') return FormStaffAdminData();
    }
}