// Text Categorization 2011 imports
import gov.nih.nlm.nls.tc.Api.JdiApi;
import gov.nih.nlm.nls.tc.Api.StiApi;
import gov.nih.nlm.nls.tc.FilterApi.InputFilterOption;
import gov.nih.nlm.nls.tc.FilterApi.LegalWordsOption;
import gov.nih.nlm.nls.tc.FilterApi.OutputFilter;
import gov.nih.nlm.nls.tc.FilterApi.OutputFilterOption;
import gov.nih.nlm.nls.tc.Lib.Configuration;
import gov.nih.nlm.nls.tc.Lib.Count2f;

// JDK imports
import java.util.List;
import java.util.ArrayList;
import java.util.Vector;


public class APIWrapper {
    /**Wrapper class for the gov.nih.nlm.nlsc.tc API's (JournalDescriptors & SemanticTypes)*/

    // JDs and STs API's
    private JdiApi jdi;
    private StiApi sti;

    public APIWrapper(){
        this.jdi = new JdiApi("./data/Config/tc.properties");
        this.sti = new StiApi(new Configuration("./data/Config/tc.properties", false));
    }

    public APIWrapper(String tcConfigFile){
        this.jdi = new JdiApi(tcConfigFile);
        this.sti = new StiApi(tcConfigFile);
    }


    public List<String> getJDs(String text){
        /**Given a PubMed ID, returns the article's Journal Descriptors*/
        Vector<Count2f> scores = jdi.GetJdiScoresByTextMesh(text, new InputFilterOption(LegalWordsOption.DEFAULT_JDI));

        OutputFilterOption outputFilterOption = new OutputFilterOption();
        outputFilterOption.SetOutputNum(3);

        String[] result = OutputFilter.ProcessText(scores, jdi.GetJournalDescriptors(), outputFilterOption).split("\n");

        List<String> journalDescriptors = new ArrayList<String>();

        if(result.length > 5) {
            for (int i = 0; i < result.length; i++) {
                if (i == 2 || i == 3 || i == 4) {
                    String[] ttt = result[i].split("\\|");
                    String blyad = ttt[3].trim().replace(",", ".");
                    journalDescriptors.add(blyad);
                }
            }
        }

        //jdi.Close();
        return journalDescriptors;
    }


    public List<String> getSTs(String text){
        /**Given a PubMed ID, returns the article's Semantic Types */
        Vector<Count2f> scores = sti.GetStiScoresByText(text, new InputFilterOption(LegalWordsOption.DEFAULT_JDI));

        OutputFilterOption outputFilterOption = new OutputFilterOption();
        outputFilterOption.SetOutputNum(3);

        String[] result = OutputFilter.ProcessText(scores, sti.GetSemanticTypes(), outputFilterOption).split("\n");

        List<String> semanticTypes = new ArrayList<String>();

        if(result.length > 5){
            for (int i = 0; i < result.length; i++){
                if(i == 2 || i == 3 || i == 4){
                    String[] ttt = result[i].split("\\|");
                    String blyad = ttt[4].trim().replace(",", ".");
                    semanticTypes.add(blyad);
                }
            }
        }

        return semanticTypes;
    }

    public void close(){
        this.sti.Close();
        this.jdi.Close();
    }
}
