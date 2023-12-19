install_data(
  'com.github.softwarecenter.desktop',
  install_dir: join_paths(get_option('datadir'), 'applications')
)


install_data(
  'com.github.softwarecenter.appdata.xml',
  install_dir: join_paths(get_option('datadir'), 'appdata')
)


install_data('com.github.softwarecenter.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file',
       compile_schemas,
       args: ['--strict', '--dry-run', meson.current_source_dir()])
endif

subdir('icons')
