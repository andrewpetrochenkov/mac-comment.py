#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- "$0" "file comment"
( set -x; python -m mac_comment "$1" "$2" )
comment="$(set -x; python -m comment "$1")" || exit
echo $comment
[[ "$comment" == "$2" ]]
