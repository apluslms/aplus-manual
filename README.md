# Course development manual for A-plus learning environment

This is an A+ course which advises how to make a new course on the
[A+ e-learning platform](https://github.com/apluslms/a-plus).
A+ is currently used on many computer science courses at Aalto University.
This manual has been deployed in the A+ server
[plus.cs.aalto.fi](https://plus.cs.aalto.fi/aplus-manual/master/)
where you may browse the manual without installing anything on your computer.

There is a simple [template](https://github.com/apluslms/aplus-course-template)
for starting new courses.
It includes the files that a course repository is always required to contain.

## Installation

This tutorial has been tested in the Ubuntu Linux environment and it probably works
on any Unix / Linux / Mac environment. There are some issues on the Windows operating system,
but if you prefer using Windows, you could either install Ubuntu in a virtual machine
or try Windows Subsystem for Linux (WSL).

The following software needs to be installed on your computer:

- [Git version control system](https://git-scm.com/)
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
  * Linux: [package docker-ce](https://docs.docker.com/engine/install/ubuntu/) and
    [package docker-compose](https://packages.ubuntu.com/focal/docker-compose)
    ([alternative instructions](https://docs.docker.com/compose/install/))
  * Mac: [Docker Desktop on Mac](https://docs.docker.com/desktop/mac/install/)

All other software runs inside Docker containers.

1. Git clone this repository:

    `git clone https://github.com/apluslms/aplus-manual.git`

2. Get A-plus-rst-tools: `git submodule update --init`

3. Run `./docker-compile.sh` in the aplus-manual directory to compile RST files to HTML and YAML.

4. Run `./docker-up.sh` to launch the A-plus system at http://localhost:8000
    * Available users are `root`:`root`, `teacher`:`teacher`, `student`:`student` and `assistant`:`assistant`
      (the password is the same as the username).
    * The course that is currently run in the container is named "Def. Course" on the front page.

5. In order to practice, you could edit some course contents,
   compile again (`./docker-compile.sh`)
   and refresh the web page to see the changes.
   You may need to import the course again in the "Edit course" page
   (unless you shut down the `./docker-up.sh` script, but it is a bit slow to restart it).
   Importing is especially required if you change course settings or add new chapters or assignments.
   If you only modify chapter contents,
   you may still need to clear the content cache in the "Edit course" page.

6. You should download new containers with `docker-compose pull` at least yearly.
   In the docker-compose.yml file,
   you can see the version tags of the images run-aplus-front and run-mooc-grader.
   When new A+ versions are released,
   you should update the image versions in your course.

Note! Docker downloads new container images when required. In this test system,
the first exercise assessment using a new container image will produce a one-time
error as the container order times out while downloading. However, the error
will disappear if you reload the submission page once the actual assessment has
completed.

For persistent A+ database and other storage, uncomment volume entries like
`data:/data` in the `docker-compose.yml` file.

## Developing new grading environments as containers

The assignment configuration can name any container in https://hub.docker.com/.
We have published a few containers,
which support grading using different programming languages or environments,
at https://hub.docker.com/u/apluslms/.
Study the sample exercises in the Aplus Manual
in order to learn how to run grader programs inside containers.

The grading container MUST register feedback by an HTTP POST request to the URI
`$REC/container-post` where `$REC` is an environment variable. The required request
fields include `points`, `max_points`, and `feedback` (HTML data). The provided base
container, [grading-base](https://github.com/apluslms/grading-base/), has
convenience commands to capture feedback output from any programs and register
the result at the end. Either build your custom container on top of our
base container or implement the HTTP POST interface yourself. Different
Dockerfiles and included scripts are a good reference.
The Dockerfiles of the existing grading containers are located
in the `grade-*` git repositories under https://github.com/apluslms,
e.g., [grade-python](https://github.com/apluslms/grade-python).
A new Dockerfile can use grading-base as the base image
with the instruction `FROM grading-base:4.0`.
