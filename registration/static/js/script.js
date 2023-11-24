ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
            center: [48.396852, 135.139371],
            zoom: 18
        }, {
            searchControlProvider: 'yandex#search'
        }),
        myGeoObject = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: [48.396852, 135.139371]
            }
        }, {
            iconColor: '#0095b6'
        })
    myMap.geoObjects
        .add(myGeoObject);
}

const navbar = document.querySelector('.navbar');

window.addEventListener('DOMContentLoaded', function() {
  if (window.scrollY > 0) {
    navbar.classList.add('fixed-top');
  } else {
    navbar.classList.remove('fixed-top');
  }
});

window.addEventListener('scroll', function() {
  if (window.scrollY > 0) {
    navbar.classList.add('fixed-top');
  } else {
    navbar.classList.remove('fixed-top');
  }
});


// Получаем элементы страницы
const searchInput = document.getElementById('search-query');
const categorySelector = document.querySelector('.prods-selector');
const products = document.getElementsByClassName('prod');

// Функция для фильтрации товаров
const filterProducts = () => {
    const searchValue = searchInput.value.toLowerCase();
    const categoryValue = categorySelector.value.toLowerCase();

    // Перебираем все товары
    for (let i = 0; i < products.length; i++) {
    const productName = products[i].querySelector('.card-title').textContent.toLowerCase();
    const productDesc = products[i].querySelector('.card-text').textContent.toLowerCase();
    const productCategory = productDesc.split(',')[0];

        // Проверяем, соответствует ли товар строке поиска и выбранной категории
        if ((productName.includes(searchValue) || productDesc.includes(searchValue)) && (categoryValue === 'всё' || (categoryValue === 'линейки' && productName.includes('линейка')) || (categoryValue === 'книги' && productName.includes('книга')) || (categoryValue === 'ручки' && productName.includes('ручка')))) {
          products[i].style.display = 'block'; // Отображаем товар
        } else {
          products[i].style.display = 'none'; // Скрываем товар
        }
    }
};

// Слушаем событие изменения в поле поиска и выбора категории
searchInput.addEventListener('input', filterProducts);
categorySelector.addEventListener('change', filterProducts);


