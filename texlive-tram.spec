# revision 24395
# category Package
# catalog-ctan /macros/latex/contrib/tram
# catalog-date 2011-10-25 13:37:10 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tram
Version:	0.1
Release:	3
Summary:	Typeset tram boxes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tram
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tram.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Tram boxes are highlighted with patterns of dots; the package
defines an environment tram that typesets its content into a
tram box. The pattern used may be selected in an optional
argument to the environment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/tram/tram.mf
%{_texmfdistdir}/tex/latex/tram/tram.sty
%doc %{_texmfdistdir}/doc/latex/tram/README
%doc %{_texmfdistdir}/doc/latex/tram/tram-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tram/tram-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 757076
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719791
- texlive-tram
- texlive-tram
- texlive-tram

