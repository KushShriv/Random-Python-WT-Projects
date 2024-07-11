# 1. hello world
# import mesop as me
# @me.page() # decorator to make the function the root path - equivalent to @me.page(path="/")
# def hello_world(): # Creates a mesop Component
#     me.text("Hello World!")

# 2. counter app
import mesop as me

@me.stateclass # decorator to make the class a state class
class State: # represents application state for this browser session
    clicks: int = 0

def button_click(event: me.ClickEvent):
    state = me.state(State)
    state.clicks += 1

@me.page(path="/counter")
def main():
    state = me.state(State)
    me.text(f"Clicks: {state.clicks}")
    me.button("Click me", on_click=button_click)









# . text_to_text
# import mesop as me
# import mesop.labs as mel

# @me.page(
#     security_policy=me.SecurityPolicy(
#         allowed_iframe_parents=["https://google.github.io"]
#     ),
#     path="/text_to_text",
#     title="Text to Text",
# )

# def app():
#     mel.text_to_text(
#         upper_case_stream,
#         title = "Text to Text",
#     )

# def upper_case_stream(s: str):
#     return f"Echo: {s}"
