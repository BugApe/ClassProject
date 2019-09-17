Neural Doodle
=============




1. Examples & Usage
===================

The main script is called ``doodle.py``, which you can run with Python 3.4+ (see setup below).  The ``--device`` argument that lets you specify which GPU or CPU to use. For the samples above, here are the performance results:

* **GPU Rendering** — Assuming you have CUDA setup and enough on-board RAM, the process should complete in 3 to 8 minutes, even with twice the iteration count.
* **CPU Rendering** — This will take hours and hours, even up to 12h on older hardware. To match quality it'd take twice the time. Do multiple runs in parallel!

The default is to use ``cpu``, if you have NVIDIA card setup with CUDA already try ``gpu0``. On the CPU, you can also set environment variable to ``OMP_NUM_THREADS=4``, but we've found the speed improvements to be minimal.

1.a) Image Analogy
------------------

The algorithm is built for style transfer, but can also generate image analogies that we call a ``#NeuralDoodle``; use the hashtag if you post your images!  Example files are included in the ``#/samples/`` folder. Execute with these commands:

.. code:: bash

    # Synthesize a coastline as if painted by Monet. This uses "*_sem.png" masks for both images.
    python3 doodle.py --style samples/Monet.jpg --output samples/Coastline.png \
                      --device=cpu --iterations=40

    # Generate a scene around a lake in the style of a Renoir painting.
    python3 doodle.py --style samples/Renoir.jpg --output samples/Landscape.png \
                      --device=gpu0 --iterations=80

Notice the Renoir results look a little better than the Monet. Some rotational variations of the source image could improve the quality of the arch outline in particular.


1.b) Style Transfer
-------------------

If you want to transfer the style given a source style with annotations, and a target content image with annotations, you can use the following command lines.  In all cases, the semantic map is loaded and used if it's found under the ``*_sem.png`` filename that matches the input file.

.. code:: bash

    # Synthesize a portrait of Seth Johnson like a Gogh portrait. This uses "*_sem.png" masks for both images.
    python3 doodle.py --style samples/Gogh.jpg --content samples/Seth.png \
                      --output SethAsGogh.png --device=cpu --phases=4 --iterations=40

    # Generate what a photo of Vincent van Gogh would look like, using Seth's portrait as reference.
    python3 doodle.py --style samples/Seth.jpg --content samples/Gogh.png \
                      --output GoghAsSeth.png --device=gpu0 --phases=4 --iterations=80

To perform regular style transfer without semantic annotations, simply delete or rename the files with the semantic maps.  The photo is originally by `Seth Johnson <http://sethjohnson.tumblr.com/post/655063019/this-was-a-project-for-an-art-history-class-turns>`_, and the concept for this style transfer by `Kyle McDonald <https://twitter.com/kcimc>`_.



1.c) Texture Synthesis
----------------------

For synthesizing bitmap textures, you only need an input style without anotations and without target output.  In this case, you simply specify one input style image and the output file as follows:

.. code:: bash

    # First synthesis uses a darker noise pattern as seed.
    python3 doodle.py --style samples/Wall.jpg --output Wall.png\
                      --seed=noise --seed-range=0:128 --iterations=50 --phases=3

    # Second synthesis uses a lighter noise pattern as seed.
    python3 doodle.py --style samples/Wall.jpg --output Wall.png\
                      --seed=noise --seed-range=192:255 --iterations=50 --phases=3

You can also control the output resolution using ``--output-size=512x512`` parameter—which also depends on the memory you have available. By default the size will be the same as the style image.

1.d) Script Parameters
----------------------
You can configure the algorithm using the following parameters. Type ``python3 doodle.py --help`` for the full list of options, or see the source code.

* ``--style-weight=50.0`` — Weight of style relative to content.
* ``--style-layers=3_1,4_1`` — The layers to match style patches.
* ``--semantic-weight=1.0`` — Global weight of semantics vs. features.
* ``--smoothness=1.0`` — Weight of image smoothing scheme.
* ``--seed=noise`` — Seed image path, "noise" or "content".
* ``--print-every=10`` — How often to log statistics to stdout.
* ``--save-every=10`` — How frequently to save PNG into `frames`.

2. Installation & Setup
=======================

This project requires Python 3.4+ and you'll also need ``numpy`` and ``scipy`` (numerical computing libraries) as well as ``python3-dev`` installed system-wide.  If you want more detailed instructions, follow these:

3. `Windows Installation of Lasagne <https://github.com/Lasagne/Lasagne/wiki/From-Zero-to-Lasagne-on-Windows-7-%2864-bit%29>`_ **(expert)**

Afterward fetching the repository, you can run the following commands from your terminal to setup a local environment:

.. code:: bash

    # Setup the required dependencies simply using the PIP module.
    python3 -m pip install --ignore-installed -r requirements.txt

    #Lasagne安装下面版本
    pip3 install git+git://github.com/Lasagne/Lasagne.git@31ac7d2bbcb4777b9a500b

After this, you should have ``scikit-image``, ``theano`` and ``lasagne`` installed in your virtual environment.  



