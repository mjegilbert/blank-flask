class Home extends app.Views.Base
  id: "home"
  template: Templates["home"]

  render: ->
    console.log @$el
    @$el.html @template
    @

@app.Views.Home = Home
