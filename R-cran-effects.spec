%define		fversion	%(echo %{version} |tr r -)
%define		modulename	effects
Summary:	Effect Displays for Linear and Generalized Linear Models
Summary(pl):	Wy¶wietlanie efektów dla liniowych i uogólnionych modeli liniowych
Name:		R-cran-%{modulename}
Version:	1.0r5
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	79390a9807537b24e92956a0614c4ac7
URL:		http://socserv.socsci.mcmaster.ca/jfox/
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R-cran-grid
Requires:	R-cran-lattice
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical and tabular effect displays, e.g., of interactions, for
linear and generalised linear models.

%description -l pl
Graficzne i tablicowe wy¶wietlanie efektów, np. interakcji, dla
liniowych i uogólnionych modeli liniowych.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
