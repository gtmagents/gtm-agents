#!/usr/bin/env sh

if [ -n "$husky_skip_init" ]; then
  return
fi

husky_skip_init=1

if [ -f "$HOME/.huskyrc" ]; then
  . "$HOME/.huskyrc"
fi
