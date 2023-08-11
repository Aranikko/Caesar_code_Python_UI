import flet as ft

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
output = []
result = ""
shift = 0

def Caesar_Encrypting(user_input, shift, alphabet, output, result):
    upper_user_input = user_input.upper()
    list_user_input = list(upper_user_input)
    for ui in range(len(list_user_input)):
        if list_user_input[ui] in alphabet:
            index = alphabet.index(list_user_input[ui])
            shifted_index = (index + shift) % len(alphabet)
            output.append(alphabet[shifted_index])
        else:
            output.append(list_user_input[ui])
    result = ''.join(output)
    return result

def main(page):
    page.title = "Caesar_Encrypting"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    t = ft.Text(value="shift: ", color="white")

    output_text = ft.Text()
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("11"),
            ft.dropdown.Option("12"),
            ft.dropdown.Option("13"),
            ft.dropdown.Option("14"),
            ft.dropdown.Option("15"),
            ft.dropdown.Option("16"),
            ft.dropdown.Option("17"),
            ft.dropdown.Option("18"),
            ft.dropdown.Option("19"),
            ft.dropdown.Option("20"),
            ft.dropdown.Option("21"),
            ft.dropdown.Option("22"),
            ft.dropdown.Option("23"),
            ft.dropdown.Option("24"),
            ft.dropdown.Option("25"),
            ft.dropdown.Option("26"),
            ft.dropdown.Option("27"),
            ft.dropdown.Option("28"),
            ft.dropdown.Option("29"),
            ft.dropdown.Option("30"),
            ft.dropdown.Option("31"),
            ft.dropdown.Option("32"),
            ft.dropdown.Option("33"),
        ],
    )
    page.add(
        ft.Row(
            [
                t,
                color_dropdown,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [
                output_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter text"
            page.update()
        else:
            user_input = txt_name.value
            page.clean()
            shift = int(color_dropdown.value)
            page.add(
                ft.Row(
                    [
                        ft.Text(f"encrypted text: {Caesar_Encrypting(user_input, shift, alphabet, output, result)}"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
            def back(e):
                global user_input, output, result
                page.clean()
                page.add(
                    ft.Row(
                        [
                            t,
                            color_dropdown,
                            output_text,
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
                page.add(
                    ft.Row(
                        [
                            txt_name,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
                page.add(
                    ft.Row(
                        [
                            encrypt_btn,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
                txt_name.value = ""
                user_input = ""
                output = []
                result = ""
                page.update()
            page.add(
                ft.Row(
                    [
                        ft.ElevatedButton("Back", on_click=back),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

    txt_name = ft.TextField(label="encryption text")
    encrypt_btn = ft.ElevatedButton("encrypt", on_click=btn_click)
    page.add(
        ft.Row(
            [
                txt_name,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        ft.Row(
            [
                encrypt_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)
