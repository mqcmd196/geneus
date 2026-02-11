"""Test that geneus modules and functions can be imported."""


def test_import_geneus():
    import geneus


def test_import_generate_module():
    from geneus import generate


def test_import_type_check_function():
    from geneus.generate import is_integer


def test_import_type_conversion_function():
    from geneus.generate import lisp_type


def test_import_init_function():
    from geneus.generate import lisp_initvalue


def test_import_classes():
    from geneus.generate import IndentedWriter, Indent


def test_import_write_function():
    from geneus.generate import write_serialize


def test_import_generate_function():
    from geneus.generate import generate_msg
