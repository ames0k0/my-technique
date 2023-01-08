from sys import argv

from ofacd import DirectoryStructure


def main():
  ds = DirectoryStructure('identities')

  ds.add(
    'ames0k0',
    (
      'profile', (
        'root',
        'code', (
          'github', (
            'organizations', (
              'organization_h2b7',
              'organization_sh1chan',
            )
            'users', (
              'users_ames0k0',
              'users_aintp3d0',
              'users_fr1ht',
            )
          ),
          'gitlab', 'heroku'
        )
      ),
    )
  )

  ds.add(
    'ames0k0',
    (
      'profile', (
        'root',
        'code', (
        )
      ),
    )
  )

  ds.add(
    'fr1th',
    (
      'profile', (
        'root',
        'code',
      ),
    )
  )

  ds.create()


if __name__ == '__main__':
  if len(argv) != 2:
    print('./ds.py root_path')
    exit(1)

  chdir(argv[1])

  main()
