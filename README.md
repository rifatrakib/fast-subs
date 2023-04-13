# fastapi sub-applications (fast-subs)

This project offers a unique approach to building APIs with [fastapi](https://fastapi.tiangolo.com/), as it allows you to create a **seemingly** (but not actually) *distributed monolith* without the drawbacks that typically come with this architecture (**PLEASE NOTE**: *this does not follow a real microservice architecture as I have not created a way for the services to communicate with each other, but it is possible to build the broker apps using this same structure*). By using separate environments and configurations for each sub-application, this structure ensures that each application can be run independently, containerized separately, and even deployed as independent pods in a Kubernetes cluster by managing the configurations as practiced. Yet, these sub-applications can also be mounted on a central [fastapi](https://fastapi.tiangolo.com/) application, which provides a seamless user experience.

This structure is especially useful because it enables you to start with a *seemingly* distributed monolith without the drawbacks of tightly coupled services and complex inter-service communication that often come with this architecture. Instead, each sub-application is designed to work independently, *making it easier to test, debug, and deploy*. Additionally, it allows you to take advantage of fastapi's high performance and scalability, while avoiding the complexity that can arise with very large monolithic applications.

Furthermore, this structure is designed in a way that can be easily migrated to build microservices by adding others necessary services like brokers, making it a versatile solution for a wide range of API projects. By starting with separate sub-applications that can be run independently, you can gradually transition to a microservices architecture as needed, without having to rebuild your entire API from scratch.

In summary, this project offers a flexible and scalable approach to building APIs with [fastapi](https://fastapi.tiangolo.com/). By allowing you to create such *seemingly* distributed monoliths that are easy to manage and deploy, while also enabling a seamless transition to microservices, this structure is ideal for developers who want to build complex, high-performance APIs with minimal overhead.

To make working with this project easier, it comes with a CLI app in `manage.py`. The CLI provides several commands for creating and managing sub-applications, such as creating new sub-applications from a template, renaming existing ones, creating routers within sub-applications, and running specific sub-applications independently. Additionally, you can use the CLI to run the central fastapi application, which mounts all sub-applications.


## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine and navigate to the root directory of the project:

```
git clone https://github.com/rifatrakib/fast-subs.git
cd fast-subs
```

2. Install the project dependencies using [Poetry](https://python-poetry.org/):

```
poetry install
```

3. Create a new sub-application using the CLI app:

```
python manage.py create-app <sub-app-name>
```

Make sure to replace `<sub-app-name>` with the name you want to give your new sub-application which can be used as part of a valid python path. The above command creates a basic skeleton consisting of necessary modules of a typical web backend and a `.env` file containing two variables. Feel free to customize the CLI functions in the `manage.py` to fit your needs.

To rename your sub-application, use the following command:

```
python manage.py rename-app <old-name> <new-name>
```

To create a new router in a sub-application and the modules typically linked to that router, run the following command:

```
python manage.py create-router <app-name> <router-name>
```

4. Open the newly created sub-application modules in your code editor and add your own routes and logic.

5. To run the sub-application independently, use the `start-server` command from the CLI:

```
python manage.py start-server --name <sub-app-name>
```

or mount the sub-application on the main application in the `server/main.py` as:

```
from server.apps.<sub_app_name>.server.main import app as <sub_app_name>_app

app = FastAPI()

app.mount("/<unique-sub-app-prefix>", <sub_app_name>_app)
```

and run the central fastapi application with all mounted sub-applications:

```
python manage.py start-server
```

That's it! You can now create and manage sub-applications using the CLI app and mount them on the central fastapi application as needed, and run the main app or the sub-applications as you like.
