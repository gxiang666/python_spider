# _*_coding:utf-8_*_


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.txt', 'a')

        # fout.write("<html>")
        # fout.write("<body>")
        # fout.write("<table>")

        for data in self.datas:
            # fout.write("<tr>")
            # fout.write("<td style='width:400px'>%s</td>" % data['url'].encode('utf-8'))
            fout.write(data['title'].encode('utf-8'))
            fout.write(data['summary'].encode('utf-8'))
            # fout.write("</tr>")

        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        fout.close()
