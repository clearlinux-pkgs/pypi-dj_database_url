#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-dj_database_url
Version  : 2.0.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/12/86/baa0420d364dc9b3d78198ff6a73c2f41d8997026ddb36615d07dbf4c472/dj-database-url-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/86/baa0420d364dc9b3d78198ff6a73c2f41d8997026ddb36615d07dbf4c472/dj-database-url-2.0.0.tar.gz
Summary  : Use Database URLs in your Django Application.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-dj_database_url-license = %{version}-%{release}
Requires: pypi-dj_database_url-python = %{version}-%{release}
Requires: pypi-dj_database_url-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
DJ-Database-URL
~~~~~~~~~~~~~~~
.. image:: https://jazzband.co/static/img/badge.png
:target: https://jazzband.co/
:alt: Jazzband

%package license
Summary: license components for the pypi-dj_database_url package.
Group: Default

%description license
license components for the pypi-dj_database_url package.


%package python
Summary: python components for the pypi-dj_database_url package.
Group: Default
Requires: pypi-dj_database_url-python3 = %{version}-%{release}

%description python
python components for the pypi-dj_database_url package.


%package python3
Summary: python3 components for the pypi-dj_database_url package.
Group: Default
Requires: python3-core
Provides: pypi(dj_database_url)
Requires: pypi(django)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-dj_database_url package.


%prep
%setup -q -n dj-database-url-2.0.0
cd %{_builddir}/dj-database-url-2.0.0
pushd ..
cp -a dj-database-url-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682972692
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dj_database_url
cp %{_builddir}/dj-database-url-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dj_database_url/77728a126517af7d601bac9cd4c8f69556b7e3da || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dj_database_url/77728a126517af7d601bac9cd4c8f69556b7e3da

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
