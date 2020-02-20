Name:           zerofree
Version:        1.1.1
Release:        3
Summary:        Utility to force unused ext2/3/4 inodes and blocks to zero
License:        GPLv2
URL:            https://frippery.org/uml/
Source0:        https://frippery.org/uml/%{name}-%{version}.tgz
Source1:        https://frippery.org/uml/sparsify.c
Source2:        zerofree.8
BuildRequires:  e2fsprogs-devel

%description
This module is a utility to set unused filesystem inodes and blocks of an ext2/3/4 filesystem to zero,
which can improve the compressibility and privacy of an ext2/3/4 filesystem.

%package        help
Summary:        man files for %{name}
Requires:       man

%description    help
This package includes man files for %{name}.

%prep
%autosetup -p1
cp -p %{SOURCE1} .

%build
make CC="gcc $RPM_OPT_FLAGS"
gcc $RPM_OPT_FLAGS sparsify.c -o sparsify -lext2fs

%install
install -D -p -m 755 zerofree $RPM_BUILD_ROOT%{_sbindir}/zerofree
install -D -p -m 755 sparsify $RPM_BUILD_ROOT%{_sbindir}/sparsify
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man8/zerofree.8

%files
%license COPYING
%{_sbindir}/*

%files help
%{_mandir}/man*/*

%changelog
* Thu Dec 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.1-3
- Package init
