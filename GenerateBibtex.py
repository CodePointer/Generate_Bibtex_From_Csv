def append_author(write_out_data, authors):
    """Append author into write_out_data"""
    author_num = len(authors)
    for author_idx in range(0, author_num):
        tmp_line = ""
        if author_idx == 0:
            tmp_line = "author = {"
        else:
            tmp_line = " and "
        tmp_line += authors[author_idx]
        if author_idx == author_num - 1:
            tmp_line += "},"
        tmp_line += "\n"
        write_out_data.append(tmp_line)
    return


def append_others(write_out_data, key_word, value):
    """Append simple values into write_out_data"""
    tmp_line = key_word + " = {" + value + "},\n"
    write_out_data.append(tmp_line)
    return


def BuildUpBibtex(type, name, requires, options):
    """
    :param type: paper type.
    :param name: cite name.
    :param requires: paper required fields.
    :param options: paper optional fields.
    :return: True for success.

    type: "article"
        requires: [author(list), title, journal, year]
        options: {"VOLUME":"", "NUMBER":"", "PAGES":"",
            "MONTH":"", "NOTE":"", "KEY":""}
    type: "book"
        requires: [author/editor(list), title, publisher, year]
        options: {"VOLUME":"", "SERIES":"", "ADDRESS":"",
            "EDITION":"", "MONTH":"", "NOTE":"", "KEY":""
            "PAGES":""}
    type: "booklet"
        requires: [title]
        options: {"AUTHOR":[], "HOWPUBLISHED":"", "ADDRESS":"",
            "MONTH":"", "YEAR":"", "NOTE":"", "KEY":""}
    type: "conference"
        requires: [author(list), title, booktitle, year]
        options: {"EDITOR":"", "PAGES":"", "ORGANIZATION":"",
            "PUBLISHER":"", "ADDRESS":"", "MONTH":"", "NOTE":"",
            "KEY":""}
    type: "incollection"
        requires: [author(list), title, booktitle, year]
        options: {"EDITOR":"", "PAGES":"", "ORGANIZATION":"",
            "PUBLISHER":"", "ADDRESS":"", "MONTH":"", "NOTE":"",
            "KEY":""}
    type: "mastersthesis"
        requires: [author(list), title, school, year]
        options: {"ADDRESS":"", "MONTH":"", "NOTE":"", "KEY":""}
    type: "phdthesis"
        requires: [author(list), title, school, year]
        options: {"ADDRESS":"", "MONTH":"", "NOTE":"", "KEY":""}
    """

    write_out_data = []

    tmp_line = "@" + type + "{" + name + ",\n"
    write_out_data.append(tmp_line)

    if type == "article":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "journal", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif type == "book":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "publisher", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options.
        # options: {"VOLUME": "", "SERIES": "", "ADDRESS": "",
        #   "EDITION": "", "MONTH": "", "NOTE": "", "KEY": "", "PAGES":""}
    elif type == "booklet":
        append_others(write_out_data, "title", requires[0])
        # TODO: Finish options.
    elif type == "conference":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "booktitle", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif type == "incollection":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "booktitle", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif type == "mastersthesis":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "school", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options
    elif type == "phdthesis":
        append_author(write_out_data, requires[0])
        append_others(write_out_data, "title", requires[1])
        append_others(write_out_data, "school", requires[2])
        append_others(write_out_data, "year", requires[3])
        # TODO: Finish options
    write_out_data.append("}\n")

    file_name = "./" + name + ".bib"
    file = open(file_name, "w", encoding='utf8')
    file.writelines(write_out_data)
    file.close()

    return True

type = "article"
name = "blabla"
requires = [["甲","乙","丙"], "呵呵呵", "期刊", "2017"]
options = {}

BuildUpBibtex(type, name, requires, options)