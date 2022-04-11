import imp
test = imp.load_source('test', './test.py')

import re


def domain_name(url):
    return re.search(r"^(?:(?:http:\/\/)|(?:https:\/\/)|(?:www\.))*([^\.]+).*", url).group(1)


test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
test.assert_equals(domain_name("https://www.youtube.com"), "youtube")
test.assert_equals(domain_name("youtube.com"), "youtube")