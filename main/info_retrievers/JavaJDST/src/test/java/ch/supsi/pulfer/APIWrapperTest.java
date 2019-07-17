package ch.supsi.pulfer;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


import java.util.Arrays;
import java.util.List;

public class APIWrapperTest{
    /** Test class for the ch.supsi.pulfer.APIWrapper class. Checks that the */

    private APIWrapper apiWrapper;

    // String text passed to the APIWrapper to retrieve JDs and STs.
    // Its taken from the PUBMED article with ID '31310458'.
    private static final String text =
            "This volume of the IARC Monographs presents evaluations of the carcinogenic hazard to humans of drinking" +
                    " coffee and very hot beverages including, but not limited to, mate. An IARC Monographs Working" +
                    " Group reviewed epidemiological evidence, animal bioassays and co-carcinogenicity studies, and" +
                    " mechanistic and other relevant data to reach conclusions as to the carcinogenic hazard to" +
                    " humans of drinking coffee, mate, and very hot beverages. The Working Group assessed more than" +
                    " 1000 observational and experimental studies that investigated the association between cancer at" +
                    " more than 20 sites with drinking coffee, mate, and very hot beverages.";


    @Before
    public void setUp(){
        //Creates a new instance of APIWrapper for each test
        apiWrapper = new APIWrapper();
    }

    @After
    public void tearDown(){
        // Closes the instance of the APIWrapper after each test
        apiWrapper.close();
    }

    @Test
    public void testGetJDS(){
        /** Tests that the Journal Descriptors are correctly retrieved from the text.*/
        List<String> expected = Arrays.asList("Nutritional Sciences", "Toxicology", "Substance-Related Disorders");
        List<String> jds = apiWrapper.getJDs(text);

        Assert.assertEquals(expected, jds);
    }

    @Test
    public void testGetSTS(){
        /** Tests that the Semantic Types are correctly retrieved from the text.*/
        List<String> expected = Arrays.asList("Food", "Biologic Function", "Substance");
        List<String> sts = apiWrapper.getSTs(text);

        Assert.assertEquals(expected, sts);
    }
}