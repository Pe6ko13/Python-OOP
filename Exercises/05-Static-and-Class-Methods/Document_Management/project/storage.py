from typing import List, Any


class Storage:
    categories: List[Any]
    topics: List[Any]
    documents: List[Any]

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for cat in self.categories:
            if cat.id == category_id:
                cat.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for top in self.topics:
            if top.id == topic_id:
                top.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        if document:
            return document

    def __repr__(self):
        result = []

        for d in self.documents:
            result.append(repr(d))

        return ', '.join(result)
