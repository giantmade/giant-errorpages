# Giant Error Pages

A small package to trigger specific non-200 HTTP responses. This is useful for previewing your error pages while DEBUG=True. Once enabled, you will be able to access three new routes:

- /errors/404/, which will return a 404 response and error page.
- /errors/403/, which will return a 403 response and error page.
- /errors/500/, which will return a 500 response and error page.

## Installation

To install with Poetry, run:

    $ poetry add giant-errorpages

You should then add `"errorpages"` to the `INSTALLED_APPS` in your settings file. Finally, update your root `urlpatterns` to include:

    path("errors/", include("errorpages.urls"), name="errorpages"),

## Preparing for release
 
In order to prepare the package for a new release on TestPyPi and PyPi, you need to update the version number in the `pyproject.toml`. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.
 
## Publishing
 
Once the version number has been updated, run:
 
   $ `poetry build` 

This will package the project ready for publication:

   $ `poetry publish`

...will then publish the package to PyPi. You will need to enter the username and password for the account which can be found in the company password manager.