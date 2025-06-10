# idea-monorepo-setup
A script that configure the project structure in Jetbrains IDEA when working with mono repos. 
If the repo has multiple python projects that each use a service in a docker compose file in the root of the project.
It will follow the build context and the docker file location. Then it will generate the correct XML files for IDEA to:
* Add an SDK
* Add a module
* Set the module dependency to the correct SDK
