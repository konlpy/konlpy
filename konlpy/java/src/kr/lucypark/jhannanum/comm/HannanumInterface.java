package kr.lucypark.jhannanum.comm;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import kr.ac.kaist.swrc.jhannanum.comm.Eojeol;
import kr.ac.kaist.swrc.jhannanum.comm.Sentence;
import kr.ac.kaist.swrc.jhannanum.hannanum.Workflow;
import kr.lucypark.jhannanum.hannanum.WorkflowFactory;


public class HannanumInterface {

    public String[] extractNoun(String phrase) throws Exception {
        Workflow workflow = WorkflowFactory.getPredefinedWorkflow(WorkflowFactory.WORKFLOW_NOUN_EXTRACTOR);
        workflow.activateWorkflow(true);
        workflow.analyze(phrase);

        LinkedList<Sentence> resultList = workflow.
                                getResultOfDocument(new Sentence(0, 0, false));
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
        workflow.close();
        return list.toArray(new String[0]);
    }

    public static void main(String[] args) throws Exception {
        HannanumInterface hi = new HannanumInterface();
        String[] nouns = hi.extractNoun("성긴털제비꽃은 근무중이다.");
        for (int i=0; i<nouns.length; i++) {
            System.out.println(nouns[i]);
        }
    }
}