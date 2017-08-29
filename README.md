

## A course template for A-plus learning environment

1. Download the template files.

2. Install Docker for Mac/Windows or docker-ce & docker-compose for Linux.
    * https://docs.docker.com/engine/installation/
    * https://docs.docker.com/compose/install/

3. ./docker-up.sh to run A-plus system at http://localhost:8000
    * Available users are `root`:`root` and `student`:`student`.
    * The default course is created from the material.
    * On first start, go `Edit Course` on left and click `Apply` on top.
      This configures the course modules and excercises according to index.yaml.

4. ./docker-compile.sh to compile changes in RST files.

5. Insert the course material in a new git repository for the course.
Keep editing and test in browser.

Note! Docker downloads new container images when required. In this test system,
the first exercise assessment using new container image will produce a one time
error as the container order times out while downloading. However, the error
will disappear if you reload the submission page once the actual assessment has
completed.


## Developing new assessment environments as containers

The exercise config can name any container in https://hub.docker.com/. We have
published few containers that support assessment for different environments at
https://hub.docker.com/u/apluslms/. Use the sample exercises in the course
template for reference to run assessment programs inside the containers.

The assessment container MUST register feedback by HTTP POST request to URI
$REC/container-post where $REC is an environment variable. The required request
fields are points, max_points, and feedback (HTML data). The provided base
container, https://github.com/A-plus-LMS/grading-base/tree/debian-stretch, has
convenience commands to capture feedback output from any programs and register
the result at end. Either build your custom container on hierarchy from our
base container or implement the HTTP POST interface yourself. Different
Dockerfiles and included scripts are a good reference.
