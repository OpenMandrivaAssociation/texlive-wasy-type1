%global tl_name wasy-type1
%global tl_revision 53534

Name:		texlive-%{tl_name}
Epoch:		1
Version:	001.002
Release:	%{tl_revision}.1
Summary:	Type 1 versions of wasy fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/wasy-type1
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(wasy)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Converted (Adobe Type 1) outlines of the wasy fonts.

