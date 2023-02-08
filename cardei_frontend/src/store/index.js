import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

export default createStore({
    state: () => ({
        user: {
            email: null
        },
        masterpass: ''
    }),
    getters: {
        getServerURL(state) {
            return state.backendURL
        }

    },
    mutations: {
        // Мутации, это функции, в нутри которых мы меняем значения
        // какого-то поля в состоянии
        setUser(state, user) {
            state.user = user;
        },
        setMasterpass(state, masterpass) {
            state.masterpass = masterpass;
        }

        
    },
    actions: {
        // это тоже функции, которые внутри себя используют мутации
        // изменять состояние из actions не рекомендуется, но можно делать
        // side ефекты, например получаем какие-то данные из сервера
        // вызываем мутацию и сохраняем эти данные в состояние

    },
    modules: {
        // это изолираванный кусок состояния. Со своими getters, mutations и actions
        // все модули подключаются в один глобальный стор

    },

    plugins: [createPersistedState({ storage: window.sessionStorage })]

})