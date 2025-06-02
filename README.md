# Django HTMX Components

This is a collection of components for [Django](https://www.djangoproject.com/) and [htmx](https://htmx.org/). They are meant to be copy-pasted into your project and customized to your needs.

They're designed to be as simple as possible, so you can easily understand how they work and modify them to your needs. They have very little styling, for the same reason.

## Installation

1. Install [Django](https://www.djangoproject.com/) and [htmx](https://htmx.org/).
2. Install and set up [django-components](https://github.com/EmilStenstrom/django-components)
3. Create a `urls.py` file in `components/` and add the following code:
   ```python
       from django.urls import path
       urlpatterns = []
   ```
   Then import this file in your project's `urls.py` file:
   ```python
       from django.urls import path, include
       urlpatterns = [
           path('components/', include('components.urls')),
       ]
   ```
   This step simplifies adding URL patterns for your components and keeps them separate from your project's URL patterns. Then, adding a single-file component to your `components/urls.py` file is as easy as:
   ```python
       from django.urls import path
       from components.mycomponent import MyComponent
       urlpatterns = [
           path('mycomponent/', MyComponent.as_view()),
       ]
   ```
   It will handle requests to `/components/mycomponent/` and render the component.
4. Copy-paste the components you want to use into your `components/` folder. Add them to your `components/urls.py` file as described above.

## Contributing

Contributions are welcome! Please open an issue or pull request if you have a component you'd like to add or a bug to report.

### Local development

1. Clone this repository.
2. Create a virtual environment and install the dependencies:
   ```bash
   poetry install
   npm install
   ```
3. Run the Tailwind CSS build:
   ```bash
   make tailwind
   ```
4. Start redis:
   ```bash
   make redis
   ```
5. Run the development server:
   ```bash
   make run
   ```
6. Open http://localhost:8000/ in your browser.
7. Make your changes and test them in your browser.
8. Commit your changes and open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
