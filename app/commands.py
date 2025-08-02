commands = {
  'login': {
    '--use-device-code': {
      'param': True,
      'required': False,
    },
  },
  'role': {
    'assignment': {
      'create': {
        '--role': {
          'param': True,
          'required': True,
          'refs': '' # SPECIFY A CMD or API  /// HERE STR or DICT?
        },
        '--scope': {
          'param': True,
          'required': True,
          'refs': '' # SPECIFY A CMD or API  /// HERE STR or DICT?
        }
      },
      'delete': {},
      'list': {},
      'list-changelogs': {},
      'update': {},
    }
  }
}
