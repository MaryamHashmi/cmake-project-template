import sys

#from skbuild import setup
from distutils.command.build import build
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError

from setuptools import setup, find_packages
#from setuptools.command.build import build

def make_install():
    if subprocess.call(["make", "install"]) != 0:
        raise EnvironmentError("error calling make install")

def make():
    if subprocess.call(["make"]) != 0:
        raise EnvironmentError("error calling make")

def mkdir():
    if subprocess.call(["mkdir", "build"]) != 0:
        raise EnvironmentError("error calling mkdir build")
def cd_build():
    if subprocess.call(["cd", "build"]) != 0:
        raise EnvironmentError("error calling cd build")

def cmake():
    if subprocess.call(["cmake", ".."]) != 0:
        raise EnvironmentError("error calling cmake")
class MyInstall(build):

    def run(self):
        print('\n\n\nIN RUN SETUP.PY')
        try:
            self.spawn(['ls', '-l'])
        except DistutilsExecError:
            self.warn('Listing failed')
        
        mkdir()
        cd_build()
        cmake()
        build.run(self)
        make()
        make_install()
# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])
setup_requires = pytest_runner
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="dummy-cmake-project",
    version="1.0.0",
    description="a minimal example package (cpp version)",
    author='phylanx',
    license="MIT",
    long_description="version 1.0.0",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    tests_require=['pytest'],
    setup_requires=setup_requires,
    python_requires='>=3.6',
    mdclass={'build': MyInstall}
)

