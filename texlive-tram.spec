%global tl_name tram
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Typeset tram boxes in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tram
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Tram boxes are highlighted with patterns of dots; the package defines an
environment tram that typesets its content into a tram box. The pattern
used may be selected in an optional argument to the environment.

