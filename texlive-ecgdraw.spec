%global tl_name ecgdraw
%global tl_revision 76130

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Draws electrocardiograms (ECG)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/ecgdraw
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecgdraw.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the \ECG{<code>} command which draws
electrocardiograms (ECG). The <code> represents a series of
abbreviations which allow to draw different types of wave.

