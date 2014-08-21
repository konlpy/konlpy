package kr.lucypark.jhannanum.comm;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import kr.ac.kaist.swrc.jhannanum.comm.Eojeol;
import kr.ac.kaist.swrc.jhannanum.comm.Sentence;
import kr.ac.kaist.swrc.jhannanum.exception.ResultTypeException;
import kr.ac.kaist.swrc.jhannanum.hannanum.Workflow;
import kr.lucypark.jhannanum.hannanum.WorkflowFactory;


public class HannanumInterface {
    private Workflow wfMorph = null;
    private Workflow wfNoun = null;
    private Workflow wfPos09 = null;
    private Workflow wfPos22 = null;

    public String morphAnalyzer(String phrase) {
        if (phrase == null || phrase == "" || phrase.length()==0) { return null; }
        if (wfMorph == null) {
            wfMorph = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_MORPH_ANALYZER);
            try {
                wfMorph.activateWorkflow(false);
            } catch (Exception e) {
                e.printStackTrace();
                wfMorph.close();
                wfMorph = null;
                return null;
            }
        }
        String morphs = null;
        wfMorph.analyze(phrase);
        morphs = wfMorph.getResultOfDocument();
        wfMorph.close();
        return morphs;
    }

    public String[] extractNoun(String phrase) throws ResultTypeException {
        if (phrase == null || phrase == "" || phrase.length()==0) {
            String[] tmp = new String[] {""};
            return tmp;
        }
        if (wfNoun == null) {
            wfNoun = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_NOUN_EXTRACTOR);
            try {
                wfNoun.activateWorkflow(false);
            } catch (Exception e) {
                e.printStackTrace();
                wfNoun.close();
                wfNoun = null;
                return null;
            }
        }
        wfNoun.analyze(phrase);

        LinkedList<Sentence> resultList = wfNoun.getResultOfDocument(new Sentence(0, 0, false));
        List<String> list = new ArrayList<String>();
        for (Sentence s : resultList) {
            Eojeol[] eojeolArray = s.getEojeols();
            for (int i = 0; i < eojeolArray.length; i++) {
                if (eojeolArray[i].length > 0) {
                    String[] morphemes = eojeolArray[i].getMorphemes();
                    for (int j = 0; j < morphemes.length; j++) {
                        list.add(morphemes[j]);
                    }
                }
            }
        }
        wfNoun.close();
        return list.toArray(new String[0]);
    }

    public String simplePos09(String phrase) {
        if (phrase == null || phrase == "" || phrase.length()==0) { return null; }
        if (wfPos09 == null) {
            wfPos09 = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_HMM_POS_TAGGER_09);
            try {
                wfPos09.activateWorkflow(false);
            } catch (Exception e) {
                e.printStackTrace();
                wfPos09.close();
                wfPos09 = null;
                return null;
            }
        }
        String morphs = null;
        wfPos09.analyze(phrase);
        morphs = wfPos09.getResultOfDocument();
        wfPos09.close();
        return morphs;
    }

    public String simplePos22(String phrase) {
        if (phrase == null || phrase == "" || phrase.length()==0) { return null; }
        if (wfPos22 == null) {
            wfPos22 = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_HMM_POS_TAGGER_22);
            try {
                wfPos22.activateWorkflow(false);
            } catch (Exception e) {
                e.printStackTrace();
                wfPos22.close();
                wfPos22 = null;
                return null;
            }
        }
        String morphs = null;
        wfPos22.analyze(phrase);
        morphs = wfPos22.getResultOfDocument();
        wfPos22.close();
        return morphs;
    }

    public static void main(String[] args) throws Exception {
        HannanumInterface hi = new HannanumInterface();

        // Test morphAnalyzer
        String morphs = hi.morphAnalyzer(null);
        System.out.println(morphs);

        // Test extractNoun
        String[] nouns = hi.extractNoun("");
        for (int i=0; i<nouns.length; i++) {
            System.out.println(nouns[i]);
        }

        // Test SimplePOS
        String pos09 = hi.simplePos09(null);
        System.out.println(pos09);
        String pos22 = hi.simplePos22("성긴털제비꽃은 근무중이다.");
        System.out.println(pos22);
    }
}
