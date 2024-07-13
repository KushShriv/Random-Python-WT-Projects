# # 1. hello world
# import mesop as me
# @me.page() # decorator to make the function the root component for the root path - equivalent to @me.page(path="/")
# def hello_world(): # Creates a mesop Component
#     me.text("Hello World!")

# # 2. counter app
# import mesop as me

# @me.stateclass # like python's dataclass but also sets default value based on type hints and allows Mesop to inject the class
# class State: # represents application state for this browser session
#     clicks: int = 0

# def button_click(event: me.ClickEvent): # event handler - has a single parameter, event, which can contain a value
#     state = me.state(State) # retrieves the instance of the state class for the current session.
#     state.clicks += 1 # state mutation must be done in an event handler and not in a component function

# @me.page(path="/counter") # root component for the /counter path
# def main():
#     state = me.state(State)
#     me.text(f"Clicks: {state.clicks}")
#     me.button("Click me", on_click=button_click)

# # . text_to_text
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

# # badges
# import mesop as me


# @me.page(
#   security_policy=me.SecurityPolicy(
#     allowed_iframe_parents=["https://google.github.io"]
#   ),
#   path="/badge",
# )
# def app():
#   with me.box(
#     style=me.Style(
#       display="block",
#       padding=me.Padding(top=16, right=16, bottom=16, left=16),
#       height=50,
#       width=30,
#     )
#   ):
#     with me.badge(content="1", size="medium"):
#       me.text(text="text with badge")

import mesop as me
import components.badges as badges

@me.page(path="/")
def hello_world():
    badges.app()