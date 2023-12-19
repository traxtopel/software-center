pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), 'software-center')
moduledir = join_paths(pkgdatadir, 'software_center')



python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'software-center.in',
  output: 'software-center',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

software_center_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'about.py',
  'main_page.py',
  'utils.py',
  'classesplugin.py',
  'gui_widgets.py',
  'output_page.py'
]

install_data(software_center_sources, install_dir: moduledir)

install_subdir(
      'plugins',
      install_dir : pkgdatadir
)

install_subdir(
      'images',
      install_dir : pkgdatadir
)
