import gov.nih.nlm.nls.tc.Api.JdiApi;
import gov.nih.nlm.nls.tc.Api.StiApi;

import java.util.List;


public class APIWrapper {
    /**Wrapper class for the gov.nih.nlm.nlsc.tc API's (JournalDescriptors & SemanticTypes)*/

    public APIWrapper(){

    }

    public List<String> getJDs(String articleContent){
        /**Given a PubMed ID, returns the article's Journal Descriptors*/
        // TODO
        return null;
    }

    public List<String> getSTs(String articleContent){
        /**Given a PubMed ID, returns the article's Semantic Types */
        // TODO
        return null;
    }
}
