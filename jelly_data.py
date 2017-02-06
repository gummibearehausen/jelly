import csv

from pprint import pprint
from practnlptools.tools import Annotator


class Document:
    def __init__(self, heading, true_passage, false_passage):
        self.heading = heading
        self.true_passage = true_passage
        self.false_passage = false_passage

    def get_true_passage(self):
        return self.true_passage

    def get_false_passage(self):
        return self.false_passage

    def get_heading(self):
        return self.heading

    def get_parsed_heading(self):
        heading = self.heading
        parsed_heading = heading.split("  ")
        return parsed_heading

    def annotation(self, n):
        parsed_heading= self.get_parsed_heading()
        annotator = Annotator()
        try:
            annotation = annotator.getAnnotations(parsed_heading[n])
            return annotation
        except:
            pass


class Jelly:
    def __init__(self, file_name, path):
        self.file_name=file_name
        self.path = path

    def readfile(self,num_of_lines):
        n=0
        annotator=Annotator()
        with open(self.path + self.file_name) as f:
            reader = csv.reader(f)
            for l in reader:
                if n<num_of_lines:
                    line = l[0].split("\t")
                    heading = line[0]
                    true_passage =line[1]
                    false_passage =line[2:]
                    document=Document(heading, true_passage, false_passage)
                    anno = annotator.getAnnotations(document.get_parsed_heading()[0])
                    pprint(anno)
                    n+=1
                else:
                    break


path1 ="/Volumes/Samsung USB/jelly/"
file_name1 = "fold1.train.tsv"
corpus=Jelly(file_name1,path1)
corpus.readfile(10)
