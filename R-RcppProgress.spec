#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppProgress
Version  : 0.4.1
Release  : 9
URL      : https://cran.r-project.org/src/contrib/RcppProgress_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppProgress_0.4.1.tar.gz
Summary  : An Interruptible Progress Bar with OpenMP Support for C++ in R
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
BuildRequires : clr-R-helpers

%description
console for long running computations taking place in c++ code,
    and support for interrupting those computations even in multithreaded
    code, typically using OpenMP.

%prep
%setup -q -c -n RcppProgress

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526565282

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1526565282
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppProgress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppProgress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppProgress
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RcppProgress|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppProgress/DESCRIPTION
/usr/lib64/R/library/RcppProgress/INDEX
/usr/lib64/R/library/RcppProgress/Meta/Rd.rds
/usr/lib64/R/library/RcppProgress/Meta/features.rds
/usr/lib64/R/library/RcppProgress/Meta/hsearch.rds
/usr/lib64/R/library/RcppProgress/Meta/links.rds
/usr/lib64/R/library/RcppProgress/Meta/nsInfo.rds
/usr/lib64/R/library/RcppProgress/Meta/package.rds
/usr/lib64/R/library/RcppProgress/NAMESPACE
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/DESCRIPTION
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/NAMESPACE
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/R/examples.R
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/man/RcppProgressExample-package.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/man/test_multithreaded.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/man/test_sequential.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/src/Makevars
/usr/lib64/R/library/RcppProgress/examples/RcppProgressArmadillo/src/example.cpp
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/DESCRIPTION
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/NAMESPACE
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/R/examples.R
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/src/Makevars
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/src/eta_progress_bar.hpp
/usr/lib64/R/library/RcppProgress/examples/RcppProgressETA/src/example.cpp
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/DESCRIPTION
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/NAMESPACE
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/R/examples.R
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/man/RcppProgressExample-package.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/man/test_multithreaded.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/man/test_sequential.Rd
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/src/Makevars
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/src/dummy.cpp
/usr/lib64/R/library/RcppProgress/examples/RcppProgressExample/src/example.cpp
/usr/lib64/R/library/RcppProgress/help/AnIndex
/usr/lib64/R/library/RcppProgress/help/RcppProgress.rdb
/usr/lib64/R/library/RcppProgress/help/RcppProgress.rdx
/usr/lib64/R/library/RcppProgress/help/aliases.rds
/usr/lib64/R/library/RcppProgress/help/paths.rds
/usr/lib64/R/library/RcppProgress/html/00Index.html
/usr/lib64/R/library/RcppProgress/html/R.css
/usr/lib64/R/library/RcppProgress/include/interruptable_progress_monitor.hpp
/usr/lib64/R/library/RcppProgress/include/interrupts.hpp
/usr/lib64/R/library/RcppProgress/include/progress.hpp
/usr/lib64/R/library/RcppProgress/include/progress_bar.hpp
/usr/lib64/R/library/RcppProgress/include/simple_progress_bar.hpp
