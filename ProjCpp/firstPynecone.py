"""Welcome to Pynecone! this Card Gen."""
import pynecone as pc
from datetime import datetime
import random


month = [f"{i:02d}" for i in range(1, 13)]
year = [str(datetime.now().year +i) for i in range(10)]

image_url = [
    "https://wallpaperaccess.com/full/25565.jpg",
    "https://getwallpapers.com/wallpaper/full/6/7/6/21099.jpg",
    "https://eskipaper.com/images/shape-wallpapers-1.jpg",
    "https://i.pinimg.com/originals/d2/35/0c/d2350cc140de0a4a2cf0fd8cf8a7a66f.png",
]

class State(pc.State):
    
    number_input: str
    name_input: str

    # expirations settings
    exp_month: str = "MM"
    sep_date: str = "/"
    exp_year: str = "YYYY"

    # card UI logic
    number_row_list: list[str] = [
        "#" if i not in (4, 9, 14) else " " for i in range(19)
    ]

    # function to get number input
    def get_number_input(self, number_input):
        self.number_input = number_input

        # to update the #'s with the numbers from the input, we need to handle a few things in this function.
        # first, turn the input field intoa list of char
        to_list = list(self.number_input)

        # next, add spaces to the number_input
        # this allows a space bettween evary 4 digits
        if len(to_list) in [4, 9, 14]:
            self.number_input += " "

        to_list = [
            char if i not in (4, 9, 14) else " " for i, char in enumerate(to_list)
        ]

        # now update the number_row_list which is what display to the card
        self.number_row_list = [char for char in to_list]

        # handle empty input
        if len(self.number_row_list) == 0:
            self.number_row_list = [
                "#" if i not in (4, 8, 14) else " " for i in range(19)
            ]

    # function to get number input
    def get_name_input(self, name_input):
        self.name_input = name_input


def number_row():
    return pc.container(
        pc.hstack(
            pc.foreach(
                State.number_row_list,
                display_number_on_card,
            ),
            
        ),
        cursor="pointer",
        display="grid",
        center_content=True,
        justify_content='center',
        width="100%",
    )

def display_number_on_card(txt: int):
    return pc.text(
        txt,
        font_size="24px",
        font_weight="bold",
        color="white",
    )

# the display name is esier than the
def display_name_on_card():
    return pc.text(
        State.name_input,
        font_size="18px",
        font_weight="bold",
        color="white",
    )

def dispay_expiration_date_on_card():
    return pc.hstack(
        pc.container(
            pc.text(
                State.exp_month,
                font_size="18px",
                color="white",
                font_weight="bold",
            ),
            padding="0px",
        ),
        pc.container(
            pc.text(
                "/",
                font_size="18px",
                color="white",
                font_weight="bold",
            ),
            padding="0px",
        ),
        pc.container(
            pc.text(
                State.exp_year,
                font_size="18px",
                color="white",
                font_weight="bold",
            ),
            padding="0px",
        ),
        spacing="2px",
    )    

        
    
def main_card():
    return pc.container(
        pc.vstack(
            # first, let's add the card numbers
            number_row(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.hstack(
                pc.container(
                    pc.vstack(
                        pc.text(
                            "Card Holder",
                            color="#fff",
                            weight="600",
                        ),
                        pc.hstack(
                            display_name_on_card(),
                            width="100%",
                            margin="auto",
                        ),
                        spacing="0px",
                    ),
                    height="55px",
                ),
                pc.container(
                    pc.vstack(
                        pc.text(
                            "Expires",
                            color="#fff",
                            weight="600",
                        ),
                        pc.hstack(
                            dispay_expiration_date_on_card(),
                            width="100%",
                            margin="auto",
                            spacing="0px"
                        ),
                    spacing="0px",                    
                ),
                height="55px",
                display="flex",
                width="40%",
            ),
                width="100%",
            ),

        ),
        padding_top="100px",
        width="100%",
        max_width="430px",
        height="260px",
        z_index="2",
        margin_right="auto",
        margin_left="auto",
        position="absolute",
        transform="translate(0px, -280px)",
        box_shadow="0 30px 60px 0 rgba(90, 116, 148, 0.4)",
        border_radius="12px",
        background_image=f"url({random.choice(image_url)})",
        background_size="cover",

    )

# finally the botton
def button():
    return pc.button(
        "Sumbit",
        width="100%",
        height="55px",
        color_scheme="None",
        background="#2364d2",
        border="None",
        border_radius="5px",
        font_size="22px",
        font_weight="500",
        box_shadow="3px 10px 20px 0px rgba(35, 100, 210, 0.3)",
        color="#fff",
        margin_top="20px",
        cursor="pointer",
    )
# create a seperate one for the cvv
def card_cvv():
    return pc.input(
        width="140px",
        height="50px",
        border_radius="5px",
        bg="None",
        border="1px solid #ced6e0",
        font_size="10px",
        padding="5px 15px",
        color="#1a3b5d",
        focus_border_color="None",
        _hover={"border-color": "ced6e0"},
        _focus={
            "borderColor": "#3d9cff",
            "boxShadow": "0px 10px 20px -13px rgba(32, 56, 117, 0.35)",
            },
    )
# now for dates for inputs
def card_dates(options, placeholder, function):
    return pc.vstack(
        pc.select(
            options,
            placeholder=placeholder,
            color="#1a3b5d",
            flex_wrap="wrap",
            height="50px",
            width="140px",
            border="1px solid #ced6e0",
            font_size="18px",
            padding="10px",
            white_space="nowrap",
            _hover={"border-color": "ced6e0"},
            on_change=function,

        ),
    )


#start working with the inputs first
def card_input(card_title, input_value, function):
    return pc.container(
        pc.vstack(
            pc.text(
                card_title,
            ),
            pc.input(
                value=input_value,
                width="100%",
                height="50px",
                bg='None',
                border="1px solid #ced6e0",
                font_size="18px",
                padding="5px 15px",
                color='#1a3b5d',
                focus_border_color="None",
                on_change=function,
                _hover={"border-color": "#3d9cff"},
                _focus={
                    "borderColor": "#3d9cff",
                    "boxShadow": "0px 10px 20px -13px rgba(32, 56, 117, 0.35)",
                },             

            ),
        ),
    )


#main card form
def card():
    return pc.container(
        # main UI stack
        pc.vstack(
            #credit card UI display
            main_card(),
            card_input(
                "Card Number", 
                State.number_input, 
                lambda: State.get_number_input(),
            ),
            pc.spacer(),
            card_input(
                "Card Holder",
                State.name_input,
                lambda: State.get_name_input(),
            ),
            pc.spacer(),
            pc.hstack(
                pc.container(
                    pc.vstack(
                        pc.text(
                                "Expiraton Date",
                                ),
                                pc.hstack(
                                    card_dates(
                                        month, 
                                        "Month", 
                                        lambda: State.
                                        set_exp_month
                                        ),
                                    card_dates(
                                        year, 
                                        "Years", 
                                        lambda: State.
                                        set_exp_year
                                        ),

                                    width="100%",
                                    margin="auto",
                                    spacing="15px",

                                ),
                    ),
                ),
                pc.container(
                    pc.vstack(
                        pc.text("CVV"),
                        pc.hstack(
                        card_cvv(),
                        width="100%",
                        margin="auto",
                    ),
                ),
                    display="flex",
                    align_items="center",
                    justify_content="flex-end",
                    width="80%",
                ),
                width="100%",
            ),
            pc.spacer(),
            pc.container(
                button(),
            ),
            pc.spacer(),
        ),
        #form settings
        bg="#fff",
        padding="35px",
        padding_top="150px",
        padding_bottom="35px",
        max_width="570px",        
        width='100%',
        margin="auto",
        border_radius="10px",
        box_shadow="0 30px 60px 0 rgba(90, 116, 148, 0.4)",
        transform="Scale(0.73)",
    )

# Add state and page
def index() -> pc.Component:
    return pc.center(
        #main card form component
        card(),
        #page settings
        bg="#ddeefc",
        min_height="100vh",
        display="flex",
        flex_wrap="wrap",
        flex_direction="column",
        align_items="flex-start",
        padding="50px, 15px",
    )

style = {
    pc.Text: {
        "width": "100%",
        "font_size": "14px",
        "margin_bottom": "5px",
        "font_bottom": "500",
        "color": "#1a3b5d",
        "display": "block",
    }
}

# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index)
app.compile()