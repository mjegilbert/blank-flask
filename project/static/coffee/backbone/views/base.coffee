# Base view for all other Backbone Views used in the app

Base = (options) ->
  @children = _([])
  @bindings = _([])
  Backbone.View.apply(@,[options])

_.extend(Base.prototype, Backbone.View.prototype,

  # Handles shift/cmd/ctrl clicks for items that don't have
  # an anchor tag
  click_link: (e) ->
    href = $(e.target).attr("href")

    # If a special click is detected and the element is not an anchor tag
    # use JS to open the new window.  Otherwise, let the browser handle it,
    # and prevent the Backbone router from going there on the current page
    if !(e.metaKey || e.ctrlKey || e.shiftKey)
      e.preventDefault()
      app.router.navigate(href, trigger: true)

  # Adapted from backbone-support.js
  #   resetChildren(), bindTo(), unbindFromAll(), removeChild(), leave()
  # These functions handle cleaning up after views
  resetChildren: ->
    @children.each (child) ->
      child.leave()
    @children = _([])

  bindTo: (source, vent, callback) ->
    source.on vent, callback, @
    @bindings.push( source: source, vent: vent, callback: callback )

  unbindFromAll: ->
    @bindings.each (binding) =>
      binding.source.off binding.vent, binding.callback, @
    @bindings = _([])

  removeChild: (view) ->
    @children.splice( @children.indexOf(view), 1 )
    view.leave()

  leave: ->
    @unbindFromAll()
    @off()
    @remove()
    if @onLeave
      @onLeave()
    @children.each (child) ->
      child.leave()

  debug: (obj) ->
    console.log "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n"
    console.log obj
    console.log "\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
)

Base.extend = Backbone.View.extend
@app.Views.Base = Base