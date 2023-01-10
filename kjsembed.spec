#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kjsembed
Version  : 5.101.0
Release  : 122
URL      : https://download.kde.org/stable/frameworks/5.101/portingAids/kjsembed-5.101.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.101/portingAids/kjsembed-5.101.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.101/portingAids/kjsembed-5.101.0.tar.xz.sig
Summary  : Embedded JS
Group    : Development/Tools
License  : LGPL-2.1
Requires: kjsembed-bin = %{version}-%{release}
Requires: kjsembed-lib = %{version}-%{release}
Requires: kjsembed-license = %{version}-%{release}
Requires: kjsembed-locales = %{version}-%{release}
Requires: kjsembed-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kjs-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KJSEmbed
Binding Javascript object to QObjects
## Introduction
KSJEmbed provides a method of binding JavaScript objects to QObjects,
so you can script your applications.

%package bin
Summary: bin components for the kjsembed package.
Group: Binaries
Requires: kjsembed-license = %{version}-%{release}

%description bin
bin components for the kjsembed package.


%package dev
Summary: dev components for the kjsembed package.
Group: Development
Requires: kjsembed-lib = %{version}-%{release}
Requires: kjsembed-bin = %{version}-%{release}
Provides: kjsembed-devel = %{version}-%{release}
Requires: kjsembed = %{version}-%{release}

%description dev
dev components for the kjsembed package.


%package lib
Summary: lib components for the kjsembed package.
Group: Libraries
Requires: kjsembed-license = %{version}-%{release}

%description lib
lib components for the kjsembed package.


%package license
Summary: license components for the kjsembed package.
Group: Default

%description license
license components for the kjsembed package.


%package locales
Summary: locales components for the kjsembed package.
Group: Default

%description locales
locales components for the kjsembed package.


%package man
Summary: man components for the kjsembed package.
Group: Default

%description man
man components for the kjsembed package.


%prep
%setup -q -n kjsembed-5.101.0
cd %{_builddir}/kjsembed-5.101.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673365565
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673365565
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kjsembed
cp %{_builddir}/kjsembed-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kjsembed/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
pushd clr-build
%make_install
popd
%find_lang kjsembed5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kjscmd5
/usr/bin/kjsconsole

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KJsEmbed/KJsEmbed/KJsEmbed
/usr/include/KF5/KJsEmbed/kjsembed/binding_support.h
/usr/include/KF5/KJsEmbed/kjsembed/kjseglobal.h
/usr/include/KF5/KJsEmbed/kjsembed/kjsembed.h
/usr/include/KF5/KJsEmbed/kjsembed/kjsembed_export.h
/usr/include/KF5/KJsEmbed/kjsembed/pointer.h
/usr/include/KF5/KJsEmbed/kjsembed/static_binding.h
/usr/include/KF5/KJsEmbed/kjsembed/variant_binding.h
/usr/lib64/cmake/KF5JsEmbed/KF5JsEmbedConfig.cmake
/usr/lib64/cmake/KF5JsEmbed/KF5JsEmbedConfigVersion.cmake
/usr/lib64/cmake/KF5JsEmbed/KF5JsEmbedTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5JsEmbed/KF5JsEmbedTargets.cmake
/usr/lib64/libKF5JsEmbed.so
/usr/lib64/qt5/mkspecs/modules/qt_KJsEmbed.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5JsEmbed.so.5
/usr/lib64/libKF5JsEmbed.so.5.101.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kjsembed/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kjscmd5.1
/usr/share/man/ca@valencia/man1/kjscmd5.1
/usr/share/man/de/man1/kjscmd5.1
/usr/share/man/es/man1/kjscmd5.1
/usr/share/man/fr/man1/kjscmd5.1
/usr/share/man/it/man1/kjscmd5.1
/usr/share/man/man1/kjscmd5.1
/usr/share/man/nl/man1/kjscmd5.1
/usr/share/man/pt/man1/kjscmd5.1
/usr/share/man/pt_BR/man1/kjscmd5.1
/usr/share/man/ru/man1/kjscmd5.1
/usr/share/man/sv/man1/kjscmd5.1
/usr/share/man/uk/man1/kjscmd5.1

%files locales -f kjsembed5.lang
%defattr(-,root,root,-)

