CLI
===

ntc_rosetta comes with a simple CLI tool to help with various things:

   1. Lint parsers/translators
   2. Print the supported models as an ASCII tree
   3. Print the parser/translator as an ASCII tree similar to the supported models output

To execute the command line tool type ``ntc_rosetta`` after installing the library::

   $ ntc_rosetta git:(docs) ✗ ntc_rosetta
   Usage: ntc_rosetta [OPTIONS] COMMAND [ARGS]...

   Options:
     --help  Show this message and exit.

   Commands:
     lint          Lint files/folders with Parsers/Translators: Errors/Warning...
     print-model   Prints the model as an ASCII tree
     print-parser  Prints a tree representation of a parser/translator.

The command line tool is self-documented and you can check it's documentation using the ``--help`` flag.
