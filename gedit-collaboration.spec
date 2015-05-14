# NOTE: needs more fixes for libinfinity 0.6.x; doesn't build with gedit 3.16
Summary:	GEdit plugin providing support for collaborative editing
Summary(pl.UTF-8):	Wtyczka GEdita z obsługą edycji grupowej
Name:		gedit-collaboration
Version:	3.6.1
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-collaboration/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	c6e3aa8b41798586d8d46ff837b0871b
Patch0:		%{name}-libinfinity.patch
URL:		https://git.gnome.org/browse/gedit-collaboration/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	gedit-devel >= 3.6
# uses some APIs removed later
BuildRequires:	gedit-devel < 3.8
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.41.0
BuildRequires:	libinfinity-devel >= 0.5
BuildRequires:	libinfinity-gtk3-devel >= 0.5
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26
Requires:	gedit >= 3.6
Requires:	gtk+3 >= 3.4
Requires:	libinfinity >= 0.5
Requires:	libinfinity-gtk3 >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEdit plugin providing support for collaborative editing.

%description -l pl.UTF-8
Wtyczka GEdita z obsługą edycji grupowej.

%prep
%setup -q
#%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%{_libdir}/gedit/plugins/collaboration.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libcollaboration.so
%{_datadir}/gedit/plugins/collaboration
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.collaboration.gschema.xml
