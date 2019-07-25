import os
import definitions

os.environ['CLASSPATH'] = definitions.ROOT_DIR + "/main/retrievers/jnius_jdst/tc2011dist.jar"

from jnius import autoclass

# Getting Text Categorization 2011 classes constructors
JdiApi = autoclass('gov.nih.nlm.nls.tc.Api.JdiApi')
StiApi = autoclass('gov.nih.nlm.nls.tc.Api.StiApi')
InputFilterOption = autoclass('gov.nih.nlm.nls.tc.FilterApi.InputFilterOption')
LegalWordsOption = autoclass('gov.nih.nlm.nls.tc.FilterApi.LegalWordsOption')
OutputFilter = autoclass('gov.nih.nlm.nls.tc.FilterApi.OutputFilter')
OutputFilterOption = autoclass('gov.nih.nlm.nls.tc.FilterApi.OutputFilterOption')
Configuration = autoclass('gov.nih.nlm.nls.tc.Lib.Configuration')
Count2f = autoclass('gov.nih.nlm.nls.tc.Lib.Count2f')

# Getting standard JDK classes constructors
ArrayList = autoclass('java.util.ArrayList')
Vector = autoclass('java.util.Vector')


# Instatiating Jdi and Sti
path_to_configuration = definitions.ROOT_DIR + "/main/data/Config/tc.properties"

jdi = JdiApi(path_to_configuration)
sti = StiApi(Configuration(path_to_configuration, False))


def get_jds(text):
    """Given a text (string), returns a list of the Journal Descriptors contained"""
    scores = jdi.GetJdiScoresByTextMesh(text, InputFilterOption(LegalWordsOption.DEFAULT_JDI))

    output_filter_option = OutputFilterOption()
    output_filter_option.SetOutputNum(3)

    result = OutputFilter.ProcessText(scores, jdi.GetJournalDescriptors(), output_filter_option).split("\n")

    journal_descriptors = list()

    if len(result) > 5:
        for i in range(len(result)):
            if i == 2 or i == 3 or i == 4:
                ttt = result[i].split("|")
                blyad = ttt[3].strip().replace(",", ".")
                journal_descriptors.append(blyad)

    return journal_descriptors


def get_sts(text):
    """Given a text (string), returns a list of the Semantic Types contained"""
    scores = sti.GetStiScoresByText(text, InputFilterOption(LegalWordsOption.DEFAULT_JDI))

    output_filter_option = OutputFilterOption()
    output_filter_option.SetOutputNum(3)

    result = OutputFilter.ProcessText(scores, sti.GetSemanticTypes(), output_filter_option).split("\n")

    semantic_types = list()

    if len(result) > 5:
        for i in range(len(result)):
            if i == 2 or i == 3 or i == 4:
                ttt = result[i].split("|")
                blyad = ttt[4].strip().replace(",", ".")
                semantic_types.append(blyad)

    return semantic_types
