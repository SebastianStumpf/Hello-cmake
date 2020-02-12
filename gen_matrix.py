# print strategy matrix for azure devops

import itertools
import string

matrix = [[('agent', 'ubuntu-16.04'), ('agent', 'ubuntu-18.04')],
          [('compilerVersion', '7'), ('compilerVersion', '9')],
          [('buildType', 'Release'), ('buildType', 'Debug')]]

print('jobs:')
print('- job:')
print('  strategy:')
print('    matrix:')

for t in itertools.product(*matrix):
    print('      {0}:'.format('--'.join(list(map(lambda x: '-'.join(x), t)))))
    for name, val in t:
        print('        {0}: \'{1}\''.format(name, val))
