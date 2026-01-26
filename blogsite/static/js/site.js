let id_category = document.getElementById('id_category_name');

document.getElementById('form_submit').addEventListener('click', function (e) {
    if (!confirm('Are you sure to add category?')) {
        e.preventDefault(); // stops form submission
    }
});

