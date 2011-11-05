# revision 24395
# category Package
# catalog-ctan /macros/latex/contrib/tram
# catalog-date 2011-10-25 13:37:10 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tram
Version:	0.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Tram boxes are highlighted with patterns of dots; the package
defines an environment tram that typesets its content into a
tram box. The pattern used may be selected in an optional
argument to the environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/tram/tram.mf
%{_texmfdistdir}/tex/latex/tram/tram.sty
%doc %{_texmfdistdir}/doc/latex/tram/README
%doc %{_texmfdistdir}/doc/latex/tram/tram-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tram/tram-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
