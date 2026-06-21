def myxml(tag, content="", **attrs):

    attributes = ""

    for key, value in attrs.items():
        attributes += f' {key}="{value}"'

    return f"<{tag}{attributes}>{content}</{tag}>"


print(myxml("foo", "bar", a=1, b=2, c=3))