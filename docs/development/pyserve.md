title: "Python server command"
tags: webdev, python, commandline, development
author: Colm Britton
--------------------

I use the inbuilt python server a lot. It allows me to test a directory of HTML files.

I kept forgetting the full command (`python -m http.server 8000 --bind 127.0.0.1`) so created an `alias` in my bash profile.

Put this line in `~/.bash_profile`:

    alias pyserve='python -m http.server 8000 --bind 127.0.0.1'

The to serve, `cd` into dir and run `pyserve`.

There was one problem with this approach. If the whole directory gets replaced (deleted then rebuilt) it breaks.

Python 3.8+ has the answer. You can include the directory to serve as an argument using `--directory`.

To make use of the change I replace the `pyserve` alias with a function.

    function pyserve-dir() {
        python -m http.server 8000 --bind 127.0.0.1 --directory $1
    }

Now to serve a directory I run

    pyserve-dir <path-to-dir>
