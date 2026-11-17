from pyscript import document

grade7 = {"Ishabel Manaloto", "Lyxander Trinchera", "Venice Sibug"}
grade8 = {"June Bae", "Inigo Ducut", "Cassandra Mallari"}
grade9 = {"Chesca Ignacio", "Elisha Masangcay", "Megan Tan"}
grade10 = {"Mikaella Genove", "Lexi Narciso", "Brielle Maglaqui", "Pauline Chu Tan"}

members = grade7 | grade8 | grade9 | grade10

def update_results():
    document.getElementById("member_list").innerHTML = (
        f"<ul><li>{'</li><li>'.join(members)}</li></ul>"
    )
    document.getElementById("total").innerHTML = (
        f"{len(members)} members"
    )

def add_member(event):
    global members

    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    members = members | {first + " " + last}

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""

    update_results()
update_results()