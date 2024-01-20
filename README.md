# chakrachipz-server

{% load socialaccount %}
  <h2>Google Login</h2>
  <a href="{% provider_login_url 'google' %}?next=/">Login With Google</a>