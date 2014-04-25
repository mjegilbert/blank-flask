window.App =
  Models: {}
  Collections: {}
  Routers: {}
  Views: {}
  Error: {}

  init: (bootstrapped_data) ->
    @vent = _.extend({}, Backbone.Events)
    @bootstrapped_data = $.parseJSON(bootstrapped_data)

    @router = new App.Routers.AppRouter()
    if (!Backbone.history.started)
      Backbone.history.start({pushState: true})
      Backbone.history.started = true
      app.vent.trigger "routerStarted"

    @router.on "route", (opts) ->
      app.vent.trigger "routerPathChange"
      @clearErrorMessages()

@app = @App
@app.rootId = "#content"
