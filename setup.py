from distutils.core import setup, Extension

lion_scrypt_module = Extension('lion_scrypt',
                               sources = ['scryptmodule.c',
                                          'scrypt.c'],
                               include_dirs=['.'], extra_compile_args=['-O3', '-msse3'])

setup (name = 'lion_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by Lioncoin',
       ext_modules = [lion_scrypt_module])
