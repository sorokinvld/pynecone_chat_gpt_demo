from typing import Union
import pynecone as pc
import openai

# model: the model string for the ChatGPT version used in this application
openai.api_key = "sk-API_KEY_HERE"

#
class State(pc.State):
    """The app state."""

    # store the application title
    title: str = "Create a new username"

    # store the user's name for display purposes & database managment
    username: str

    # store the user's prompt from the input widget
    user_prompt: str

    # store the session in a list of dictionaries
    session: list[list]

    # user info settings and animation
    input_width: str = "0px"
    input_opacity: str = "0"
    input_container_width: str = "0px"
    input_container_height: str = "60px"
    save_prompt_opacity: str = "0"

    # method: update input from user
    def update_input_from_user(self, user_prompt):
        self.user_prompt = user_prompt

    # method: animate the username container
    def animate_username_container(self):
        self.input_container_width = "360px"

    # method: animate the input field
    def animate_input_field(self):
        self.input_opacity = "100"
        self.input_width = "320px"

    # method: animate the save prompt
    def animate_save_prompt(self):
        self.save_prompt_opacity = "100"

    # method: save the username
    def save_username(self, key):
        if key == "Enter":
            if self.username == "":
                self.username = self.user_prompt
                self.user_prompt = ""

                self.title = f"Welcome {self.username} to ChatGPT!"
                self.save_prompt_opacity = "0"
                self.input_container_height = "500px"
                self.input_container_width = "500px"
                self.input_width = "400px"

            else:
                self.session.append([self.username, self.user_prompt, "#20222c"])

                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": self.user_prompt,
                        }
                    ],
                )
                self.user_prompt = ""

                self.session.append(
                    [
                        "ChatGPT Turbo",
                        completion.choices[0].message.content,
                        "#2e2f3e",
                    ]
                )


# method: return data to display from both USER and AI
def return_data_to_display(data: list):
    return pc.vstack(
        pc.container(
            pc.heading(
                data[0],
                size="sm",
                text_align="start",
                color="white",
            ),
            width="100%",
            height="45px",
            display="flex",
            align_items="center",
            justify_content="start",
        ),
        pc.container(
            pc.text(data[1], color="white", text_align="start", weight="bold"),
        ),
        width="500px",
        display="flex",
        align_items="start",
        justify_content="start",
        padding="10px",
        border_radius="6px",
        bg=data[2],
    )


@pc.route(
    "/",
    on_load=[
        State.animate_username_container,
        State.animate_input_field,
        State.animate_save_prompt,
    ],
)
def index() -> pc.Component:
    return pc.vstack(
        pc.heading(State.title, size="lg", text_align="center", color="white"),
        pc.container(
            pc.vstack(
                pc.vstack(
                    pc.foreach(
                        State.session,
                        return_data_to_display,
                    ),
                    align_items="center",
                    justify_content="start",
                    width="inherit",
                    height="inherit",
                    display="flex",
                    overflow_y="auto",
                    overflow_x="hidden",
                    scroll_behavior="smooth",
                ),
                pc.input(
                    value=State.user_prompt,
                    border="None",
                    border_bottom="0.05rem solid #bbbbbb",
                    border_radius="0",
                    focus_border_color="None",
                    color="white",
                    padding_left="2px",
                    width=State.input_width,
                    opacity=State.input_opacity,
                    transition="width 500ms, opacity 500ms ease 550ms",
                    on_change=lambda: State.update_input_from_user,
                    on_key_down=lambda key: State.save_username(key),
                ),
                width=State.input_container_width,
                height=State.input_container_height,
                transition="width 500ms, height 500ms ease",
                dispaly="flex",
                align_items="center",
                justify_content="end",
                padding_bottom="10px",
            ),
            width=State.input_container_width,
            height=State.input_container_height,
            bg="#20222c",
            border_radius="6px",
            box_shadow="0px 10px 20px 0px rgba(0, 0, 0, 0.4)",
            display="flex",
            align_items="center",
            justify_content="center",
            transition="width 500ms, height 500ms ease",
        ),
        pc.heading(
            "Press",
            pc.span(" Enter ", color="lightblue", as_="i", font_weight="bold"),
            "to continue.",
            size="xs",
            color="white",
            padding_top="10px",
            opacity=State.save_prompt_opacity,
            transition="opacity 500ms ease 1000ms",
        ),
        spacing="2rem",
        width="100%",
        height="100vh",
        bg="#2e2f3e",
        display="flex",
        align_items="center",
        justify_content="center",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.compile()
