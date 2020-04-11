def get_text():
    """Get text file"""
    return "plain text"


def get_xml():
    """Get xml file"""
    return "xml"


def convert_to_text(data):
    """Method used to convert the data into text format"""
    print("[CONVERT]")
    return f"{data} as text"


def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):

    data = getter()
    print(f"Got {data}.")

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    # Saves the data only if user want to save it
    if to_save:
        saver()

    print(f"{data} is processed.")


if __name__ == "__main__":

    template_function(get_text, to_save=True)
    template_function(get_xml, converter=convert_to_text)
