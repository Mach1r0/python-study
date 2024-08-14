function deleteCookie(name) {
    document.cookie = name + '=; Max-Age=0; path=/;';
}

window.addEventListener('pageshow', function(event) {
    if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
        sessionStorage.clear();
        deleteCookie('session_id');
        deleteCookie('username');
        document.location = '/portal';
    }
});
