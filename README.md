# pipapi

**I. Overview.**
Developed an API using Flask that empowers users to seamlessly install, uninstall, and retrieve a list of installed pip packages. This API eliminates the need for users to directly interact with the command line for managing their pip packages.
<br>
<br>
**II. Key Features:**
<br>
**Package Installation:**
Users can send a POST request with package details, and the API will handle the installation of the specified pip package. This provides a user-friendly alternative to the command-line installation process.
<br>
**Package Uninstallation:**
The API will enable users to send a DELETE request with package information, resulting in the removal of the specified pip package from their environment. This streamlines the package removal process.
<br>
**List Installed Packages:**
Users can send a GET request to the API, and in response, they will receive a list of all currently installed pip packages in their environment. This information is retrieved directly from the environment without the need for command-line interaction.
<br>
**Search Packages:(Updated Version)**
Users can send a request to the API for details of a package, it will return the url redirecting to the offical PIP website with details like description, Version History, How to use etc for the searched package.
<br>
<br>
User-Friendly Interface:
The API will be designed with a user-friendly and intuitive interface, making it accessible even to those without extensive technical knowledge. Clear API endpoints and well-documented usage instructions will guide users through the process.
<br>
<br>
**III. Technology Stack:**

**Flask**: Utilizing Flask, a lightweight and flexible Python web framework, to build the API.<br>
**Python**: Using Python as the primary programming language for developing the API logic.<br>
**Pip**: Leveraging the pip package manager to handle package installation and uninstallation.<br>
**RESTful API Design**: Implementing a RESTful architecture to ensure consistent and predictable interactions with the API.<br>


<br>
<br>

**IV. User Flow:**
<br>
**Install Package:**
User sends a POST request to the /install endpoint with package details.
API processes the request, uses the pip library to install the package, and responds with a success message or an error if the installation fails.
<br>
**Uninstall Package:**
User sends a DELETE request to the /uninstall endpoint with package information.
API processes the request, uses the pip library to uninstall the package, and responds with a success message or an error if the uninstallation fails.
<br>
**Get Installed Packages:**
User sends a GET request to the /list endpoint.
API retrieves the list of installed packages from the environment using the pip library and responds with a JSON array containing the package names.
<br>

**V. Benefits:**
<br>
<ol>Simplifies pip package management for users without requiring command-line expertise.</ol>
<ul>Reduces the potential for errors during package installation and uninstallation.</ul>
<ul>Offers a centralized platform for managing installed packages, enhancing user convenience.</ul>
<ul>Provides a customizable and extensible solution that can be expanded with additional features in the future.</ul>


**Live Demo Link** : http://pipapi-u6jn.onrender.com/

**version update**
Added a new feature to search about a PIP package. 
