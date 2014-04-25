class Base extends Backbone.Collection
  # Override Backbone's default parse method because Flask doesn't allow a top level array
  # in JSON due to security
  # -------------------------------------------------------------------------------------
  # See: http://flask.pocoo.org/docs/security/#json-security
  # See: http://saxuality.blogspot.com/2012/05/backbonejs-integration-with-flask.html
  parse: (response) ->
    return response.data

@app.Collections.Base = Base
