## A course template for A-plus learning environment

This is a codebase which teaches how to make a new course on
[A+ e-learning system](https://github.com/Aalto-LeTech/a-plus>).
A+ is currently used on many computer science courses on Aalto University.

## Installation

This tutorial is tested with Aalto Ubuntu Linux environment and it probably works
on any Unix / Linux / Mac environment. It is assumed that you already have
the following software.

- [git](https://git-scm.com/)
- [make](https://www.gnu.org/software/make/)

All other software runs inside [Docker](https://www.docker.com/) containers.

1. Git clone this repository. Select branch `rst` for courses using RST materials and `master for simple exercise courses. E.g.:

    `git clone --branch rst https://github.com/apluslms/course-templates.git my_new_course`

2. Install Docker for Mac/Windows or docker-ce & docker-compose for Linux.
    * https://docs.docker.com/engine/installation/
    * https://docs.docker.com/compose/install/

2. Get a-plus-rst-tools: `git submodule init` and `git submodule update`

3. ./docker-compile.sh to compile RST files to HTML and YAML.

4. ./docker-up.sh to run A-plus system at http://localhost:8000
    * Available users are `root`:`root` and `student`:`student`.
    * The default course is created from the material.

5. Insert the course material in a new git repository for the course.
Keep editing and test in browser.

6. You should download new containers with `docker-compose pull` at least yearly.

Note! Docker downloads new container images when required. In this test system,
the first exercise assessment using new container image will produce a one time
error as the container order times out while downloading. However, the error
will disappear if you reload the submission page once the actual assessment has
completed.

For persistent A+ database and other storage, uncomment volume entries like
`./_data:...` in the `docker-compose.yml`.

## Developing new assessment environments as containers

The exercise config can name any container in https://hub.docker.com/. We have
published few containers that support assessment for different environments at
https://hub.docker.com/u/apluslms/. Use the sample exercises in the course
template for reference to run assessment programs inside the containers.

The assessment container MUST register feedback by HTTP POST request to URI
$REC/container-post where $REC is an environment variable. The required request
fields are `points`, `max_points`, and `feedback` (HTML data). The provided base
container, https://github.com/A-plus-LMS/grading-base/tree/debian-stretch, has
convenience commands to capture feedback output from any programs and register
the result at end. Either build your custom container on hierarchy from our
base container or implement the HTTP POST interface yourself. Different
Dockerfiles and included scripts are a good reference.
