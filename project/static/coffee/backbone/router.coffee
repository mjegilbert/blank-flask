class AppRouter extends Backbone.Router

  routes:
    "(/)" : "home"

  initialize: ->
    # Set parent el (for SwappingRouter @swap() functionality)
    @el = $("#content")

  home: ->
    view = new app.Views.Home
    @swap(view)

  # Adapted from backbone-support.js
  # Leaves the old view and replaces with the new view
  swap: (newView) ->
    if @currentView && @currentView.leave
      @currentView.leave()
    @currentView = newView
    @el.empty().append @currentView.render().el

@app.Routers.AppRouter = AppRouter
