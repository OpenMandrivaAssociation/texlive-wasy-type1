Name:		texlive-wasy-type1
Version:	53534
Release:	1
Summary:	Type 1 versions of wasy fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wasy-type1
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Converted (Adobe Type 1) outlines of the wasy fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/public/wasy-type1
%{_texmfdistdir}/fonts/map/dvips/wasy-type1
%{_texmfdistdir}/fonts/afm/public/wasy-type1
%doc %{_texmfdistdir}/doc/fonts/wasy-type1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
