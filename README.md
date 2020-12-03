<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-comment.svg?maxAge=3600)](https://pypi.org/project/mac-comment/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-comment.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-comment.py/actions)

### Installation
```bash
$ [sudo] pip install mac-comment
```

#### Examples
```python
>>> import mac_comment
>>> mac_comment.write(__file__,"comment")
>>> mac_comment.read(__file__)
'comment'
```

```bash
$ python -m mac_comment ~ "CLI works too"
$ python -m mac_comment ~
CLI works too
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
