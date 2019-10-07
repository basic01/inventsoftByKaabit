
let userSingleton = (function(){
    let userInstance;
    const create = (userObject) => {
        let user = userObject;
        let getUser = () => {return user}
        return{
            getUser: getUser
        }
    }
    return {
        getInstance: (userObject) => {
            if(!userInstance) userInstance = create(userObject);
            return userInstance;
        },
        removeInstance: () => {
            if(userInstance) userInstance = null;
            return userInstance;
        }
    }
})();


//userInstance = userSingleton.getInstance(userData);
//user = userInstance.getUser();
