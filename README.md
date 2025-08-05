### Hexlet tests and linter status:
[![Actions Status](https://github.com/UselessHumster/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/UselessHumster/python-project-50/actions)

### Project owns tests and linter status:
[![Python CI](https://github.com/UselessHumster/python-project-50/actions/workflows/test.yaml/badge.svg)](https://github.com/UselessHumster/python-project-50/actions/workflows/test.yaml)

### SonarQube Badges:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50) 
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=UselessHumster_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=UselessHumster_python-project-50)


---
### Installation
```
git clone https://github.com/UselessHumster/python-project-50.git
cd python-project-50
make install
```

[![Asciicast](https://asciinema.org/a/731720.svg?f=t&v=79)](https://asciinema.org/a/731720)

### Usage
```bash
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output

```

There are 3 types of formatting `stylish` (by default), `plain` and `json`

[![Asciicast](https://asciinema.org/a/731721.svg?f=t&v=79)](https://asciinema.org/a/731721)

For stylish format just type:
```bash
gendiff file1.json file2.json

{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
```

For other formats use `-f` or `--format` keys:
Example:
```bash
gendiff file1.json file2.json --format plain

Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

Example 2:
```bash
gendiff file1.json file2.json --f json

[
  {
    "name": "common",
    "children": [
      {
        "name": "follow",
        "value": false,
        "status": "added",
        "type": "flat"
      },
      {
        "name": "setting1",
        "value": "Value 1",
        "status": "not_changed",
        "type": "flat"
      },
      {
        "name": "setting2",
        "value": 200,
        "status": "removed",
        "type": "flat"
      },
      {
        "name": "setting3",
        "value": true,
        "status": "removed",
        "type": "flat"
      },
      {
        "name": "setting3",
        "value": null,
        "status": "added",
        "type": "flat"
      },
      {
        "name": "setting4",
        "value": "blah blah",
        "status": "added",
        "type": "flat"
      },
      {
        "name": "setting5",
        "children": [
          {
            "name": "key5",
            "value": "value5",
            "status": "not_changed",
            "type": "flat"
          }
        ],
        "status": "added",
        "type": "complex"
      },
      {
        "name": "setting6",
        "children": [
          {
            "name": "doge",
            "children": [
              {
                "name": "wow",
                "value": "",
                "status": "removed",
                "type": "flat"
              },
              {
                "name": "wow",
                "value": "so much",
                "status": "added",
                "type": "flat"
              }
            ],
            "status": "not_changed",
            "type": "complex"
          },
          {
            "name": "key",
            "value": "value",
            "status": "not_changed",
            "type": "flat"
          },
          {
            "name": "ops",
            "value": "vops",
            "status": "added",
            "type": "flat"
          }
        ],
        "status": "not_changed",
        "type": "complex"
      }
    ],
    "status": "not_changed",
    "type": "complex"
  },
  {
    "name": "group1",
    "children": [
      {
        "name": "baz",
        "value": "bas",
        "status": "removed",
        "type": "flat"
      },
      {
        "name": "baz",
        "value": "bars",
        "status": "added",
        "type": "flat"
      },
      {
        "name": "foo",
        "value": "bar",
        "status": "not_changed",
        "type": "flat"
      },
      {
        "name": "nest",
        "children": [
          {
            "name": "key",
            "value": "value",
            "status": "not_changed",
            "type": "flat"
          }
        ],
        "status": "removed",
        "type": "complex"
      },
      {
        "name": "nest",
        "value": "str",
        "status": "added",
        "type": "flat"
      }
    ],
    "status": "not_changed",
    "type": "complex"
  },
  {
    "name": "group2",
    "children": [
      {
        "name": "abc",
        "value": 12345,
        "status": "not_changed",
        "type": "flat"
      },
      {
        "name": "deep",
        "children": [
          {
            "name": "id",
            "value": 45,
            "status": "not_changed",
            "type": "flat"
          }
        ],
        "status": "not_changed",
        "type": "complex"
      }
    ],
    "status": "removed",
    "type": "complex"
  },
  {
    "name": "group3",
    "children": [
      {
        "name": "deep",
        "children": [
          {
            "name": "id",
            "children": [
              {
                "name": "number",
                "value": 45,
                "status": "not_changed",
                "type": "flat"
              }
            ],
            "status": "not_changed",
            "type": "complex"
          }
        ],
        "status": "not_changed",
        "type": "complex"
      },
      {
        "name": "fee",
        "value": 100500,
        "status": "not_changed",
        "type": "flat"
      }
    ],
    "status": "added",
    "type": "complex"
  }
]
```