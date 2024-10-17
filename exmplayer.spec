Summary:	MPlayer GUI with thumbnail seeking and 3D Video support
Name:		exmplayer
Version:	3.2.0
Release:	2
Group:		Video
License:	GPLv2+
Url:		https://exmplayer.sourceforge.net/
Source0:	https://github.com/rupeshs/ExMplayer/archive/%{name}_%{version}.tar.gz
Patch0:		exmplayer-3.2.0-gcc47.patch
Patch1:		exmplayer-3.2.0-segfault.patch
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	qt4-devel
Requires:	ffmpeg
Requires:	mplayer

%description
ExMplayer(Extended MPlayer) is a GUI front-end for MPlayer.

Version 3 introduces 3D video playback,wide variety of 3D video formats
supported. Volume booster with volume boost up to 5000%. It can play audio,
video, dvd files(.vob), vcd files(.mpg, .dat), mp4, mkv etc, supports network
streaming and subtitles. ExMplayer has many useful tools like audio converter,
audio extractor,media cutter.

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_enqueue.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n ExMplayer
%patch0 -p1
%patch1 -p1

%build
cd src
%qmake_qt4
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/%{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 linux_build/fmts %{buildroot}%{_sysconfdir}/%{name}/fmts
install -m 0644 linux_build/sc_default.xml %{buildroot}%{_sysconfdir}/%{name}/sc_default.xml

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m 0644 %{name}_enqueue.desktop %{buildroot}%{_datadir}/applications/%{name}_enqueue.desktop

mkdir -p %{buildroot}%{_datadir}/%{name}
ln -s %{_bindir}/ffmpeg %{buildroot}%{_datadir}/%{name}/ffmpeg

# install menu icons
for N in 16 32 48 64 128 256;
do
convert debian/%{name}.png -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

