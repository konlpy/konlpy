package kr.lucypark.kkma;

/* Copyright 2014 Lucy Park <me@lucypark.kr> */

import java.io.OutputStream;
import java.io.PrintStream;
import java.util.List;

import org.snu.ids.ha.index.Keyword;
import org.snu.ids.ha.index.KeywordExtractor;
import org.snu.ids.ha.index.KeywordList;
import org.snu.ids.ha.ma.MExpression;
import org.snu.ids.ha.ma.MorphemeAnalyzer;
import org.snu.ids.ha.ma.Sentence;


public class KkmaInterface {

    public List<Sentence> morphAnalyzer(String phrase) throws Exception {
        if (phrase == null || "".equals(phrase) || phrase.length()==0) { return null; }
        System.setOut(new PrintStream(new OutputStream() { public void write(int b) {}}){});

        MorphemeAnalyzer ma = new MorphemeAnalyzer();
        List<MExpression> ret = ma.analyze(phrase);
        ret = ma.postProcess(ret);
        ret = ma.leaveJustBest(ret);
        List<Sentence> sentenceList = ma.divideToSentences(ret);
        return sentenceList;
    }

    public KeywordList extractNoun(String phrase) {
        if (phrase == null || "".equals(phrase) || phrase.length()==0) {return null; }
        System.setOut(new PrintStream(new OutputStream() { public void write(int b) {}}){});

        KeywordExtractor ke = new KeywordExtractor();
        KeywordList kl = ke.extractKeyword(phrase, true);
        return kl;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(System.getProperty("java.class.path"));

        String phrase = "저는 대학생이구요. 소프트웨어 관련학과 입니다. DB는 수업을 한번 들은 적이 있으며, 수학은 대학에서 통계학, 선형대수학, 이산수학, 대학수학 등을 배웠지만... 자주 사용을 안하다보니 모두 까먹은 상태입니다.";
        KkmaInterface ki = new KkmaInterface();

        // Test morphAnalyzer
        List<Sentence> sentenceList = ki.morphAnalyzer(phrase);
        for (int i = 0; i < sentenceList.size(); i++) {
            Sentence st = sentenceList.get(i);
            System.out.println("* " + st.getSentence());
            for (int j = 0; j < st.size(); j++) {
                System.out.println((st.get(j)));
            }
        }

        // Test extractNoun
        KeywordList kl = ki.extractNoun(phrase);
        for (int i = 0; i < kl.size(); i++) {
            Keyword kwrd = kl.get(i);
            System.out.println(kwrd.getString() + "\t" + kwrd.getCnt());
        }
    }
}
