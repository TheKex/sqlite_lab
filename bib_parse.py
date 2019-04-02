import re

FORMAT_DICT = {
    'Author': '{Author} ',
    'Title': '{Title} ',
    'Journal': '// {Journal} ',
    'Year': '.-  {Year} ',
    'Publisher': '{Publisher} ',
    'Address': '{Address} ',
    'Pages': '.- p  {Pages} ',
    'Volume': '.- vol. {Volume}'
}
bib_parse_exp = r"@(?P<type>\w+)\{(?P<id>[\w.:]+),\n(?P<content>(.*\n*)+?)\}"
content_parse_exp = r"\s+(?P<key>\w+)\s+=\s\{(?P<value>.*)\}"


def parse_authors(_str):
    return _str.replace(',', '').replace(' and', ',')


def parse_bib_lib(bibtex_path):
    f = open(bibtex_path, 'r', encoding='utf-8')
    data = f.read()
    parse_data = re.finditer(bib_parse_exp, data)

    bib_list = list()

    for item in parse_data:
        tmp = dict()
        tmp['type'] = item['type']
        tmp['id'] = item['id']
        tmp_parse = re.finditer(content_parse_exp, item.group('content'))
        for i in tmp_parse:
            tmp[i['key']] = i['value'].strip()
        bib_list.append(tmp)
    return bib_list


def print_bibtex(bib_list):
    for i in bib_list:
        tmp_str = ''
        for j in FORMAT_DICT:
            if i.get(j):
                tmp_str += FORMAT_DICT[j]
        if i.get('Author'):
            i['Author'] = parse_authors(i['Author'])
        print(tmp_str.format(**i))


if __name__ == "__main__":
    path = 'biblio.bib'
    bib = parse_bib_lib(path)
    print_bibtex(bib)

