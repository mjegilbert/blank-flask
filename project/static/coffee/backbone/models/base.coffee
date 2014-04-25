class Base extends Backbone.Model

  parse: (response) ->
    return response.data

@app.Models.Base = Base