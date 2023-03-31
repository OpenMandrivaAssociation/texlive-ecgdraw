Name:		texlive-ecgdraw
Version:	41617
Release:	2
Summary:	Draws electrocardiograms (ECG)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ecgdraw
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the \ECG{<code>} command which draws
electrocardiograms (ECG). The <code> represents a series of
abbreviations which allow to draw different types of wave.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ecgdraw
%{_texmfdistdir}/tex/latex/ecgdraw
%doc %{_texmfdistdir}/doc/latex/ecgdraw

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
