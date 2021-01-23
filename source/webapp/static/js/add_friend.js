function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};
    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }
    let response = await fetch(url, opts);
    if (response.ok) {  // нормальный ответ
        return response;
    }
    else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function AddFriend(event) {
    event.preventDefault()
    let ButtonAddFriend = event.target;
    let id = ButtonAddFriend.id;
    let my_user = ButtonAddFriend.My
    let url = ButtonAddFriend.href;
    try {
        let response = await makeRequest(url, 'POST', {'id': id}).then((response) => response.json());
        console.log(response)
    }
    catch (error) {
        console.log(error);
    }
}

// async function Done_with_hint(event) {
//     event.preventDefault()
//     let ButtonDone_with_hint = event.target;
//     let id = ButtonDone_with_hint.id;
//     let url = ButtonDone_with_hint.href;
//     ButtonDone_with_hint.href = '#';
//     try {
//         let response = await makeRequest(url, 'POST', {'id': id}).then((response) => response.json());
//         console.log(response)
//         ButtonDone_with_hint.innerText = 'Hint ' + response['count']
//         ButtonDone_with_hint.href = url;
//     }
//     catch (error) {
//         console.log(error);
//     }
// }