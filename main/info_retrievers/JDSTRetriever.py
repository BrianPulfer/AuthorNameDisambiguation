import os
import time

from py4j.java_gateway import JavaGateway


def initialize_java_server():
    # TODO: Run command line commands to start the java program
    setup_command_1 = "export CLASSPATH=tc2011dist.jar:$CLASSPATH"
    setup_command_2 = "export CLASSPATH=py4j-0.10.8.1.jar:$CLASSPATH"

    java_class_path = os.path.dirname(os.path.abspath(__file__)) + "/JavaJDST JDSTServer"
    run_command = "java -cp "+java_class_path

    total_command = setup_command_1+" && "+setup_command_2+" && "+run_command
    os.system(total_command)


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

    def close(self):
        self._apiwrapper.close()
