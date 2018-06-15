Converting an existing A+ course to Docker
==========================================

If you maintain an existing A+ course, and it uses a `Python virtual
environment <https://docs.python.org/3/tutorial/venv.html>`_ (just
"virtualenv"), this section describes how to convert it to the `Docker
environment <../m01_introduction/05_docker>`_.

An A+ course not using Docker does not have `docker-compile.sh` and
`docker-up.sh` scripts. Instead, the course is typically compiled with commands
`source venv/bin/activate` and `make html`. A python virtualenv is more like a
Python package manager compared to Docker; each virtualenv installs a specific
version of Python and specific version of libraries. A+ Docker containers
also have that, but moreover, they have all the software preconfigured and
ready to use. In contrast, developing a virtualenv A+ course with also A+
and mooc-grader installed on your computer with virtualenv requires extra
manual configuration steps. Therefore the aim of A+ Docker containers is to
make course development and deployment as easy as possible.
