package kr.lucypark.jhannanum.hannanum;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.lang.UnsupportedOperationException;
import kr.ac.kaist.swrc.jhannanum.hannanum.Workflow;
import kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.MorphAnalyzer.ChartMorphAnalyzer.ChartMorphAnalyzer;
import kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.PosTagger.HmmPosTagger.HMMTagger;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.MorphemeProcessor.UnknownMorphProcessor.UnknownProcessor;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PlainTextProcessor.InformalSentenceFilter.InformalSentenceFilter;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PlainTextProcessor.SentenceSegmentor.SentenceSegmentor;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PosProcessor.NounExtractor.NounExtractor;

public class WorkflowFactory {
    public static final int WORKFLOW_HMM_POS_TAGGER = 0x01;
    public static final int WORKFLOW_MORPH_ANALYZER = 0x02;
    public static final int WORKFLOW_NOUN_EXTRACTOR = 0x03;

    public static Workflow getPredefinedWorkflow(int workflowFlag) {
    	String chartMorphAnalyzerConf = "conf/plugin/MajorPlugin/MorphAnalyzer/ChartMorphAnalyzer.json";
    	String hmmTaggerAnalyzerConf = "conf/plugin/MajorPlugin/PosTagger/HmmPosTagger.json";
		Workflow workflow = new Workflow();

        switch (workflowFlag) {
            case WORKFLOW_HMM_POS_TAGGER:
            	throw new UnsupportedOperationException();
            case WORKFLOW_MORPH_ANALYZER:
            	throw new UnsupportedOperationException();
            case WORKFLOW_NOUN_EXTRACTOR:
                workflow = new Workflow();
                workflow.appendPlainTextProcessor(new SentenceSegmentor(), null);
                workflow.appendPlainTextProcessor(new InformalSentenceFilter(), null);
                workflow.setMorphAnalyzer(new ChartMorphAnalyzer(), chartMorphAnalyzerConf);
                workflow.appendMorphemeProcessor(new UnknownProcessor(), null);
                workflow.setPosTagger(new HMMTagger(), hmmTaggerAnalyzerConf);
                workflow.appendPosProcessor(new NounExtractor(), null);
                // TODO: Add workflow.setMorphUserDic(userdic)
                break;
        }
        return workflow;
    }
}