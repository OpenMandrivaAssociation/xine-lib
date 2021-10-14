%define build_optimization 0
%define dvdnav 0.1.4

%define build_pulse 1
%define build_magick 0
%define build_caca 1
%define build_directfb 1
%define external_vcdnav 1
%define build_smb 1
%define build_alsa 1
%define build_linuxfb 1

%define build_vidix 0

%define build_xvid 0
%define build_faad 0
%define build_win32 0
%ifarch %{ix86}
%define build_win32 1
%endif

%if %mdvver <= 3000000
%define x86_64 x86_64
%endif

%define external_ffmpeg 1

%{?_with_plf: %{expand: %%global build_plf 1}}

######################
# Hardcode PLF buildTo 
%define build_plf 0
######################

%if %{build_plf}
%define distsuffix plf
%define build_faad 1
%define extrarelsuffix plf
%endif

%{?_with_optimization: %{expand: %%global build_optimization 1}}
%{?_with_directfb: %{expand: %%global build_directfb 1}}
%{?_without_directfb: %{expand: %%global build_directfb 0}}
%{?_with_alsa: %{expand: %%global build_alsa 1}}
%{?_without_alsa: %{expand: %%global build_alsa 0}}
%{?_with_vcdnav: %{expand: %%global external_vcdnav 1}}
%{?_without_vcdnav: %{expand: %%global external_vcdnav 0}}
%{?_with_vidix: %{expand: %%global build_vidix 1}}
%{?_without_vidix: %{expand: %%global build_vidix 0}}
%{?_with_linuxfb: %{expand: %%global build_linuxfb 1}}
%{?_without_linuxfb: %{expand: %%global build_linuxfb 0}}
%{?_with_faad: %{expand: %%global build_faad 1}}
%{?_without_faad: %{expand: %%global build_faad 0}}
%{?_with_win32: %{expand: %%global build_win32 1}}
%{?_without_win32: %{expand: %%global build_win32 0}}
%{?_with_xvid: %{expand: %%global build_xvid 1}}
%{?_without_xvid: %{expand: %%global build_xvid 0}}
%{?_with_smb: %{expand: %%global build_smb 1}}
%{?_without_smb: %{expand: %%global build_smb 0}}
%{?_with_pulse: %{expand: %%global build_pulse 1}}
%{?_without_pulse: %{expand: %%global build_pulse 0}}
%{?_with_magick: %{expand: %%global build_magick 1}}
%{?_without_magick: %{expand: %%global build_magick 0}}
%{?_with_ffmpeg: %{expand: %%global external_ffmpeg 1}}
%{?_without_ffmpeg: %{expand: %%global external_ffmpeg 0}}

%define bname xine
%define major 2
%define api 2.9
%define libname %mklibname xine %{major}
%define devname %mklibname -d xine

Summary:	A Free Video Player (Libraries)
Name:		xine-lib
Version:	1.2.11
Release:	2%{?extrarelsuffix}
License:	GPLv2+
Group:		System/Libraries
Url:		http://xine.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/xine/xine-lib/%{version}/xine-lib-%{version}.tar.xz
Patch1:		xine-lib-1.2.6-clang.patch

BuildRequires:	pkgconfig(slang)
BuildRequires:	a52dec-devel
BuildRequires:	aalib-devel
BuildRequires:	gettext-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	optipng
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xvmc)
BuildRequires:  pkgconfig(alsa)
BuildRequires:	pkgconfig(dav1d)
BuildRequires:	pkgconfig(aom)
%if %{build_smb}
BuildRequires:	pkgconfig(smbclient)
%endif
%if %{external_vcdnav}
BuildRequires:	pkgconfig(libvcdinfo)
%endif
%if %{build_directfb}
BuildRequires:	pkgconfig(directfb)
%endif
%if %{external_ffmpeg}
BuildRequires:	pkgconfig(libavcodec)
%endif

%description
xine is a free gpl-licensed video player for unix-like systems.

%if %{build_plf}
This package is in restricted repository because the AAC decoder is
covered by patents.
%endif

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A Free Video Player (Libraries)
Group:		System/Libraries
Provides:	xine-lib

%description -n %{libname}
xine is a free gpl-licensed video player for unix-like systems.

This package contains the shared libraries required by xine.

%files -n %{libname}
%{_libdir}/libxine.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel files for xine
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libxine-devel = %{version}-%{release}

%description -n %{devname}
xine is a free gpl-licensed video player for unix-like systems.

This package contains the development files required for compiling xine
front ends or plugins.

%files -n %{devname}
%doc README AUTHORS TODO
%doc ChangeLog installed-docs/hackersguide
%{_bindir}/xine-config
%{_bindir}/xine-list-1.2
%{_mandir}/man1/xine-config.1*
%{_mandir}/man1/xine-list-1.2.1*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libxine.pc
%{_datadir}/aclocal/xine.m4
%{_includedir}/*.h
%{_includedir}/xine

#----------------------------------------------------------------------------

%package -n %{bname}-plugins
Summary:	A Free Video Player (main plugins)
Group:		Video
Provides:	%{bname}-xv %{bname}-gl %{bname}-oss %{libname}-docs %{bname}-speex
Provides:	%{bname}-dvdnav %{bname}-alsa %{bname}-musepack
%if %{build_win32}
Provides:	xine-plugins-win32
Provides:	xine-win32
#Suggests: win32-codecs
%endif
# Plugins are in versioned dir, so require the exact version
Requires:	%{libname} = %{version}
# provide the plugin API version
Provides:	xine-plugin-api = %{api}

%description -n %{bname}-plugins
xine is a free gpl-licensed video player for unix-like systems.

This package includes the main plugins for xine, they allow the input
from files, Video CDs, network streams and (not encrypted) DVDs in
several video formats.

%if %{build_optimization}
Warning: This package was optimized for the build machine and probably
will not run on other computers.
%endif

%files -n %{bname}-plugins -f libxine2.lang
%doc installed-docs/README* installed-docs/faq.*
%{_mandir}/man5/xine.5*
%dir %{_libdir}/xine/
%dir %{_libdir}/xine/plugins/
%dir %{_libdir}/xine/plugins/%{api}/
%dir %{_libdir}/xine/plugins/%{api}/post/
%{_libdir}/xine/plugins/%{api}/mime.types
%if %{build_alsa}
%{_libdir}/xine/plugins/%{api}/xineplug_ao_out_alsa.so
%endif
%{_libdir}/xine/plugins/%{api}/xineplug_ao_out_oss.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_cdda.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_dvb.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_dvd.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_mms.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_network.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_pvr.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_rtp.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_vcd.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_v4l2.so
%{_libdir}/xine/plugins/%{api}/xineplug_dmx_*so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_a52.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_dts.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_dvaudio.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_ff.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_gdk_pixbuf.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_gsm610.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_libjpeg.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_libvpx.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_lpcm.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_mad.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_mpc.so*
%{_libdir}/xine/plugins/%{api}/xineplug_decode_mpeg2.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_spu*.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_rawvideo.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_real.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_vdpau.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_bluray.so
%{_libdir}/xine/plugins/%{api}/xineplug_nsf.so
%{_libdir}/xine/plugins/%{api}/xineplug_sputext.so
%{_libdir}/xine/plugins/%{api}/xineplug_vdr.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_vaapi.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_vdpau.so
%{_libdir}/xine/plugins/%{api}/xineplug_xiph.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_dav1d.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_libaom.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_libpng.so
%{_libdir}/xine/plugins/%{api}/xineplug_decode_to_spdif.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_nfs.so
%{_libdir}/xine/plugins/%{api}/xineplug_inp_ssh.so
%{_libdir}/xine/plugins/%{api}/xineplug_tls_gnutls.so
%{_libdir}/xine/plugins/%{api}/xineplug_tls_openssl.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_gl_egl_wl.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_gl_egl_x11.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_gl_glx.so
%if %{build_directfb}
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_directfb.so
%endif
%if %{build_linuxfb}
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_fb.so
%endif
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_opengl.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_opengl2.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_raw.so
%if %{build_vidix}
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_vidix.so
%{_libdir}/xine/plugins/%{api}/vidix/
%endif
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xshm.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xv.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xvmc.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xxmc.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xcbshm.so
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_xcbxv.so
%if %{build_win32}
%{_libdir}/xine/plugins/%{api}/xineplug_decode_qt.so*
%{_libdir}/xine/plugins/%{api}/xineplug_decode_w32dll.so*
%endif
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_audio_filters.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_goom.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_mosaico.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_planar.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_switch.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_tvtime.so
%{_libdir}/xine/plugins/%{api}/post/xineplug_post_visualizations.so
%{_datadir}/xine-lib

#----------------------------------------------------------------------------

%package -n %{bname}-wavpack
Group:		Sound
Summary:	Wavpack Audio decoder plugin for xine
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-wavpack
xine is a free gpl-licensed video player for unix-like systems.

This package contains the wavpack audio decoder plugin.

%files -n %{bname}-wavpack
%doc README
%{_libdir}/xine/plugins/%{api}/xineplug_wavpack.so

#----------------------------------------------------------------------------

%package -n %{bname}-sdl
Group:		Video
Summary:	SDL video output plugin for xine
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-sdl
xine is a free gpl-licensed video player for unix-like systems.

This package contains the SDL video output plugin.

%files -n %{bname}-sdl
%doc README
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_sdl.so

#----------------------------------------------------------------------------

%if %{build_caca}
%package -n %{bname}-caca
Group:		Video
Summary:	Caca video output plugin for xine
Requires:	%{bname}-plugins = %{version}
BuildRequires:	libcaca-devel >= 0.99

%description -n %{bname}-caca
xine is a free gpl-licensed video player for unix-like systems.

This package contains the Caca video output plugin.

%files -n %{bname}-caca
%doc README
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_caca.so
%endif

#----------------------------------------------------------------------------

%package -n %{bname}-jack
Summary:	Jack plugin for xine
Group:		Sound
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-jack
xine is a free gpl-licensed video player for unix-like systems.

- Jack audio output plugin

%files -n %{bname}-jack
%{_libdir}/xine/plugins/%{api}/xineplug_ao_out_jack.so

#----------------------------------------------------------------------------

%if %{build_pulse}
%package -n %{bname}-pulse
Summary:	Pulseaudio plugin for xine
Group:		Sound
Requires:	%{bname}-plugins = %{version}
BuildRequires:	pkgconfig(libpulse)

%description -n %{bname}-pulse
xine is a free gpl-licensed video player for unix-like systems.

- pulseaudio audio output plugin

%files -n %{bname}-pulse
%{_libdir}/xine/plugins/%{api}/xineplug_ao_out_pulseaudio.so
%endif

#----------------------------------------------------------------------------

%if %{build_magick}
%package -n %{bname}-image
Summary:	ImageMagick plugin for xine
Group:		Graphics
Requires:	%{bname}-plugins = %{version}
BuildRequires:	pkgconfig(ImageMagick)

%description -n %{bname}-image
xine is a free gpl-licensed video player for unix-like systems.

- image display plugin based on ImageMagick

%files -n %{bname}-image
%doc README
%{_libdir}/xine/plugins/%{api}/xineplug_decode_image.so
%endif

#----------------------------------------------------------------------------

%package -n %{bname}-aa
Summary:	Aalib plugin for xine
Group:		Video
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-aa
xine is a free gpl-licensed video player for unix-like systems.

- Aalib textmode output plugin

%files -n %{bname}-aa
%{_libdir}/xine/plugins/%{api}/xineplug_vo_out_aa.so

#----------------------------------------------------------------------------

%ifarch %{ix86} %{x86_64} %{armx}
%package -n %{bname}-dxr3
Summary:	DXR3 plugin for xine
Group:		Video
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-dxr3
xine is a free gpl-licensed video player for unix-like systems.

- DXR3/Hollywood+ (MPEG2 hardware decoder) decoding/output plugin
%if %{build_plf}
- this version has mpeg encoding enabled using libfame.
%endif

%files -n %{bname}-dxr3
%{_libdir}/xine/plugins/%{api}/xineplug_*dxr3*.so
%endif

#----------------------------------------------------------------------------

%package -n %{bname}-flac
Summary:	FLAC plugin for xine
Group:		Sound
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-flac
xine is a free gpl-licensed video player for unix-like systems.

- FLAC audio decoder plugin

%files -n %{bname}-flac
%{_libdir}/xine/plugins/%{api}/xineplug_flac.so

#----------------------------------------------------------------------------

%if %{build_smb}
%package -n %{bname}-smb
Summary:	Samba input plugin for xine
Group:		System/Libraries
Requires:	%{bname}-plugins = %{version}

%description -n %{bname}-smb
xine is a free gpl-licensed video player for unix-like systems.

- Samba input plugin

%files -n %{bname}-smb
%{_libdir}/xine/plugins/%{api}/xineplug_inp_smb.so
%endif

#----------------------------------------------------------------------------

%if %{build_faad}
%package -n %{bname}-faad
Summary:	FAAD plugin for %{bname}
Group:		Sound
Requires:	%{bname}-plugins = %{version}
BuildRequires:	libfaad2-devel

%description -n %{bname}-faad
This package contains the AAC decoder plugin for %{bname}. It is in
restricted repository because it is covered by software patents.

%files -n %{bname}-faad
%{_libdir}/xine/plugins/%{api}/xineplug_decode_faad.so*
%endif

#----------------------------------------------------------------------------

%if %{build_xvid}
%package -n %{bname}-xvid
Summary:	XviD plugin for %{bname}
Group:		Video
Requires:	%{bname}-plugins = %{version}
Provides:	xine-plugins-xvid

%description -n %{bname}-xvid
This package contains the XviD plugin for %{bname}. It is in
restricted because it is covered by software patents.

%files -n %{bname}-xvid
%{_libdir}/xine/plugins/%{api}/xineplug_decode_xvid.so*
%endif

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#gw for flac
export OGG_LIBS=-logg

%ifarch %{ix86}
# cb - with clang gives:
# <inline asm>:22:2: error: instruction requires: 64-bit mode
export CC=gcc
export CXX=g++
%endif

%if ! %{build_optimization}
export CFLAGS="%(echo %optflags|sed s/-Wp,-D_FORTIFY_SOURCE=2//)"
%configure \
%else
%{?__cputoolize: %{__cputoolize}}
#gw expanded configure2_5x macro without the CFLAGS and --build stuff
[ -f configure.in -o -f configure.ac ] && %__libtoolize --copy --force
./configure \
 	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--localstatedir=/var/lib \
	--sharedstatedir=%{_prefix}/com \
	--mandir=%{_mandir} \
	--infodir=%{_datadir}/info \
%endif
%if ! %{external_vcdnav}
	--with-internal-vcdlibs \
%endif
%if %{build_directfb}
	--enable-directfb \
%endif
%if ! %{build_alsa}
	--disable-alsa \
%endif
%if ! %{build_vidix}
	--disable-vidix \
%endif
%if ! %{build_faad}
	--disable-faad \
%endif
%if ! %{build_pulse}
	--disable-polypaudio \
%endif
%if ! %{build_linuxfb}
	--disable-fb \
%endif
%if ! %{build_magick}
	--without-imagemagick \
%endif
%if %{external_ffmpeg}
 	--with-external-ffmpeg \
%endif
	--enable-ipv6 \
	--with-libflac \
	--with-wavpack \
	--with-w32-path=%{_libdir}/codecs \
	--with-external-libmpcdec
# real-codecs-path is not set so that runtime searching is used. We want
# to use either codecs from RealPlayer or real-codecs, whichever is
# present.

%make_build

%install
%make_install

#clean out unpackaged files
rm -f %{buildroot}%{_libdir}/xine/plugins/*/*.la
rm -f %{buildroot}%{_libdir}/xine/plugins/*/post/*.la
rm -rf installed-docs
mv %{buildroot}%{_datadir}/doc/xine-lib installed-docs
rm -f %{buildroot}%{_libdir}/xine/plugins/*/xineplug_inp_vcdo.so

%find_lang libxine2 || touch libxine2.lang
