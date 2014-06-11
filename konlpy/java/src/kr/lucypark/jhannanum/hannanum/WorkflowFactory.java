package kr.lucypark.jhannanum.hannanum;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.io.File;

import kr.ac.kaist.swrc.jhannanum.hannanum.Workflow;
import kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.MorphAnalyzer.ChartMorphAnalyzer.ChartMorphAnalyzer;
import kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.PosTagger.HmmPosTagger.HMMTagger;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.MorphemeProcessor.UnknownMorphProcessor.UnknownProcessor;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PlainTextProcessor.InformalSentenceFilter.InformalSentenceFilter;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PlainTextProcessor.SentenceSegmentor.SentenceSegmentor;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PosProcessor.NounExtractor.NounExtractor;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PosProcessor.SimplePOSResult09.SimplePOSResult09;
import kr.ac.kaist.swrc.jhannanum.plugin.SupplementPlugin.PosProcessor.SimplePOSResult22.SimplePOSResult22;

public class WorkflowFactory {
    public static final int WORKFLOW_HMM_POS_TAGGER_09 = 0x01;
    public static final int WORKFLOW_HMM_POS_TAGGER_22 = 0x02;
    public static final int WORKFLOW_MORPH_ANALYZER = 0x03;
    public static final int WORKFLOW_NOUN_EXTRACTOR = 0x04;

    public static Workflow getPredefinedWorkflow(int workflowFlag) {
        String chartMorphAnalyzerConf = "conf/plugin/MajorPlugin/MorphAnalyzer/ChartMorphAnalyzer.json";
        String hmmTaggerAnalyzerConf = "conf/plugin/MajorPlugin/PosTagger/HmmPosTagger.json";
        File wf = new File(WorkflowFactory.class.getProtectionDomain().getCodeSource().getLocation().getPath());
        String wfpath = wf.getParentFile().getPath();

        Workflow workflow = new Workflow(wfpath);
        workflow.appendPlainTextProcessor(new SentenceSegmentor(), null);
        workflow.appendPlainTextProcessor(new InformalSentenceFilter(), null);
        workflow.setMorphAnalyzer(new ChartMorphAnalyzer(), chartMorphAnalyzerConf);
        // TODO: Add workflow.setMorphUserDic(userDicFile);
        workflow.appendMorphemeProcessor(new UnknownProcessor(), null);

        switch (workflowFlag) {
            case WORKFLOW_HMM_POS_TAGGER_09:
                workflow.setPosTagger(new HMMTagger(), hmmTaggerAnalyzerConf);
                workflow.appendPosProcessor(new SimplePOSResult09(), null);
                break;
            case WORKFLOW_HMM_POS_TAGGER_22:
                workflow.setPosTagger(new HMMTagger(), hmmTaggerAnalyzerConf);
                workflow.appendPosProcessor(new SimplePOSResult22(), null);
                break;
            case WORKFLOW_MORPH_ANALYZER:
                break;
            case WORKFLOW_NOUN_EXTRACTOR:
                workflow.setPosTagger(new HMMTagger(), hmmTaggerAnalyzerConf);
                workflow.appendPosProcessor(new NounExtractor(), null);
                break;
        }
        return workflow;
    }
}
