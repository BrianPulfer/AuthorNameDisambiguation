import os
import time

from py4j.java_gateway import JavaGateway


def initialize_java_server():
    java_class_path = os.path.dirname(os.path.abspath(__file__)) + "/JavaJDST/target/classes/JDSTServer"
    command = "java "+java_class_path
    os.system(command)
    time.sleep(3)


class JDSTRetriever:

    JAVA_SERVER_INITIALIZED = True

    def __init__(self):
        if not self.JAVA_SERVER_INITIALIZED:
            initialize_java_server()
            self.JAVA_SERVER_INITIALIZED = True

        self._apiwrapper = JavaGateway().entry_point

    def get_jds(self, text):
        """Given an article's PMID, returns the article Journal Descriptors"""
        return self._apiwrapper.getJDs(text)

    def get_sts(self, text):
        """Given an article's PMID, returns the article Semantic Types"""
        return self._apiwrapper.getSTs(text)
