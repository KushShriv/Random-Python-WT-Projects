import mesop as me

@me.stateclass
class CounterState:
    counter: int = 0
    label: str = ""

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/badge",
)

def app():
  counter_state = me.state(CounterState)
  with me.box(
    style=me.Style(
      display="block",
      padding=me.Padding(top=16, right=16, bottom=16, left=16),
      height=50,
      width=30,
    )
  ):
    with me.badge(content=str(counter_state.counter), size="medium"):
      me.text(text = counter_state.label)