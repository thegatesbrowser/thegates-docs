# TODOs

## Recipes section

A `Recipes` sidebar pillar — short, task-focused, copy-paste how-tos
that sit between Quickstart (long, sequential) and Reference (lookup).

Drafted candidates we held back from v1.0:

- **Open another gate from a button** — minimum pattern for triggering
  navigation from any node (Button, Area3D, etc.). Variants for
  relative URLs and `open_link` for external URLs.
- **Persist player state between visits** — `ConfigFile` + `user://`
  save/load. First-time-visit detection. Caveats about clearing
  browser data.
- **Play background audio in your world** — bundle audio into the
  `.pck`, autoplay vs from-script patterns, ogg-vs-wav tip.

Don't ship until there are 5+ recipes worth shipping; one or two
recipes look like a stub. Drafts saved in
`https://github.com/thegatesbrowser/thegates-docs` history (commit
`c323035` had a `recipes/` directory).

## Other deferred sections

- **Best practices page** — five tips from internal docs (Godot
  version stickiness, .pck vs .zip, discoverable isn't private,
  GDExtension all-platforms, AMD driver heads-up). Held back because
  it overlapped with existing pages. Revisit when there's a clearer
  story.
- **Discover / showcase page** — wait for a curated gate list to
  fill it. Current FAQ entry on "Where can I find worlds to visit?"
  covers the in-app discovery in the meantime.
- **Roadmap page** — wait until the post-v1.0 roadmap is concrete
  enough to commit to publicly.
- **Changelog page** — start one once there's a v1.1 to add. v1.0
  alone in a changelog reads thin.

## Post-restructure follow-ups

Items surfaced during the About + Concepts → About + Architecture
restructure (see git log: the deletion of `concepts/`, addition of
`architecture/`).

- **Architecture pillar may grow.** Single page at launch
  (`architecture/overview.rst`). Add deeper pages (shared GPU texture
  details, command channel internals, sandbox internals beyond what
  Security covers) only when at least one reader asks. Don't
  pre-build.
- **Refresh the Introduction screenshot if the launcher UI changes.**
  Using `_static/launcher_home.png` (copied from
  `../thegates/screenshots/1-home.png` at restructure time). If the
  home screen changes meaningfully post-v1.0, refresh.
- **Mention the Godot Web Editor in Quickstart prerequisites.**
  `../web-editor/` hosts the official Godot Web Editor (Godot's WASM
  build) as a no-install alternative for creators. Surface it in
  Quickstart prerequisites — *"or use the Godot Web Editor at
  &lt;url&gt;"* — once the hosted URL is confirmed stable and
  supported.
- **In-app docs link target.** If the launcher's Help / Docs button
  links into the docs, confirm it lands on the new
  `about/introduction.rst` and update if needed.
