import { createStore } from "vuex";

export default createStore({
    state: () => ({
        backendURL: 'http://127.0.0.1:80/api/v1'
    }),
    getters: {
        getServerURL(state) {
            return state.backendURL
        }

    },
    mutations: {
        // Мутации, это функции, в нутри которых мы меняем значения
        // какого-то поля в состоянии

        
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

    }

})