def _append_author_(write_out_data, authors):
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


def _append_others_(write_out_data, key_word, value):
    """Append simple values into write_out_data"""
    tmp_line = key_word + " = {" + value + "},\n"
    write_out_data.append(tmp_line)
    return


def buildup_bibtex(paper_type, mark_name, requires, options):
    """
    :param paper_type: paper type.
    :param mark_name: cite name.
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

    tmp_line = "@" + paper_type + "{" + mark_name + ",\n"
    write_out_data.append(tmp_line)

    if paper_type == "article":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "journal", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif paper_type == "book":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "publisher", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options.
        # options: {"VOLUME": "", "SERIES": "", "ADDRESS": "",
        #   "EDITION": "", "MONTH": "", "NOTE": "", "KEY": "", "PAGES":""}
    elif paper_type == "booklet":
        _append_others_(write_out_data, "title", requires[0])
        # TODO: Finish options.
    elif paper_type == "conference":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "booktitle", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif paper_type == "incollection":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "booktitle", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options.
    elif paper_type == "mastersthesis":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "school", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options
    elif paper_type == "phdthesis":
        _append_author_(write_out_data, requires[0])
        _append_others_(write_out_data, "title", requires[1])
        _append_others_(write_out_data, "school", requires[2])
        _append_others_(write_out_data, "year", requires[3])
        # TODO: Finish options
    write_out_data.append("}\n")

    file_name = "./" + mark_name + ".bib"
    file = open(file_name, "w", encoding='utf8')
    file.writelines(write_out_data)
    file.close()

    return True

test_paper_type = "article"
test_mark_name = "blabla"
requires_key = [["甲","乙","丙"], "呵呵呵", "期刊", "2017"]
options = {}

buildup_bibtex(test_paper_type, test_mark_name, requires_key, options)