function navigate(url){
    window.location.assign(url);
}

function changeClass(styleClass, HTMLElement){
    document.getElementById(HTMLElement).classList.toggle(styleClass);
}

function setTimeoutHTML(styleClass, HTMLElement, duration){
    changeClass(styleClass, HTMLElement);
    setTimeout(function(){
        changeClass(styleClass, HTMLElement);
    }, duration);
}

function resetInputError(){
    const error = document.getElementById('error');
    if(error.innerHTML != ""){
        error.innerHTML = "";
    }
}

function showModal(text, icon, location){
    document.body.innerHTML += `
        <div class="modal-back" id="modal-back">
            <div class="modal-container">
                <div class="modal-div">
                    <h3>${text}</h3>
                    <i class="${icon}"></i>
                </div>
            </div>
        </div>
        `;         
    setTimeoutHTML('modal-back-show', 'modal-back', 1000);  
    if(location){ 
        setTimeout(function(){
            window.location.href = location;
        }, 1000)
    }
}


function showOptionModal(text){
    return `
        <div class="modal-back" id="modal-options">
            <div class="modal-container">
                <div class="modal-div">
                    <h3>${text}</h3>
                    <div class="modal-options">
                        <button id="ok" class="btn primary-btn" onclick="changeClass('modal-back-show', 'modal-options');">Aceptar</button>
                        <button id="cancel" class="btn secondary-btn" onclick="changeClass('modal-back-show', 'modal-options');">Cancelar</button>
                    </div>
                </div>
            </div>
        </div>
    `; 
}


function includeModal(){
    return `
        <div class="modal-back" id="modal-back">
            <div class="modal-container">
                <div class="modal-div" id="modal-info">
                </div>
            </div>
        </div>
    `
}

function showSuccessModal(text, icon){
    document.getElementById('modal-info').innerHTML = `
        <h3>${text}</h3>
        <i class="${icon}"></i>
    `;         
    setTimeoutHTML('modal-back-show', 'modal-back', 1000);
}


function getPDF(divId, name){
    let div = document.getElementById(divId);
    domtoimage.toPng(div)
    .then(function(dataUrl){
        //Crear imagen y asignarle como src el div convertido a imagen
        let img = new Image();
        img.src = dataUrl;

        //Settings PDF
        const wid = div.offsetWidth - 40;
        // const hgt = div.offsetHeight - 75;
        const hgt = div.offsetHeight;
        const hratio = hgt/wid;
        let doc = new jsPDF();
        const width = doc.internal.pageSize.getWidth();  
        const height = width * hratio;
        doc.addImage(img.src, 'JPEG', 20, 10, width-40, height);
        doc.save(`reporte_${name}.pdf`);
        showSuccessModal('Reporte creado <br> exitosamente', 'fas fa-check-circle');
    })
    .catch(function(error){
        console.log(error);
        showSuccessModal('Ocurrió un error <br> intenta de nuevo', 'fas fa-times');
    });
}