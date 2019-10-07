function getNotifications(data){
    this.notifications = '';
    for(let element of data){
        this.notifications += ` 
            <div class="col-xl-3 col-lg-4 col-sm-6 col-12">
                <div class="record">
                    <div class="details">
                        <label>Área: ${element.transmitter_area}</label>
                        <label>Responsable: ${element.transmitter}</label>
                    </div>
                    <div class="content">
                        <p>${element.description}</p>
                    </div>
                </div>
            </div>
        `
    }
    return this.notifications;
}

function ZeroNotifications(){
    this.template = `
        <div class="container-fluid main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="far fa-clock"></i>
                        <h2>Historial<h2>
                    </div>
                    <div class="row records-container" id="records-container">
                        <h3 id="zero-notif">No hay notificaciones</h3>
                    </div>
                </div>
            </div>
        </div>
    `
    return this.template;

}

function AllNotifications(data){
    this.template = `
        <div class="container-fluid main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="far fa-clock"></i>
                        <h2>Historial<h2>
                    </div>
                    <div class="row records-container" id="records-container">`;
                        this.template += getNotifications(data);
                        this.template += `</div>
                </div>
            </div>
        </div>
    `
    return this.template;
}

function ViewNotifications(data){
    if(data.length > 0) return AllNotifications(data);
    if(data.length === 0) return ZeroNotifications();
}