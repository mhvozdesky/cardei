<template>
    <div class="content-RightDash">
        <div class="work-area">
            <div class="item-dash">
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Copy</button>
                    </div>
                </div>
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Copy</button>
                    </div>
                </div>
                <div class="item-field name-field">
                    <label class="item-field__label" for="name">Назва</label>
                    <div class="item-field__group">
                        <input class="item-field__input" type="search" id="name" name="name">
                        <button class="item-field__btn" type="button">Copy</button>
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
        background-color: #4CAF50;
        border: 1px solid #4CAF50;
        padding: 1px .75rem;
        font-size: 1rem;
        border-radius: .25rem;
        transition: background-color .15s ease-in-out;
    }
    .item-field__btn:hover {
        background-color: #60cd65;
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
        color: white;
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
        background-color: #f4f4f7;
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
        border: 0.5px solid #4caf50;
        padding-left: 5px;
    }

    @media (max-width: 1130px) {
        .item-field__input {
            width: 355px;
        }
    }

    @media (max-width: 870px) {
        .item-field__input {
            width: 260px;
        }
    }

    @media (max-width: 425px) {
        .item-field__input {
            width: 195px;
        }
    }

    .btn-set {
        display: flex;
        background-color: #f4f4f7;
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
        background: #4CAF50; /* фон кнопки */
        padding: .7em 1.5em; /* отступ от текста */
        outline: none; /* убирать контур в Mozilla */
        width: 127px;
        margin: 5px;
    } 
    .btn:hover {
        background: #60cd65; 
    } /* при наведении курсора мышки */
    .btn:active {
        background: #409344; 
    } /* при нажатии */
</style>