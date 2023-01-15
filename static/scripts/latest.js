let days = document.querySelectorAll('.day')
let urlStart = "https://api.hh.ru/vacancies"
let spec = ['web develop', 'веб разработчик', 'web разработчик', 'web programmer', 'web программист', 'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик', 'cms разработчик', 'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer', 'cms developer', 'wordpress developer', 'wp developer', 'joomla developer']
let text = spec.map(e => "'" + e + "'").join(' OR ')
let vacsElement = document.querySelector('.vacancies')
let loading = document.querySelector('.loading')

function removeSelected() {
    days.forEach(e => e.classList.remove('selected'))
}

function loadVacancies(e) {
    e.classList.add('selected')
    vacsElement.innerHTML = ''
    loading.classList.remove('hidden')

    getVacancies(e.innerHTML.trim())
        .then((vacs) => {
            updateVacancies(vacs)
        })
}

function updateVacancies(vacs) {
    vacs.sort((a, b) => a.published_at > b.published_at)
    loading.classList.add('hidden')

    vacs.forEach(vacancy => {
        let vacElement = createElem('', 'vacancy')

        vacElement.append(createField('Название', vacancy.name))
        vacElement.append(createField('Описание', vacancy.description))
        vacElement.append(createField('Навыки',
            vacancy.key_skills.length > 0 ? vacancy.key_skills.map(e => e.name).join(', ') : 'Не указано'))
        vacElement.append(createField('Компания', vacancy.employer.name))
        vacElement.append(createField('Оклад', getSalary(vacancy)))
        vacElement.append(createField('Название региона', vacancy.area.name))
        vacElement.append(createField('Дата публикации', vacancy.published_at.replace('2023-01', '2022-12')))

        vacsElement.append(vacElement)
    })
}

function getSalary(vacancy) {
    if (!vacancy.salary || !vacancy.salary.from && !vacancy.salary.to)
        return 'Не указано'

    let salary = 0

    salary += vacancy.salary.from ?  parseInt(vacancy.salary.from) : parseInt(vacancy.salary.to)
    salary += vacancy.salary.to ?  parseInt(vacancy.salary.to) : parseInt(vacancy.salary.from)

    salary /= 2

    return salary.toString() + (vacancy.salary.currency ? ' ' + vacancy.salary.currency : '')
}

function createElem(content, className) {
    let element = document.createElement('div')
    element.classList.add(className)
    element.innerHTML = content

    return element
}

function createField(name, content) {
    let field = createElem('', 'field')
    field.append(createElem(name, 'field-name'))
    field.append(createElem(content, 'field-content'))

    return field
}

async function getVacancies(day) {
    let now = new Date()
    return new Promise((resolve) => {
        let xhr = new XMLHttpRequest()
        let params = {
            per_page: 10,
            date_from: `${day < now.getDate() - 6 ? '2023' : '2022'}-${day < now.getDate() - 6 ? '01' : '12'}-${day >= 10 ? day : `0${day}`}T00:00:00`,
            date_to: `${day < now.getDate() - 6 ? '2023' : '2022'}-${day < now.getDate() - 6 ? '01' : '12'}-${day >= 10 ? day : `0${day}`}T23:59:59`,
            text: text
        }

        let url = new URL(urlStart)
        url.searchParams.set('text', params.text)
        url.searchParams.set('date_from', params.date_from)
        url.searchParams.set('date_to', params.date_to)
        url.searchParams.set('per_page', params.per_page)

        xhr.open('GET', url)
        xhr.send()

        xhr.onload = async function() {
            let response = JSON.parse(xhr.response).items
            let ids = response.map(e => e.url)

            await Promise.all(
                ids.map(e => getFields(e))
            ).then(e => {
                resolve(e)
            })
        }
    })
}

async function getFields(url) {
    return new Promise((resolve) => {
        let xhr = new XMLHttpRequest()
        xhr.open("GET", url)
        xhr.send()

        xhr.onload = function() {
            resolve(JSON.parse(xhr.response))
        }
    })
}

days.forEach(el => {
    el.addEventListener('click', e => {
        removeSelected()
        loadVacancies(el)
    })
})

days[days.length - 1].dispatchEvent(new Event('click'))