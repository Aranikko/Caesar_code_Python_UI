import flet as ft

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
output = []
result = ""
shift = 0

output_2 = []
result_2 = ""
shift_2 = 0

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

def Caesar_Deencrypting(user_input, shift, alphabet, output, result):
    upper_user_input = user_input.upper()
    list_user_input = list(upper_user_input)
    for ui in range(len(list_user_input)):
        if list_user_input[ui] in alphabet:
            index = alphabet.index(list_user_input[ui])
            shifted_index = (index - shift) % len(alphabet)
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
    
    t_2 = ft.Text(value="shift: ", color="white")

    output_text_2 = ft.Text()
    color_dropdown_2 = ft.Dropdown(
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
                t_2,
                color_dropdown_2,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [
                output_text,
                output_text_2
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def back(e):
        global user_input_2, output_2, result_2
        page.clean()
        page.add(
            ft.Row(
                [
                    t,
                    color_dropdown,
                    output_text,
                    t_2,
                    color_dropdown_2,
                    output_text_2,
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.add(
            ft.Row(
                [
                    txt_name,
                    txt_name_2
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.add(
            ft.Row(
                [
                    encrypt_btn,
                    deencrypt_btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        txt_name_2.value = ""
        user_input_2 = ""
        output_2 = []
        result_2 = ""
        page.update()

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
    
    def btn_click_2(e):
        if not txt_name_2.value:
            txt_name_2.error_text = "Please enter text"
            page.update()
        else:
            user_input_2 = txt_name_2.value
            page.clean()
            shift_2 = int(color_dropdown_2.value)
            page.add(
                ft.Row(
                    [
                        ft.Text(f"encrypted text: {Caesar_Deencrypting(user_input_2, shift_2, alphabet, output_2, result_2)}"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
            page.add(
                ft.Row(
                    [
                        ft.ElevatedButton("Back", on_click=back),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

    txt_name_2 = ft.TextField(label="deencryption text")
    deencrypt_btn = ft.ElevatedButton("deencrypt", on_click=btn_click_2)
    
    page.add(
        ft.Row(
            [
                txt_name,
                txt_name_2,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        ft.Row(
            [
                encrypt_btn,
                deencrypt_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main, view=ft.FLET_APP_WEB)
