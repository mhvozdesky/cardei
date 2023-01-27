<template>
    <div class="content-RightDash">
        <div class="work-area">
            <div class="item-dash">
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Coppy</button>
                    </div>
                </div>
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Coppy</button>
                    </div>
                </div>
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Coppy</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="button-area">
            <div class="btn-set">
                <div class="btn edit-btn">Редагувати</div>
                <div class="btn save-btn">Зберегти</div>
                <div class="btn delete-btn">Видалити</div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "RightDash"
    }
</script>

<style>
    .item-field__group {
        display: flex;
    }

    .item-field__btn {
        display: inline-block;
        font-weight: 400;
        line-height: 1.5;
        color: #212529;
        text-align: center;
        vertical-align: middle;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
        background-color: #eee;
        border: 1px solid #bdbdbd;
        padding: 1px .75rem;
        font-size: 1rem;
        border-radius: .25rem;
        transition: background-color .15s ease-in-out;
    }
    .item-field__btn:hover {
        background-color: #bdbdbd;
    }
    .item-field__group .text-field__input {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        position: relative;
        z-index: 2;
    }
    .item-field__group .item-field__btn {
        position: relative;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
        border-left-width: 0;
    }

    .item-field {
        display: flex;
        align-items: center;
        padding-top: 25px;
    }

    .content-RightDash {
        display: flex;
        flex-direction: column;
    }

    .button-area {
        height: 50px;
        border: 0.5px solid #dbdbdb;
    }

    .work-area {
        flex-grow: 1;
    }

    .item-dash {
        padding: 10px;
    }

    .item-field__group {
        padding-left: 30px;
    }

    .item-field__input {
        text-overflow: ellipsis;
        width: 500px;
    }

    .btn-set {
        display: flex;
    }

    /* .btn {
        cursor:pointer;
        border-width:1px;
        border-style:solid;
        background-color:gray;
        width:100px;
        text-align:center;
        color:#ffffff;
    } */

    .btn {
        color: #fff; /* цвет текста */
        text-decoration: none; /* убирать подчёркивание у ссылок */
        user-select: none; /* убирать выделение текста */
        background: #858585; /* фон кнопки */
        padding: .7em 1.5em; /* отступ от текста */
        outline: none; /* убирать контур в Mozilla */
        width: 80px;
        margin: 5px;
    } 
    .btn:hover {
        background: #9f9f9f; 
    } /* при наведении курсора мышки */
    .btn:active {
        background: #5e5e5e; 
    } /* при нажатии */
</style>