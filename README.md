# Django HTMX Components

This is a collection of components for [Django](https://www.djangoproject.com/) and [htmx](https://htmx.org/). They are designed to be copy-pasted into your project and customized to your needs.

They're designed to be as simple as possible, so you can easily understand how they work and modify them to your needs. They have very little styling, so you can easily customize them to match your site.

## Installation

1. Install [Django](https://www.djangoproject.com/) and [htmx](https://htmx.org/).
2. Install and set up [django-compoenents](https://github.com/EmilStenstrom/django-components)
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
           path('mycomponent/', MyCompponent.as_view()),
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
4. Run the development server:
   ```bash
   make run-django
   ```
5. Open http://localhost:5000/ in your browser.
6. Once you're happy with your changes, test that it works within Pyodide:
   ```bash
   make run-pyodide
   ```
7. Commit your changes and open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
