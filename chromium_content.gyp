{
  'targets': [
    {
      'target_name': 'chromium_content',
      'type': 'shared_library',
      'dependencies': [
        'vendor/chromium/src/content/content.gyp:content',
        'vendor/chromium/src/content/content.gyp:content_shell_pak',
      ], 
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-all_load',
        ],
        'LD_DYLIB_INSTALL_NAME': '@rpath/libchromium_content.dylib',
      },
    },
  ],
}