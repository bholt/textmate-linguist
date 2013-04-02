##Progress:
* Now using Python (against my will, but it has a working Plist lib builtin and libclang bindings...), able to parse out types

--------
* Able to add things to syntax by creating a new syntax ("Custom.tmLanguage"), including the parent syntax, and then adding patterns for things we want to add
  * Using updated version of `osx-plist` (https://github.com/kballard/osx-plist):
  * Build by running `./ext/plist/extconf.rb`, then `make` (generates `plist.bundle`)
  * Replace old version in Bundle Support (/Users/bholt/Library/Application Support/TextMate/Managed/Bundles/Bundle Support.tmbundle/Support/shared/lib/osx)
  * Sometimes Textmate gets screwed up or doesn't update the syntax based on changes to the syntax definition. Currently just need to re-open the target file
  * Other problems exist if the .tmLanguage file gets screwed up--if this happens, just clean out any .tmLanguage files in the bundle and regenerate it (it holds on if there are any tmLanguage files remaining in the Syntaxes directory
* libclang:
  * Python bindings exist and seem to be used
    * libraries exist to parse
  * Ruby: ffi/clang (https://github.com/jarib/ffi-clang)
    * very preliminary, only does the absolute basics of parsing out diagnostics
    * could easily hack this to add what I want
* Other directions:
    * Use MacRuby NSDictionary bridge if performance becomes a problem?
    * Directly hack Textmate's scope highlighting mechanism to support this?
