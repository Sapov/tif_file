

{% block content %}
<form method="post" , enctype="multipart/form-data">

    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Сохранить</Update>
</form>
{% endblock %}