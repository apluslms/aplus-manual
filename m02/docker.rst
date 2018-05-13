Docker
=======================================================

.. styled-topic::

  Main questions:
      What is Docker? How are A+ and other software related to each other?

  Topics?
      Docker containers, A+ architecture.

  What you are supposed to do?
      Read the material. Try the Docker tutorial if you want to know more.

  Difficulty:
      You need UNIX terminal. We will not go deep into software technology,
      but show some things that are good to know for all course authors.

  Laboriousness:
      1-2 hours

.. admonition:: Software: Docker
  :class: meta

  `Docker <https://www.docker.com/>`_ is software which runs another software
  inside a *container*: an independent, executable package of software.
  When a software, like web server, Sphinx, or A+, runs inside a container,
  it thinks it has a computer of its own. The container has all the files
  that the software requires, like some particular directory structure and
  particular versions of some software libraries. When a container is built
  for a software, it will always run the similar way regardless of what kind
  of hardware and software is outside the container.

.. admonition:: Docker versus virtual machines
  :class: note

  A technical remark: Docker is not a typical *virtual machine* or *emulator*,
  which creates a whole imaginary computer inside another physical computer.
  Different Docker containers running on the same computer utilise the hardware
  operating system kernel (the software which controls the other software
  resources, like memory, disk and processor time efficiently. They share the
  same and shares those resources by their request).

The Docker home page also has `a short explanation of containers
<https://www.docker.com/what-container>`_.

The reasons for using Docker in A+ are the following:

- Easy installation 1: just install Docker and it will install all other
  software for you.

- Easy installation 2: the containers work the same way both on your own
  computer and the A+ production server which students use.

- Easy server updates: there are many containers running on the prodution
  server. One can update just one container and it will surely not affect
  all other containers.

- Fault-tolerance: there can be multiple similar containers running,
  for example, grading students' programming exercises. If one container
  would break, because it has a bug or the student's program has a bug,
  it can be shut down and other grading containers can still finish
  their job.

- Scalability: it is easy to build a large service which uses many different
  types of containers and runs on many server computers together.

The A+ architecture
-------------------

It is good to know a little what happens inside your computer when you
develop a course.

.. image:: /images/aplus-architecture.png

The image above shows the software architecture of A+. The course directory
on your computer
